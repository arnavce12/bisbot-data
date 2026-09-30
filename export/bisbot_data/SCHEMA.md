# BISBot Export Data Schema Specification

Schema Version: 1.0
Build Date: 2026-09-30

---

## 1. `rag_documents.jsonl`

Contains page-aware text chunks extracted from verified Public.Resource.Org BIS standard PDFs.

| Field Name | Data Type | Nullable | Description |
| :--- | :--- | :--- | :--- |
| `chunk_id` | String | No | Unique identifier for chunk (`doc_<base>_<part>_p<page>_c<idx>`). |
| `record_type` | String | No | Fixed value `"document"`. |
| `is_number` | String | No | Base Indian Standard number (e.g., `"2062"`). |
| `part` | String | No | Part/section designation, or empty string `""` if single-part. |
| `title` | String | No | Catalogue title of the standard. |
| `edition_year` | String | No | Year of standard edition from PDF filename. |
| `catalogue_year` | String | No | Year of standard in catalogue record. |
| `edition_status` | String | No | `"current-matching"` if edition_year == catalogue_year, else `"older-than-catalogue"`. |
| `provenance` | String | No | Fixed value `"Official document — third-party host"`. |
| `source_url` | String | No | Full HTTP URL on law.resource.org. |
| `source_host` | String | No | Fixed value `"law.resource.org"`. |
| `sha256` | String | No | SHA-256 hash of the source PDF document. |
| `page` | Integer | No | 1-indexed page number within the PDF document. |
| `section_hint` | String | Yes | `"scope"` if chunk contains a scope heading, otherwise `null`. |
| `text` | String | No | Cleaned, whitespace-normalized verbatim text of the chunk. |
| `char_count` | Integer | No | Total character length of `text`. |

---

## 2. `catalogue_records.jsonl`

Contains official catalogue metadata for all 23,866 Indian Standards.

| Field Name | Data Type | Nullable | Description |
| :--- | :--- | :--- | :--- |
| `record_type` | String | No | Fixed value `"catalogue"`. |
| `is_number` | String | No | Base Indian Standard number. |
| `part` | String | No | Part designation, or empty string `""`. |
| `title` | String | No | Official standard title. |
| `publication_date` | String | No | Date of publication, or empty string `""`. |
| `type_of_standard` | String | No | Standard category (e.g. `"Product Specification"`). |
| `degree_of_equivalence` | String | No | International equivalence designation, or `""`. |
| `has_document_evidence` | Boolean | No | `true` if a verified PDF document exists for exact IS number + part, else `false`. |
| `evidence_edition_year` | String | Yes | Edition year of verified PDF if `has_document_evidence == true`, else `null`. |
| `provenance` | String | No | Fixed value `"Official catalogue (BIS)"`. |

---

## 3. `scope_snippets.jsonl`

Contains extracted verbatim scope clause headings and initial text for verified documents.

| Field Name | Data Type | Nullable | Description |
| :--- | :--- | :--- | :--- |
| `is_number` | String | No | Base Indian Standard number. |
| `part` | String | No | Part designation, or empty string `""`. |
| `source_url` | String | No | Full HTTP URL on law.resource.org. |
| `page` | Integer | Yes | 1-indexed page where scope heading was found, or `null`. |
| `scope_found` | Boolean | No | `true` if scope heading was detected in document, else `false`. |
| `text` | String | Yes | Verbatim first 700 characters after scope heading if `scope_found == true`, else `null`. |
