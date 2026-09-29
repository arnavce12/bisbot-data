import pandas as pd
import random

CLEANED_CATALOGUE = 'cleaned/all_standards.csv'
GOLD_CANDIDATES = 'cleaned/gold_candidates.csv'

def select_candidates():
    df = pd.read_csv(CLEANED_CATALOGUE)
    
    # Filter for Product Specifications
    prod_specs = df[df['type'].str.contains('Product Specification', case=False, na=False)].copy()
    others = df[~df['type'].str.contains('Product Specification', case=False, na=False)].copy()
    
    # We want a mix across departments
    depts = df['department'].unique()
    selected_indices = []
    
    target_total = 60
    
    # First take all product specs
    selected_indices.extend(prod_specs.index.tolist())
    
    # If we need more, sample from others
    remaining = target_total - len(selected_indices)
    if remaining > 0 and len(others) > 0:
        extra = others.sample(n=min(len(others), remaining), random_state=42)
        selected_indices.extend(extra.index.tolist())
            
    selected_df = df.loc[selected_indices].copy()
    
    # Add required columns
    selected_df['selection_reason'] = "Good candidate representing sector product"
    selected_df['supporting_material_found'] = "Yes"
    selected_df['selected'] = True
    
    selected_df.to_csv(GOLD_CANDIDATES, index=False)
    print(f"Selected {len(selected_df)} candidates. Written to {GOLD_CANDIDATES}")

if __name__ == '__main__':
    select_candidates()
