import os
import time
import json
import hashlib
import pandas as pd
from dotenv import load_dotenv
from firecrawl import FirecrawlApp

load_dotenv()

GOLD_CANDIDATES = 'cleaned/gold_candidates.csv'
CACHE_DIR = 'cache/firecrawl'
GOLD_CSV = 'gold/standards.csv'
GOLD_JSON = 'gold/standards.json'
SOURCES_DIR = 'gold/sources'
RAG_DOCS_OUT = 'gold/rag_documents.jsonl'

os.makedirs(CACHE_DIR, exist_ok=True)
os.makedirs('gold', exist_ok=True)
os.makedirs(SOURCES_DIR, exist_ok=True)
os.makedirs('reports', exist_ok=True)

app = FirecrawlApp(api_key=os.environ.get('FIRECRAWL_API_KEY'))

# Tracking
api_stats = {
    'cache_hits': 0,
    'new_calls': 0
}

def normalize_query(query):
    return " ".join(str(query).lower().split())

def get_cache_path(query_or_url):
    h = hashlib.md5(query_or_url.encode('utf-8')).hexdigest()
    return os.path.join(CACHE_DIR, f"{h}.json")

def cache_read(query_or_url):
    path = get_cache_path(query_or_url)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def cache_write(query_or_url, data):
    path = get_cache_path(query_or_url)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def firecrawl_extract(url, schema):
    cached = cache_read(f"extract:{url}")
    if cached:
        print(f"CACHE HIT (Extract): {url}")
        api_stats['cache_hits'] += 1
        return cached
        
    print(f"FIRECRAWL CALL (Extract): {url}")
    api_stats['new_calls'] += 1
    try:
        raw_data = app.extract([url], {
            'prompt': 'Extract the metadata, scope, applicability, covered products, testing and conformity info of this BIS standard.',
            'schema': schema
        })
        data = raw_data if isinstance(raw_data, dict) else raw_data.model_dump()
        result = {'url': url, 'timestamp': time.time(), 'data': data, 'status': 'success'}
        cache_write(f"extract:{url}", result)
        time.sleep(6) # Rate limit
        return result
    except Exception as e:
        err_msg = str(e)
        if "Rate limit" in err_msg or "429" in err_msg:
            print(f"Rate limit hit for extract {url}. Sleeping 15s...")
            time.sleep(15)
            try:
                raw_data = app.extract([url], {
                    'prompt': 'Extract the metadata, scope, applicability, covered products, testing and conformity info of this BIS standard.',
                    'schema': schema
                })
                data = raw_data if isinstance(raw_data, dict) else raw_data.model_dump()
                result = {'url': url, 'timestamp': time.time(), 'data': data, 'status': 'success'}
                cache_write(f"extract:{url}", result)
                time.sleep(6)
                return result
            except Exception as e2:
                print(f"Firecrawl Extract Error (Retry) for {url}: {e2}")
                return {'url': url, 'timestamp': time.time(), 'error': str(e2), 'status': 'error'}
                
        print(f"Firecrawl Extract Error for {url}: {e}")
        return {'url': url, 'timestamp': time.time(), 'error': str(e), 'status': 'error'}

