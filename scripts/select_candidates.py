import pandas as pd
import random

CLEANED_CATALOGUE = 'cleaned/all_standards.csv'
GOLD_CANDIDATES = 'cleaned/gold_candidates.csv'

def select_candidates():
    df = pd.read_csv(CLEANED_CATALOGUE)
    
    # Filter for Product Specifications
    prod_specs = df[df['type'].str.contains('Product Specification', case=False, na=False)].copy()
    
    selected_indices = []
    
    # Heuristics: Highly regulated/certified consumer and industrial products
    high_priority_keywords = [
        'steel', 'cement', 'cable', 'pipe', 'cylinder', 'tyre', 'helmet', 
        'water', 'pump', 'electrical', 'food', 'textile', 'glass', 'battery',
        'transformer', 'switch', 'socket', 'plug', 'valve', 'pesticide'
    ]
    
    def score_row(row):
        title = str(row['title']).lower()
        score = 0
        if any(kw in title for kw in high_priority_keywords):
            score += 10
        if 'part ' in title:
            score -= 2 # Parts are often too specific
        if 'method of test' in title or 'code of practice' in title or 'glossary' in title:
            score -= 100
        return score
        
    prod_specs['score'] = prod_specs.apply(score_row, axis=1)
    
    # Filter only positive scores and sort
    df_filtered = prod_specs[prod_specs['score'] > 0].sort_values(by='score', ascending=False)
    
    # Select 30 highly probable candidates
    selected_df = df_filtered.head(30).copy()
    
    selected_df.drop(columns=['score']).to_csv(GOLD_CANDIDATES, index=False)
    print(f"Selected {len(selected_df)} high-probability candidates for enrichment evaluation. Written to {GOLD_CANDIDATES}")

if __name__ == '__main__':
    select_candidates()
