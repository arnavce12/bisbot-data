# Law.Resource.Org BIS Standard Probe & Diagnostics Report

Date: 2026-09-30
Target Repository: `https://law.resource.org/pub/in/bis/`

---

## STEP 1 — Reachability

### 1. HTTP Endpoint Probes

```
--- URL [a]: https://law.resource.org/pub/in/bis/ (GET) ---
Status Code: 200
Content-Type: text/html
Content-Length: 74993
First 500 chars of body:
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>Law.Resource.Org</title>

  <link id="www-core-css" rel="stylesheet" href="/html/mosh/bulk.css" type="text/css" />

</head>

<body>

<!-- House Header -->

  <div class="jsloaded" id="channel-body" style="background-image: url('/html/mosh/teal.stripes.png')">
    <div id="chann


--- URL [b]: https://law.resource.org/pub/in/bis/S10/ (GET) ---
Status Code: 200
Content-Type: text/xml
Content-Length: 724780
First 500 chars of body:
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>Law.Resource.Org</title>

  <link id="www-core-css" rel="stylesheet" href="/html/mosh/bulk.css" type="text/css" />

</head>

<body>

<!-- House Header -->

  <div class="jsloaded" id="channel-body" style="background-image: url('/html/mosh/teal.stripes.png')">
    <div id="chann


--- URL [c]: https://law.resource.org/pub/in/bis/S06/ (GET) ---
Status Code: 200
Content-Type: text/html
Content-Length: 1006733
First 500 chars of body:
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>Law.Resource.Org</title>

  <link id="www-core-css" rel="stylesheet" href="/html/mosh/bulk.css" type="text/css" />

</head>

<body>

<!-- House Header -->

  <div class="jsloaded" id="channel-body" style="background-image: url('/html/mosh/teal.stripes.png')">
    <div id="chann


--- URL [d_head]: https://law.resource.org/pub/in/bis/S10/is.2062.2011.pdf (HEAD) ---
Status Code: 200
Content-Type: application/pdf
Content-Length: 1133971
First 500 chars of body:
(No body content - HEAD request)


--- URL [d_get]: https://law.resource.org/pub/in/bis/S10/is.2062.2011.pdf (GET) ---
Status Code: 200
Content-Type: application/pdf
Content-Length: 1133971
First 500 bytes (binary repr):
b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n1 0 obj\n<</Metadata 2 0 R/NeedsRendering true/Pages 3 0 R/Type/Catalog>>\nendobj\n2 0 obj\n<</Length 3574/Subtype/XML/Type/Metadata>>stream\n<?xpacket begin="\xef\xbb\xbf" id="W5M0MpCehiHzreSzNTczkc9d"?>\n<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.2-c001 63.139439, 2010/09/27-13:37:26        ">\n <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n  <rdf:Description rdf:about="" xmlns:pdf="http://ns.adobe.com/pdf/1.3/">\n   <pdf:Producer>OmniPage 18</pdf:Producer>\n  </rdf:Description>\n'
```

### 2. Archive.org Advanced Search Probe

URL: `https://archive.org/advancedsearch.php?q=creator%3A%22Bureau+of+Indian+Standards+%28BIS%29%22&fl%5B%5D=identifier&fl%5B%5D=title&rows=20&output=json`

```
Status Code: 200
numFound: 703
Total docs returned: 20

First 10 Identifiers and Titles:
 1. Identifier: gov.law.is.4263.1967 | Title: IS 4263: Code of Safety for Chlorine
 2. Identifier: gov.law.is.14572.1998 | Title: IS 14572: Chloroform--Code of Safety
 3. Identifier: gov.law.is.10118.2.1982 | Title: IS 10118 (Part 2): Code of Practice for Selection, Installation and Maintenance of Switchgear and Controlgear, Part 2: Selection
 4. Identifier: gov.law.is.10242.2.2.1983 | Title: IS 10242 (Part 2-2): Specification for Electrical Installations in Ships, Part 2: System Design, Section 2: Protection
 5. Identifier: gov.law.is.4644.1968 | Title: IS 4644: Code of Safety for Benzene, Toluene and Xylene
 6. Identifier: gov.law.is.8149.2.1984 | Title: IS 8149 (Part 2): Requirements for Rapid Sand Gravity Filtration Equipment, Part 2: Underdrainage System
 7. Identifier: gov.law.is.11833.1986 | Title: IS 11833: Specification for Dry Powder Fire Extinguisher for Metal Fires
 8. Identifier: gov.law.is.12027.1987 | Title: IS 12027: Specification for Silicone-Based Water Repellents
 9. Identifier: gov.law.is.12143.1987 | Title: IS 12143: Code of Safety for Tetracholoroethane
 10. Identifier: gov.law.is.12647.1989 | Title: IS 12647: Solid Waste Management Systems--Collection Equipment--Guidelines
```

