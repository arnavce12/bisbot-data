import os
import json
import time
import hashlib
import re
import urllib.parse
from urllib.parse import urlparse
import pandas as pd
import requests
import fitz  # PyMuPDF
from dotenv import load_dotenv
from firecrawl import FirecrawlApp

load_dotenv()
API_KEY = os.getenv('FIRECRAWL_API_KEY')
if not API_KEY:
    raise ValueError("FIRECRAWL_API_KEY not found in environment.")

app = FirecrawlApp(api_key=API_KEY)

# Directories
RAW_DOCS_DIR = 'raw/documents'
CACHE_DIR = 'cache/documents'
FC_CACHE_DIR = 'cache/firecrawl'
GOLD_DIR = 'gold'
REPORTS_DIR = 'reports'

for d in [RAW_DOCS_DIR, CACHE_DIR, FC_CACHE_DIR, GOLD_DIR, REPORTS_DIR]:
    os.makedirs(d, exist_ok=True)

# Files
MANIFEST_FILE = os.path.join(RAW_DOCS_DIR, 'manifest.json')
CANDIDATES_CSV = 'cleaned/gold_candidates.csv'
REPORT_OUT = os.path.join(REPORTS_DIR, 'document_discovery_report.md')
GOLD_JSON = os.path.join(GOLD_DIR, 'standards.json')
GOLD_CSV = os.path.join(GOLD_DIR, 'standards.csv')
RAG_JSONL = os.path.join(GOLD_DIR, 'rag_documents.jsonl')

def get_fc_cache_path(query):
    h = hashlib.md5(query.encode('utf-8')).hexdigest()
    return os.path.join(FC_CACHE_DIR, f"{h}.json")

def firecrawl_search_cached(query):
    cpath = get_fc_cache_path(query)
    if os.path.exists(cpath):
        try:
            with open(cpath, 'r', encoding='utf-8') as f:
                return json.load(f), True
        except Exception:
            pass # corrupted or empty file, will re-fetch
            
    print(f"FIRECRAWL CALL (Search): {query}")
    try:
        res = app.search(query)
        # Handle pydantic v2 / SearchData object serialization
        res_dict = res.model_dump() if hasattr(res, 'model_dump') else (res.dict() if hasattr(res, 'dict') else res)
        with open(cpath, 'w', encoding='utf-8') as f:
            json.dump(res_dict, f)
        time.sleep(6)  # rate limit buffer
        return res_dict, False
    except Exception as e:
        print(f"Firecrawl error for {query}: {e}")
        return None, False

