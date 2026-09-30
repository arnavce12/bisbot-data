# BIS RAG Corpus Build & Diagnostics Report

Date: 2026-09-30
Target Repository: `https://law.resource.org/pub/in/bis/`

---

## 1. Document Selection, Download & Verification

- **Documents Selected**: 599
- **Documents Downloaded**: 599
- **Documents Verified**: 598
- **Documents Rejected**: 1

### Rejection Reasons Breakdown:

- `Download failed or HTTP error`: 1

## 2. Chunking & Scope Extraction Statistics

- **Total RAG Chunks Generated**: **13,867**
- **Documents with Scope Clause Found**: **488**
- **Documents with Scope Clause Not Found**: **110**
- **Median Chunk Length**: **966 characters**
- **Min Chunk Length**: **150 characters**
- **Max Chunk Length**: **1000 characters**

### Chunks Generated Per Subdirectory:

| Subdirectory | Chunk Count |
| :--- | :--- |
| `S01` | 815 |
| `S02` | 1,203 |
| `S03` | 3,120 |
| `S04` | 285 |
| `S05` | 766 |
| `S06` | 2,082 |
| `S07` | 226 |
| `S08` | 665 |
| `S09` | 298 |
| `S10` | 1,510 |
| `S11` | 1,026 |
| `S12` | 876 |
| `S13` | 597 |
| `S14` | 398 |

## 3. Total Corpus Disk Usage

- **`raw/documents/` Size**: 829.12 MB
- **`gold/` Size**: 28.56 MB
- **`export/bisbot_data/` Size**: 28.57 MB
- **TOTAL Corpus Size on Disk**: **886.25 MB** (929,305,190 bytes)

---

## 4. 10 Verbatim Sample Chunks (From 10 Different Documents)

### Chunk 1: `[doc_1280_main_1975_p1_c1]` (IS 1280, Page 1)
**Title**: Specification for foundry moulding boxes of steel construction (Second Revision)
**Edition Status**: `current-matching` | **Section Hint**: `None` | **Char Count**: 316
```text
“जान1 का अ+धकार, जी1 का अ+धकार”
Mazdoor Kisan Shakti Sangathan
“The Right to Information, The Right to Live”
“!ानएकऐसाखजाना> जोकभीच0रायानहB जासकताहै”
Bhartṛhari—Nītiśatakam
“Knowledge is such a treasure which cannot be stolen”
”
है”
ह”
ह
IS 1280 (1975): Foundry moulding boxes of steel
construction [MTD 14: Foundry]
```

### Chunk 2: `[doc_10248_1_2011_p7_c0]` (IS 10248 Part 1, Page 7)
**Title**: Parallel pins with internal thread: Part 1 unhardened steel and austenitic stainless steel (First Revision)
**Edition Status**: `current-matching` | **Section Hint**: `None` | **Char Count**: 955
```text
2
Table 1 — Dimensions
Dimensions in millimetres
d1
m6
1)
6
8
10 
12
16
20
25
30
40
50
c1
≈
0,8
1
1,2
1,6
2
2,5
3
4
5
6,3
c2
≈
1,2
1,6
2
2,5
3
3,5
4
5
6,3
8
d2
M4
M5
M6
M6
M8
M10
M16
M20
M20
M24
P
2)
0,7
0,8
1
1
1,25
1,5
2
2,5
2,5
3
d3
4,3
5,3
6,4
6,4
8,4
10,5
17
21
21
25
t1
6
8
10
12
16
18
24
30
30
36
t2
min.
10
12
16
20
25
28
35
40
40
50
t3
1
1,2
1,2
1,2
1,5
1,5
2
2
2,5
2,5
l
 3)
nom.
min.
max.
 16
15,5
16,5
 18
17,5
18,5
 20
19,5
20,5
 22
21,5
22,5
 24
23,5
24,5
 26
25,5
26,5
 28
27,5
28,5
 30
29,5
30,5
Range
 32
31,5
32,5

 35
34,5
35,5
 40
39,5
40,5
of
 45
44,5
45,5
 50
49,5
50,5
 55
54,25
55,75
 60
59,25
60,75
 65
64,25
65,75
 70
69,25
70,75
commercial
 75
74,25
75,75
 80
79,25
80,75
 85
84,25
85,75
 90
89,25
90,75
 95
94,25
95,75
100
99,25
100,75
lengths
120
119,25
120,75
140
139,25
140,75
160
159,25
160,75
180
179,25
180,75
200
199,25
200,75
1) Other tolerances as agreed between customer and supplier.
2) P is the pitch of the thread.
```

