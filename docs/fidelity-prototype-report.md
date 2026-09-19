# Six-module fidelity assessment

## Result and scope

The preserved CNXML can produce static HTML and a PDF sample through a small
semantic HTML adapter, a vendored MathJax renderer, and browser printing. Both
CNX and course-numbering builds use identical source content, section paths,
and object anchors. This validates a promising direction; it does not select
a final framework or establish publication readiness.

The six complete modules contain 852 MathML expressions, 31 image references,
52 exercises, and two tables. Of these expressions, 849 render; three fail
explicitly with visible review markers. The automated checks preserve 748
source IDs and find all 812 tested prose fragments longer than 20 characters.
This is structural evidence, not proof that every equation is semantically
correct or that every historical page has been reproduced.

All 959 baseline files remain subject to the existing byte/hash verification.
No historical prose, equations, module files, images, or archives were edited.
Generated builds include byte-identical copies of the six CNXML files,
serialized math for inspection, an adaptation log, issue log, identity registry,
source hashes, and inherited module attribution/license notices.

## Reference evidence

The user-supplied historical PDF remains the authority for how the old book
appeared. Its SHA-256 is recorded in the recovery lock and attribution manifest.
The user identifies it as version 12.1; its printed legacy collection URL uses
`col25183/1.12`. Those literal identifiers remain distinct in the evidence.
The Git import and PDF are not assumed to be identical in every detail.

The July 7, 2026 course PDF supplies the transition numbering, irrespective of
subsequent LibreTexts renumbering. Page numbers below count PDF pages from one.

| Module | Sample | CNX label / PDF page | Course label / PDF page |
|---|---|---|---|
| m67034 | Constant acceleration | 2.5 / 41 | 1.6 / 51 |
| m67530 | Newton's second law | 3.3 / 70 | 2.4 / 80 |
| m71410 | Gravitation | 3.8 / 91 | 2.9 / 105 |
| m67122 | Ideal gas law | 9.2 / 236 | 8.3 / 273 |
| m67807 | Bohr model | 13.6 / 472 | 12.7 / 547 |
| m42709 | Glossary of symbols | Appendix D / 635 | Chapter 18 / 722 |

`prototype/numbering-observations.json` records these observations and selected
figure/example/equation labels. Only the six demonstrated CNX section labels
have been filled into the proposed CNX manifest; unverified entries remain null.

## Math and source findings requiring review

| Source location | Finding | Proposed disposition; not applied |
|---|---|---|
| m67807, eip-53; math-0065 | Two Content MathML power operators each lack an exponent. The archived PDF page 476 (printed 470), equation 13.36, also shows the terms without the squares. | Review the intended equation against the preceding derivation and upstream evidence. Supplying powers would be an editorial correction, not merely formatting. |
| m67807, import-auto-id3143059; math-0091 | A one-child msup at the end of the Bohr-radius expression is malformed. | Compare the later migration and reference rendering; consider removing an empty superscript wrapper in a separate, reviewable patch. |
| m42709, import-auto-id1688908; math-0345 | Nuclear notation has a three-child msup and nested one-child msub. The annotation suggests lower Z and upper A, but the historical PDF page 644 (printed 638) shows upper Z and omits A. | Review intended nuclear notation explicitly. Do not infer a faithful repair solely from the visibly defective historical rendering. |
| m67122, target fs-id1444855 | An internal source reference targets an absent ID. | Locate its intended destination using adjacent prose, historical PDF, and upstream ancestry; add a reviewed mapping or repair. |

The renderer flags these cases and retains their original XML. No guessed
equations have been inserted. Render-only adaptations cover the observed
Content MathML operations, valid presentation wrappers, row/cell structure,
and invalid spacing syntax. Bold vector styling follows the inspected archived
force example. Unsupported operations and invalid arities fail visibly.
The 97 adaptation records are not 97 content errors.

Eight focused unit tests exercise missing operands, unknown operators, token
attributes, vector style, fraction/grouping behavior, and input immutability.
They do not validate the physics of all 849 displayed expressions.