---

## STEP 2 — Index Structure

### 1. Top-Level Index Links

- Total links found on top-level index (`https://law.resource.org/pub/in/bis/`): **330**
- First 30 hrefs on top-level index:

```
  1. /
  2. /
  3. https://public.resource.org/
  4. https://Yo.YourHonor.Org/
  5. /pub/in/index.html
  6. bis.bill.2015.pdf
  7. bis.certification.act.1952.pdf
  8. bis.gazette.20150924.pdf
  9. bis.purchase.costs.pdf
  10. bis.report.2014.pdf
  11. bis.rules.html
  12. manifest.ced.2.html
  13. manifest.ced.3.html
  14. manifest.ced.4.html
  15. manifest.ced.5.html
  16. manifest.ced.6.html
  17. manifest.ced.7.html
  18. manifest.ced.9.html
  19. manifest.ced.11.html
  20. manifest.ced.12.html
  21. manifest.ced.13.html
  22. manifest.ced.15.html
  23. manifest.ced.20.html
  24. manifest.ced.22.html
  25. manifest.ced.24.html
  26. manifest.ced.29.html
  27. manifest.ced.30.html
  28. manifest.ced.35.html
  29. manifest.ced.36.html
  30. manifest.ced.37.html
```

### 2. Subdirectory PDF Indexing (S10/ and S06/)

- Total PDF links in `S10/`: **1,667**
- First 30 `.pdf` filenames in `S10/`:

```
  1. is.6.1983.pdf
  2. is.8.1994.pdf
  3. is.21.1992.pdf
  4. is.23.1980.pdf
  5. is.25.1979.pdf
  6. is.26.1992.pdf
  7. is.27.1992.pdf
  8. is.28.1985.pdf
  9. is.191.2007.pdf
  10. is.193.2000.pdf
  11. is.195.2005.pdf
  12. is.202.1981.pdf
  13. is.209.1992.pdf
  14. is.210.2009.pdf
  15. is.211.1992.pdf
  16. is.228.1.1987.pdf
  17. is.228.2.1987.pdf
  18. is.228.3.1987.pdf
  19. is.228.4.1987.pdf
  20. is.228.5.1987.pdf
  21. is.228.6.1987.pdf
  22. is.228.7.1990.pdf
  23. is.228.8.1989.pdf
  24. is.228.9.1989.pdf
  25. is.228.10.1989.pdf
  26. is.228.11.1990.pdf
  27. is.228.12.2001.pdf
  28. is.228.13.1982.pdf
  29. is.228.14.1988.pdf
  30. is.228.15.1992.pdf
```

- Total PDF links in `S06/`: **1,980**
- First 30 `.pdf` filenames in `S06/`:

```
  1. is.75.1973.pdf
  2. is.253.1985.pdf
  3. is.294.1979.pdf
  4. is.435.1973.pdf
  5. is.498.2003.pdf
  6. is.542.1968.pdf
  7. is.543.1968.pdf
  8. is.544.1968.pdf
  9. is.545.1984.pdf
  10. is.546.1975.pdf
  11. is.547.1968.pdf
  12. is.548.1.1964.pdf
  13. is.548.2.9.1988.pdf
  14. is.548.2.20.1983.pdf
  15. is.548.2.21.1988.pdf
  16. is.548.2.22.1993.pdf
  17. is.548.2.1976.pdf
  18. is.548.3.1976.pdf
  19. is.563.1973.pdf
  20. is.565.1984.pdf
  21. is.594.1981.pdf
  22. is.595.1954.pdf
  23. is.609.1955.pdf
  24. is.612.1992.pdf
  25. is.619.1979.pdf
  26. is.631.1979.pdf
  27. is.632.1978.pdf
  28. is.633.1985.pdf
  29. is.634.1965.pdf
  30. is.826.1980.pdf
```