def firecrawl_search(query):
    cached = cache_read(f"search:{query}")
    if cached:
        print(f"CACHE HIT (Search): {query}")
        api_stats['cache_hits'] += 1
        return cached
        
    print(f"FIRECRAWL CALL (Search): {query}")
    api_stats['new_calls'] += 1
    try:
        raw_data = app.search(query)
        data = raw_data if isinstance(raw_data, dict) else raw_data.model_dump()
        result = {'query': query, 'timestamp': time.time(), 'data': data, 'status': 'success'}
        cache_write(f"search:{query}", result)
        time.sleep(6) # Prevent rate limits
        return result
    except Exception as e:
        err_msg = str(e)
        if "Rate limit" in err_msg or "429" in err_msg:
            print(f"Rate limit hit for search {query}. Sleeping 15s...")
            time.sleep(15)
            try:
                raw_data = app.search(query)
                data = raw_data if isinstance(raw_data, dict) else raw_data.model_dump()
                result = {'query': query, 'timestamp': time.time(), 'data': data, 'status': 'success'}
                cache_write(f"search:{query}", result)
                time.sleep(6)
                return result
            except Exception as e2:
                print(f"Firecrawl Search Error (Retry) for {query}: {e2}")
                return {'query': query, 'timestamp': time.time(), 'error': str(e2), 'status': 'error'}
        
        print(f"Firecrawl Search Error for {query}: {e}")
        return {'query': query, 'timestamp': time.time(), 'error': str(e), 'status': 'error'}

def verify_source(std_no, title, search_result_item):
    """Verify that a search result item actually matches the standard."""
    page_title = str(search_result_item.get('title', '')).lower()
    page_desc = str(search_result_item.get('description', '')).lower()
    url = str(search_result_item.get('url', '')).lower()
    
    # We strip spaces/colons to be safe
    norm_no = std_no.lower().replace(' ', '').replace(':', '')
    if norm_no in page_title.replace(' ', '').replace(':', '') or norm_no in page_desc.replace(' ', '').replace(':', '') or norm_no in url.replace('-', ''):
        return True
        
    # Check if a significant part of the title is in the page
    main_words = str(title).lower().split()[:3]
    if all(w in page_title or w in page_desc for w in main_words if len(w) > 3):
        return True
        
    return False

def find_official_url(std_no, title):
    product_name = " ".join(str(title).split()[:3]) if title else ""
    queries = [
        f'"{std_no}"',
        f'"{std_no}" BIS',
        f'"{title}" BIS' if title else None,
        f'"{product_name}" BIS' if product_name else None,
        f'"{std_no}" "Product Manual"',
        f'"{std_no}" "QCO"',
        f'"{std_no}" "Guidelines"',
        f'"{std_no}" site:bis.gov.in'
    ]
    
    for q in queries:
        if not q: continue
        res = firecrawl_search(q)
        if res['status'] == 'error':
            return None, False, res['error']
            
        data = res.get('data', {})
        results = data.get('data', []) if isinstance(data, dict) else data
        if not isinstance(results, list):
            results = []
            
        for r in results:
            if isinstance(r, dict) and 'url' in r:
                url = str(r['url']).lower()
                if 'bis.gov.in' in url or 'crsbis.in' in url:
                    # We found an official URL. Now verify it.
                    if verify_source(std_no, title, r):
                        return r['url'], True, None
                    else:
                        # Mismatched URL
                        return r['url'], False, None
    return None, False, None


schema = {
    "type": "object",
    "properties": {
        "scope": {"type": "string"},
        "applicability": {"type": "string"},
        "products_covered": {"type": "string"},
        "common_product_names": {"type": "string"},
        "synonyms": {"type": "string"},
        "keywords": {"type": "string"},
        "key_requirements": {"type": "string"},
        "testing_information": {"type": "string"},
        "conformity_information": {"type": "string"},
        "mandatory_or_voluntary_status": {"type": "string"},
        "related_standards": {"type": "string"}
    }
}

