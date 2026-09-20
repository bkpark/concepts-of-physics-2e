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

The requested Unit 3 batch is ready: 49 sections compared, 58 scoped correction records applied, all author-review holds resolved or explicitly deferred. See http://127.0.0.1:8765/review-1.1/unit3-review/ and `proposals/1.1/unit3-holds.json`. Retain published 1.0. Remaining units and final release PDF checks are still outstanding; Unit 3 review does not certify the whole book.


### Unit 3 author decisions (September 19, 2026)

- H01 applied: upstream metal-block example, omitting an unnecessary Thermodynamics aside; coverage is not missing.
- H02 deferred by author to the exercise revision.
- H03 figure applied from the pinned CC BY archive, with the 2020 caption, NASA credit and corrected color-scale alternative text. Paragraph also applied with author-approved limited factual adjustments: omit the undated country ranking and replace the incorrect 2020 record claim with “large and long-lasting.”
- H04 prose applied with the author-approved limited qualification: studies have not established that power-line fields cause cancer, rather than upstream’s blanket absence-of-risk statement.
- H05 upstream generator arrows applied, with synchronized alternative text.
- H06 applied: retain the electron-transition explanation and tie the majority claim explicitly to table categories, infrared through X-rays. Author completed a quick review of the remaining Unit 3 changes; no Unit 3 backport holds remain. H02 stays deferred to exercise revision.

Evidence for approved H03/H04 qualifications: [NASA 2020 ozone map and account](https://science.nasa.gov/earth/climate-change/ozone-layer/large-deep-antarctic-ozone-hole-in-2020-147465/), [NCI electromagnetic fields fact sheet](https://www.cancer.gov/about-cancer/causes-prevention/risk/radiation/electromagnetic-fields-fact-sheet). These sources support factual checking; prose backports and figure bytes come from the recorded CC BY snapshot.


## Between 1.1 and 1.2: author read-through

The author plans a careful full-text read-through after 1.1, to catch issues missed during the current quick review and identify explanations or pedagogical choices they now wish to revise. Record findings for a broader author-led 1.2 revision; this is not an additional prerequisite for releasing 1.1.


## Unit 4 backport review packet

The Unit 4 packet covers 29 textbook sections and four supporting appendices. Eight correction records are applied in `proposals/1.1/upstream-batch-06.json`: the electron/photon diagram and caption, thorium notation, proton-rich beta-plus sign, ion-pair clarification, programmed-cell-death wording, and matching dosimeter image/caption/credit. Source: the existing pinned CC BY 4.0 archive only.

Review: http://127.0.0.1:8765/review-1.1/unit4-review/ . Rebuild the packet with `python tools/render_unit4_review.py`; rebuild the development textbook with `python prototype/build.py course --all`.

U4-H01 holds the reactor-safety generalization and obsolete next-chapter promise for author choice. Other shared problems and optional coverage additions are visible in the page and recorded in `reports/1.1/unit4-review/followups.json`; they have not been silently changed or certified by upstream agreement. The author can prioritize them before 1.1 or during the planned full read-through/exercise revision.

The packet records 191 unmatched upstream boundaries and row-by-row comparisons of supporting tables. It preserves custom quantum explanations, previous relativity/reference repairs, newer local constants, and repaired nuclide notation. Upstream-only AP exercises and broader history/coverage are not restored.

Validation: maintained-source ledger reconstructs 955 files with four initial repairs and 154 editorial changes; historical baseline still verifies 959 files and preservation tags. Desktop/mobile review checks and all eight change anchors pass. The development build has 7389 equations and only the three known external-media notices. No new release PDF or public deployment was produced.

Before declaring the full backport finished, resolve U4-H01 and reconcile eleven remaining opening-chapter math-ordinal differences in m67032 (separate from Unit 4), then complete final PDF/layout and release checks. An applicability review is not independent validation of every inherited exercise or scientific/historical claim.


Photoelectric follow-up: U4-09/U4-10 correct the displayed subtraction to 0.25 eV and stopping potential to 0.25 V. A shorter Discussion using the existing sentences is proposed separately; no new prose rewrite applied.

The author approved the shortened photoelectric Discussion; U4-11 applies the three retained sentences. The permeability approximation is under discussion; no constants-table edits have been made.

### Unit 4 factual follow-up

Applied U4-12 (Stefan–Boltzmann units and vacuum permeability approximation) and U4-13 (tau-decay neutrinos), as approved. U4-H02 contains a shorter medical-imaging-dose proposal beside the unchanged paragraph; awaiting author review. Values are factual references, not imported external prose.

U4-14 applies the approved risk-benefit/radiopharmaceutical paragraph. U4-H03–H06 propose historical corrections and CC BY Wu/Yalow/Berson additions. The RIA mechanism needs the shown correction; the Wu portrait requires separate rights verification. Reconcile the neighboring diagnostic-dose table before release.

Applied U4-H05 as U4-15–U4-17: pinned CC BY Wu prose plus exact upstream composite and caption. Wu source SIA2010-1507 has Smithsonian’s No known copyright restrictions statement, recorded in wu-image-provenance.json. U4-H06 remains unapplied for author review.

Applied U4-H06 as U4-18: Yalow/Berson radioimmunoassay history with the approved competitive-binding and radioactive-tracer measurement correction.

Unit 4 review closed: U4-19–U4-21 resolve reactor wording and historical corrections; U4-22 reconciles diagnostic doses with cited radiology references. No Unit 4 author holds remain. Full-book reconciliation and release verification remain separate.
