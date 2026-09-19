# Maintained source and native MathML milestone

The project now has one editable source under `maintained/`, separate from the
historical baseline and upstream reference snapshots. The four author-approved
repairs are applied there. Their original proposals remain archived under
`proposals/fidelity-repairs/`; approval/application history is recorded in
`maintained/initialization.json`.

The corpus contains 141 modules, 813 media assets, and one collection file:
955 content files. Verification establishes byte identity with the baseline
except for the exact four approved replacements in three modules. All 959
original baseline files, historical tags, archives, and the 12.1 PDF remain
unchanged. No remote repository or hosting settings have been changed.

The author's submission of [OpenStax erratum 30172](https://openstax.org/errata/30172)
is linked to R3 in the initialization record. The page could not be retrieved by
the browsing tool; OpenStax's review/disposition is not independently verified.

## Current build

Both six-section profiles now read maintained CNXML and use native MathML.
The build includes all 852 expressions, 31 image references, 748 source anchors,
and the approved repairs. There are no remaining unresolved-math or missing-link
findings in this sample. This is not a claim about all 141 modules or the
correctness of every historical equation.

Legacy fenced expressions and styles are adapted for browser display only.
Presentation adaptations are logged separately from editorial repairs. All
rendered equations retain actual MathML; the PDF is printed from the same HTML.
A page toolbar copies the selected equation as MathML without intercepting
ordinary symbol selection. Browser checks exercise both clipboard modes on each
section/profile combination. Native math still uses installed Cambria Math and
the installed Chrome version; fonts and renderer packaging are not finalized.

The two profiles have byte-identical URL/anchor registries. Their labels are
generated independently, so replacing a deployed profile does not change page
identity. `maintained/sections.json` is now the source-path/slug authority;
`metadata/sections.proposed.json` remains the initial recovery proposal.

## Numbering findings and changes

The initial discrepancies were caused by presentation rules, not source identity:

1. CNX section-summary equations repeat previous formulas without advancing
   the equation counter. Excluding them restores the first acceleration equation
   to 2.23 and the ideal gas law to 9.1. The repaired Rydberg equation becomes
   13.36, matching the archived PDF's label.
2. Figures in end-of-chapter question/exercise sections follow the main chapter
   figures, even though their XML lives earlier in individual module files.
   Counting the chapter body before those sections restores the opening kayak
   figure to 2.23.
3. CNX conceptual-question and problem/exercise lists have separate counters.
   The tire-pressure conversion exercise becomes 10 and the Bohr-radius exercise
   becomes 46, matching PDF pages 290 and 484.
4. The four custom, untyped exercises in m67034 are different: the PDF keeps them
   inside the section and labels them 2.1–2.4 (page 50). They retain their own
   chapter-prefixed counter. Their "Conceptual Questions" title is not treated
   as permission to relocate or reclassify them.

These rules live in `maintained/numbering.json`. Stable source-ID-based overrides
are supported but none were needed for the checked cases. Fixtures record 16
CNX labels and three course labels with PDF-page evidence. They test selected
observations, not full-book equivalence. The six existing verified CNX section
labels remain in use; labels for the remaining sections still need verification.

The course profile continues to demonstrate section-based labels and stable
identities. Its exercise counters and equation-label visibility remain provisional:
the course reference has separate exercise views, and inspected equations may
have no displayed label. Those differences have not been replaced by guessed
global rules. The sample still keeps exercises in their source modules; full
book end matter and web exercise views remain to be built.

## Verification and scope

- Permanent baseline verification and exact maintained-initialization comparison.
- Source coverage, local page/anchor links, duplicate IDs, images, and prose checks.
- Twelve MathML adapter/native-rendering unit tests and the numbered fixtures.
- Twelve browser section/profile checks: no script errors, broken images,
  measured desktop math overflow, or external network dependencies.
- Visual inspection of all sample PDF pages via contact sheets, plus enlarged
  views of the Rydberg repair and glossary notation. This is layout QA, not an
  exhaustive equation-by-equation comparison with the historical PDF.

The prototype still reads the inventoried hierarchy from `reports/sections.json`.
Editing the maintained collection structure is not yet reflected automatically;
the full-book builder must read that collection directly before reorganizing it.

## Next work and useful review

No new content approval is needed for the changes in this milestone. A useful
optional review is the full native-math Bohr section and its PDF, including
selection/copying in the author's normal PDF viewer. Viewer-specific clipboard
behavior and cross-browser accessibility still need testing.

Before full publication: finish course exercise/equation presentation rules,
verify additional chapter boundaries and appendix numbering, extend the renderer
to every inventoried CNXML construct, render all modules, and pin a redistributable
math font/build environment. Compare any new content defects through the same
reviewable proposal process rather than automatically importing upstream changes.
