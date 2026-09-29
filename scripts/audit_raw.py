import os
import pandas as pd
from collections import defaultdict
import glob

RAW_DIR = 'raw'
OUTPUT_REPORT = 'reports/raw_data_audit.md'

def main():
    files = glob.glob(os.path.join(RAW_DIR, '*'))
    
    report_lines = [
        "# Raw Data Audit Report",
        "",
        "## 1. Inventory & Basic Stats",
        ""
    ]
    
    total_rows = 0
    all_columns = set()
    standard_counts = defaultdict(int)
    file_stats = []
    
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
                # Fallback for encoding issues
                if f.endswith('.csv'):
                    df = pd.read_csv(f, encoding='ISO-8859-1')
            except Exception as e2:
                report_lines.append(f"**Error reading {filename}:** {e2}")
                continue
        
        rows, cols = df.shape
        total_rows += rows
        col_names = list(df.columns)
        all_columns.update(col_names)
        
        # Try to find the standard number column
        std_col = None
        for col in col_names:
            c = str(col).lower()
            if 'standard no' in c or 'is no' in c or 'is_number' in c or 'standard_no' in c or 'standard number' in c:
                std_col = col
                break
                
        if std_col:
            standards = df[std_col].dropna().astype(str).tolist()
            for s in standards:
                standard_counts[s] += 1
                
        # Try to find type column
        type_col = None
        for col in col_names:
            c = str(col).lower()
            if 'type' in c:
                type_col = col
                break
                
        types = []
        if type_col:
            types = df[type_col].dropna().astype(str).value_counts().to_dict()

        file_stats.append({
            'filename': filename,
            'rows': rows,
            'columns': col_names,
            'missing': df.isna().sum().to_dict(),
            'std_col': std_col,
            'types': types
        })
    
    # Generate Inventory Section
    for stat in file_stats:
        report_lines.append(f"### File: `{stat['filename']}`")
        report_lines.append(f"- **Rows:** {stat['rows']}")
        report_lines.append(f"- **Columns:** {', '.join(stat['columns'])}")
        
        if stat['types']:
            report_lines.append("- **Standard Types Distribution:**")
            for t, count in stat['types'].items():
                report_lines.append(f"  - {t}: {count}")
                
        report_lines.append("- **Missing Values:**")
        for col, count in stat['missing'].items():
            if count > 0:
                report_lines.append(f"  - {col}: {count}")
        report_lines.append("")

    report_lines.append("## 2. Global Observations")
    report_lines.append(f"- **Total Rows Across All Files:** {total_rows}")
    report_lines.append(f"- **Unique Standards Identified:** {len(standard_counts)}")
    
    duplicates = {s: c for s, c in standard_counts.items() if c > 1}
    report_lines.append(f"- **Standards in Multiple Files:** {len(duplicates)}")
    
    report_lines.append("\n## 3. Recommendations for Cleaning")
    report_lines.append("- Combine all datasets into a single catalogue.")
    report_lines.append("- Normalize standard number column names.")
    report_lines.append("- Deduplicate standards.")
    report_lines.append("- Clean standard types to distinguish Product Specifications.")
    
    with open(OUTPUT_REPORT, 'w', encoding='utf-8') as out:
        out.write('\n'.join(report_lines))
        
    print(f"Report written to {OUTPUT_REPORT}")

if __name__ == '__main__':
    main()