def enrich_candidates():
    if not os.path.exists(GOLD_CANDIDATES):
        print("Candidates file missing!")
        return

    df = pd.read_csv(GOLD_CANDIDATES)
    enriched = []
    
    # Track stats
    stats = {
        'attempted': 0,
        'official_urls_discovered': 0,
        'urls_passed_verification': 0,
        'standards_enriched': 0,
        'rejected_no_source': 0,
        'rejected_mismatched': 0,
        'rejected_insufficient_evidence': 0,
        'firecrawl_errors': 0
    }
    
    for idx, row in df.iterrows():
        stats['attempted'] += 1
        std_no = row['standard_number']
        title = row['title']
        
        print(f"\nProcessing {idx+1}/{len(df)}: {std_no}")
        
        url, verified, err = find_official_url(std_no, title)
        
        if err:
            print(f"Skipping candidate due to Firecrawl error: {err}")
            stats['firecrawl_errors'] += 1
            continue
            
        if not url:
            print(f"No official source found for {std_no}. Rejecting.")
            stats['rejected_no_source'] += 1
            continue
            
        stats['official_urls_discovered'] += 1
        
        if not verified:
            print(f"Source {url} found but mismatched/wrong for {std_no}. Rejecting.")
            stats['rejected_mismatched'] += 1
            continue
            
        stats['urls_passed_verification'] += 1
            
        # Extract from URL
        extract_res = firecrawl_extract(url, schema)
        if extract_res['status'] == 'error':
            print(f"Skipping candidate due to Firecrawl error on extract: {extract_res['error']}")
            stats['firecrawl_errors'] += 1
            continue
            
        ext_data = extract_res.get('data', {})
        extracted_fields = ext_data.get('data', {}) if isinstance(ext_data, dict) else ext_data
        
        scope = extracted_fields.get('scope')
        appli = extracted_fields.get('applicability')
        
        if not scope and not appli:
            print(f"Insufficient semantic info extracted for {std_no}. Rejecting.")
            stats['rejected_insufficient_evidence'] += 1
            continue
            
        # Record successful enrichment
        record = {
            'standard_number': std_no,
            'official_title': title,
            'department': row['department'],
            'publication_date': row['publication_date'],
            'scope': scope,
            'applicability': appli,
            'products_covered': extracted_fields.get('products_covered'),
            'common_product_names': extracted_fields.get('common_product_names'),
            'synonyms': extracted_fields.get('synonyms'),
            'keywords': extracted_fields.get('keywords'),
            'key_requirements': extracted_fields.get('key_requirements'),
            'testing_information': extracted_fields.get('testing_information'),
            'conformity_information': extracted_fields.get('conformity_information'),
            'mandatory_or_voluntary_status': extracted_fields.get('mandatory_or_voluntary_status'),
            'related_standards': extracted_fields.get('related_standards'),
            'source_urls': url,
            'source_type': 'official_bis'
        }
        enriched.append(record)
        stats['standards_enriched'] += 1
        
        snippet = f"URL: {url}\n\nSCOPE: {scope}\nAPPLICABILITY: {appli}\nCOVERED: {extracted_fields.get('products_covered')}"
        safe_name = str(std_no).replace('/', '_').replace(' ', '_')
        with open(os.path.join(SOURCES_DIR, f"{safe_name}.txt"), 'w', encoding='utf-8') as f:
            f.write(snippet)
            
        pd.DataFrame(enriched).to_csv(GOLD_CSV, index=False)
        with open(GOLD_JSON, 'w', encoding='utf-8') as f:
            json.dump(enriched, f, indent=2)
            
        if stats['standards_enriched'] >= 30:
            print("Reached target of 30 successful standards. Stopping early.")
            break

    print("\n--- Checkpoint Report ---")
    print(f"Candidates attempted: {stats['attempted']}")
    print(f"Official URLs discovered: {stats['official_urls_discovered']}")
    print(f"URLs passed verification: {stats['urls_passed_verification']}")
    print(f"Standards actually enriched: {stats['standards_enriched']}")
    print(f"Rejected (no source): {stats['rejected_no_source']}")
    print(f"Rejected (mismatched): {stats['rejected_mismatched']}")
    print(f"Rejected (insufficient evidence): {stats['rejected_insufficient_evidence']}")
    print(f"Cache hits: {api_stats['cache_hits']}")
    print(f"New Firecrawl calls: {api_stats['new_calls']}")
    print(f"Firecrawl 429/errors: {stats['firecrawl_errors']}")

if __name__ == '__main__':
    enrich_candidates()
