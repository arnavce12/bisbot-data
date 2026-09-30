import os
import pandas as pd
from collections import defaultdict
import glob

RAW_DIR = 'raw'
OUTPUT_REPORT = 'reports/raw_data_audit.md'

def get_department_from_filename(filename):
    if 'CHD' in filename: return 'CHD'
    if 'CED' in filename: return 'CED'
    if 'LITD' in filename: return 'LITD'
    if 'FAD' in filename: return 'FAD'
    if 'TED' in filename: return 'TED'
    if 'WRD' in filename: return 'WRD'
    return 'Unknown'

def main():
    files = glob.glob(os.path.join(RAW_DIR, '*'))
    
    report_lines = [
        "# Raw Data Audit Report",
        "",
        "## 1. Inventory & Basic Stats",
        ""
    ]
    
    total_rows = 0
    standard_counts = defaultdict(int)
    file_stats = []
    
    for f in files:
        filename = os.path.basename(f)
        dept = get_department_from_filename(filename)
        
        try:
            if f.endswith('.xlsx'):
                # Read skipping the first row because it contains 'Generated On'
                df = pd.read_excel(f, skiprows=1)
            elif f.endswith('.csv'):
                # Try reading with utf-8 or ISO-8859-1
                try:
                    df = pd.read_csv(f, encoding='utf-8')
                except Exception:
                    df = pd.read_csv(f, encoding='ISO-8859-1')
            else:
                continue
        except Exception as e:
            report_lines.append(f"**Error reading {filename}:** {e}")
            continue
            
        rows, cols = df.shape
        total_rows += rows
        col_names = list(df.columns)
        
        # Missing values
        missing = df.isna().sum().to_dict()
        
        # Standard Number column finding
        std_col = next((c for c in col_names if 'standard no' in str(c).lower() or 'is no' in str(c).lower() or 'standard number' in str(c).lower()), None)
        
        if std_col:
            standards = df[std_col].dropna().astype(str).tolist()
            for s in standards:
                standard_counts[s] += 1
                
        # Type column finding
        type_col = next((c for c in col_names if 'type' in str(c).lower()), None)
        types = df[type_col].dropna().astype(str).value_counts().to_dict() if type_col else {}
        
        file_stats.append({
            'filename': filename,
            'department': dept,
            'rows': rows,
            'columns': col_names,
            'missing': missing,
            'types': types
        })
        
    for stat in file_stats:
        report_lines.append(f"### File: `{stat['filename']}`")
        report_lines.append(f"- **Department:** {stat['department']}")
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
    
    with open(OUTPUT_REPORT, 'w', encoding='utf-8') as out:
        out.write('\n'.join(report_lines))
        
    print(f"Audit complete. Report saved to {OUTPUT_REPORT}")

if __name__ == '__main__':
    main()
