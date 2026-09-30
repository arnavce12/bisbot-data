# Firecrawl Discovery Diagnostic Report

**Candidates tested:** 10 (IS 1752, IS 13262, IS 9342, IS 11459, IS 3167, IS 3470, IS 484, IS 14432, IS 15787, IS 19236)
**Average seconds per candidate:** ~48.0s
**Projected runtime for 200 candidates:** ~160.0 minutes

## Results Table

| Standard | Search found URL | Direct BIS discovery found URL | Exact match verified | Enrichable | Reason |
| -------- | ---------------- | ------------------------------ | -------------------- | ---------- | ------ |
| IS 1752:2023 | No | No | No | No | No official source |
| IS 13262:1992 | No | No | No | No | No official source |
| IS 9342:1987 | No | No | No | No | No official source |
| IS 11459:2024 | No | No | No | No | No official source |
| IS 3167:1982 | No | No | No | No | No official source |
| IS 3470:2017 | No | No | No | No | No official source |
| IS 484:1980 | No | No | No | No | No official source |
| IS 14432:1997 | No | No | No | No | No official source |
| IS 15787:2025 | No | No | No | No | No official source |
| IS 19236:2025 | No | No | No | No | No official source |

## Summary
Both discovery methods (Firecrawl web index via `app.search()` and Direct DDG web search) resulted in ZERO publicly accessible `bis.gov.in` URLs that contained the necessary information. Since neither engine indexes valid public PDF pages or manuals for these specific randomly selected items, we are hitting **Case B**. The current batch of candidates genuinely lack public online enrichment sources on the official domains.
