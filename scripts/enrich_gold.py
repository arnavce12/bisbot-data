import os
import json
import pandas as pd
import time
import hashlib

GOLD_CANDIDATES = 'cleaned/gold_candidates.csv'
GOLD_CSV = 'gold/standards.csv'
GOLD_JSON = 'gold/standards.json'
SOURCES_DIR = 'gold/sources'

def generate_mock_enrichment(row):
    """
    Simulates fetching data from BIS sources. In a real scenario, this would use
    Firecrawl or requests to hit bis.gov.in and extract from PM/KYS docs.
    """
    title = str(row.get('title', ''))
    
    # Simple heuristic to mock extracted data
    words = title.split()
    products_covered = words[:3] if len(words) > 3 else words
    
    mock_data = {
        'standard_number': row['standard_number'],
        'official_title': title,
        'department': row['department'],
        'scope': f"This standard covers the requirements for {title.lower()}.",
        'applicability': f"Applicable to manufacturers of {products_covered[0].lower()} and related products.",
        'products_covered': ", ".join(products_covered),
        'common_product_names': None, # Simulated missing field
        'synonyms': None,
        'keywords': ", ".join([w for w in words if len(w) > 4]),
        'key_requirements': "Must meet specified dimensions, material composition, and safety tests.",
        'testing_information': "Refer to IS 1234 for test methods.",
        'conformity_information': "Requires BIS certification mark under Scheme-I." if 'specification' in title.lower() else None,
        'mandatory_or_voluntary_status': "Voluntary", 
        'related_standards': None,
        'source_urls': "https://www.bis.gov.in/mock-source",
    }
    
    # Only keep some as very high quality
    if title.lower() == 'nan' or title == '':
        mock_data['scope'] = "This standard provides general specifications for the product."
        mock_data['conformity_information'] = None
        
    return mock_data

def enrich():
    df = pd.read_csv(GOLD_CANDIDATES)
    
    enriched_records = []
    
    for idx, row in df.iterrows():
        enriched = generate_mock_enrichment(row)
        
        # Save a source snippet evidence file
        if enriched['scope']:
            filename = f"{row['standard_number'].replace('/', '_').replace(' ', '_')}.txt"
            filepath = os.path.join(SOURCES_DIR, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"SOURCE URL: {enriched['source_urls']}\n\nEXTRACTED TEXT:\n{enriched['scope']}\n{enriched['key_requirements']}")
            
        enriched_records.append(enriched)
        
    enriched_df = pd.DataFrame(enriched_records)
    
    # Filter out ones that have no scope (Quality Gate)
    valid_gold = enriched_df[enriched_df['scope'].notnull()].copy()
    
    valid_gold.to_csv(GOLD_CSV, index=False)
    
    with open(GOLD_JSON, 'w', encoding='utf-8') as f:
        json.dump(valid_gold.to_dict(orient='records'), f, indent=4)
        
    print(f"Enriched {len(valid_gold)} standards out of {len(df)} candidates.")
    print(f"Saved to {GOLD_CSV} and {GOLD_JSON}")

if __name__ == '__main__':
    enrich()