### 3. Enumeration of S{NN} Subdirectories

Probe results for `S00..S20` using `HEAD` requests:

```
  S00: 404
  S01: 200
  S02: 200
  S03: 200
  S04: 200
  S05: 200
  S06: 200
  S07: 200
  S08: 200
  S09: 200
  S10: 200
  S11: 200
  S12: 200
  S13: 200
  S14: 200
  S15: 404
  S16: 404
  S17: 404
  S18: 404
  S19: 404
  S20: 404
```

Existing subdirectories: `['S01', 'S02', 'S03', 'S04', 'S05', 'S06', 'S07', 'S08', 'S09', 'S10', 'S11', 'S12', 'S13', 'S14']` (Total: 14 subdirectories).

### 4. Full Index Crawl & Cache

All 14 subdirectories were crawled with polite 1 request/sec rate limiting. Index saved to `cache/law_resource_index.json`.

Count per `S{NN}` subdirectory:

| Subdirectory | PDF Count |
| :--- | :--- |
| `S01` | 2,131 |
| `S02` | 1,592 |
| `S03` | 1,729 |
| `S04` | 1,504 |
| `S05` | 1,505 |
| `S06` | 1,980 |
| `S07` | 242 |
| `S08` | 1,171 |
| `S09` | 1,172 |
| `S10` | 1,667 |
| `S11` | 1,382 |
| `S12` | 1,141 |
| `S13` | 1,141 |
| `S14` | 464 |
| **TOTAL** | **18,821** |

### 5. Filename Pattern Matching Analysis

Pattern checked: `^is\.\d+\.\d{4}\.pdf$` (standard base number + 4-digit year format).

- Filenames matching exact pattern `is.<number>.<year>.pdf`: **12,471**
- Filenames NOT matching pattern: **6,350**

20 Examples of non-matching filenames:
```
 1. [S01] is.196.b.1966.pdf
 2. [S01] is.274.1-2.1981.pdf
 3. [S01] is.666.1.1972.pdf
 4. [S01] is.666.2.1972.pdf
 5. [S01] is.786.b.1967.pdf
 6. [S01] is.786.s.b.1967.pdf
 7. [S01] is.844.1.1979.pdf
 8. [S01] is.844.1.b.1979.pdf
 9. [S01] is.844.2.1979.pdf
 10. [S01] is.844.3.1979.pdf
 11. [S01] is.919.1.1993.pdf
 12. [S01] is.919.2.1993.pdf
 13. [S01] is.1076.1.1985.pdf
 14. [S01] is.1076.2.1985.pdf
 15. [S01] is.1076.3.1985.pdf
 16. [S01] is.1269.1.1997.pdf
 17. [S01] is.1269.2.1997.pdf
 18. [S01] is.1363.1.2002.pdf
 19. [S01] is.1363.2.2002.pdf
 20. [S01] is.1363.3.2002.pdf
```

---

## STEP 3 — Download + Extraction Quality Test

### 1. Download & File Metadata (5 Probe Files)

Downloaded to `cache/probe/`:

| Subdir | Filename | Download Status | File Size (bytes) | SHA-256 Hash |
| :--- | :--- | :--- | :--- | :--- |
| `S10` | `is.2062.2011.pdf` | 200 OK | 1,133,971 | `5985b8fbb160cf59b8a41ce84bf40d93b67ad734398c5a5c8e3147e1bef1fdd3` |
| `S06` | `is.10500.2012.pdf` | 200 OK | 894,843 | `64260e66cbc1b44f7263ab9373dfb8064e81d12b1a280d24064f77675e77a80e` |
| `S06` | `is.3865.2001.pdf` | 200 OK | 1,266,536 | `8f53087794540a4339ae9a7f3ab5c38500509f325089befddccd3908f4ae141b` |
| `S09` | `is.3994.1993.pdf` | 200 OK | 1,076,952 | `ef85ca1c2bd2b34a0e6f2fdb19d2e38080400195092c1a8edad44275c3f1e457` |
| `S11` | `is.1448.97.1980.pdf` | 200 OK | 4,726,762 | `b689f5f4eeed37a4aac5bb498668ca5df4d345ba94a8a7f2f8b67619e4aca5cc` |

### 2. PyMuPDF Extraction & OCR Assessment

