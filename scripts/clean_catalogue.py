import os
import pandas as pd
import glob
import re

RAW_DIR = 'raw'
CLEANED_DIR = 'cleaned'
ALL_STANDARDS_OUT = os.path.join(CLEANED_DIR, 'all_standards.csv')
REPORT_OUT = 'reports/catalogue_cleaning_report.md'

def normalize_text(text):
    if pd.isna(text):
        return None
    # Convert to string and remove extra whitespace
    text = str(text).strip()
    text = re.sub(r'\s+', ' ', text)
    return text

def determine_standard_type(title):
    if pd.isna(title):
        return 'Unknown'
    title_lower = title.lower()
    if 'glossary' in title_lower or 'terminology' in title_lower or 'terms' in title_lower:
        return 'Terminology'
    elif 'code of practice' in title_lower:
        return 'Code of Practice'
    elif 'method' in title_lower and 'test' in title_lower:
        return 'Methods of Test'
    elif 'service' in title_lower and 'specification' in title_lower:
        return 'Service Specification'
    elif 'process' in title_lower:
        return 'Process Specification'
    elif 'specification' in title_lower:
        return 'Product Specification'
    else:
        return 'Product Specification' # Default to product spec if uncertain but could be others.

def clean_catalogue():
    files = glob.glob(os.path.join(RAW_DIR, '*'))
    all_data = []
    
    report_lines = ["# Catalogue Cleaning Report\n"]
    
    total_raw_rows = 0
    
    for f in files:
        filename = os.path.basename(f)
        try:
            if f.endswith('.csv'):
                df = pd.read_csv(f, encoding='utf-8')
            elif f.endswith('.xlsx'):
                df = pd.read_excel(f)
            else:
                continue
        except Exception as e:
            try:
                if f.endswith('.csv'):
                    df = pd.read_csv(f, encoding='ISO-8859-1')
            except:
                continue
                
        total_raw_rows += len(df)
        
        # Standardize columns
        cols = {str(c).lower().strip(): c for c in df.columns}
        
        # Find mapped columns
        std_col = next((c for k, c in cols.items() if 'standard no' in k or 'is no' in k or 'is_number' in k or 'standard_no' in k or 'standard number' in k), None)
        title_col = next((c for k, c in cols.items() if 'title' in k), None)
        dept_col = next((c for k, c in cols.items() if 'department' in k), None)
        pub_date_col = next((c for k, c in cols.items() if 'publication' in k or 'date' in k), None)
        type_col = next((c for k, c in cols.items() if 'type' in k), None)
        eq_col = next((c for k, c in cols.items() if 'equivalence' in k or 'degree' in k), None)
        
        dept_name = "Unknown"
        if "CHEMICAL" in filename: dept_name = "CHD"
        elif "CIVIL" in filename: dept_name = "CED"
        elif "ELECTRONICS" in filename: dept_name = "LITD"
        elif "FOOD" in filename: dept_name = "FAD"
        elif "TRANSPORT" in filename: dept_name = "TED"
        elif "WATER" in filename: dept_name = "WRD"
        
        for _, row in df.iterrows():
            std_no = row[std_col] if std_col else None
            title = row[title_col] if title_col else None
            dept = row[dept_col] if dept_col else dept_name
            pub_date = row[pub_date_col] if pub_date_col else None
            std_type = row[type_col] if type_col else determine_standard_type(title)
            eq = row[eq_col] if eq_col else None
            
            std_no = normalize_text(std_no)
            if not std_no:
                continue
            
            all_data.append({
                'standard_number': std_no,
                'title': normalize_text(title),
                'department': normalize_text(dept),
                'publication_date': normalize_text(pub_date),
                'type': normalize_text(std_type),
                'degree_of_equivalence': normalize_text(eq),
                'source_file': filename
            })

    report_lines.append(f"**Total Raw Rows:** {total_raw_rows}")
    
    cleaned_df = pd.DataFrame(all_data)
    
    # Deduplicate
    initial_cleaned = len(cleaned_df)
    cleaned_df.drop_duplicates(subset=['standard_number'], keep='first', inplace=True)
    final_cleaned = len(cleaned_df)
    
    report_lines.append(f"**Total Rows After Deduplication & Empty Standard No Removal:** {final_cleaned}")
    report_lines.append(f"**Removed Duplicates/Invalid:** {total_raw_rows - final_cleaned}")
    
    # Type Distribution
    report_lines.append("\n## Type Distribution")
    for t, count in cleaned_df['type'].value_counts().items():
        report_lines.append(f"- {t}: {count}")

    cleaned_df.to_csv(ALL_STANDARDS_OUT, index=False)
    
    with open(REPORT_OUT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
        
    print(f"Cleaned catalogue written to {ALL_STANDARDS_OUT}")
    print(f"Report written to {REPORT_OUT}")

if __name__ == '__main__':
    clean_catalogue()
