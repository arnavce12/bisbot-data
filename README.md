# BISBOT DATA RESEARCH DATASET

This repository contains the data collection, cleaning, enrichment, and RAG-corpus preparation work behind the SIH 2026 BISBOT project.

## 1. Objective and Motivation
The BISBOT project aims to provide accurate natural language access to Indian Standards. A major challenge in this domain is that catalogue metadata (Standard Number, Title, Department) alone is insufficient to support semantic Retrieval-Augmented Generation (RAG). Users ask about products, materials, testing requirements, and conformity schemes—not just catalogue identifiers.

To solve this, we created a dual-tier dataset:
1. **A Broad Collected Catalogue (~23k records):** Used for standard discovery and broad lookup.
2. **A Gold Semantic Corpus (60 records):** Deeply enriched product specification standards used as the primary high-quality knowledge base for natural language retrieval.

**IMPORTANT DISTINCTION:** We do NOT claim that our 23k catalogue rows are equivalent to 23k semantically enriched standards. The catalogue is for breadth; the Gold corpus is for semantic depth.

## 2. The Raw Dataset (`raw/`)
The raw data consists of originally collected CSV and Excel files containing catalogue information published by various BIS departments. 
These files are strictly treated as **immutable source data**. All transformations happen programmatically without manual overwrites.

## 3. Cleaned Catalogue (`cleaned/`)
The `cleaned/all_standards.csv` file represents a normalized version of all raw datasets.
- Obvious whitespace, encoding, and duplicate issues were resolved.
- Standard types were classified to help distinguish Product Specifications from Methods of Test, Terminology, etc.

## 4. The Gold Semantic Corpus (`gold/`)
We selected 60 genuinely useful standard candidates based on:
- Being Product Specifications.
- Representing useful real-world manufacturing queries.
- Spanning multiple BIS departments and sectors.
- Having publicly accessible BIS supporting material (e.g., Product Manuals, Quality Control Orders).

### 4.1 Enrichment Methodology
Each Gold Standard was enriched using publicly available official BIS information. The process specifically sought to establish:
- Scope and applicability
- Products covered
- Key testing and conformity requirements (e.g., Scheme-I mandatory status)
- Keywords and related standards

**Quality Gate:** If a standard lacked sufficient supporting material for natural language retrieval (i.e., we could only find its title and number), it was excluded from the Gold corpus. Hallucination of missing fields was strictly forbidden.

### 4.2 RAG-Ready Representation
The `gold/rag_documents.jsonl` file contains retrieval-friendly chunks derived from the Gold Corpus. Each chunk preserves essential metadata (standard number, source URL, field type) and contains semantically meaningful text. This is the dataset ready for ingestion into a vector database like Qdrant.

## 5. Limitations
- **Source Constraints:** Synonyms and exhaustive common product names are occasionally missing if not explicitly stated in public BIS docs.
- **Scope:** The semantic corpus is intentionally limited to 60 high-value examples to demonstrate the pipeline's effectiveness without resorting to massive, low-quality scraping.
- **Living Documents:** Standards are frequently updated; this dataset represents a specific point-in-time snapshot.

## 6. Reproducibility
All steps in this pipeline are reproducible. Run the scripts in the following order:
1. `python scripts/audit_raw.py`
2. `python scripts/clean_catalogue.py`
3. `python scripts/select_candidates.py`
4. `python scripts/enrich_gold.py`
5. `python scripts/validate_gold.py`
6. `python scripts/build_rag_documents.py`

## 7. Ethical and Legal Considerations
We strictly adhered to ethical scraping guidelines:
- **No Copyright Infringement:** We did NOT scrape, download, or redistribute full, paywalled, or copyrighted BIS standards.
- **Fair Use:** Our dataset only contains publicly accessible supporting information (catalogue metadata, Product Manuals, KYS snippets, QCO details) necessary to establish scope and applicability.
- **Rate Limiting:** Any automated data collection respected source server limits and prioritized caching.