- Page 1 of all Law.Resource.Org PDFs contains a standard generated digital cover text ("Disclosure to Promote the Right To Information").
- Pages 2 & 3 are image scans of the original standard cover/title pages and contain 0 digital text characters.
- Text extraction results (chars per page for pages 1, 2, 3):

| Filename | Total Pages | Chars (P1, P2, P3) | Avg (P1-P3) | Flagged (<200 chars/page on P2/P3) | IS Num Found | "BUREAU OF INDIAN STANDARDS" Found | "SCOPE" Heading Found |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `is.2062.2011.pdf` | 17 | `[1207, 0, 0]` | 402.3 | **YES** | YES | YES | YES |
| `is.10500.2012.pdf` | 18 | `[1164, 0, 0]` | 388.0 | **YES** | YES | YES | YES |
| `is.3865.2001.pdf` | 11 | `[1170, 0, 0]` | 390.0 | **YES** | YES | YES | YES |
| `is.3994.1993.pdf` | 9 | `[1163, 0, 0]` | 387.7 | **YES** | YES | YES | YES |
| `is.1448.97.1980.pdf` | 37 | `[1342, 0, 0]` | 447.3 | **YES** | YES | YES | YES |

*Note: All 5 files contain OCR text in body pages (starting from Page 4), where full text search successfully finds the IS number, "BUREAU OF INDIAN STANDARDS", and "SCOPE".*

### 3. Raw Extracted Text Samples

#### Sample 1: `is.2062.2011.pdf` (Page 1 & Page 4)

```
--- PAGE 1 ---
Disclosure to Promote the Right To Information
Whereas the Parliament of India has set out to provide a practical regime of right to 
information for citizens to secure access to information under the control of public authorities, 
in order to promote transparency and accountability in the working of every public authority, 
and whereas the attached publication of the Bureau of Indian Standards is of particular interest 
to the public, particularly disadvantaged communities and those engaged in the pursuit of 
education and knowledge, the attached public safety standard is made available to promote the 
timely dissemination of this information in an accurate manner to the public. 
इंटरनेट
मानक
“!ान$ एकन' भारतका+नम-ण”
Satyanarayan Gangaram Pitroda
“Invent a New India Using Knowledge”
“प0रा1 कोछोडन' 5 तरफ”
Jawaharlal Nehru
“Step Out From the Old to the New”
“जान1 का अ+धकार, जी1 का अ+धकार”
Mazdoor Kisan Shakti Sangathan
“The Right to Information, The Right to Live”
“!ानएकऐसाखजाना> जोकभीच

--- PAGE 2 ---
[PAGE 2 HAS 0 EXTRACTED CHARACTERS / IMAGE SCAN]

--- PAGE 4 (FIRST BODY PAGE) ---
IS 2062 : 2011
Hkkjrh; ekud
rIr csfYyr eè;e ,oa mPp rU;rk osQ
lajpuk bLikr — fof'kf"V
(lkrok¡ iqujh{k.k)
Indian Standard
HOT ROLLED MEDIUM AND HIGH TENSILE
STRUCTURAL STEEL — SPECIFICATION
( Seventh Revision )
ICS  77.140.01
©  BIS  2011
September  2011
   Price Group 5
B U R E A U   O F   I N D I A N   S T A N D A R D S
MANAK BHAVAN, 9 BAHADUR SHAH ZAFAR MARG
NEW DELHI 110002
```

#### Sample 2: `is.10500.2012.pdf` (Page 1 & Page 4)

```
--- PAGE 1 ---
Disclosure to Promote the Right To Information
Whereas the Parliament of India has set out to provide a practical regime of right to 
information for citizens to secure access to information under the control of public authorities, 
in order to promote transparency and accountability in the working of every public authority, 
and whereas the attached publication of the Bureau of Indian Standards is of particular interest 
to the public, particularly disadvantaged communities and those engaged in the pursuit of 
education and knowledge, the attached public safety standard is made available to promote the 
timely dissemination of this information in an accurate manner to the public. 
इंटरनेट
मानक
“!ान$ एकन' भारतका+नम-ण”
Satyanarayan Gangaram Pitroda
“Invent a New India Using Knowledge”
“प0रा1 कोछोडन' 5 तरफ”
Jawaharlal Nehru
“Step Out From the Old to the New”
“जान1 का अ+धकार, जी1 का अ+धकार”
Mazdoor Kisan Shakti Sangathan
“The Right to Information, The Right to Live”
“!ानएकऐसाखजाना> जोकभीच

--- PAGE 2 ---
[PAGE 2 HAS 0 EXTRACTED CHARACTERS / IMAGE SCAN]

--- PAGE 4 (FIRST BODY PAGE) ---
© BIS 2012
B U R E A U  O F  I N D I A N  S T A N D A R D S
MANAK BHAVAN, 9 BAHADUR SHAH ZAFAR MARG
NEW DELHI 110002
May 2012
Price Group 6
IS 10500 : 2012
Hkkjrh; ekud
ihus dk ikuh — fof'kf"V
¼ nwljk iqujh{k.k½
Indian Standard
DRINKING WATER — SPECIFICATION
( Second Revision )
ICS 13.060.20
```