## Numbering and identity

Section identity is `cnx:{module-id}`, and public paths come from the proposed
frozen slug manifest. Renaming a title must not regenerate an established slug.
Objects use module ID plus an injective encoding of their existing XML ID.
Neither identity includes a chapter, section, figure, or equation number.
Both builds have byte-identical identity registries; local paths and fragments
are checked for resolution. The `/cnx/` and `/course/` preview prefixes are not
proposed public URL changes: deploy either profile at `intro.coaphys.xyz`.

The experimental object counter is deliberately not presented as correct.
For example, it gives the opening acceleration figure 2.24 instead of the
historical 2.23, the first acceleration equation 2.27 instead of 2.23, and the
ideal gas equation 9.5 instead of 9.1. The historical kayak and jogger examples
use chapter-based counters; the course PDF uses section-based figure/example
counters, such as 1.6.1. No visible equation number was found on the inspected
course opening page; this does not establish a rule for the whole book.

The next numbering pass should build an evidence-backed object-label map keyed
by stable source IDs, recover reset/exclusion rules, and test them against both
PDFs. Explicit historical label overrides may be necessary. Exercise numbering
and the course edition's separate exercise-page views remain unimplemented.
Do not freeze the current experimental counter into a production specification.

## Upstream comparison

All 141 local sections now carry structured historical attribution evidence,
including module version, author/copyright/license, direct ancestry where
extracted, and PDF provenance. The existing College Physics 2e candidate mapping
has grown from 22 to 86 local sections with at least one candidate; 55 remain
unresolved. Historical ancestry is evidence, not confirmation of a modern
counterpart. None of these candidates has been approved for automatic merging.

The manifest retains arrays of local and upstream sections, selectors, evidence,
intentional differences, and review fields, supporting splits and combinations.
The pinned upstream collection is a reference snapshot, not a full upstream
content checkout. Future work should acquire a pinned reference source, produce
section and object diffs separately for prose, MathML, media, and metadata,
and distinguish intentional local changes before proposing any patch. Raw XML
must remain available beside any normalized comparison view. Check licensing
for each reference version before incorporating upstream content.

## Layout and remaining limitations

The PDFs are sample reflows, not facsimiles. Figures, captions, learning objectives,
examples, exercises, solutions, and glossary tables are included. Footnotes are
currently inline notes. The source's unspecified list types need closer review:
some historical worked-example lists are numbered while this adapter uses its
default bullet treatment. Source table accessibility metadata is retained but
not corrected. Tagged PDF output is enabled; accessibility is not certified,
and SVG math search/copy/screen-reader behavior needs dedicated testing.

Browser checks cover both profiles, no external requests, no broken images,
duplicate anchors, MathJax error nodes, or measured desktop overflow. PDF visual
review uses page contact sheets and selected enlarged pages; that does not
establish exhaustive equation fidelity. The preview remains unsuitable for
student distribution because of flagged equations and provisional numbering.

Chrome and host fonts are not yet locked. Production requires pinned fonts and
a renderer environment, full-book pagination tests, and a decision on whether
browser printing is sufficient or a paged-media engine is needed. No PHP is
needed for the demonstrated output. MathJax is vendored so static pages can work
offline without a CDN.

## Recommended next implementation pass

1. Resolve the three sample math issues and missing target as separate proposed
   patches with historical and upstream evidence, leaving the baseline intact.
2. Recover object-numbering rules and label exceptions; validate a broader set
   of chapters and the course exercise organization before expanding the build.
3. Add rendering fixtures for every CNXML/MathML construct found in the full
   inventory, plus mobile, accessibility, and paginated-layout checks.
4. Choose and lock the production renderer/fonts only after those checks; then
   establish a maintained source layer and extend the build to all 141 modules.
5. Review and freeze URL and upstream mappings before publication. Configure CI
   to verify the baseline, build both formats, and produce reviewable reports.
6. Ask the user for repository visibility and consequential hosting settings
   before creating the remote `concepts-of-physics-2e` repository or deploying.

No remote repository or hosting changes are part of this prototype.