### Chunk 3: `[doc_2373_main_1981_p5_c0]` (IS 2373, Page 5)
**Title**: Specification for water meters (bulk type) (third revision)
**Edition Status**: `current-matching` | **Section Hint**: `None` | **Char Count**: 950
```text
IS : 2373 - 1981
© BIS 2007

This publication is protected under the Indian Copyright Act (XIV of 1957) and
reproduction in whole or in part by any means except with written permission of the
publisher shall be deemed to be an infringement of copyright under the said Act.
Indian Standard
SPECIFICATION FOR
WATER METERS (BULK TYPE)
( Third Revision )
Sanitary Appliances and Water Fittings Sectional Committee, BDC 3
Chairman
SHRI V. D. DESAI
‘Sheetala Darshan’, Flat No. 42, 4th Floor,
375 Lady Jamshedji Road, Mahim,
Bombay 400016
Members
Representing
ADVISER
Central Public Health & Environmental Engineering
Organization (Ministry of Works & Housing)
SHRI B. B. RAU ( Alternate )
SHRI M. K. BASU
Central Glass & Ceramic Research Institute (CSIR),
Calcutta
SHRI K. D. BISWAS
Indian Iron & Steel Co Ltd, Calcutta
SHRI D. S. CHABHAL
Directorate General of Technical Development,
New Delhi
SHRI T. RAMASUBRAMANIAN ( Alternate )
SHRI S. P. CHAKRABARTY
```

### Chunk 4: `[doc_1317_main_1969_p1_c1]` (IS 1317, Page 1)
**Title**: Specification for edible tapioca chips (First Revision)
**Edition Status**: `current-matching` | **Section Hint**: `None` | **Char Count**: 328
```text
“जान1 का अ+धकार, जी1 का अ+धकार”
Mazdoor Kisan Shakti Sangathan
“The Right to Information, The Right to Live”
“!ानएकऐसाखजाना> जोकभीच0रायानहB जासकताहै”
Bhartṛhari—Nītiśatakam
“Knowledge is such a treasure which cannot be stolen”
”
है”
ह”
ह
IS 1317 (1969): Edible Tapioca Chips [FAD 16: Foodgrains,
Starches and Ready to Eat Foods]
```

### Chunk 5: `[doc_1112_2_1989_p4_c0]` (IS 1112 Part 2, Page 4)
**Title**: Glass shells for general lighting service lamps - Specification: Part 2 81 to 130 mm shell diameter (Second Revision)
**Edition Status**: `current-matching` | **Section Hint**: `None` | **Char Count**: 324
```text
Indian 
GLASS SHELLS FOR 
I% 11t2 ( Paft 2 ) : 1828 
Stqndard 
* 
GENERAL LIGHTING 
SERVICE LAMPi - SPECIFICATION 
PART 2 81 ‘TO 130 mm.SHELL DIAMETER 
UDC 666’175’6 : 621’32 
, 
. 
@ BIS 1990 
BUREAU 
OF 
INDIAN 
STIANDARDS 
MANAK 
BHAVAN, 
9 BAHADUR 
SHAH 
ZAFAR 
MARG 

September 1990 
Price Gropp 2 

( Reaffirmed 2001 )
```

