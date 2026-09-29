import json
import pandas as pd

GOLD_JSON = 'gold/standards.json'
REPORT_OUT = 'reports/gold_corpus_quality.md'

def validate():
    with open(GOLD_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    df = pd.DataFrame(data)
    
    report_lines = [
        "# Gold Corpus Quality Report",
        "",
        f"**Number of Selected Standards:** {len(df)}",
        ""
    ]
    
    # Departments represented
    report_lines.append("## Departments Represented")
    for dept, count in df['department'].value_counts().items():
        report_lines.append(f"- {dept}: {count}")
        
    report_lines.append("")
        
    # Completeness
    report_lines.append("## Field Completeness")
    total = len(df)
    for col in df.columns:
        filled = df[col].notnull().sum()
        pct = (filled / total) * 100
        report_lines.append(f"- **{col}:** {filled}/{total} ({pct:.1f}%)")
        
    report_lines.append("\n## Limitations")
    report_lines.append("- Synonyms and common product names are often missing from sources.")
    report_lines.append("- Certification information could only be verified for certain standards.")
    
    with open(REPORT_OUT, 'w', encoding='utf-8') as out:
        out.write('\n'.join(report_lines))
        
    print(f"Quality report written to {REPORT_OUT}")

if __name__ == '__main__':
    validate()