---

## STEP 4 — Match Against Our Catalogue

### 1. Cleaned Catalogue Details

- File Path: `cleaned/all_standards.csv`
- Total Row Count: **23,866**
- Exact Column Names: `['standard_number', 'title', 'publication_date', 'type', 'degree_of_equivalence', 'department', 'original_source_file']`

15 Sample Rows (`standard_number` column):
```
 1. IS 12437:2026
 2. IS 6274:2026
 3. IS 6092 (Part 6):2026
 4. IS 4668:2026
 5. IS 11691:2026
 6. IS 13730 (Part 57):2026
 7. IS 13730 (Part 58):2026
 8. IS 13730 (Part 60):2026
 9. IS 18991:2026
 10. IS 17822:2026
 11. IS 18990:2026
 12. IS 16503 (Part 4):2026
 13. IS 18987:2026
 14. IS 18988:2026
 15. IS 18989:2026
```

### 2. Normalizer & Index Filename Patterns

Normalizer maps strings to `(base_number, part_string, year_string)` tuples:
- Catalogue input e.g. `IS 2062 (Part 1) : 2011` -> `("2062", "1", "2011")`
- Index filename input e.g. `is.2062.1.2011.pdf` -> `("2062", "1", "2011")`

Observed Index Filename Structure Patterns:
1. `is.<num>.<year>.pdf`: 12,471 files (e.g. `is.2062.2011.pdf`)
2. `is.<num>.<part>.<year>.pdf`: 4,818 files (e.g. `is.1363.1.2002.pdf`)
3. `is.<num>.<part1>.<part2>.<year>.pdf`: 1,189 files (e.g. `is.548.2.9.1988.pdf`)
4. `is.<num>.<suffix>.<year>.pdf`: 335 files (e.g. `is.196.b.1966.pdf`, `is.786.s.b.1967.pdf`)
5. Non-standard format: 8 files

### 3. Match Statistics

- **(a) Match by Base Number (regardless of year)**: **17,129** / 23,866 (**71.77%**)
- **(b) Exact Match by Base Number + Year**: **9,299** / 23,866 (**38.96%**)
- **Superseded Edition Matches**: **1,235** cases (where indexed PDF year is older than catalogue record year for the same base standard).

### 4. 25 Random Matched Examples

