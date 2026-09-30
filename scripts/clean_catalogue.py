import os
import pandas as pd
import glob
import re

RAW_DIR = 'raw'
CLEANED_DIR = 'cleaned'
ALL_STANDARDS_OUT = os.path.join(CLEANED_DIR, 'all_standards.csv')
REPORT_OUT = 'reports/catalogue_cleaning_report.md'

def get_department_from_filename(filename):
    if 'CHD' in filename: return 'CHD'
    if 'CED' in filename: return 'CED'
    if 'LITD' in filename: return 'LITD'
    if 'FAD' in filename: return 'FAD'
    if 'TED' in filename: return 'TED'
    if 'WRD' in filename: return 'WRD'
    return 'Unknown'

def normalize_text(text):
    if pd.isna(text):
        return None
    text = str(text).strip()
    text = re.sub(r'\s+', ' ', text)
    return text

def main():
    files = glob.glob(os.path.join(RAW_DIR, '*'))
    all_data = []
    
    report_lines = ["# Catalogue Cleaning Report\n"]
    total_raw_rows = 0
    
    for f in files:
        filename = os.path.basename(f)
        dept_name = get_department_from_filename(filename)
        
        try:
            if f.endswith('.xlsx'):
                df = pd.read_excel(f, skiprows=1)
            elif f.endswith('.csv'):
                try:
                    df = pd.read_csv(f, encoding='utf-8')
                except Exception:
                    df = pd.read_csv(f, encoding='ISO-8859-1')
            else:
                continue
        except Exception as e:
            continue
            
        total_raw_rows += len(df)
        
        # Identify columns
        cols = {str(c).lower().strip(): c for c in df.columns}
        
        std_col = next((c for k, c in cols.items() if 'standard number' in k or 'standard no' in k or 'is no' in k), None)
        title_col = next((c for k, c in cols.items() if 'title' in k or 'standard name' in k), None)
        pub_date_col = next((c for k, c in cols.items() if 'publish' in k or 'publication date' in k), None)
        type_col = next((c for k, c in cols.items() if 'type' in k), None)
        eq_col = next((c for k, c in cols.items() if 'equivalence' in k), None)
        
        for _, row in df.iterrows():
            std_no = row[std_col] if std_col else None
            title = row[title_col] if title_col else None
            pub_date = row[pub_date_col] if pub_date_col else None
            std_type = row[type_col] if type_col else None
            eq = row[eq_col] if eq_col else None
            
            std_no = normalize_text(std_no)
            if not std_no or std_no == 'nan':
                continue
                
            all_data.append({
                'standard_number': std_no,
                'title': normalize_text(title),
                'publication_date': normalize_text(pub_date),
                'type': normalize_text(std_type),
                'degree_of_equivalence': normalize_text(eq),
                'department': dept_name,
                'original_source_file': filename
            })

    cleaned_df = pd.DataFrame(all_data)
    
    report_lines.append(f"**Total Raw Rows Read:** {total_raw_rows}")
    report_lines.append(f"**Rows Extracted:** {len(cleaned_df)}")
    
    # Deduplicate
    initial_cleaned = len(cleaned_df)
    cleaned_df.drop_duplicates(subset=['standard_number'], keep='first', inplace=True)
    final_cleaned = len(cleaned_df)
    
    report_lines.append(f"**Total Rows After Deduplication:** {final_cleaned}")
    report_lines.append(f"**Removed Duplicates:** {initial_cleaned - final_cleaned}")
    
    report_lines.append("\n## Type Distribution")
    for t, count in cleaned_df['type'].value_counts().items():
        report_lines.append(f"- {t}: {count}")
        
    report_lines.append("\n## Missing Values")
    for col, count in cleaned_df.isna().sum().items():
        report_lines.append(f"- **{col}:** {count}")

    cleaned_df.to_csv(ALL_STANDARDS_OUT, index=False)
    
    with open(REPORT_OUT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
        
    print(f"Cleaned catalogue written to {ALL_STANDARDS_OUT}. Total rows: {final_cleaned}")
    print(f"Report written to {REPORT_OUT}")

if __name__ == '__main__':
    main()
