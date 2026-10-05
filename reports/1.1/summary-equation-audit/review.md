# Summary equation audit

## Presentation change

All 108 displayed equations in section summaries now omit their visible equation numbers in web and generated book/PDF input. Stable IDs, internal numbering assignments and links are unchanged. Both numbering profiles verified; non-summary equation labels match the previous published preview. There are no source links targeting summary equations. House style documented in docs/style-guide.md.

## Content audit

Inventoried 193 displayed/inline mathematical relationship candidates in summaries. 156 matched body expressions automatically; 37 required manual comparison for rearrangement, combined relations, notation, prose definitions or prior-section coverage. Dispositions are in relationships.json. The matching script is a triage tool, not a proof of algebraic equivalence; manual dispositions are retained in this audit snapshot.

### Needs a body introduction

Section 8.2 (Temperature), m52364: four conversion formulas between Fahrenheit, Celsius and kelvin occur explicitly only in the summary. The body explains scale ratios and offsets but gives no conversion formulas. Proposed copying these four formulas into the body after the scale-comparison figure, preserving existing summary copies and numbering. Maintainer explicitly deferred this to Chapter 8 review (September 29); reminder in docs/exercise-revision-1.1.md.

### Separate consistency findings

- Section 10.8 (m52420), summary item import-auto-id1166991832296: current-loop field formula uses lowercase n, while body import-auto-id1166991833146 uses N for total loop count. Lowercase n elsewhere means turns per unit length for a solenoid. Recommend matching body N.
- Section 12.6 (m67805), summary equation eip-115: proton charge-to-mass ratio is 9.57 × 10^7 C/kg versus 9.58 × 10^7 in body eip-62. Recommend matching body 9.58.

Neither finding introduces a new relationship. Recorded in the chapter review checklist: n/N for Chapter 10 (maintainer-requested reminder), and proton ratio for Chapter 12; not altered in this presentation change. Section 12.8's photon-transition equation repeats the preceding section, and Bohr angular momentum, phase-change, continuity and nuclide formulas combine already introduced relations. Temperature conversions are the only identified first-explicit-presentation issue in this scoped audit. This is not a fresh book-wide numerical or factual certification.

## Checks

Both full builds and full validation passed with two pre-existing external-media findings. Validation of all 108 summary equation anchors and unchanged non-summary labels is in validation.json. No PDF binary was rebuilt.
