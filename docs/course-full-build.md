# Course-first full-book HTML milestone

Course numbering is the publication target. CNX remains a compatibility preview;
exhaustive CNX verification is deferred until lecture-video revisions.
See `metadata/publication-policy.json`.

## What is now built

- All 141 maintained modules, using the editable collection hierarchy directly.
- 15 frozen, title-slugged chapter exercise views projecting 944 exercises from
  153 source blocks. The other 49 exercises remain inline. There is no second
  editable copy of the content. Canonical section URLs/anchors are retained.
- Native MathML coverage for 7,394 expressions: 7,391 rendered and three visible
  review placeholders. Scientific notation in 28 expressions is now supported
  as a display adaptation, without changing source values or XML. Its meaning
  follows [MathML 3 Content Markup](https://www.w3.org/TR/MathML3/chapter4.html).
- CALS table column spans and alignment; preservation of a caption anchor missed
  by the six-module sample; explicit links for three external video/interactives.
- 563 image references, 12,236 source anchors, and 10,819 prose fragments checked.
- All 156 section/exercise pages audited in Chrome: no script errors, broken
  images, duplicate IDs, measured desktop overflow, or external network requests.
  This is not exhaustive visual, mobile, accessibility, or equation accuracy QA.
- All 141 section URL/anchor registries match the CNX compatibility build.

## Course numbering evidence and review

Course PDF page 327 places conceptual questions on the chapter exercise page:
Ideal Gas Law questions are 5 and 6, and the thermos figure is 8.E.1. Page 331
restarts the problem counter, placing Ideal Gas Law problems at 9 onward; the
repaired pressure-conversion problem is 10. These observations are checked in
fixtures (seven course sample labels plus the full-build thermos figure).
Chapter exercise figures are counted through conceptual questions first, then
problems. CNX's existing sixteen fixtures still pass.

The archived course PDF is internally inconsistent: its main contents call
Temperature 8.2 and Ideal Gas Law 8.3, while the exercise-page headings call them
8.1 and 8.2. Generated exercise views use the main section labels consistently;
question/problem counters retain the checked historical numbers. Please review
this presentation choice in the Thermal Physics exercise view. No source text
or pedagogical classification was changed. Unclassified inline exercises stay
inline rather than being moved merely because of their heading text.

Object numbering remains provisional outside those observations, especially
appendices, inline exercises, and equation-label visibility. The full printable
HTML still follows source module order; chapter-end exercise placement for the
PDF is not implemented. No new full-book PDF is delivered in this milestone.
Earlier six-module PDFs remain evidence of the preceding milestone, not exports
of this updated course numbering.

## Findings requiring the next review pass

Machine-readable details are in `reports/course-full-findings.json`; the build's
`review.html` includes exact source MathML and IDs.

1. `m67804`, `eip-691`: a hybrid approximate-equality operator inside Content
   MathML (`apply/mo`). The adapter deliberately leaves it unresolved pending
   an explicit handling decision.
2. `m42531`, `import-auto-id1744942`: a time-dilation equation
   has a three-child `msub` where two children are required. Compare the archived
   rendering and source annotation before proposing a grouping repair.
3. `m42674`, `eip-id6767649`: the lepton-number expression has one-child subscripts.
   Compare historical evidence before proposing a repair.
4. 25 references remain unresolved: 24 point outside the recovered book and one
   points to a missing local object. This is the original inventory's 26 minus
   the already approved tire-example repair. Do not guess replacements solely
   from upstream module similarity.
5. Two videos and one external simulation are linked, not archived or embedded.
   They are not available as offline textbook content.

No new editorial repairs were applied. Historical verification and the exact
maintained-initialization comparison still pass.

## Rebuild and next work

```powershell
python prototype/build.py course --all
python prototype/build.py cnx --all  # compatibility/identity check only
# Playwright and Chrome configured as in prototype/README.md:
node prototype/tools/audit-full.cjs
python prototype/validate_full.py
```

Outputs are under `prototype/dist/course-full/`; this prefix is a local preview
location, not part of eventual public section URLs. The generated exercise views
have their own frozen identities in `maintained/exercise-views.json`.

Next: prepare evidence-backed proposals for the three expressions and unresolved
references; settle course equation display rules; assemble chapter-end exercise
placement and test full-book PDF pagination. Pin the renderer and redistributable
fonts before calling the build reproducible for publication.

## Author review page and revised exercise scope

Run `python prototype/tools/review_items.py` after a full build to generate
`course-full/review-items/index.html`. It contains M01–M03 and X01–X25, context,
exact section links, and unchanged archived PDF page images for the expressions.
Requires Poppler pdftoppm and the checksum-pinned 12.1 reference PDF.

Exercise editorial shortcomings are explicitly deferred until after the initial
CNX-content/course-numbered publication. Later work may backport course questions.
Exercise-related findings remain visible but are labeled as deferred context,
not requests to complete the broader exercise revision now.
