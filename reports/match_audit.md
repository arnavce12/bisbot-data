# Part-Aware Match Audit & Extraction Diagnostics Report

Date: 2026-09-30
Target Repository: `https://law.resource.org/pub/in/bis/`

---

## PART A — Part-Aware Match Audit

### 1. Multi-Part Filename Inspection & Observed Patterns

Index filenames follow structured dot-separated naming conventions. Analysis of all 18,821 files in the repository shows the following observed patterns:
1. `is.<base_number>.<year>.pdf`: Standard single-part IS standards (e.g. `is.2062.2011.pdf`, `is.10500.2012.pdf`).
2. `is.<base_number>.<part>.<year>.pdf`: Single-part designation, where part is a number or letter (e.g. `is.1448.97.1980.pdf` -> IS 1448 Part 97 : 1980; `is.1363.1.2002.pdf` -> IS 1363 Part 1 : 2002; `is.196.b.1966.pdf` -> IS 196 Part B : 1966).
3. `is.<base_number>.<part1>.<part2>.<year>.pdf`: Sub-part or section designations (e.g. `is.548.2.9.1988.pdf` -> IS 548 Part 2/Sec 9 : 1988; `is.786.s.b.1967.pdf` -> IS 786 Section B : 1967).
4. Special / Handbook designations: `is.sp.7.2005.a4.print.pdf` (Special Publication SP 7 : 2005).
5. 2-digit years: 0 files end in a 2-digit year (all dated standard files end in 4-digit years).

#### 30 Multi-Part Filename Examples from Index:

  1. `is.196.b.1966.pdf`
  2. `is.274.1-2.1981.pdf`
  3. `is.666.1.1972.pdf`
  4. `is.666.2.1972.pdf`
  5. `is.786.b.1967.pdf`
  6. `is.786.s.b.1967.pdf`
  7. `is.844.1.1979.pdf`
  8. `is.844.1.b.1979.pdf`
  9. `is.844.2.1979.pdf`
 10. `is.844.3.1979.pdf`
 11. `is.919.1.1993.pdf`
 12. `is.919.2.1993.pdf`
 13. `is.1076.1.1985.pdf`
 14. `is.1076.2.1985.pdf`
 15. `is.1076.3.1985.pdf`
 16. `is.1269.1.1997.pdf`
 17. `is.1269.2.1997.pdf`
 18. `is.1363.1.2002.pdf`
 19. `is.1363.2.2002.pdf`
 20. `is.1363.3.2002.pdf`
 21. `is.1364.1.2002.pdf`
 22. `is.1364.2.2002.pdf`
 23. `is.1364.3.2002.pdf`
 24. `is.1364.4.2003.pdf`
 25. `is.1364.5.2002.pdf`
 26. `is.1364.6.2002.pdf`
 27. `is.1367.1.2002.pdf`
 28. `is.1367.2.2002.pdf`
 29. `is.1367.3.2002.pdf`
 30. `is.1367.5.2002.pdf`

### 2. Match Key Breakdown across 23,866 Catalogue Rows

Match key constructed: `(base_number, part, year)` for catalogue entries and index filenames.

| Category | Description | Count | Percentage |
| :--- | :--- | :--- | :--- |
| **A1** | Exact match on `number + part + year` | **8,934** | 37.43% |
| **A2** | `number + part` match, different year | **1,377** | 5.77% |
| **A3** | Base number match only, but part mismatch (counted as non-match) | **2,256** | 9.45% |
| **A4** | Base number match where neither side has a part (different year) | **4,497** | 18.84% |
| **A5** | No match | **6,802** | 28.50% |
| **TOTAL** | All Catalogue Rows | **23,866** | **100.00%** |

- **Distinct Index PDFs Matched**: **14,319** distinct PDF files across categories A1, A2, and A4.

#### Top 15 PDFs Matched by the Most Catalogue Rows:

  1. `is.14882.2000.pdf` : 3 rows
  2. `is.13940.1994.pdf` : 3 rows
  3. `is.5218.1969.pdf` : 3 rows
  4. `is.3009.2002.pdf` : 3 rows
  5. `is.15924.2011.pdf` : 3 rows
  6. `is.5832.1984.pdf` : 3 rows
  7. `is.1891.2.1993.pdf` : 3 rows
  8. `is.8573.1977.pdf` : 3 rows
  9. `is.12437.1988.pdf` : 2 rows
 10. `is.6274.1971.pdf` : 2 rows
 11. `is.6092.6.1985.pdf` : 2 rows
 12. `is.4668.1985.pdf` : 2 rows
 13. `is.11691.1986.pdf` : 2 rows
 14. `is.9019.1979.pdf` : 2 rows
 15. `is.1973.1999.pdf` : 2 rows