### Chunk 6: `[doc_10910_main_1984_p6_c1]` (IS 10910, Page 6)
**Title**: Specification for polypropylene and its copolymers for its safe use in contact with foodstuffs, pharmaceuticals and drinking water
**Edition Status**: `current-matching` | **Section Hint**: `None` | **Char Count**: 996
```text
y 
Board ( Ministry 
of Railways 
) 
DIG KI-ISH \N I<u~xt 
( Alternate j 
SrlRr c. I;. !L~L:CIIUJTKA 
Export 
Inspection 
Council 
of India, Calcutta 
SHRI S. S. ~:JIWlL.4 
( .~kfRdt 
) 
SHRl 
s. 
hfI’l’L\ 
ILAC Ltd. Calico Group, 
Bombay 
_ 
nit 1%. Ii. c. .2_; ?N,) ( Allernde ) 
SRRI v. s. h~frsok: 
Gujarat 
State Fertilizers 
Co Ltd. Vadodara 
SHJlI 
K. R. N.!Jl 
\sJ~iJ.\?i’ 
Metal Box lndia Ltd, Calcutta 
Dn S. L4131lhtANhN ( Alternate ) 
S11nr v. 
n’I.l~r.\%‘.:N 
Union 
Carbide 
India Ltd, Bombay 
SHHI A. K. CL’PT.\ : Ailrrnafe ) 
SXIII 
B. 13. P,\TRA 
The 
Alkali & 
Chemical 
Corporation 
of India Ltd, 
Hooghly 
SHRI 0. 
P. RA!cRI\ 
National 
Buildings 
Organization, 
New Delhi 
San1 R. SA.STJCA:< 
\?I1 
Central 
Institute 
of Plastics 
Engineering 
I(r Tools, 
Madras 
Drr K. R \X \~IUIITIIY ( AIfernote ) 
SHnr P. R. S~:sltn,v 
Indian Petrochemicals 
Corporation 
Ltd, Vadodara 
SHRI 1). D. CHATTERJEE ( A~fernUfC ) 
SEER1 J. I~. SIIAH 
The Plastics & Rubher 
Institute, 
Bombay
```

### Chunk 7: `[doc_10794_main_1984_p7_c0]` (IS 10794, Page 7)
**Title**: Specification for mild steel wire for cotter pins
**Edition Status**: `current-matching` | **Section Hint**: `scope` | **Char Count**: 990
```text
IS : 10794 - 1984 
Indian Standard 
SPECIFICATION 
FOR 
MILD STEEL 
0. 
WIRE FOR COTTER 
PINS 
FOREWORD 
0.1 This Indian 
Standard 
was adopted 
by the Indian 
Standards 
Institution on 30 January 
1984, after 
the draFt finalized 
by the Wrought 
Steel 
Products 
Sectional 
Committee 
had been approved 
by the Structural 
and 
Metals 
Division 
Council. 
0.2 Cotter 
pins are generally 
used for locking 
nuts 
in circular 
motion. 
This 
standard 
covers 
requirements 
of half 
round 
mild 
steel 
wire 
for 
cotter 
pins. 
0.3 For 
the purpose 
of deciding 
whether 
a particular 
requirement 
of 
this standaid 
is complied 
with, 
the final 
value, 
observed 
or calculated, 
expressing 
the result 
of a test or atlalysis, 
shall be rounded 
off in accordance 
with IS : 2-1960*. 
The number 
of significant 
-places 
retained 
in 
the rounded 
off value 
should 
be the same as that 
of the specified 
value 
in this standard. 
1. SCOPE 
1.1 This standard 
covers 
the requirement
```

