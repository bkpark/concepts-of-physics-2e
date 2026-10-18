# Second-pass italic audit

Read-only scan of all maintained modules after Chapter 14 review. No textbook source was changed.

## Findings

- 6,389 MathML expressions examined.
- 71 explicit italic mstyle wrappers remain, primarily around variable products. These are candidates for redundant-style cleanup, not 71 confirmed visible errors.
- 19 multi-character mi identifiers remain; all explicitly use normal mathvariant (ln, cost, rod, disk, net, PE, KE). No repeat of the combined delta-m error was found.
- Four punctuation tokens inherit italic styling: three periods and one comma.
- 103 prose emphasis elements contain MathML; these require context because some intentionally emphasize whole statements.
- Three isolated A/a prose emphasis elements were flagged; two clearly denote mass number and acceleration.

This inventory detects explicit styles, inherited MathML styles, and multi-character identifiers. It cannot establish authorial intent for every italic phrase or inspect lettering embedded in images. Browser review remains useful.

## Inherited italic punctuation

- `m67044#import-auto-id3246114`: `F=−kx.`
- `m71411#fs-id2448434`: `Wnet=mad.`
- `m71415#fs-id2081885`: `E=Pt.`
- `m71625#fs-id1867952`: `V=Ad,`

## Explicit italic wrapper inventory

| Module | Source ID | Expression |
|---|---|---|
| m42235 | import-auto-id1169738035492 | PV |
| m42235 | import-auto-id1169737710626 | PV |
| m42236 | import-auto-id1169738163546 | PV |
| m42236 | import-auto-id1169737869808 | COP |
| m42236 | import-auto-id1169737869808 | EER |
| m42236 | import-auto-id1169737869808 | EER |
| m42236 | eip-492 | EER |
| m42236 | eip-683 | EER |
| m67044 | import-auto-id3246114 | kx. |
| m67044 | import-auto-id2612856 | mg |
| m67044 | import-auto-id1872043 | kx |
| m67044 | import-auto-id3385046 | kx |
| m67122 | import-auto-id2374115 | PV |
| m67122 | import-auto-id2374115 | NkBT |
| m67122 | import-auto-id2238750 | PV |
| m67122 | import-auto-id2248763 | PV |
| m67122 | import-auto-id2248763 | NkBT |
| m67122 | import-auto-id2717709 | PV |
| m67122 | import-auto-id2717709 | NkBT |
| m67122 | import-auto-id3224643 | PV |
| m67122 | import-auto-id3224643 | NkBT |
| m67122 | import-auto-id3224643 | PV |
| m67122 | import-auto-id3224643 | kBT |
| m67122 | import-auto-id2887530 | PV |
| m67122 | import-auto-id2887530 | kBT |
| m67127 | import-auto-id1169738036935 | PV |
| m68329 | eip-id1640254 | mg |
| m68329 | eip-id2489897 | mg |
| m68329 | eip-id1331551 | mg |
| m68329 | eip-id1166246 | mg |
| m68330 | eip-id2367884 | ma |
| m68330 | eip-id3477001 | ma |
| m68876 | import-auto-id2222965 | gt |
| m68876 | import-auto-id4138788 | gt |
| m68876 | import-auto-id4138788 | at |
| m68876 | import-auto-id1688803 | gt |
| m71411 | import-auto-id1526244 | ma |
| m71411 | fs-id2448434 | mad. |
| m71411 | import-auto-id1809184 | ad |
| m71415 | fs-id2081885 | Pt. |
| m71415 | import-auto-id1399884 | Pt |
| m71415 | fs-id1710936 | Pt |
| m71582 | eip-605 | mv |
| m71582 | import-auto-id1512339 | ma |
| m71593 | import-auto-id3229264 | ma |
| m71593 | import-auto-id3229264 | ma |
| m71593 | eip-426 | mr |
| m71593 | eip-304 | rF |
| m71593 | import-auto-id3089520 | ma |
| m71594 | import-auto-id3105554 | mv |
| m71594 | import-auto-id3063259 | rF |
| m71594 | import-auto-id2625259 | mv |
| m71613 | eip-289 | Ah |
| m71613 | import-auto-id2009193 | mg |
| m71615 | eip-914 | PA |
| m71615 | import-auto-id3175478 | PA |
| m71623 | import-auto-id3138842 | mg |
| m71623 | eip-764 | mg |
| m71623 | eip-958 | Ah |
| m71623 | eip-476 | Ah |
| m71623 | eip-58 | Ah |
| m71623 | import-auto-id1355895 | mg |
| m71623 | eip-998 | mg |
| m71625 | import-auto-id1062406 | Ad |
| m71625 | import-auto-id1062406 | Ad |
| m71625 | fs-id2590610 | Qt |
| m71625 | fs-id1867952 | Ad, |
| m71625 | fs-id2668235 | Ad |
| m71626 | import-auto-id1411337 | gh |
| m71626 | import-auto-id2668144 | mgh |
| m71626 | import-auto-id2668144 | gh |