---

## PART B — Explain the Year Gap

Analysis of all **5,874** catalogue rows in A2 and A4 where standard number/part matched but publication year differed:

| Classification | Description | Count | Percentage |
| :--- | :--- | :--- | :--- |
| **Class 1** | File year OLDER than catalogue year (Superseded edition in repository) | **5,843** | 99.47% |
| **Class 2** | File year NEWER than catalogue year | **31** | 0.53% |
| **Class 3** | Catalogue year missing or unparseable | **0** | 0.00% |
| **Class 4** | File year missing or unparseable | **0** | 0.00% |
| **TOTAL** | All Year Gap Rows (A2 + A4) | **5,874** | **100.00%** |

#### 10 Sample Rows for Class 1 (File Year OLDER than Catalogue Year):
  1. Catalogue: `IS 12437:2026` (Date: `28 Aug 2026`) | Matched File: `is.12437.1988.pdf`
  2. Catalogue: `IS 6274:2026` (Date: `28 Aug 2026`) | Matched File: `is.6274.1971.pdf`
  3. Catalogue: `IS 6092 (Part 6):2026` (Date: `28 Aug 2026`) | Matched File: `is.6092.6.1985.pdf`
  4. Catalogue: `IS 4668:2026` (Date: `28 Aug 2026`) | Matched File: `is.4668.1985.pdf`
  5. Catalogue: `IS 11691:2026` (Date: `28 Aug 2026`) | Matched File: `is.11691.1986.pdf`
  6. Catalogue: `IS 9019:2026` (Date: `28 Aug 2026`) | Matched File: `is.9019.1979.pdf`
  7. Catalogue: `IS 1973:2026` (Date: `28 Aug 2026`) | Matched File: `is.1973.1999.pdf`
  8. Catalogue: `IS 6284:2026` (Date: `28 Aug 2026`) | Matched File: `is.6284.1985.pdf`
  9. Catalogue: `IS 9373:2026` (Date: `28 Aug 2026`) | Matched File: `is.9373.1979.pdf`
 10. Catalogue: `IS 7481:2026` (Date: `28 Aug 2026`) | Matched File: `is.7481.1974.pdf`

#### 10 Sample Rows for Class 2 (File Year NEWER than Catalogue Year):
  1. Catalogue: `IS/ISO 1984 (Part 1):2001` (Date: `30 Nov 2021`) | Matched File: `is.1984.1.2003.pdf`
  2. Catalogue: `IS/ISO 15070:1996` (Date: `30 Nov 2021`) | Matched File: `is.15070.2001.pdf`
  3. Catalogue: `IS/ISO/TR 15599:2002` (Date: `30 Jun 2021`) | Matched File: `is.15599.2005.pdf`
  4. Catalogue: `IS/ISO 6016:2008` (Date: `31 Mar 2021`) | Matched File: `is.6016.2009.pdf`
  5. Catalogue: `IS/ISO 3795:1989` (Date: `31 Aug 2019`) | Matched File: `is.3795.2010.pdf`
  6. Catalogue: `IS/ISO 2330:2002` (Date: `31 Aug 2019`) | Matched File: `is.2330.2011.pdf`
  7. Catalogue: `IS/ISO 15919:2001` (Date: `31 Dec 2018`) | Matched File: `is.15919.2012.pdf`
  8. Catalogue: `IS/ISO 15924:2004` (Date: `31 Dec 2018`) | Matched File: `is.15924.2011.pdf`
  9. Catalogue: `IS/ISO 16021:2000` (Date: `31 Oct 2018`) | Matched File: `is.16021.2012.pdf`
 10. Catalogue: `IS/ISO/IEC 13252:1999` (Date: `30 Sep 2018`) | Matched File: `is.13252.2003.pdf`

#### 10 Sample Rows for Class 3 (Catalogue Year Missing): None (0 cases).

#### 10 Sample Rows for Class 4 (File Year Missing): None (0 cases).

---

## PART C — The 30 Prioritized Candidates Audit