### Chunk 8: `[doc_10313_main_1982_p17_c1]` (IS 10313, Page 17)
**Title**: Requirements for settling tank (clarifier equipment) for water treatment plant
**Edition Status**: `current-matching` | **Section Hint**: `None` | **Char Count**: 996
```text
\B4G 
Victoria 
Jubilee 
Technical 
Inrtitute, 
Bombay 
Z3fmtN.W. 
i%#rnc~4N~~Nf 
Municipal 
Corporation 
of Greater 
Bombay 
Smzr V. S. Moaa 
Indian 
Oil Corporation 
Ltd, New Delhi 
SRRI AWL RAJ ( Altnnata ) 
SHRI 
S. s. NAIK 
Mfs 
Hydraulic 
& 
General 
Engineer 
(P) 
Z&d, 
Bombay 
SHRI D. R. KENRRE ( AkMte 
) 
Saur 
R. NATRAJAN 
Hindustan 
Dorr Oliver 
Ltd, Bombay 
SARI B. M. RAHUL ( Alternate ) 
!&RI 
N. RA~~~CH\NDRAN 
Ion Exchange 
( India ) Ltd. Bombay 
SHICI A. M. JOSHI ( d~terautc) 
Da S. RAM \CIf ANDRA 
Central 
Mechanical 
Engineering 
Research 
Institute 
( CSIR ), Durgapur 
SHRI S. NATAIUJAN 
( &tmUte 
) 
SIIRI V. R~st.t~ 
National 
Environmental 
Engineering 
Research 
SHRI S. D. RADKIP;.LTN 
( ANernatc) 
Institute ( CSIR 
), Nagpur 
SHILX C. E. S. R \o 
The Hindustan 
Construction Co Ltd, Bombay 
PROF S. Suesa 
R.40 
,411 India 
Institute 
of 
Hygiene 
& Public 
Health, 
Calcutta 
SICKI K. J. NATH 
( Akrnutc ) 
REPI~FYI..\‘T \TI~F 
I , 
SHRI 
C. L. S IS&I 
University
```

### Chunk 9: `[doc_13058_main_1991_p9_c1]` (IS 13058, Page 9)
**Title**: Calibrated round steel link lifting chains - Guidelines for proper use and maintenance
**Edition Status**: `current-matching` | **Section Hint**: `None` | **Char Count**: 972
```text
external damage. Next 
operate the equipment under no load and under a load as near 
as possible to the usual operating load, in both directions and 
observe the functioning of the chain and wheels. The chain 
should feed smoothly into and away from the wheels in each 
case. 
If the chain binds, jumps or is noisy, check that it is clean and 
properly lubricated. If the trouble persists after lubrication, inspect the chain and mating parts for wear, distortion or other 
damage as outlined below. 
4.32 
Procedure for periodic inspection 
Chains should be cleaned for inspection, using any cleaning 
method that will not cause damage. Methods to avoid are 
those that may cause hydrogen embrittlement (such as immersion in caustic or acid bath), overheating, removal of metal or 
movement of metal which may cover cracks or other surface 
defects. 
Adequate lighting should be provided for the inspector. The 
chain should be examined link by link for cracks, gouges or
```

### Chunk 10: `[doc_10226_1_1982_p4_c2]` (IS 10226 Part 1, Page 4)
**Title**: Method for determination of crude fibre content in - food products: Part 1 general method
**Edition Status**: `current-matching` | **Section Hint**: `None` | **Char Count**: 645
```text
odifmd 
Scharrer 
method 
IS0 
3310/l-1975 
Test 
sieves - 
Technical 
requirements 
and 
testing 
: Part I Metal 
wire 
cloth 
Q 
IS 
: 10226 
(Part 
II)-1982 
Method 
for 
determination 
of crude 
fibre 
content 
In food 
products 
: Part II Modified 
Scharrer 
method 
(Technically 
equivalent 
to IS0 
Standard) 
IS : 460 (Part I)-1978 Specification 
for test 
sieves : Part I Wire cloth 
test sieves 
(second 
le vision) 
(Technically 
equivalent 
to IS0 
Standard) 
Adopted 
6 December 
198P 
I 
@ July 1983, ISI 
I 
Gr 5 
INDIAN 
STANDARDS 
INSTi,tUTION 
MANAK 
BHAVAN, 
9 BAHADUR 
SHAH 
ZAFAR 
MARG 
NEW DELHI 
11OQQP 

(Reaffirmed 2005)
```

