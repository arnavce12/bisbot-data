import sys
import os
import json
import hashlib
import glob

def compute_sha256(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def validate_export(export_dir):
    print(f"Validating export package in '{export_dir}'...")
    
    if not os.path.isdir(export_dir):
        print(f"FAIL: Directory '{export_dir}' does not exist.")
        sys.exit(1)
        
    manifest_path = os.path.join(export_dir, "data_manifest.json")
    if not os.path.isfile(manifest_path):
        print("FAIL: data_manifest.json is missing.")
        sys.exit(1)
        
    with open(manifest_path, 'r', encoding='utf-8') as f:
        try:
            manifest = json.load(f)
        except Exception as e:
            print(f"FAIL: Invalid data_manifest.json: {e}")
            sys.exit(1)
            
    # Check file hashes in manifest
    manifest_files = manifest.get('files', {})
    for fname, meta in manifest_files.items():
        fpath = os.path.join(export_dir, fname)
        if not os.path.isfile(fpath):
            print(f"FAIL: File '{fname}' listed in manifest is missing on disk.")
            sys.exit(1)
        actual_hash = compute_sha256(fpath)
        expected_hash = meta.get('sha256')
        if actual_hash != expected_hash:
            print(f"FAIL: Hash mismatch for '{fname}'. Expected {expected_hash}, got {actual_hash}")
            sys.exit(1)
            
    # Parse catalogue_records.jsonl
    cat_file = os.path.join(export_dir, "catalogue_records.jsonl")
    if not os.path.isfile(cat_file):
        print("FAIL: catalogue_records.jsonl is missing.")
        sys.exit(1)
        
    catalogue_is_numbers = set()
    cat_required_fields = ['record_type', 'is_number', 'part', 'title', 'publication_date', 'type_of_standard', 'degree_of_equivalence', 'has_document_evidence', 'provenance']
    
    with open(cat_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except Exception as e:
                print(f"FAIL: JSON parse error in catalogue_records.jsonl line {line_num}: {e}")
                sys.exit(1)
                
            for field in cat_required_fields:
                if field not in obj:
                    print(f"FAIL: Missing field '{field}' in catalogue_records.jsonl line {line_num}")
                    sys.exit(1)
                    
            catalogue_is_numbers.add(obj['is_number'])
            
    # Parse rag_documents.jsonl (or part files)
    rag_files = glob.glob(os.path.join(export_dir, "rag_documents*.jsonl"))
    if not rag_files:
        print("FAIL: No rag_documents*.jsonl files found.")
        sys.exit(1)
        
    seen_chunk_ids = set()
    doc_required_fields = ['chunk_id', 'record_type', 'is_number', 'part', 'title', 'edition_year', 'catalogue_year', 'edition_status', 'provenance', 'source_url', 'source_host', 'sha256', 'page', 'text', 'char_count']
    
    for rfile in rag_files:
        fname = os.path.basename(rfile)
        with open(rfile, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except Exception as e:
                    print(f"FAIL: JSON parse error in {fname} line {line_num}: {e}")
                    sys.exit(1)
                    
                for field in doc_required_fields:
                    if field not in obj:
                        print(f"FAIL: Missing field '{field}' in {fname} line {line_num}")
                        sys.exit(1)
                        
                cid = obj['chunk_id']
                if cid in seen_chunk_ids:
                    print(f"FAIL: Duplicate chunk_id '{cid}' found in {fname} line {line_num}")
                    sys.exit(1)
                seen_chunk_ids.add(cid)
                
                is_num = obj['is_number']
                if is_num not in catalogue_is_numbers:
                    print(f"FAIL: Document chunk is_number '{is_num}' not found in catalogue_records.jsonl ({fname} line {line_num})")
                    sys.exit(1)

    # Parse scope_snippets.jsonl
    scope_file = os.path.join(export_dir, "scope_snippets.jsonl")
    if not os.path.isfile(scope_file):
        print("FAIL: scope_snippets.jsonl is missing.")
        sys.exit(1)
        
    scope_required_fields = ['is_number', 'part', 'source_url', 'scope_found']
    with open(scope_file, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except Exception as e:
                print(f"FAIL: JSON parse error in scope_snippets.jsonl line {line_num}: {e}")
                sys.exit(1)
                
            for field in scope_required_fields:
                if field not in obj:
                    print(f"FAIL: Missing field '{field}' in scope_snippets.jsonl line {line_num}")
                    sys.exit(1)
                    
    print(f"PASS: Export package validation succeeded for '{export_dir}' ({len(seen_chunk_ids)} document chunks, {len(catalogue_is_numbers)} catalogue records).")
    sys.exit(0)

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "export/bisbot_data"
    validate_export(target_dir)
