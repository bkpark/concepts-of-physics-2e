# Four fidelity repair proposals

**Update:** The author approved all four proposals. They are now applied only in
`maintained/`; see [current status](maintained-source-status.md). The remainder
of this document records the proposal-stage evidence.

These proposals are prepared and tested, but not applied to historical or
maintained textbook source. The review page is `/repair-review/` on the local
prototype server. It shows proposed equations in native MathML.

## Recommendations

| ID | Location | Proposed change | Review significance |
|---|---|---|---|
| R1 | m67807, eip-53; archived equation 13.36 | Add the missing exponent 2 to both n_f and n_i | Corrects the equation as displayed in the historical PDF; author review recommended |
| R2 | m67807, import-auto-id3143059; archived exercise 46 | Remove an empty one-child superscript after the Bohr-radius formula | Markup repair only; no visible mathematical content removed |
| R3 | m42709, import-auto-id1688908; nuclide notation row | Restore A upper left, Z lower left, N lower right of X | Corrects the historical display to agree with its annotation and the book's nuclear-decay notation; author review recommended |
| R4 | m67122, import-auto-id2677616; archived exercise 10 | Retarget the missing example link to fs-id1667893 | Retained tire-pressure example contains the exact fact the exercise references |

## Evidence and conflicts

R1 is supported by the preceding local derivation `eip-237` and the same module's
`eip-854` and `eip-59`: all have inverse-square quantum-number terms. PDF page
476 (printed 470) visibly omits the two exponents in equation 13.36. The proposal
preserves the local coefficient and variables; it does not import upstream prose.
[OpenStax's Bohr section](https://openstax.org/books/college-physics-2e/pages/30-3-bohrs-theory-of-the-hydrogen-atom)
corroborates the squared dependence.

R2's malformed superscript contains only empty rows. The later recovered Git
version replaces it with an empty row, while the pinned upstream m42596 omits
the branch. The proposed repair removes that empty branch only. PDF page 484
(printed 478) displays the retained expression in exercise 46. No changes to
the existing coefficient grouping or q_e notation are included.

R3 is supported directly by the original StarMath annotation, which specifies
`lSub Z` and `lSup A`, and by local m76603 `import-auto-id3033441`. The original
PDF page 644 (printed 638) instead displays upper Z without A. The later recovered
source and pinned upstream glossary still put A below Z. Those versions are
counter-evidence to automatic upstream adoption, not valid repair templates.
The proposed display agrees with the book's existing nuclear notation and
[OpenStax's nuclear-physics summary](https://openstax.org/books/college-physics-2e/pages/31-section-summary).
The original annotation and the X_N subtree are retained.

R4's absent target `fs-id1444855` belongs to the upstream example “Calculating
Number of Moles: Gas in a Bike Tire.” That example is not in the local module.
Restoring it would change the chosen content. Instead, the retained example
`fs-id1667893`, “Calculating Pressure Changes Due to Temperature Changes: Tire
Pressure,” already states an absolute pressure of 7.00 × 10^5 Pa and gauge
pressure just under 90.0 lb/in². It appears as Example 9.1 on PDF page 237
(printed 231). The exercise's broken link is visible as “???” on PDF page 290
(printed 284); it is not a new migration failure. Only the target ID changes.

## Review artifacts and checks

`proposals/fidelity-repairs/manifest.json` stores source object IDs, original
file and fragment SHA-256 checks, exact before/after fragments, classification,
evidence, and proposed status. Four independent patch files accompany it.
R2 is generated after R1 in the same module, so apply patches in R1–R4 order.
Math ordinals are diagnostic locators; source IDs plus hashes guard the actual
changes. These are not new canonical section or object identities.

`prototype/prepare_repairs.py` regenerates the review package, applies proposals
only to generated review copies, and checks:

- original file/fragment hashes and unique replacement matches;
- valid resulting XML;
- identical ID sequences and MathML counts;
- every expression in the three affected modules passes the MathML adapter;
- the repaired module's local cross-reference destinations exist.

This validates patch mechanics and renderer acceptance, not independent proof
of mathematical correctness. The recommendation rests on the evidence above.
The proposed expressions have also been visually inspected in native MathML.

Pinned upstream reference files and their checksums are kept separately under
`references/repair-evidence/`, with their repository and commit recorded. They
are comparison evidence, not merged canonical content. The original PDF and
all 959 baseline files retain their existing verification protections.

## Decision and next work

Recommend accepting all four proposals into a future maintained source layer.
The useful author review is R1 and R3: they correct historically displayed
equations/notation, rather than merely making invalid XML render. This review
follows the user's instruction not to silently change textbook mathematics.
No restoration of omitted upstream material is proposed.

After recording the decision, integrate accepted repairs into a maintained
layer while leaving baseline modules immutable. The object-numbering audit
remains the next separate task; these proposals neither change nor validate
the prototype's provisional figure, example, equation, or exercise counters.
