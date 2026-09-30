import os
import time
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup
from enrich_gold import find_official_url, firecrawl_extract, schema, get_cache_path

CANDIDATES = 'cleaned/gold_candidates.csv'
REPORT_OUT = 'reports/firecrawl_discovery_diagnostic.md'
os.makedirs('reports', exist_ok=True)

def direct_discovery(std_no, title):
    # Approach B: Use DuckDuckGo HTML search to simulate alternative direct discovery
    # (Checking if general search engines have it indexed when Firecrawl's engine fails)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    q = f'"{std_no}" site:bis.gov.in'
    cache_file = get_cache_path(f"ddg:{q}")
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            urls = json.load(f)
    else:
        print(f"Direct DDG Search for: {q}")
        try:
            resp = requests.get('https://html.duckduckgo.com/html/', params={'q': q}, headers=headers, timeout=10)
            soup = BeautifulSoup(resp.text, 'html.parser')
            urls = []
            for a in soup.find_all('a', class_='result__url'):
                href = a.get('href')
                if href and ('bis.gov.in' in href or 'crsbis.in' in href):
                    urls.append(href)
            with open(cache_file, 'w') as f:
                json.dump(urls, f)
            time.sleep(2)
        except Exception as e:
            print(f"DDG Error: {e}")
            urls = []
            
    if urls:
        return urls[0]
    return None

def run_diagnostic():
    df = pd.read_csv(CANDIDATES)
    # Pick 12 diverse candidates
    test_df = df.head(12)
    
    results = []
    
    start_time = time.time()
    
    for idx, row in test_df.iterrows():
        std_no = row['standard_number']
        title = row['title']
        print(f"\n--- Diagnostic: {std_no} ---")
        
        # Approach A
        url_a, verified_a, err_a = find_official_url(std_no, title)
        
        # Approach B
        url_b = direct_discovery(std_no, title)
        
        best_url = url_a if url_a else url_b
        enrichable = False
        reason = "No official source"
        
        if best_url:
            if not verified_a and url_a:
                reason = "Mismatched source"
            else:
                # Test extraction
                ext = firecrawl_extract(best_url, schema)
                if ext.get('status') == 'success':
                    data = ext.get('data', {}).get('data', {}) if isinstance(ext.get('data'), dict) else ext.get('data', {})
                    scope = data.get('scope') if isinstance(data, dict) else None
                    if scope:
                        enrichable = True
                        reason = "Success"
                    else:
                        reason = "Insufficient evidence"
                else:
                    reason = "Extraction failed"
        
        results.append({
            'Standard': std_no,
            'Search found URL': url_a if url_a else 'No',
            'Direct DDG found URL': url_b if url_b else 'No',
            'Exact match verified': 'Yes' if verified_a else 'No',
            'Enrichable': 'Yes' if enrichable else 'No',
            'Reason': reason
        })
        
    end_time = time.time()
    avg_time = (end_time - start_time) / len(test_df)
    
    # Generate Report
    lines = [
        "# Firecrawl Discovery Diagnostic Report\n",
        f"**Candidates tested:** {len(test_df)}",
        f"**Average seconds per candidate:** {avg_time:.1f}s",
        f"**Projected runtime for 200 candidates:** {(avg_time * 200) / 60:.1f} minutes\n",
        "## Results Table\n",
        "| Standard | Search found URL | Direct BIS discovery found URL | Exact match verified | Enrichable | Reason |",
        "| -------- | ---------------- | ------------------------------ | -------------------- | ---------- | ------ |"
    ]
    
    for r in results:
        lines.append(f"| {r['Standard']} | {r['Search found URL']} | {r['Direct DDG found URL']} | {r['Exact match verified']} | {r['Enrichable']} | {r['Reason']} |")
        
    with open(REPORT_OUT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
        
    print(f"\nDiagnostic finished. Report saved to {REPORT_OUT}")

if __name__ == '__main__':
    run_diagnostic()