```
 1. Catalogue [IS 14877 (Part 1):2000] : "Hydraulic presses - Straight sided column/C - Frame type: Part 1 test chart for geometrical accuracy"
    Matched Index File: [S01] is.14877.1.2000.pdf

 2. Catalogue [IS 10694 (Part 6):2009] : "Automotivevehicles - Rims - Generalrequirements: Part 6 rims for agricultural tractors,tillers and implements (Second Revision)"
    Matched Index File: [S13] is.10694.1.2009.pdf

 3. Catalogue [IS 12251:1987] : "Code of practice for drainage of building basements"
    Matched Index File: [S03] is.12251.1987.pdf

 4. Catalogue [IS 12861:1989] : "Fire fighting - Double bit axe for forest fires - Specification"
    Matched Index File: [S03] is.12861.1989.pdf

 5. Catalogue [IS 8023:1991] : "Gauges - Single ended progressive type plate snap gauges (Up to 160 mm) - Specification (First Revision)"
    Matched Index File: [S01] is.8023.1991.pdf

 6. Catalogue [IS 14515:1998] : "Fish pickles - Specification"
    Matched Index File: [S06] is.14515.1998.pdf

 7. Catalogue [IS 401:2001] : "Preservation of Timber - Code of Practice (Fourth Revision)"
    Matched Index File: [S03] is.401.2001.pdf

 8. Catalogue [IS 3140:1965] : "Code of practice for painting asbestos cement building products"
    Matched Index File: [S03] is.3140.1965.pdf

 9. Catalogue [IS 7910:2003] : "Monoethanolamine - Specification (First Revision)"
    Matched Index File: [S11] is.7910.2003.pdf

 10. Catalogue [IS 3346:1980] : "Method for the determination of thermal conductivity of thermal insulation materials (Two Slab, Guarded Hot - Plate Method) (First Revision)"
     Matched Index File: [S02] is.3346.1980.pdf

 11. Catalogue [IS 9967 (Part 3):2008] : "Milk and milk products - Determination of nitrate and nitrite contents: Part 3 method using cadmium reduction and flow injection analysis with in - Line dialysis (Routine Method) (Second Revision)"
     Matched Index File: [S06] is.9967.1.2008.pdf

 12. Catalogue [IS 7079:2008] : "Automotive vehicles - Brake hose assemblies forhydraulicbraking systems used with non - Petroleum base brake fluid specification (Third Revision)"
     Matched Index File: [S13] is.7079.2008.pdf

 13. Catalogue [IS 15144:2002] : "Indexable hardmetal (Carbide) inserts with rounded corners with partly cylindrical fixing hole -- Dimensions of inserts with 7° normal clearance for light alloy and plastic components turning"
     Matched Index File: [S01] is.15144.2002.pdf

 14. Catalogue [IS 1448 (Part 58):1991] : "Methods of test for petroleum and its products [P: 58] determination of insolubles in greases (First Revision)"
     Matched Index File: [S11] is.1448.18.1991.pdf

 15. Catalogue [IS 13018:1990] : "Internal combustion of test for pressure engines - Method charged engines"
     Matched Index File: [S13] is.13018.1990.pdf

 16. Catalogue [IS 6191:1971] : "Micro - Biological colour fastness and microscopical tests for leather"
     Matched Index File: [S02] is.6191.1971.pdf

 17. Catalogue [IS 1132:2009] : "Bicycle - Bottom bracket ball cups - Specification (Third Revision)"
     Matched Index File: [S13] is.1132.2009.pdf

 18. Catalogue [IS 8694:1978] : "Specification for latex bladders, seamless, valve type"
     Matched Index File: [S11] is.8694.1978.pdf

 19. Catalogue [IS 9401 (Part 14):1992] : "Method of measurement of works in river valley projects (Damsand Appurtenantstructures): Part 14 canal works"
     Matched Index File: [S14] is.9401.12.1992.pdf

 20. Catalogue [IS 3096:1965] : "Specification for fine grade palladium"
     Matched Index File: [S10] is.3096.1965.pdf

 21. Catalogue [IS 9642:1980] : "Dimensions for case pipe for wrist watch case"
     Matched Index File: [S01] is.9642.1980.pdf

 22. Catalogue [IS 13161 (Part 4):1991] : "Shipbuilding - Noise levels onboard ships: Part 4 noise exposure limits"
     Matched Index File: [S13] is.13161.1.1991.pdf

 23. Catalogue [IS 4571:1977] : "Specification for aluminium extension ladders for fire brigade use (First Revision)"
     Matched Index File: [S03] is.4571.1977.pdf

 24. Catalogue [IS 12405:1988] : "Specification for gear type flexible couplings"
     Matched Index File: [S01] is.12405.1988.pdf

 25. Catalogue [IS 16029:2012] : "Roasted ground coffee - Determination of moisture content - Karl fischer method (Reference Method)"
     Matched Index File: [S06] is.16029.2012.pdf
```

### 5. Breakdown by Standard Type & Department

#### Top 20 `type` Values (Matched vs Unmatched):

| Standard Type | Count Matched | Count Unmatched |
| :--- | :--- | :--- |
| Product Specification | 4,964 | 5,900 |
| Methods of Tests | 1,699 | 3,573 |
| Code of Practice | 1,335 | 1,831 |
| Others | 479 | 1,397 |
| Terminology | 340 | 543 |
| Dimensions | 369 | 292 |
| Safety Standard | 69 | 348 |
| System Standard | 23 | 225 |
| Service Specification | 7 | 219 |
| Process Specification | 5 | 141 |
| Unspecified (`-`) | 9 | 98 |

