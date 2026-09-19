# cp2e-ver1.1 planning

Status: SR01 applied to maintained 1.1 source with two author-approved typo fixes. SR02’s upstream stars-to-bodies wording is also applied; the example title is unchanged. Published 1.0 remains unchanged.

The author subsequently authorized the full applicable CC BY upstream correction backport. Whole-book mapping and comparison are generated, and seven additional minimal corrections are applied. See `docs/upstream-backport-1.1.md` for the current scope, evidence, and remaining work; the full backport is not yet complete.

The next review batch adds thirteen opening-chapter corrections and a fingerprinted disposition log. BR01 is applied with minimal timeline wording; BR02 is applied: position axis label and alt text corrected, with original paths and answers retained. The Units 1–2 comparison pass now covers 55 sections, with 35 additional scoped corrections in batch 04. The author deferred the coordinated plasma expansion to broader revision on 2026-09-19. The author approved the Units 1–2 review batch, including the conservative-force heuristic follow-up, on 2026-09-19; no required author decisions remain in that packet. During broader revision, decide whether plasma needs coverage or merely a brief explanation of its omission. The bridge/catenary loading distinction remains a broader-revision note. Later-unit review and final release PDF/layout verification remain outstanding. There is no background process continuing this review between assistant turns.

1. Review Special Relativity against the pinned CC BY snapshot, then systematically review all remaining chapters. Produce reports before edits.
2. Revise chapter-end exercises for conceptual Physics 10, using author-supplied MyOpenMath exports as references after checking provenance.
3. Check numbering, accessibility, solutions policy, and permalink/anchor compatibility as part of those revisions.
4. Maintain a substantive change log. Keep published 1.0 artifacts and its Git tag unchanged.

Before producing release artifacts, deliberately prepare metadata/release.json for cp2e-ver1.1 with new filenames, candidate status, and artifacts_frozen=false. Do not repurpose the 1.0 output directory.

## First review packet

- Review page: `reports/1.1/special-relativity/index.html`, locally served at http://127.0.0.1:8765/review-1.1/special-relativity/ .
- Proposals: `proposals/1.1/special-relativity.json` (SR01 simultaneity explanation, SR02 Earth/Alpha Centauri wording).
- Inventory: seven modules, 584 local and 603 upstream mathematical expressions, 23 local image references.
- Retain the existing higher-resolution Einstein portrait and approved reference/notation adaptations.
- Follow up separately on special relativity versus acceleration, MathML structural differences, and exercise/solution changes. The chapter is inventoried, not certified exhaustively correct.
- Reproduce with `python tools/review_relativity.py`; it reads the checksummed upstream archive and writes only reports and a development preview.
- Request an up-to-date MyOpenMath export for this project when starting the exercise pilot; no export is needed for this physics review.

## Editorial scope

At the author's request, prefer direct upstream updates with minimal prose changes. Extensive rewriting is author-led. SR01 now replaces two paragraphs with verbatim pinned upstream XML and removes the paragraph upstream folded into the first replacement; retain its public anchor. Other prose and figure caption/description are unchanged. The author approved removing “and” from “and arrive” and the doubled period; those two fixes are applied. The expanded rewrite in commit `2ad02f9` is withdrawn. SR01 is applied and recorded in the ordered editorial ledger. All other awkward wording is deferred to a later, broader author-led revision.

## Final 1.1 task: equation-copy interface

After the upstream backport and exercise work, reconsider the public “Copy selected equation as MathML” interface. The author expects LaTeX code to be more useful; consider AsciiMath as an additional option where expressions can be represented faithfully. Assess conversion coverage and an explicit fallback for unsupported constructs rather than silently losing structure. Preserve canonical MathML and symbol-level selection. This is a deferred interface/design task, not authorization to replace equation source or interrupt the current upstream review.

## Unit 3 review packet

The requested Unit 3 batch is ready: 49 sections compared, 50 scoped correction records applied, and six items held for author review. See http://127.0.0.1:8765/review-1.1/unit3-review/ and `proposals/1.1/unit3-holds.json`. Retain published 1.0. Resolve these holds before declaring the full backport complete; remaining units and final release PDF checks are still outstanding.