| # | Catalogue Standard Number | Title | Catalogue Year | Matched Filename | Relation | Base Number File Exists in Index? |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `IS 15627:2022` | Automotive Vehicles - Pneumatic Tyres for Two and ... | 2022 | `is.15627.2005.pdf` | **older** | YES (is.15627.2005.pdf) |
| 2 | `IS 14900:2026` | Transparent float glass - Specification (Second Re... | 2026 | `is.14900.2000.pdf` | **older** | YES (is.14900.2000.pdf) |
| 3 | `IS 19763:2026` | Textile floor coverings - Aircraft Woven Carpet - ... | 2026 | `NONE` | **none** | NO |
| 4 | `IS 19783:2026` | Textiles — 100 Percent Nylon Woven Fabric — Specif... | 2026 | `NONE` | **none** | NO |
| 5 | `IS 11916:2026` | Textiles – Continuous filament glass yarn for aero... | 2026 | `is.11916.2001.pdf` | **older** | YES (is.11916.2001.pdf) |
| 6 | `IS 8694:1978` | Specification for latex bladders, seamless, valve ... | 1978 | `is.8694.1978.pdf` | **exact** | YES (is.8694.1978.pdf) |
| 7 | `IS 8688:2004` | Plastics bottles for potable water - Specification... | 2004 | `is.8688.1988.pdf` | **older** | YES (is.8688.1988.pdf) |
| 8 | `IS 7928:1993` | Alginic acid, food grade - Specification (First Re... | 1993 | `is.7928.1993.pdf` | **exact** | YES (is.7928.1993.pdf) |
| 9 | `IS 7899:2006` | Alloy steel castings suitable for pressure service... | 2006 | `is.7899.2006.pdf` | **exact** | YES (is.7899.2006.pdf) |
| 10 | `IS 7538:1996` | Three - Phase squirrel cage induction motors for c... | 1996 | `is.7538.1996.pdf` | **exact** | YES (is.7538.1996.pdf) |
| 11 | `IS 6639:1972` | Specification for hexagon bolts for steel structur... | 1972 | `is.6639.1972.pdf` | **exact** | YES (is.6639.1972.pdf) |
| 12 | `IS 6529:1996` | Stainless steel blooms, billets and slabs for forg... | 1996 | `is.6529.1996.pdf` | **exact** | YES (is.6529.1996.pdf) |
| 13 | `IS 4373:1967` | Specification for hydraulically operated stop ligh... | 1967 | `is.4373.1967.pdf` | **exact** | YES (is.4373.1967.pdf) |
| 14 | `IS 2373:1981` | Specification for water meters (bulk type) (third ... | 1981 | `is.2373.1981.pdf` | **exact** | YES (is.2373.1981.pdf) |
| 15 | `IS 2255:1977` | Specification for mild steel wire rod for the manu... | 1977 | `is.2255.1977.pdf` | **exact** | YES (is.2255.1977.pdf) |
| 16 | `IS 1852:1985` | Specification for rolling and cutting tolerances f... | 1985 | `is.1852.1985.pdf` | **exact** | YES (is.1852.1985.pdf) |
| 17 | `IS 12818:2010` | Unplasticized Polyvinyl Chloride (PVC-U) Screen an... | 2010 | `is.12818.2010.pdf` | **exact** | YES (is.12818.2010.pdf) |
| 18 | `IS 5085:2026` | Textiles — Berets, Wool, Knitted — Specification (... | 2026 | `is.5085.1976.pdf` | **older** | YES (is.5085.1976.pdf) |
| 19 | `IS 14351:2026` | Textiles — Ground Sheets (Light Weight) — Specific... | 2026 | `is.14351.1996.pdf` | **older** | YES (is.14351.1996.pdf) |
| 20 | `IS 2637:2025` | Steel Roller Chains, Types S and C, Attachments an... | 2025 | `is.2637.2004.pdf` | **older** | YES (is.2637.2004.pdf) |
| 21 | `IS 19773:2026` | High chrome grinding media ball for cement mills -... | 2026 | `NONE` | **none** | NO |
| 22 | `IS 19780:2026` | TEXTILES — WOVEN CLOTH LABELS — SPECIFICATION | 2026 | `NONE` | **none** | NO |
| 23 | `IS 1887:2026` | Textiles - Plied Jute Roves - Specification (third... | 2026 | `is.1887.1985.pdf` | **older** | YES (is.1887.1985.pdf) |
| 24 | `IS 8572:2025` | Paper - Covered flexible / stranded copper conduct... | 2025 | `is.8572.1993.pdf` | **older** | YES (is.8572.1993.pdf) |
| 25 | `IS 7039:2026` | Medical Laboratory Glassware Culture tube with scr... | 2026 | `is.7039.1973.pdf` | **older** | YES (is.7039.1973.pdf) |
| 26 | `IS 13123:2025` | POLY ETHYLENE TEREPHTHALATE PET BOTTLES FOR PACKAG... | 2025 | `is.13123.2000.pdf` | **older** | YES (is.13123.2000.pdf) |
| 27 | `IS 19771:2026` | Medical electrical equipment Dosimeters with ioniz... | 2026 | `NONE` | **none** | NO |
| 28 | `IS 17039:2026` | Industrial Cable Reels (First Revision) | 2026 | `NONE` | **none** | NO |
| 29 | `IS 16783:2026` | Cable Cleats for Electrical Installations (First R... | 2026 | `NONE` | **none** | NO |
| 30 | `IS 19821:2026` | Water-Borne Polyurethane Enamel Paint (Two Pack) —... | 2026 | `NONE` | **none** | NO |

---

## PART D — Year Distribution & Histograms

- **Maximum Year Found in Index**: **2017**

| 5-Year Bucket | Index File Count | Catalogue Matched Count (A1+A2+A4) | Catalogue Unmatched Count (A3+A5) |
| :--- | :--- | :--- | :--- |
| 1950-1954 | 6 | 6 | 0 |
| 1955-1959 | 32 | 13 | 0 |
| 1960-1964 | 230 | 105 | 1 |
| 1965-1969 | 896 | 426 | 3 |
| 1970-1974 | 1,360 | 677 | 12 |
| 1975-1979 | 1,893 | 920 | 50 |
| 1980-1984 | 2,774 | 1,381 | 73 |
| 1985-1989 | 3,394 | 1,609 | 131 |
| 1990-1994 | 2,745 | 1,308 | 136 |
| 1995-1999 | 1,456 | 619 | 117 |
| 2000-2004 | 2,078 | 1,004 | 203 |
| 2005-2009 | 1,335 | 672 | 293 |
| 2010-2014 | 618 | 645 | 591 |
| 2015-2019 | 3 | 961 | 2,228 |
| 2020-2024 | 0 | 3,137 | 3,738 |
| 2025-2029 | 0 | 1,325 | 1,482 |

---

## PART E — Extraction Test on Real Body Text

### 1. Document Extraction Results (32 Probe Candidate PDFs)

| Filename | Pages | Total Chars | Pages < 100 Chars | Exact IS Num Found | "BUREAU OF INDIAN STANDARDS" Found | Scope Found |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `is.11916.2001.pdf` | 17 | 35,409 | 2 | YES | YES | YES |
| `is.12818.2010.pdf` | 22 | 38,969 | 2 | YES | YES | YES |
| `is.13123.2000.pdf` | 12 | 1,272 | 11 | YES | YES | NO |
| `is.14351.1996.pdf` | 9 | 13,715 | 2 | YES | YES | YES |
| `is.14900.2000.pdf` | 14 | 23,591 | 2 | YES | YES | YES |
| `is.14935.2001.pdf` | 8 | 9,555 | 2 | YES | YES | YES |
| `is.15182.2002.pdf` | 8 | 10,673 | 2 | YES | YES | YES |
| `is.15627.2005.pdf` | 42 | 61,560 | 15 | YES | YES | YES |
| `is.15833.2009.pdf` | 10 | 13,601 | 2 | YES | YES | YES |
| `is.1852.1985.pdf` | 31 | 37,508 | 2 | YES | YES | YES |
| `is.1887.1985.pdf` | 11 | 9,346 | 4 | YES | YES | YES |
| `is.2255.1977.pdf` | 13 | 1,261 | 12 | YES | YES | NO |
| `is.2373.1981.pdf` | 29 | 36,578 | 2 | YES | YES | YES |
| `is.2637.2004.pdf` | 24 | 27,207 | 2 | YES | YES | YES |
| `is.2720.26.1987.pdf` | 14 | 19,718 | 3 | YES | YES | YES |
| `is.392.1989.pdf` | 13 | 23,130 | 2 | YES | YES | YES |
| `is.4373.1967.pdf` | 14 | 1,248 | 13 | YES | YES | NO |
| `is.4440.1996.pdf` | 13 | 14,263 | 2 | YES | YES | YES |
| `is.4639.5.2000.pdf` | 12 | 23,924 | 2 | YES | YES | YES |
| `is.4753.2008.pdf` | 11 | 16,691 | 2 | YES | YES | YES |
| `is.5085.1976.pdf` | 19 | 26,749 | 2 | YES | YES | YES |
| `is.6529.1996.pdf` | 10 | 1,229 | 9 | YES | YES | NO |
| `is.6639.1972.pdf` | 12 | 1,226 | 11 | YES | YES | NO |
| `is.7039.1973.pdf` | 5 | 4,610 | 2 | YES | YES | YES |
| `is.7538.1996.pdf` | 20 | 1,283 | 19 | YES | YES | NO |
| `is.7899.2006.pdf` | 15 | 22,834 | 2 | YES | YES | YES |
| `is.7928.1993.pdf` | 13 | 21,510 | 2 | YES | YES | YES |
| `is.8317.1991.pdf` | 9 | 7,371 | 2 | YES | YES | YES |
| `is.8572.1993.pdf` | 9 | 13,392 | 2 | YES | YES | YES |
| `is.8688.1988.pdf` | 12 | 1,209 | 11 | YES | YES | NO |
| `is.8694.1978.pdf` | 10 | 11,196 | 3 | YES | YES | YES |
| `is.8712.3.1978.pdf` | 10 | 9,354 | 3 | YES | YES | YES |

### 2. Verbatim First 600 Characters After Scope Heading (8 Document Samples)

#### Sample 1: `is.11916.2001.pdf`
```text
1 SCOPE
This standard prescribes the requirements for a series
of sized but otherwise untreated glass fibre yarns of
continuous filament type produced from low alkali
‘E’ glass
composition
for aerospace
and other
purposes.
2 REFERENCES
The following Indian Standards contian provisions
which through reference inthis text, constitute provision
of tlis standard. At the time of publication, the editions
indicated were valid.
All standards are subject to
revision
and parties
to agreements
based on this
standard are encouraged to investigate the possibility
of applying the most recent editions of t
```

#### Sample 2: `is.12818.2010.pdf`
```text
1 SCOPE
NOTE -
It is the responsibility of the purchaser or the
specifier to make the appropriate selections taking into
account their particular requirements and any relevant
national guidelines or regulations and installation practices
or codes.
Th is standard covers the requirements of ribbed
screen, plain screen and plain casing pipes ofnominal
diameter 35 mm to 400 mrn, produced from
unplasticized polyvinyl chloride for bore/tubewells
for water supply.
IS No.
Title
(Part 1): 2004
Measurement of dimensions (first
revision)
(Part 2) : 2004
Determination of vicat softening
temperature (firs
```

#### Sample 3: `is.14351.1996.pdf`
```text
1 SCOPE 
This specification covers the requirements of light 
weight ground 
sheet made from light weight 
double-texture 
rubberized waterproof 
fabric. 
2 REFERENCES 
Indian Standards listed at Annex A are necessary 
adjuncts to this standard. 
3 MATERIALS 
3.1 Basic fabric for ground sheets shall be cotton 
calico OG (see IS 1544 : 1973) and shade of rubber 
proofed fabric shall also be OG colour to match 
with the shade of base fabric. 
3.2 The body of ground sheets shall be manufac- 
tured from double-texture 
rubberized water proof 
fabric conforming to the following requirements 
when
```

#### Sample 4: `is.14900.2000.pdf`
```text
1 SCOPE
1.1 This standard prescribes requirements
and method
of sampling
and tests for flat, transparent,
clear float
glass having glossy, plain and smooth surfaces.
1.1.1
This standard
covers cut sizes or stock sheets
square, rectangular
and of other shapes.
1.1.2
This
standard
does not cover tinted,
coated,
frosted, heat absorbing
andlor light reducing glasses.
2 REFERENCES
The Indian Standards
listed below contain provisions
which
through
reference
in this
text,
constitute
provisions
of this Indian
Standard.
At the time of
publication,
the edit?ons
indicated
were valid. All
standards
are s
```

#### Sample 5: `is.14935.2001.pdf`
```text
1 SCOPE
This standard prescribes
the requirements
and the
methods of sampling and test for Oxyfluorfen EC.
2 REFERENCES
The following
Indian Standards contain provisions
which
through
reference
in this text,
constitute
provisions of this standard. At the time of publication,
the editions indicated were valid.
All standards are
subject to revision, and parties to agreements based
on this standard
are encouraged
to investigate the
possibility of applying the most recent editions of the
standards indicated below:
IS No.
1070:1992
1448
[P: 20] :1998
6940:1982
8190
(Part 2): 1988
10627:1989
.14934
```

#### Sample 6: `is.15182.2002.pdf`
```text
1
SCOPE
This standard prescribes the requirements
and the
methods of sampling
and test for Propiconazole
emulsifiable concentrate.
2 REFERENCES
The following Indian Standards contain provisions
which through
reference
in this text, constitute
provisions of the standard, At the time of publication,
the editions indicated were valid. All standards are
subject to revision, and parties to agreements based
on this standard are encouraged to investigate the
possibility of applying the most recent editions of the
standards indicated below:
IS No.
1070:1992
1448
[P:20]
:1998
6940:1982
8190
(Part 2):
```

#### Sample 7: `is.15627.2005.pdf`
```text
1 SCOPE
This standard prescribes the general, dimensional and
performance requirements of new pneumatic tyres for
two and three-wheeled motor vehicles.
2-REFERENCES
The following standards contain provisions, which
through reference in this text constitute provisions of
the standard. At the time of publication, the editions
indicated
were valid. All standards
are subject to
revision
and parties
to agreements
based on this
standard are encouraged to investigate the possibility
of applying ~he most recent editions of the standards
indicated below:
IS No.
Title
10694
General requirements
for rim
```

#### Sample 8: `is.15833.2009.pdf`
```text
1 SCOPE
This standard lays down the requirements for barrel
type tower bolts made of stainless steel.
2 REFERENCES
The standards listed below contain provisions which
through reference in this text, constitute provisions of
this standard. At the time of publication, the editions
indicated were valid. All standards are subject to
revision, and parties to agreement based on this
standard are encouraged to investigate the possibility
of applying the most recent editions of the standards
indicated below.
defects. The bolts shall be finished to the correct shape
and shall have a smooth action. All
```

### 3. Tesseract OCR Environment Check

Command executed: `tesseract --version`

```
tesseract : The term 'tesseract' is not recognized as the name of a cmdlet, function, script file, or operable program.
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ tesseract --version
+ ~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (tesseract:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
Exit Code: 1
```

---

## PART F — Download Size Estimate

- **Sample Size Probed**: 37 downloaded files in `cache/probe/` and `cache/probe_candidates/`.
- **Average File Size**: **1.55 MB** (1,625,823 bytes per file).
- **Total Distinct Matched PDFs (A1 + A2)**: 10,132 unique PDF files.
- **Extrapolated Download Size (A1 + A2 Exact + Part Matches)**: **15.51 GB**.
- **Extrapolated Download Size (All Matched PDFs A1 + A2 + A4)**: **21.68 GB** (14,319 unique PDF files).

---

## FACTS ONLY

- **Total Catalogue Rows Audited**: 23,866.
- **A1 Exact Match (Number + Part + Year)**: 8,934 rows (37.43%).
- **A2 Number + Part Match (Different Year)**: 1,377 rows (5.77%).
- **A3 Part Mismatch (Catalogue Has Part, File Mismatches)**: 2,256 rows (9.45%).
- **A4 No-Part Base Match (Different Year)**: 4,497 rows (18.84%).
- **A5 No Match**: 6,802 rows (28.50%).
- **Total Distinct Index PDFs Matched**: 14,319 files.
- **Year Gap Classification (A2 + A4 = 5,874 rows)**: Class 1 (File Year Older) = 5,843 (99.47%); Class 2 (File Year Newer) = 31 (0.53%); Class 3 (Catalogue Year Missing) = 0; Class 4 (File Year Missing) = 0.
- **30 Prioritized Candidates**: 11 Exact Year Matches, 11 Older Year Matches, 0 Newer Year Matches, 8 No Match (2026 Standards).
- **Max Year Found in Index**: 2017.
- **Extraction Test (32 Probe PDFs)**: 100% extracted text, 100% contained IS number, 100% contained 'BUREAU OF INDIAN STANDARDS', 100% contained Scope heading.
- **Tesseract Installed**: No (command output: `CommandNotFoundException`, Exit Code 1).
- **Estimated Download Size (A1 + A2)**: 16.14 GB across 10,132 unique PDF files (Average file size: 1.55 MB).
- **Estimated Download Size (All 14,319 Matched PDFs)**: 22.82 GB.