#### Top `department` Values (Matched vs Unmatched):
- All 23,866 rows in `cleaned/all_standards.csv` have `department` = `Unknown`.

### 6. Prioritized Candidates Match Check (`cleaned/gold_candidates.csv`)

- Total Prioritized Candidates: **30**
- Matched by Base Number: **22** / 30
- Matched by Exact Base Number + Year: **11** / 30
- Unmatched Candidates (8 total): standards published in 2026 (`IS 19763:2026`, `IS 19783:2026`, `IS 19773:2026`, `IS 19780:2026`, `IS 19771:2026`, `IS 17039:2026`, `IS 16783:2026`, `IS 19821:2026`).

Candidate match status per item:

```
 1. [IS 15627:2022] -> Match: is.15627.2005.pdf (BASE_ONLY)
 2. [IS 14900:2026] -> Match: is.14900.2000.pdf (BASE_ONLY)
 3. [IS 19763:2026] -> Match: NO MATCH (NONE)
 4. [IS 19783:2026] -> Match: NO MATCH (NONE)
 5. [IS 11916:2026] -> Match: is.11916.2001.pdf (BASE_ONLY)
 6. [IS 8694:1978]  -> Match: is.8694.1978.pdf (EXACT)
 7. [IS 8688:2004]  -> Match: is.8688.1988.pdf (BASE_ONLY)
 8. [IS 7928:1993]  -> Match: is.7928.1993.pdf (EXACT)
 9. [IS 7899:2006]  -> Match: is.7899.2006.pdf (EXACT)
 10. [IS 7538:1996] -> Match: is.7538.1996.pdf (EXACT)
 11. [IS 6639:1972] -> Match: is.6639.1972.pdf (EXACT)
 12. [IS 6529:1996] -> Match: is.6529.1996.pdf (EXACT)
 13. [IS 4373:1967] -> Match: is.4373.1967.pdf (EXACT)
 14. [IS 2373:1981] -> Match: is.2373.1981.pdf (EXACT)
 15. [IS 2255:1977] -> Match: is.2255.1977.pdf (EXACT)
 16. [IS 1852:1985] -> Match: is.1852.1985.pdf (EXACT)
 17. [IS 12818:2010]-> Match: is.12818.2010.pdf (EXACT)
 18. [IS 5085:2026] -> Match: is.5085.1976.pdf (BASE_ONLY)
 19. [IS 14351:2026]-> Match: is.14351.1996.pdf (BASE_ONLY)
 20. [IS 2637:2025] -> Match: is.2637.2004.pdf (BASE_ONLY)
 21. [IS 19773:2026]-> Match: NO MATCH (NONE)
 22. [IS 19780:2026]-> Match: NO MATCH (NONE)
 23. [IS 1887:2026] -> Match: is.1887.1985.pdf (BASE_ONLY)
 24. [IS 8572:2025] -> Match: is.8572.1993.pdf (BASE_ONLY)
 25. [IS 7039:2026] -> Match: is.7039.1973.pdf (BASE_ONLY)
 26. [IS 13123:2025]-> Match: is.13123.2000.pdf (BASE_ONLY)
 27. [IS 19771:2026]-> Match: NO MATCH (NONE)
 28. [IS 17039:2026]-> Match: NO MATCH (NONE)
 29. [IS 16783:2026]-> Match: NO MATCH (NONE)
 30. [IS 19821:2026]-> Match: NO MATCH (NONE)
```

---

## FACTS ONLY

- **Total PDFs Indexed**: 18,821 across 14 subdirectories (`S01` to `S14`).
- **Download Success Rate (Probes)**: 5 / 5 (100% success, 0 HTTP 404s).
- **OCR-Needed Rate (First 3 Pages of Probes)**: 5 / 5 (100% of tested probe PDFs contain 0 digital text characters on Pages 2 & 3 due to image scans of original cover pages; body pages contain OCR text).
- **Catalogue Matching Rate (Base Number)**: 17,129 / 23,866 (71.77%).
- **Catalogue Matching Rate (Exact Base Number + Year)**: 9,299 / 23,866 (38.96%).
- **Superseded Edition Matches**: 1,235.
- **Prioritized Candidates Match Rate**: 22 / 30 (Base Number), 11 / 30 (Exact Base Number + Year).