def load_manifest():
    if os.path.exists(MANIFEST_FILE):
        with open(MANIFEST_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_manifest(manifest):
    with open(MANIFEST_FILE, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)

def download_document(url):
    h = hashlib.md5(url.encode('utf-8')).hexdigest()
    cache_path = os.path.join(CACHE_DIR, f"{h}.pdf")
    
    if os.path.exists(cache_path):
        return cache_path, True
        
    try:
        print(f"Downloading: {url}")
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=headers, stream=True, timeout=15)
        if r.status_code == 200:
            if 'text/html' in r.headers.get('Content-Type', '').lower() and not url.endswith('.pdf'):
                # Not a PDF
                return None, False
            with open(cache_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            return cache_path, False
    except Exception as e:
        print(f"Download error: {e}")
    return None, False

def verify_and_extract_pdf(pdf_path, std_no):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        # Extract up to first 20 pages for verification
        num_pages = min(20, len(doc))
        for i in range(num_pages):
            text += doc[i].get_text()
            
        text_upper = text.upper()
        norm_std = str(std_no).upper()
        # The IS number might be like IS 15627:2022
        # Just check the base number
        base_no = norm_std.split(':')[0].strip() if ':' in norm_std else norm_std
        
        has_std = base_no in text_upper
        has_bis = "BUREAU OF INDIAN STANDARDS" in text_upper or " BIS " in text_upper or "PRODUCT MANUAL" in text_upper
        
        return has_std, has_bis, text, doc
    except Exception as e:
        print(f"PDF Parsing error: {e}")
        return False, False, "", None

def run_discovery():
    df = pd.read_csv(CANDIDATES_CSV)
    manifest = load_manifest()
    
    stats = {
        'candidates_searched': 0,
        'search_queries': 0,
        'cache_hits': 0,
        'new_calls': 0,
        'urls_discovered': 0,
        'pdfs_downloaded': 0,
        'pdfs_rejected': 0,
        'verified_documents': 0,
        'official': 0,
        'official_third_party': 0,
        'secondary': 0,
        'unverified': 0
    }
    
    report_rows = []
    gold_records = []
    
    start_time = time.time()
    
    # Open JSONL for appending
    rag_file = open(RAG_JSONL, 'a', encoding='utf-8')
    
    for idx, row in df.iterrows():
        std_no = row['standard_number']
        title = row['title']
        stats['candidates_searched'] += 1
        
        print(f"\nProcessing {idx+1}/{len(df)}: {std_no}")
        
        queries = [
            f'"{std_no}" filetype:pdf',
            f'"{std_no}" "Product Manual" pdf',
            f'"{std_no}" BIS pdf',
            f'"{std_no}" "{title[:30]}" pdf'
        ]
        
        found_valid = False
        doc_urls = set()
        
        for q in queries:
            if found_valid:
                break
                
            res, is_cached = firecrawl_search_cached(q)
            stats['search_queries'] += 1
            if is_cached:
                stats['cache_hits'] += 1
            else:
                stats['new_calls'] += 1
                
            if not res or not res.get('data'):
                continue
                
            for item in res.get('data', []):
                url = item.get('url', '')
                if url and (url.endswith('.pdf') or 'pdf' in url.lower() or 'bis.gov.in' in url):
                    doc_urls.add(url)
                    
        stats['urls_discovered'] += len(doc_urls)
        
        best_prov = "Unverified"
        best_host = ""
        best_doc = False
        
        for url in list(doc_urls)[:5]: # Test max 5 URLs per candidate
            if found_valid:
                break
                
            pdf_path, cached_dl = download_document(url)
            if not pdf_path:
                continue
                
            stats['pdfs_downloaded'] += 1
            
            has_std, has_bis, text, fitz_doc = verify_and_extract_pdf(pdf_path, std_no)
            
            domain = urlparse(url).netloc.lower()
            
            if not has_std:
                stats['pdfs_rejected'] += 1
                stats['unverified'] += 1
                continue
                
            # Provenance Logic
            if ('bis.gov.in' in domain or 'crsbis.in' in domain) and has_std:
                prov = "Official"
            elif has_bis and has_std:
                prov = "Official document — third-party host"
            else:
                prov = "Secondary"
                
            # If we found at least a secondary, we might keep it if we don't find official, but prefer official.
            if prov in ["Official", "Official document — third-party host"]:
                found_valid = True
                best_prov = prov
                best_host = domain
                best_doc = True
                
                # Hash PDF
                with open(pdf_path, 'rb') as f:
                    pdf_hash = hashlib.sha256(f.read()).hexdigest()
                    
                final_pdf_name = f"{str(std_no).replace(':', '_').replace('/', '_')}_{pdf_hash[:8]}.pdf"
                final_pdf_path = os.path.join(RAW_DOCS_DIR, final_pdf_name)
                
                # Copy to raw/documents
                import shutil
                shutil.copy(pdf_path, final_pdf_path)
                
                # Update manifest
                manifest.append({
                    "filename": final_pdf_name,
                    "original_url": url,
                    "hosting_domain": domain,
                    "issuer": "Bureau of Indian Standards" if prov != "Secondary" else "Unknown",
                    "standard_number": std_no,
                    "title": title,
                    "retrieval_timestamp": time.time(),
                    "sha256": pdf_hash,
                    "provenance": prov,
                    "verification_status": "Verified"
                })
                save_manifest(manifest)
                
                stats['verified_documents'] += 1
                if prov == "Official":
                    stats['official'] += 1
                else:
                    stats['official_third_party'] += 1
                    
                # RAG Chunking (simple page-by-page)
                for page_num in range(len(fitz_doc)):
                    page_text = fitz_doc[page_num].get_text()
                    if len(page_text.strip()) > 50:
                        rag_record = {
                            "standard_number": std_no,
                            "title": title,
                            "page_number": page_num + 1,
                            "content": page_text,
                            "provenance": prov,
                            "source_filename": final_pdf_name,
                            "original_url": url
                        }
                        rag_file.write(json.dumps(rag_record) + "\n")
                        
                # Add to Gold standard record
                gold_records.append({
                    "standard_number": std_no,
                    "title": title,
                    "provenance": prov,
                    "source_url": url,
                    "hosting_domain": domain,
                    "scope": {"value": None, "provenance": "Not established"},
                    "mandatory_status": {"value": None, "provenance": "Not established"}
                })
                
                fitz_doc.close()
                break
                
        if not best_doc:
            report_rows.append(f"| {std_no} | {title[:30]}... | No | - | - | Unverified | No |")
        else:
            report_rows.append(f"| {std_no} | {title[:30]}... | Yes | {best_host} | BIS | {best_prov} | Yes |")
            
    rag_file.close()
    
    # Save Gold Corpus
    if gold_records:
        gold_df = pd.DataFrame(gold_records)
        gold_df.to_csv(GOLD_CSV, index=False)
        with open(GOLD_JSON, 'w', encoding='utf-8') as f:
            json.dump(gold_records, f, indent=2)
            
    # Write Report
    end_time = time.time()
    runtime = (end_time - start_time) / 60
    
    report_lines = [
        "# Document Discovery Report\n",
        f"**Candidates searched:** {stats['candidates_searched']}",
        f"**Search queries:** {stats['search_queries']}",
        f"**Cache hits:** {stats['cache_hits']}",
        f"**New search calls:** {stats['new_calls']}",
        f"**URLs discovered:** {stats['urls_discovered']}",
        f"**PDFs downloaded:** {stats['pdfs_downloaded']}",
        f"**PDFs rejected (unverified):** {stats['pdfs_rejected']}",
        f"**Verified documents:** {stats['verified_documents']}",
        f"**Official documents:** {stats['official']}",
        f"**Official documents (third-party host):** {stats['official_third_party']}",
        f"**Secondary sources:** {stats['secondary']}",
        f"**Runtime:** {runtime:.1f} minutes",
        f"**Final Gold Corpus size:** {len(gold_records)}\n",
        "## Details\n",
        "| IS Number | Title | Document Found | Host | Issuer | Provenance | Verified |",
        "| --------- | ----- | -------------- | ---- | ------ | ---------- | -------- |"
    ]
    report_lines.extend(report_rows)
    
    with open(REPORT_OUT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
        
    print(f"\nDiscovery complete! Found {stats['verified_documents']} verified documents.")

if __name__ == '__main__':
    run_discovery()
