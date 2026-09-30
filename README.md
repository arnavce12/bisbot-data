# BISBOT Data

This repository contains the data and research artifacts for the SIH 2026 BISBOT project. 

BISBOT is an AI-powered assistant for accessing and understanding Indian Standards and BIS-related compliance information. This dataset provides the necessary standard catalogues, extracted evidence, and scope definitions that allow BISBOT to find relevant standards and answer queries based on verified source texts, rather than inventing answers.

## 1. What This Data Does

BISBOT needs more than a simple list of standard numbers and titles to be useful. When a user asks:
- "Which standard applies to this product?"
- "What does the standard cover?"
- "What evidence supports that answer?"

The system requires structured data to respond accurately. 
- The **catalogue** answers: "What standards exist?"
- The **evidence corpus** answers: "What does the available source evidence actually say?"

This separation ensures the system only provides claims backed by verifiable source texts.

## 2. What Is Included

| Dataset | Purpose | Approximate Size |
|---------|---------|------------------|
| **Catalogue Records** (`catalogue_records.jsonl`) | Comprehensive list of Indian Standards, their titles, and metadata | ~23,866 records |
| **Evidence Corpus** (`rag_documents.jsonl`) | Page-aware evidence chunks extracted from standard documents | ~13,867 chunks |
| **Scope Snippets** (`scope_snippets.jsonl`) | Extracted scope text directly detailing what each standard covers | ~598 records |

*Note: The sizes reflect the current snapshot of the repository. The semantic evidence corpus represents a selected subset for research and demonstration purposes.*

## 3. How the Data Was Built

The data pipeline processes raw information into a usable format for the application:

BIS Catalogue → Document Discovery → Verification → Page-Aware Evidence Extraction → Scope Extraction → Validation → Selected Application Corpus

## 4. Quality and Validation

Ensuring the reliability of this dataset is a core focus:
- **Reconciliation**: Records have been reconciled against source data.
- **Duplicates**: Legitimate duplicate catalogue entries (e.g., sharing the same IS number but differing parts) are preserved to maintain accuracy.
- **Traceability**: All extracted evidence is directly linked to specific source documents and pages.
- **Strict Boundaries**: Unsupported claims are not treated as verified evidence. The system is designed to return "insufficient evidence" rather than invent an answer.

## 5. Coverage and Limitations

It is important to understand the boundaries of this dataset:
- The **catalogue** is broad and encompasses a large number of standards.
- The **semantic evidence corpus** is intentionally smaller and acts as a research subset.
- Not every current BIS standard has corresponding document evidence in this corpus.
- The available public archive has historical coverage limitations, meaning some current standards may not have matching extracted evidence here.
- Therefore, this dataset and BISBOT must not be treated as a complete, authoritative, or legally binding BIS database.

## 6. Source and Provenance

For every evidence-backed answer, BISBOT tracks where the evidence came from. Where possible, the data includes:
- Standard number
- Part
- Edition/Year
- Page
- Source URL

These source links allow users to independently verify the information. This project does not claim to be the authoritative issuer of Indian Standards.

## 7. How BISBOT Uses the Data

The application follows a simple workflow:
1. **User Question**: The user asks a compliance question.
2. **Find Evidence**: The system searches for potentially relevant standards and evidence.
3. **Check Evidence**: The retrieved evidence is evaluated for relevance.
4. **Generate Answer**: An answer is generated, strictly constrained by the validated evidence.
5. **Show Provenance**: The source of the evidence is displayed to the user.
6. **Fallback**: If the evidence is insufficient to answer the question, the system clearly states so.

## 8. Data Ethics and Legal Handling

- **Source Attribution**: All data is derived from publicly available sources, with attributions maintained.
- **Redistribution**: Full copyrighted BIS standards are **not** distributed in this repository. We do not claim ownership of any BIS standards.
- **Derived Data**: The dataset contains metadata, limited extracted evidence snippets, and links to original sources, ensuring compliance with fair use and research purposes.

## 9. Reproducibility

To reproduce the dataset generation, you can run the processing scripts located in the `scripts/` directory.

### Example Workflow
1. **Data Discovery**: `python scripts/discover_pdfs.py`
   - *What it does*: Discovers links to source PDFs for standards.
2. **Extraction**: (See individual script files for exact command line parameters).
   - *Note*: Some scripts require external APIs (e.g., Firecrawl). Use environment variables (like `FIRECRAWL_API_KEY`) to run them. Never commit real credentials.

## 10. For Technical Reviewers

- **Data Formats**: Final data is exported as `.jsonl` files for efficient processing.
- **Architecture**: The repository separates catalogue metadata from the semantic evidence chunks.
- **Provenance**: Each evidence chunk maintains lineage back to its source URL and page number.

## 11. Project Relationship

This repository is the dedicated data and research companion for the SIH 2026 BISBOT project. It contains the data processing pipeline, whereas the main BISBOT application codebase is maintained separately.

## 12. Status

**Research/demo dataset for SIH 2026.**
This dataset is a research demonstration. It has been validated for the purposes of the project but is intentionally limited in scope and historical coverage. It is not a production-authoritative source for Indian Standards.
