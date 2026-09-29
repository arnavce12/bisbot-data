import json

GOLD_JSON = 'gold/standards.json'
RAG_DOCS_OUT = 'gold/rag_documents.jsonl'

def build_rag():
    with open(GOLD_JSON, 'r', encoding='utf-8') as f:
        standards = json.load(f)
        
    documents = []
    
    for std in standards:
        base_meta = {
            'standard_number': std.get('standard_number'),
            'title': std.get('official_title'),
            'department': std.get('department'),
            'source_url': std.get('source_urls'),
            'corpus_tier': 'gold'
        }
        
        # Scope chunk
        if std.get('scope'):
            doc = {
                'text': f"{std.get('standard_number')}: {std.get('official_title')}\nScope: {std.get('scope')}",
                'metadata': {**base_meta, 'field': 'scope', 'source_type': 'official_summary'}
            }
            documents.append(doc)
            
        # Applicability chunk
        if std.get('applicability'):
            doc = {
                'text': f"Applicability for {std.get('standard_number')}: {std.get('applicability')}",
                'metadata': {**base_meta, 'field': 'applicability', 'source_type': 'official_summary'}
            }
            documents.append(doc)
            
        # Requirements chunk
        if std.get('key_requirements'):
            doc = {
                'text': f"Key Requirements for {std.get('standard_number')}: {std.get('key_requirements')}",
                'metadata': {**base_meta, 'field': 'key_requirements', 'source_type': 'official_summary'}
            }
            documents.append(doc)
            
    with open(RAG_DOCS_OUT, 'w', encoding='utf-8') as out:
        for d in documents:
            out.write(json.dumps(d) + '\n')
            
    print(f"Created {len(documents)} RAG documents. Saved to {RAG_DOCS_OUT}")

if __name__ == '__main__':
    build_rag()