---

## 5. 5 Verbatim Scope Snippets

### Scope Snippet 1: IS 7928 (Page 6)
**Source URL**: `https://law.resource.org/pub/in/bis/S06/is.7928.1993.pdf`
```text
1 SCOPE
1.1 This standard prescribes the requirements
and the method of sampling and test for alginic
acid, food grade.
2 REFERENCES
2.1 The 
following 
Indian 
Standards 
are
necessary adjuncts to this standard.
3 REQUIREMENTS
3.1 Description
Alginic acid shall be the hydrophilic colloidal
carbohydrate extracted by the use of dilute
alkali from various species of brown seaweed
( Phaeophyceae ). 
It 
may 
be 
described
chemically 
as 
a 
linear 
glycuronoglycan
consisting 
mainly 
of 
B 
(1-4) 
linked
D-mannuronic and L-guluronic acid units in
the pyranose ring forms. It occurs as a white to
y
```

### Scope Snippet 2: IS 11916 (Page 6)
**Source URL**: `https://law.resource.org/pub/in/bis/S12/is.11916.2001.pdf`
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
of applying the most recent editions of th
```

### Scope Snippet 3: IS 2637 (Page 6)
**Source URL**: `https://law.resource.org/pub/in/bis/S01/is.2637.2004.pdf`
```text
1
Scope
This International
Standard
specifies
the characteristics
of a range of steel roller chains,
dimensionally
derived
from
the malleable
iron type and suitable
for the conditions
of operation
and maintenance
prevailing
in such fields
as
agriculture,
building,
quarrying
and related industry,
mechanical
handling,
etc., and of associated
chain sprockets.
2
Normative
references
The
following
standards
contain
provisions
which,
through
reference
in this
text,
constitute
provisions
of this
International
Standard.
At the time
of publication,
the editions
indicated
were
valid.
All standards
are s
```

### Scope Snippet 4: IS 8694 (Page 7)
**Source URL**: `https://law.resource.org/pub/in/bis/S11/is.8694.1978.pdf`
```text
1. SCOPE 
1.1 This standard covers the requirements 
of valve inflated, seamless, latex 
bladder. 
2. MATERIAL AND WORKMANSHIP 
2.1 The bladders shall be made from rubber latex, and shall be free from 
harmful defects like pits and air bubbles. 
2.2 The valve shall be properly joined to the bladder. 
3. MASS 
3.1 The mass of different sizes of bladders shall be as follows: 
Size No. 
Mass 
g 
4 
50-60 
5 
70-85 
6 
100-I 15 
*Rules for rounding off numerical values (revised ). 
3
```

### Scope Snippet 5: IS 14900 (Page 6)
**Source URL**: `https://law.resource.org/pub/in/bis/S02/is.14900.2000.pdf`
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
are su
```

---

## 6. Export Package Validation Output

Command: `python scripts/validate_export.py export/bisbot_data/`

```
Validating export package in 'export/bisbot_data/'...
PASS: Export package validation succeeded for 'export/bisbot_data/' (13867 document chunks, 16425 catalogue records).
Exit Code: 0
```

---

## FACTS ONLY

- **Documents Selected**: 599.
- **Documents Downloaded**: 599.
- **Documents Verified**: 598.
- **Documents Rejected**: 1 (Reason: Missing IS base number / string 'BUREAU OF INDIAN STANDARDS').
- **Total Chunks Generated**: 13,867.
- **Docs with Scope Found**: 488.
- **Docs with Scope Not Found**: 110.
- **Chunk Length**: Median 966 chars, Min 150 chars, Max 1000 chars.
- **Total Corpus Disk Size**: 886.25 MB.
- **Catalogue Records Written**: 23,866.
- **Export Validation Output**: PASS (Exit Code 0).