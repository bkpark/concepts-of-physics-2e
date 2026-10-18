# cp2e-ver1.1 planning

## October 18, 2026 - Published

The maintainer authorized final source archival, GitHub release with both PDFs, and publication on the existing public Sites project. The main site is now https://intro.coaphys.xyz, with DNS and HTTPS verified. Sites rejects the 68.7 MB PDF as a source object; the live website therefore links to the exact screen PDF on GitHub Releases. The self-hosting ZIP retains the local PDF. The GitHub release and Sites publication are complete. Final receipts record the deployment, live checks, and a renderer punctuation correction caught during visual review. The sections below are historical checkpoints.

## October 18, 2026 - Release package prepared

The maintainer has approved the full book and screen-optimized PDF. Content, appendices, front/end matter and PDF review are complete. Earlier open review checkboxes below are historical and superseded by this checkpoint.

- Website package: `output/releases/cp2e-ver1.1/cp2e-ver1.1-static-html.zip`; default download is the approved screen PDF (`cp2e-ver1.1.pdf`, 68.7 MB).
- Original PDF is staged as `cp2e-ver1.1-print-quality.pdf` for GitHub release only, excluded from the website and ZIP.
- Both numbering builds, 36 tests, immutable baseline verification, all-page desktop/mobile browser checks, search/copy/theme/numbering interactions, source/anchor coverage, sequential exercise numbering, ZIP integrity and file hashes pass.
- Restored three source link IDs omitted by the HTML renderer; no visible prose or approved PDF changes.
- Version 1.0 ledger replay cannot process later multi-file/maintainer ledger schemas. This limitation is documented; exact current source is checked against both builds and the package. No complete historical ledger replay is claimed.
- Release metadata now identifies 1.1 as an unfrozen candidate, with no publication date. Version 1.0 outputs and archival metadata are untouched.
- Remaining: final source commit/tag and archival asset, GitHub release, website deployment, and live verification. No deployment, tag, or GitHub release was performed in this preparation.
- Details: `docs/release-cp2e-ver1.1.md`; machine-readable checks, hashes and upload instructions are beside the ZIP.


## October 16, 2026 — current review checkpoint

- Chapter 14 content and exercise review is finalized by the maintainer; 70 exercises remain.
- Preview 148 is published with corrected Appendices A and B and the 5700-year carbon-14 exercises. Preview 146 included the Exercise 57 italic-m correction and global forced-italic cleanup. Full course build passed with no reported issues; representative appendix, gas-law and exercise pages checked.
- Global cleanup removed 237 explicit MathML italic attributes and 89 math-only prose emphasis wrappers in 44 modules. Natural variable italics, explicit upright styling, intentional prose emphasis, all text, and source IDs are preserved. Audit and application records: `reports/1.1/math-italic-second-pass/`.
- [ ] Maintainer review of the appendices.
- [ ] Maintainer final second pass through the sections, including remaining visual typography issues.
- [ ] Reconcile outstanding items in this planning document before finalizing v1.1 content/format review. Existing release/PDF and other deferred tasks remain open unless separately completed.

## Current status and remaining work

**September 27, 2026 current status:** P3, heat-engine and P4 changes are applied to maintained source, and the full HTML preview is rebuilt and validated. The public preview is https://intro-1-1.coaphys.xyz/ (custom domain and HTTPS active). We are beginning conceptual exercise revision; the maintainer is preparing a fresh MyOpenMath export. Final 1.1 release/PDF work remains.

The scoped CC BY upstream comparison/backport pass is complete: all 140 mapped sections have recorded dispositions, with zero unresolved comparison differences. The local Preface has no upstream counterpart. Published 1.0 remains frozen.

The focused factual-review cycles and their approved follow-ups are applied, with 264 editorial records. The historical baseline remains untouched. See the dated entries below for evidence and scope; this does not claim a complete numerical audit of every exercise.

The author is updating MyOpenMath assessment settings to reference the **published 1.0** section links and will provide a fresh export for the conceptual exercise revision. The export is not a dependency for factual review. No course settings or published website files are changed by this work.

Work order approved by the author:

1. **Immediate next task: focused factual audit.** Independently check historical dates, discovery/attribution and Nobel claims; medical, environmental and safety claims; constants, definitions and potentially outdated assertions. Produce a source-linked, side-by-side review packet with minimal proposed corrections. Separate confirmed errors from uncertainty and broader editorial preferences. Preserve existing prose where possible; substantial rewriting remains author-led. Agreement with upstream is not evidence of independent verification. This is the next work item, not a timed/background automation.
2. **Conceptual chapter-end exercise revision.** Request an up-to-date MyOpenMath export for this project when starting the exercise pilot. Inventory provenance and suitability, develop an author-review pilot, then extend across chapters. Resolve explicitly deferred exercise issues and review answer/solution policy. Keep ordinary PDF exercises at chapter ends and Check Your Understanding inline.
3. **Website exercise placement and publication artwork/front matter.** Near the end of content work, resolve the reported duplicate ordinary exercises at section ends: display them only in the chapter-end collection in static HTML as well as PDF. Keep Check Your Understanding inline. Add a website favicon. Present optional simple PDF cover and reusable front matter for author review; see scope below.
4. **Maintainer-written 1.1 preface.** Near the end of content revision, the author will write a new preface describing the changes in 1.1, highlighting the public GitHub repository and openly explaining the collaboration with Codex. Supply a verified revision inventory from the ledger when requested; preserve author control of wording. Include the approved preface in both PDF and static HTML before final release checks. See scope below.
5. **Equation-copy interface (last feature task).** Assess LaTeX as the useful primary copy format and AsciiMath where faithful; provide explicit handling of unsupported constructs. Preserve canonical MathML and symbol-level selection. See the detailed scope below.
6. **Alphabetize all glossaries (final content housekeeping).** Before finalizing 1.1, alphabetize terms within every glossary consistently in HTML and PDF. Preserve definitions, stable IDs, links and the immutable historical source; handle mathematical/symbol entries deliberately where ordinary alphabetization is not meaningful. The Electromagnetic Spectrum: Application Notes glossary is already alphabetized in the approved Priority 4 preview; extend the convention across the book near the end of revision. Requested September 27, 2026.
7. **Release-candidate build and verification.** Generate fresh 1.1 PDF and static HTML; verify equations, figures/tables, cross-references, exercise placement, numbering, stable URLs/anchors, accessibility and page layout. Retain support for both numbering profiles while prioritizing lecture-aligned presentation.
8. **Release and archival bookkeeping.** Finalize substantive change log, attribution/provenance, 1.1 metadata and filenames; package the website and linked PDF with crawler rules; record checksums, reproducible build instructions, Git tag/release assets and publication handoff. Preserve all 1.0 artifacts and tags. Do not publish an unreviewed release candidate.

Before producing release artifacts, deliberately prepare metadata/release.json for cp2e-ver1.1 with new filenames, candidate status, and artifacts_frozen=false. Do not repurpose the 1.0 output directory.

Broader prose/pedagogy revisions, plasma coverage decisions and the author's careful full-book read-through remain planned for the interval between 1.1 and 1.2.

## Maintainer-written 1.1 preface (added September 21, 2026)

Preferred public-facing role title: **Maintainer** (chosen September 21, 2026). Use this single title for the person maintaining Introduction to Physics, including its preface and project credits. Do not substitute author, editor, curator, or a combined title. Preserve original upstream authorship and historical attribution; this preference does not relabel those contributors. Earlier internal references to author approval remain historical records of editorial decisions.

The author will write most of a new preface when the 1.1 content changes are settled. Do not draft it automatically. The preface should describe the revisions made for 1.1, highlight https://github.com/bkpark/concepts-of-physics-2e as the maintained public source and revision history, and transparently describe the nature of the work with Codex. The author wants AI assistance to be disclosed openly rather than appear concealed, including assistance with newly written or revised passages.

When requested, prepare a concise, evidence-backed inventory of completed changes from editorial records, review packets, and build history. Distinguish upstream backports, independently sourced factual corrections, author-written and author-reviewed revisions, publishing/tooling work, and intentionally deferred work. Describe the respective roles of the author and Codex accurately; do not claim every number, exercise, or passage was independently checked, or make detector results a guarantee of authorship or accuracy. Exact public wording remains the author's choice.

This preface is a definite 1.1 task, separate from the optional cover and reusable publication boilerplate. Integrate the approved text into both outputs from canonical source and check its placement relative to the existing preface without silently overwriting historical front matter. Complete before release-candidate pagination and packaging. No new preface prose has been commissioned or drafted yet.

## Historical progress notes

The entries below preserve the review sequence. Statements about then-pending items are historical; the current status and work order above take precedence.

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

Final comparison reconciliation: all eleven m67032 flags resolved without content edits. Ten were shifted ordinal matches caused by an upstream omission; the structure flag comprises the retained powers-of-ten example and three expressions in approved BR01. Evidence: reports/1.1/m67032-reconciliation.json. All 140 mapped sections now have recorded decisions; local Preface is unmapped. This completes the scoped upstream comparison/backport pass, not the independent full-book content audit or release checks.


## Focused fact-check cycle 1 applied (September 20, 2026)

All 35 approved items (FC01–FC34 plus FC28b) are now applied to the maintained source for the 1.1 development preview, with individual records in the ordered editorial ledger. Overlapping edits (FC07/32, FC16/30, FC17/34, FC28b/33) are composed once each. FC27 moves the inertial-confinement paragraph and figure before the magnetic-confinement paragraph and figure while preserving IDs. Historical CNX source and published 1.0 are unchanged.

Preview: http://127.0.0.1:8765/course-full/ . The original fact-check review preserves before/approved snapshots and links to the updated textbook. This is a development preview, not a release candidate or completed factual audit.

When the author returns, start a separate cycle in this order: (1) remaining radiation/medical explanations and electrical-safety claims; (2) isotope/activity and background-dose tables, plus summary consistency; (3) conceptual physics qualifications; (4) historical and current-technology leads. Each lead in proposals/1.1/fact-check-followups.json needs a documented disposition. Significant factual issues remain in scope for 1.1; do not silently carry them into a broader stylistic deferral. Preserve the accepted conservative-force heuristic and the separate deferrals for plasma coverage and exercise revision. No new fact-check proposals have been started in this application session.

Validation for cycle 1: 955 maintained files reconstruct from four initialization repairs plus 203 editorial records; 959 historical files and pinned tags verify unchanged. All 20 changed section pages pass MathML/image checks, all 35 review context anchors resolve, and the fusion paragraph/figure order is verified in the browser. Course build: 7385 math expressions, only three known external-media notices. No PDF or public deployment was produced in this preview update. Existing trailing whitespace in untouched portions of two changed CNXML lines was retained rather than normalized.


## Late 1.1 tasks added September 20: presentation and reusable publication material

- **Remove duplicate website exercises.** The author reports ordinary questions appearing both at section ends and in chapter-end collections. Inspect the generated views and fix the build so ordinary exercises appear only at chapter ends, without deleting their canonical source content. Keep Check Your Understanding inline. Preserve existing exercise link targets where feasible (or provide an explicit forwarding/linking strategy), and verify no exercises disappear or appear twice. Include both HTML and PDF exercise placement in release QA. This presentation fix does not depend on completing the substantive exercise revision.
- **Website favicon.** Create a simple, recognizable icon appropriate for Introduction to Physics, check it at small browser-tab sizes, and include it in the generated static site and upload package. The dictated phrase “five icon” is interpreted as “favicon.” Prepare artwork for review near release preparation; no design is selected yet.
- **Optional PDF cover and reusable front matter.** The author is considering a simple cover and modest publication boilerplate, not an ISBN application or copyright registration. Prepare a restrained proposal for review: title and author/attribution, CC BY 4.0 license and existing third-party credits, release identifier/date, canonical website/repository, and a suggested citation. Keep stable material in a reusable template and derive version-specific fields from release metadata so future releases update consistently. Preserve the title Introduction to Physics; keep cp2e-ver1.1 discreet. Check existing front matter before adding duplicates. Cover/front-matter design and exact wording remain author decisions; do not invent registration claims or identifiers.

These tasks are queued near the end of 1.1, before final PDF layout checks and release packaging. No artwork or publication-output changes were made when recording this request.


## Focused fact-check cycle 2: priority-1 review ready

September 20, 2026: 11 unapplied proposals (F2-01–F2-11) and two coordinated author decisions (F2-H01/H02) are ready at http://127.0.0.1:8765/review-1.1/fact-check-cycle2/. Machine-readable packet: proposals/1.1/fact-check-cycle2.json; renderer: python tools/render_fact_check_cycle2.py; readable report: reports/1.1/fact-check-cycle2/review.md. Before snapshots are from the post-cycle-1 source; no new textbook changes applied.

Topics: cancer-cell sensitivity; inherited versus cellular genetic effects; observed latency; hereditary-risk estimates/animal evidence/hormesis; matching risk summary; radiation range and shielding; low-current reassurance and shock rescue; ECT/current path and high-frequency heating; intracardiac microshock. Dose-quantity terminology (with linked equations, tables, lens/neutron explanation, summary and exercise dependencies) and the photon-penetration mechanism are held for coordinated author discussion. Do not silently relabel the RBE table or broaden the photon rewrite. Numerical-table/CT-share audit remains priority 2.

Verification: all proposed substitutions reproduce their review XML; source hashes match; desktop and mobile review have no page overflow or MathML errors; all 16 current-context anchors resolve. The canonical source still verifies 955 files with 203 editorial records. The local server was restarted bound to 127.0.0.1:8765.

### F2-H01 dose-treatment review (2026-09-20)

Option 1 selected for drafting: compact modern treatment of absorbed, equivalent, and effective dose. Fifteen contextual comparisons are available in the cycle-2 review, covering the connected prose, equations, weighting and units tables, summary, and existing glossary entries. Replacements remain unapplied pending review. The acute-effects table and dose-band numbers still need the planned numerical audit; exercise assumptions will be reconciled during exercise revision.

### Priority 1 completed and applied — 2026-09-21

All 13 cycle-2 items are applied, including F2-H01/F2-H02 follow-ups, the minimal RBE-question repair, duplicated-sentence removal, and glossary alignment. Added radiation weighting factor, equivalent dose, and effective dose glossary entries; corrected linear-hypothesis and radiation-range definitions. Four maintained modules changed through 14 reversible editorial records (217 total). Historical baseline verification passed. Full course HTML and the two complete-section reading pages were rebuilt from canonical source. Numerical/background/activity/acute-effects tables and CT statistics remain priority 2; broad exercise revision remains separate. No 1.1 release PDF or public deployment was made in this step.

### Priority 2 inventory compiled — 2026-09-21

Six source-linked groups are available at http://127.0.0.1:8765/review-1.1/priority2-numerical-audit/ and in proposals/1.1/priority2-numerical-audit.json. Closer maintainer review: acute-effects table scope, dose-band/detection qualifications, background-table scope, and radiopharmaceutical formulation/procedure matches. Routine sourced directions: dated flight example and CT shares with explicit medical-exposure denominator. This inventory is not a completed numerical audit or an applied patch: unmatched activity rows, national-background provenance, final acute-effects rows, and adjacent carbon-14/fertilizer activity basis remain unresolved. Do not certify them. Ordinary exercises and a whole-book numerical audit are outside this pass.


## Coordinated P3 / heat-engine / P4 application completed — 2026-09-27

This entry supersedes earlier pending-application status notes. All 218 approved patches and coordinated glossary additions were applied across 26 modules, with 41 reversible editorial records (264 total). Two approved images were promoted into maintained assets with provenance and hashes. Carnot’s Principle attribution is now included by the full-book renderer. Evidence: `reports/1.1/priority34-application/manifest.json`. Preserve the original before/after review packets; do not regenerate their before snapshots from the newly edited canonical source.

Both full numbering profiles were rebuilt. The course build passed source/identity checks and a browser audit of all 156 section/exercise pages: 7,167 MathML expressions, no broken images, overflow or rendering errors. Historical baseline and editorial-ledger reconstruction passed. Three known external-media notices remain. This is a work-in-progress HTML preview; final PDF generation/layout validation and other 1.1 release tasks remain.

A dedicated generated Sites checkout keeps deployment assets separate from canonical content. Run `tools/prepare_sites_preview.py` after rebuilding to refresh it; preserve its `.openai/hosting.json` project identity. Published 1.0 remains unchanged.


## Historical exercise curation inventory — 2026-09-27

Read-only audit completed: [report](../reports/1.1/exercise-curation-audit/review.md), with per-exercise evidence in the neighboring inventory.json. Strongest sustained conceptual-curation boundary is the end of Chapter 7 (Fluids), but later chapters are partly curated, especially portions of Thermal Physics and Light. This is not proof of the last chronological edit. No exercises altered. Await fresh MyOpenMath export to guide a reviewed alignment/curation pilot.

## MyOpenMath export inspected and exercise plan proposed — 2026-09-27

Fresh export inventoried: 105 assessments, 1,642 instance records, 1,012 definitions; current, archived and unused branches separated. See [exercise revision plan](exercise-revision-1.1.md) and [separate MyOpenMath handoff](myopenmath-exercise-handoff.md). Chapters 0–7 are additions-first; later chapters require selective retention, removal, revision and addition. Proposed next step is a topic/family crosswalk and a bounded Dynamics-addition/Thermal-Physics pilot. No question content applied or published. Raw export preserved outside the publishing repository; metadata inventory records its checksum and source IDs.

## Exercise coverage crosswalk prepared — 2026-09-27

Whole-export inventory mapped to maintained sections with explicit confidence levels: 268 explicit section hints, 356 family-derived candidates, 135 topic/title candidates, 234 chapter-only, 19 unresolved archived definitions. Provisional grouping yields 437 description families; these are not certified unique objectives. See [crosswalk findings](../reports/1.1/exercise-crosswalk/README.md) and local review at http://127.0.0.1:8765/review-1.1/exercise-crosswalk/. Five initial content-level relationships identify additions, foundational practice and cross-section overlap for the Dynamics/Thermal Physics pilot. No textbook changes applied. Question-level link maintenance is intentionally deferred to winter break: maintainer manual pass, then scan a fresh export, potentially in a separate project.

Question-reference preference: review materials now identify MyOpenMath questions by full description plus an assessment/folder where they occur. Export IDs remain internal metadata only. Crosswalk refreshed accordingly.


## Chapter organization joined to exercise revision — 2026-09-27

Proceed chapter by chapter from Chapter 0, superseding the separate Dynamics/Thermal pilot. Compared original CNX Chapter 1 (PDF pages 9–22, printed 3–16) to current Chapter 0 and renderer behavior. Six proposed structural restorations are listed in [Chapter 0 structure review](../reports/1.1/chapter0-structure/review.md). Numbering compatibility remains separate from structural layout; no source or published-output changes applied. Await maintainer review of the list.

## Chapter 0 chapter-end organization applied — 2026-09-27

C0-01/C0-02 are deferred to preserve section numbering (0.1/0.2/0.3); the first-section chapter contents and self-link remain. Approved C0-03–C0-06 are applied to the website: one alphabetized glossary (21 terms), collected summaries, and 12 conceptual questions on the existing chapter exercise URL. Ordinary questions no longer appear twice; three inline checks remain. Existing source anchors provide forwarding links to moved items. No exercise content was added or removed.

Full browser audit: 156 pages, no findings. Source/math/media/link validation passed with the three previously recorded external-media limitations; this is still a 1.1 work-in-progress preview. Matching PDF end-matter assembly remains for final PDF preparation; no new PDF generated here.

Published to the existing Sites project and intro-1-1.coaphys.xyz. See docs/sites-preview-1.1.md for receipt. Next: Chapter 0 exercise additions using the MyOpenMath crosswalk, then chapter-by-chapter review.

## Website sequential navigation — 2026-09-27

Added Previous/Next links at the top and bottom of all 141 section pages and 15 chapter exercise/review pages. Destinations display section numbers and titles, or chapter names for review pages. The reading sequence follows the collection hierarchy, inserting each chapter review/exercise page after its final section. First/last pages omit the unavailable direction. URLs and numbering remain unchanged; book/PDF body excludes these controls.

Verified the complete 156-page chain, reciprocal links, identical top/bottom destinations, local link targets, mobile layout, and the full browser audit (no findings). Evidence: prototype/qa/reading-navigation-validation.json. This is a web-only presentation change.

## Section 0.2 attribution footer trial — 2026-09-27

Maintainer requested the proposed Sources and adaptations convention on Section 0.2 only, for visual review. Website footer preview stored in metadata/public-attribution.json (m52310); historical metadata and PDF footer unchanged. Preserves Bailey copyright/license/source and OpenStax ancestry, identifies subsequent revisions, and links the maintained repository. Full source/link validation passed; target footer rendered and visually inspected. Broader rollout awaits review.

## Sources and adaptations footers adopted — 2026-09-27

Maintainer approved applying the Section 0.2 convention across all modules. Shared renderer now generates Sources and adaptations, credited source/title/copyright/license, linked recorded ancestry, preserved extra-source and adapted-passage credits, and recovery/revision-history statement. Existing omission of maintainer self-credit retained. Historical attribution metadata and figure credits unchanged. Whitespace introduced by historical PDF extraction is stripped only from rendered ancestor URLs. Removed single-module trial override.

Verified all 141 footers retain source links and required recorded author/copyright credits; checked URL whitespace and mobile rendering. Full source/math/media/local-link validator passed with existing external-media limitations. Shared book HTML uses the same footer; no new PDF binary generated. Published receipt in sites-preview-1.1.md.

## Chapter 0 exercise additions applied — 2026-09-27

Added the five maintainer-approved questions: physics in other fields, recognition of units, explanation of conversion factors, a posted 65-mph conversion, and plate motion over one million years. Existing 12 ordinary questions and three inline checks retained. Chapter-end set now contains 17 questions (two short numerical tasks) under Questions and Exercises, without a separate Problems & Exercises category. Legacy XML collection class retained internally for renderer compatibility; new records distinguish conceptual and short-calculation tasks.

Stable IDs and reversible before/after records: proposals/author-corrections/EX-C0-m52310.json and EX-C0-m67032.json, registered in editorial ledger. Records identify full MyOpenMath descriptions and assessment locations; no grading code or export is published. Numbering regenerated in both profiles; old exercise anchors retained. New questions are 10 and 14–17 in the current chapter. Source validation and 156-page browser audit passed, including new MathML; desktop/mobile chapter review inspected. Numerical answers checked. PDF heading generation updated, but no new PDF binary generated.

## Chapter 0 exercise ordering before number freeze — 2026-09-27

Maintainer authorized freely reordering exercises during 1.1 preparation; after 1.1, avoid shifting existing numbers. Reordered without editing question text or IDs. New order: applications; model definition; model/theory distinction; validity; competing theories; measurement evidence; model limitations; classical conditions; satellite application; relativistic quantum mechanics. Units: base/derived definition; recognition; SI advantages; customary-unit comparison; conversion-factor explanation; posted-speed conversion; plate motion.

Recorded exact old/new mapping in reports/1.1/chapter0-structure/exercise-order.json and reversible ledger entries EX-C0-ORDER-m52310 / EX-C0-ORDER-m67032. Both numbering profiles rebuilt. All 17 rendered IDs and labels checked; mobile layout and source/link validation passed. Stable exercise links retained. No new PDF generated.

## Chapter 1 organization preview — 2026-09-27

Applied Chapter 0 pattern to Chapter 1: 28 alphabetized glossary terms, section summaries, 38 continuously numbered existing questions/exercises. Removed duplicate section-end copies; retained six inline checks, stable links and lecture-aligned section labels. Reordered existing questions by topic/progression without wording changes or additions. See reports/1.1/chapter1-structure/review.md. The original PDF's inline four constant-acceleration questions are explicitly flagged for joint review; preview collects them at chapter end.

Maintainer instruction: any future deviation in CNX PDF from this chapter-end pattern must be reviewed together. Do not assume an old deviation was intentional. Browser audit passed all 156 pages; targeted count, sequence, glossary sorting, figure loading and mobile checks passed. Both numbering profiles regenerated. PDF binary not rebuilt.

## Duplicate chapter-review link fix — 2026-09-27

Section 1.2 had two Questions and Exercises links because its two source categories each emitted a replacement navigation link. Renderer now emits each review destination once per section while preserving every moved object's forwarding anchor. Verified all section pages have unique chapter-review destinations and full source/link validation passes. No textbook content changed.

## Six Chapter 1 additions approved and applied — 2026-09-27

Added thunder distance (17), acceleration units (18), velocity-time graph sketches (27), braking-distance scaling (29), free fall while rising (30), and the cart launcher (38). Total is now 44 ordinary exercises; existing 38 and six inline checks unchanged. New questions follow matching topics rather than a separate additions block. Both numbering profiles rebuilt, stable IDs retained, 44 sequential labels and mobile layout verified, full source/math/link validation passed. No new PDF generated.

Full MyOpenMath descriptions/assessment locators and reversible before/after records are in proposals/author-corrections/EX-C1-ADD-*.json and the editorial ledger. Lecture-inspired graph/cart prompts are identified as newly formulated, not copied lecture blanks. Numerical result and conceptual answer reasoning checked; no public answer key added.

- Chapter 1 Exercise 2: applied approved total-distance/displacement wording (EX-C1-REVIEW-02-m52314); pending next preview rebuild/deployment.

- Approved exercise-answer policy: removed 223 ordinary exercise solutions across 43 modules; retained all 40 Check Your Understanding solutions and worked examples. Reversible EX-ANSWERS records preserve answer material for a possible future manual. Public preview deployment pending.

- Exercise review changes above published to intro-1-1.coaphys.xyz (Sites version 11); pending-publication notes are resolved.

## Chapter 1 approved; Chapter 2 organization — 2026-09-27

Maintainer approved Chapter 1 after exercise review. Proceed chapter by chapter; earlier separate Dynamics/Thermal pilot remains superseded. Chapter 2 organization collects 34 glossary definitions, section summaries, and 40 existing ordinary exercises. One inline check retained. CNX PDF pages 84–85 show two Normal Force and Tension questions inline; maintainer explicitly approved collecting them at chapter end. No new questions or wording changes in this pass. MyOpenMath additions will follow separate review.

## Quotation style adopted — 2026-09-27

Created [textbook style guide](style-guide.md): curly prose quotation marks/apostrophes and logical punctuation. Applied a prose-only typography pass in 65 modules with reversible TYPE-QUOTES records; preserved MathML and every XML attribute, substantive quotation wording, and historical source. Corrected the Weightlessness heading and explanatory prime marker. Punctuation in complete quoted sentences remains inside. No plural-g wording change. See reports/1.1/quotation-audit/applied.json.

- Approved Chapter 2 Exercise 5 choice wording applied (EX-C2-REVIEW-05-m67530); pending next preview refresh. Exercises 6–7 placement under discussion.

## Chapter 2 internal-force exercise placement — 2026-09-27

Maintainer requested overlap check and move before continuing review. Retained both questions: system-choice cancellation is general (now Exercise 19), while forces holding a body together is its concrete application (former 6, now 20). Former Exercise 7 remains in second-law group, now 6. Total remains 40. Exercise 5 approved wording included. Placement metadata in maintained/exercise-placement.json keeps module/exercise source identity and existing anchors intact while changing course presentation group and numbering; PDF mover consumes the same manifest placement. CNX historical profile remains unchanged. Source/link validation and targeted 40-question sequential/mobile check passed. No new PDF generated.

- Approved Chapter 2 Exercises 10, 14, 15 wording applied. Defer moving aircraft question (current 14) into second-law group until overall reorder after additions, per maintainer instruction. Ballistocardiograph source checks recorded in EX-C2-REVIEW-10-15-m68330.

- Applied approved Chapter 2 Exercise 16 replacement: book on table, contrasting second-law equilibrium and third-law force pairs. Exercise identity and numbering retained.

- Applied approved Chapter 2 Exercises 17 (garden hose), 21 (normal-force examples), and 22 (contact/tension constraints). Numbers unchanged.

- Applied approved Chapter 2 Exercise 25 eraser-on-table question to maintained source; pending next preview refresh. Batch subsequent approved exercise edits; refresh on request or chapter completion rather than after every edit. Public preview remains version 22.

- Removed former Chapter 2 Exercise 26 (adhesive tape), approved by maintainer. Chapter now has 39 ordinary exercises; later numbers shift down one. Include pending Exercise 25 eraser revision in next publication. Add actual-versus-maximum static friction/inequality coverage during MyOpenMath question additions. Exercise 14 move to Section 2.4 remains deferred until overall reorder.

- Preview version 23 published: pending Exercise 25 wording and tape-question removal are now live; 39 Chapter 2 exercises. Continue batching future edits until requested refresh or chapter completion.

- Applied approved Chapter 2 Exercise 28 replacement about predictive laws versus underlying mechanisms; pending next preview refresh.

- Applied approved Exercise 30 gravitation-unification replacement and removed former Exercise 31 (high-speed tire stress/diameter). Pending next preview refresh alongside Exercise 28. Chapter 2 will have 38 exercises; currently published Exercises 32–39 become 31–38. Public preview remains version 23 until refresh.

- Removed public-preview Exercises 35 and 36 (vertical-loop amusement rides) and their shared figure; confirmed no surviving source references to removed IDs. Pending refresh alongside prior edits/removal. Chapter now has 36 exercises. Continue using public version 23 numbers for review until refresh.

- Applied approved public-preview Exercise 37 lunch-box revision and matching caption: ground-frame path/Newton’s first law only; removed rotating-frame dust-trail question. Pending next refresh; public version 23 numbering remains the review reference.

- Removed public-preview Exercise 38 (ideally banked turn); pending refresh. Chapter 2 now has 35 exercises. Exercise 39 wording/caption proposal awaiting review. Public version 23 numbers still used for ongoing review.

- Applied approved public-preview Exercise 39 rewrite and caption (tension/third-law parts plus centripetal-force challenge). Hold preview refresh explicitly until discussing MyOpenMath Chapter 2 additions.

- Applied six approved MyOpenMath-guided Chapter 2 additions (including fixed Tommy box problem), reordered questions by section topic, and completed deferred aircraft-question display relocation into Section 2.4. Existing exercise identities and wording preserved during reorder. Chapter total now 41; final preview validation/publication pending. Provenance and orders: reports/1.1/chapter2-structure/exercise-additions-and-order.json.

- Chapter 2 preview version 24 published and validated: 41 exercises; all pending edits applied. New questions numbered 1, 24, 25, 28, 29, and 35. Aircraft question relocation completed (now Exercise 13 in Section 2.4). Await maintainer's full reordered question read-through. Use the new public numbers from now on.


- Maintainer approved all Chapter 2 questions after preview version 24 read-through. Next chapter: Chapter 3. Initial five crosswalk findings are now an explicit carry-forward checklist in docs/exercise-revision-1.1.md and status fields in reviewed-relationships.json: force classification complete; four Chapter 8 findings pending (ideal-gas reasoning, climate-question overlap/placement, phase-change classification, heating-curve energy ranking). Consult automatically when preparing that chapter; no maintainer reminder needed. No preview refresh for bookkeeping.

- Chapter 3 organization published as preview version 25: 23 glossary entries, section summaries, 20 unchanged ordinary questions collected at chapter end; two inline checks retained. CNX baseline follows expected pattern with no exception. Ready for maintainer read-through before MyOpenMath additions. Details: reports/1.1/chapter3-structure/review.md. Chapter 2 remains approved.

- Published Eq. 3.4.19 two-line numerical substitution/result (repeated symbolic expression removed) in preview version 26. Await maintainer layout check; 600px fits, very narrow phone widths still require existing math horizontal scrolling. Chapter 3 review ongoing.

- Published compact unit slashes for Eq. 3.4.19 in preview version 27; Chapter 3 read-through continues. No other equations normalized in this targeted change.

### 2026-09-27 — Unit-slash typography cleanup

Reviewed all 292 explicit MathML slash operators. Made 63 spacing-only corrections in 20 maintained modules; 3 additional unit slashes were already compact. The remaining 226 algebraic/nonunit slashes are unchanged. Text-token unit slashes required no changes. Preserved number-unit spaces, all tokens, annotations and IDs. Reversible per-module records and full operator dispositions: `reports/1.1/unit-slash-audit/inventory.json`. Course and CNX builds and full validation passed (6,921 math expressions; three pre-existing external-media findings). Representative native MathML renders inspected. Source changes apply to future PDF builds; no PDF binary regenerated.

### 2026-09-27 — Section 3.5 math typography

Moved the period preceding “In other words” inside the displayed equation and replaced mixed Content MathML to avoid unnecessary generated parentheses. Joined ΔKE and ΔPE tokens in Eq. 3.5.2 to remove unintended spacing. Removed the standalone “or” row in Eq. 3.5.3; retained both equivalent forms and the conservative-force qualification. Both builds and full validation passed; visually checked all three changes. Investigated deep radicals in Example 3.5.1: no source spacers; normal line-height test did not alter the shape. Radicals unchanged pending any further typography decision.

Section 3.5 spacing follow-up: restored comfortable space between the two equivalent equations in 3.5.3 after removal of the or row; added local margins around the unnumbered equation before 3.5.2. Published preview version 30. No global line-height changes or square-root edits.

### 2026-09-28 — Energy strategy box

Approved replacement of Section 3.5 six-step strategy with three conceptual prompts (energy forms, mechanical-energy conservation versus conversion, and reasonableness of changes), titled “Using Energy to Understand Motion”. Compared with 20 retained Chapter 3 questions and MyOpenMath Question Set 4 energy/momentum material. Reversible source record C3-ENERGY-CONCEPTUAL-STRATEGY-m67037. Published preview version 31. No exercise changes or PDF binary rebuild.

Energy box placement follow-up: moved to end of mechanical-energy subsection, immediately following the path-simplification paragraph, before Conservation of Total Energy. Wording and stable box ID unchanged. Published preview version 32.

### 2026-09-28 — Section 3.6 math cleanup

Repaired 15 MathML expressions, including the worked example and summary: proper exponent bases, numeric/unit tokens, fractions, shorter aligned lines and display spacing. Source record C3-SECTION36-MATH-DISPLAYS-m67045; preview version 33 published. All values and equation IDs preserved. Maintainer will review for remaining issues.

Section 3.6 average-force notation: bar moved over F alone with visible clearance; app remains subscript. Published preview version 34.

Chapter 3 glossary: moved (W) into watt heading; preview version 35 published.

Chapter 3 exercise review resumed: Exercise 4 references Figure 3.2.1(a), redundant unnumbered illustration removed. Published preview version 36.

### 2026-09-28 — Chapter 3 exercise review: pending batch refresh

Maintainer requests batching site updates while reviewing against published version 36. Do not publish each subsequent exercise edit; wait for batch-refresh request. Applied Exercises 7–8: predict final roller-coaster speed relative to original example and explain using energy; label book-lifting dependencies (a)–(d) and request brief explanations for each. Source XML parsed successfully; public preview unchanged.

Chapter 3: maintainer approved remaining existing questions after Exercises 7–8 edits. Continue with MyOpenMath-derived additions before batch rebuild/publication; published version 36 remains the review reference.

### 2026-09-28 — Chapter 3 batch published for final review

Maintainer authorized batch refresh: added five approved MyOpenMath-guided questions, reordered the full chapter set by topic, and published preview version 37. Chapter total is 25; new questions are 6, 7, 9, 16 and 22. Earlier book-lifting and roller-coaster revisions are now 10 and 11. Existing IDs and inline checks retained. Path comparison uses existing CC BY Figure 3.5.1. Provenance and final ordering: reports/1.1/chapter3-structure/exercise-additions-and-order.json and final-question-order.json. Both builds and full validation passed; narrow-screen browser check passed. This closes the pending batch-refresh hold above. Await final Chapter 3 exercise review; use the current public numbers.

### 2026-09-28 — Chapter 3 approved

Maintainer approved the complete Chapter 3 preview, including all 25 reordered questions, in Sites preview version 37. Chapter organization, prose/MathML follow-ups, conceptual energy box, glossary and question additions are complete for this review cycle. No Chapter 3-specific review items remain. PDF regeneration and final release-wide checks remain part of the overall 1.1 release work. Next chapter review is Chapter 4; no new publication needed for this approval record.

### 2026-09-28 — Chapter 4 organized and published

Preview version 38 collects eight glossary entries, five summaries and all 19 existing questions at chapter end. Historical PDF matches this organization, with no exception. Question wording/order and section numbers/URLs retained; no MyOpenMath additions yet. Both builds and full validation passed, with browser link/math/image/mobile checks. Ready for maintainer chapter read-through. Evidence: reports/1.1/chapter4-structure/review.md.

Chapter 4 review: removed optional collisions YouTube concept trailer from Section 4.1 (m42155). No other maintained module references URL hxMaoFcYSrw or media ID concept-trailer-collisions. Surrounding prose unchanged; historical copy retained. Both numbering builds and full validation passed; external-media findings now two. Record: C4-REMOVE-INTRO-VIDEO-m42155.

Chapter 4 section review: Section 4.5 approved with one edit clarifying that working through the collision-example algebra is optional; focus is interpreting numerical results. Applied C4-OPTIONAL-COLLISION-ALGEBRA-m67042. Both numbering builds and full validation passed. Maintainer continuing later sections.

Section 4.5 final follow-up: replaced the description of the unchanged-velocity solution with the approved hypothetical missed-collision explanation. Conservation laws hold in that case as well; the actual collision selects the other solution. Record C4-NO-COLLISION-SOLUTION-m67042. Both builds and full validation passed. Section 4.5 review complete per maintainer.

Section 4.6 review complete with Example 4.6.2 typography changes: hyphen/en dash replaced by minus, calculation operands shortened to hundredths (0.35 kg, 0.50 kg, -0.50 m/s); initial KE displayed as 0.76 J in both calculation/result and energy difference. Original three-significant-figure problem givens and final answers retained. Both builds/full validation passed; rendered equation inspected. Record C4-CARTS-CALCULATION-TYPOGRAPHY-m67043.

### 2026-09-28 — Book-wide minus-sign typography

Audited 284 minus-like MathML tokens throughout the maintained book. Corrected 174 arithmetic/negative-value/exponent/charge tokens in 40 modules, plus eight nearby prose/table passages. Preserved 78 overbars, 30 compound/value-unit hyphens, and two subscript-label separators. Dates, ranges, isotope names, source attributes and historical baseline unchanged. Per-module reversible MINUS-TYPOGRAPHY records and reports/1.1/minus-sign-audit/applied-audit.json document all dispositions. Added minus-sign convention to style guide. Both builds and full validation passed (6,916 math expressions; two existing external-media findings); rescan confirms only the 110 intentional non-minus MathML candidates remain. No PDF binary rebuilt.

Chapter 13 exercise carry-forward: m42542 / import-auto-id2719096 / exercise fs-id1346384 has existing momentum written as 4.48 × (−10)^(−19) kg·m/s. This looks like a separate source math error; do not silently change its value in a typography pass. Review during Chapter 13 exercise work (record also in minus-sign audit followups).

Minus-sign cleanup published in preview version 43. Representative renders inspected; ready to resume Chapter 4 review.

Chapter 4 exercise review: removed all five remaining Professional Application labels (three sections in Chapter 4); book-wide search found no others. Exercise text, IDs, order and numbering preserved; no incoming links to removed label paragraphs. Reversible EX-REMOVE-PROFESSIONAL-LABELS records created. Both numbering builds and full validation passed.

Chapter 4 exercises: approved removal of current public Exercise 7 (tennis sweet spots), source fs-id1700394 in m71583, applied to maintained source. Publication pending discussion of current public Exercise 8 (diving versus belly flop). Continue using preview version 44 numbering until the next refresh. Future full validator ordinary-question count must decrease by one (969 to 968), unless additional changes supersede that total.

Approved removal of current public Exercise 8 (diving/belly-flop depth), source fs-id1507984 in m67039, applied. Together with Exercise 7 removal, Chapter 4 now has 17 source questions, pending refresh. Public version 44 numbering retained during discussion of Exercise 18. Validator total must become 967 on next full validation (unless subsequent additions/removals alter total).

Approved removal of current public Exercise 18 (skaters), fs-id1672056 in m67043. Applied EX-C4-REMOVE-SKATERS-m67043. Chapter 4 now has 16 source questions after removals of public Exercises 7, 8 and 18. Preview refresh remains pending; keep public version 44 numbering during review. Validator total must become 966 on next full validation, subject to subsequent additions/removals.

Chapter 4: garden-hose cross-reference question wording approved for Section 4.4, pending insertion with additions (target Chapter 2 m68330/fs-id2661705, currently Exercise 17). Six MyOpenMath-guided additions proposed for review in reports/1.1/chapter4-structure/mom-addition-proposals.json; no approval inferred yet. Retained 16 questions plus hose plus six proposals would total 23. Public preview version 44 remains unchanged while reviewing proposals.

### 2026-09-28 — Chapter 4 additions and ordering

Applied six approved MyOpenMath-guided additions and the garden-hose cross-reference question. Reordered 23 questions in source section/topic order, preserving all 16 retained question texts and IDs. Previously approved removals (old public 7, 8, 18) included. New numbers: 1, 6, 7, 13 (hose), 15, 20, 22. Provenance and order: reports/1.1/chapter4-structure/exercise-additions-and-order.json; rendered texts/numbers: final-question-order.json. Both numbering builds and full validation passed (973 ordinary questions across book). Browser checks passed for consecutive numbering, links/anchors including Chapter 2 Exercise 17, no missing images/math errors, and 390px layout. Await final maintainer read-through after publication.

Published successfully as Sites preview version 45. Chapter 4 now has 23 questions; this supersedes the version 44 numbering and pending-publication notes above. Ready for final maintainer review at https://intro-1-1.coaphys.xyz/exercises/impulse-and-momentum-exercises/index.html#questions .


Approved removal of preview version 45 Exercise 9 (trampoline), m71583/fs-id1126726. Applied EX-C4-REMOVE-TRAMPOLINE-m71583; no incoming source references. Chapter 4 now has 22 maintained questions, with the full-book expected count updated to 972 for the next build. Do not rebuild or publish until maintainer finishes this review; continue referring to version 45 exercise numbers. Existing rendered order/validation reports describe that unchanged published preview and must be refreshed at the next build.


Approved replacement of preview version 45 Exercise 12 (m67039/fs-id1183915): projectile motion without air resistance, explaining horizontal versus vertical momentum conservation through forces and connecting to independent perpendicular motion components. Applied EX-C4-PERPENDICULAR-MOMENTUM-m67039; IDs retained and XML checked. Preview remains version 45, unchanged pending completion of maintainer review.


Approved preview version 45 Exercises 16 and 17 revisions: replaced 16 with two skaters pushing off from rest, asking how their individual momenta can sum to zero; removed 17 (vague total-energy/momentum question). Applied EX-C4-REVIEW-16-17-m67039. XML valid; no incoming references to removed IDs. Chapter 4 now has 21 maintained questions and next full-build expected count is 971. Preview remains version 45; continue using its exercise numbers until maintainer finishes review.

### 2026-09-28 — Chapter 4 second exercise review and force questions

Applied all approved review edits: removed version 45 Exercises 9 and 17; replaced 12 with the projectile-motion/perpendicular-components question and 16 with the two-skaters question. Added three approved force-as-momentum-change questions without altering Exercise 1. Reordered all 24 questions by section/topic; new questions are 4–6, skaters is 12, projectile motion is 15. See reports/1.1/chapter4-structure/force-additions-and-review-order.json and refreshed final-question-order.json. Both full builds and validation passed (974 ordinary questions). Browser checks passed for all 24 consecutive numbers, local links/anchors, missing images, MathML errors and 390px layout. Publication pending; awaiting final maintainer read-through.

Published successfully as Sites version 46. All pending Chapter 4 edits above are now live; use the new 1–24 numbering. Ready for final maintainer review at https://intro-1-1.coaphys.xyz/exercises/impulse-and-momentum-exercises/index.html#questions .

Chapter 4 final 24-question set approved by maintainer after preview version 46 review. Chapter 4 review complete. Starting Chapter 5 (Oscillations and Waves) organization against CNX 12.1, historical Chapter 6. Found another missing-classification exception: m71584/eip-964 two ordinary conceptual questions appear inline on PDF page 151 (printed 145); asked maintainer whether to collect at chapter end, consistent with Chapters 1 and 2. Awaiting that decision before applying organization and publishing.

Chapter 5 organization approved and applied, including the two inline Period and Frequency questions. Chapter-end review now has 33 alphabetized glossary entries, eight summaries, 23 ordinary questions; 12 Check Your Understanding prompts remain inline. Wording and IDs preserved. Both builds, full validation and chapter browser checks passed. See reports/1.1/chapter5-structure/review.md. Ready for maintainer chapter review after publication; no new questions added yet.

Chapter 5 organization published successfully in preview version 47. Start review at /sections/introduction-to-oscillatory-motion-and-waves/index.html; chapter-end material at /exercises/oscillations-and-waves-exercises/index.html. MyOpenMath question additions remain pending after initial read-through.


Chapter 5 review: removed extra hyphen following the em dash after “oscillate” in Section 5.1 (C5-INTRO-EXTRA-HYPHEN-m52431). XML checked. Hold preview refresh per maintainer; public preview remains version 47 during review.


Chapter 5 review: added explicit MathML spacing around “or” in Eq. 5.2.2 (m71584/eip-880), C5-FREQUENCY-OR-SPACING-m71584. XML checked. Preview refresh remains deferred.


Chapter 5 review: Eq. 5.2.7 (m71584/eip-663) split before = 3.79 into two aligned rows, preserving calculation and equation ID. C5-PERIOD-CALCULATION-LINEBREAK-m71584. XML checked; visual review pending batched preview refresh.


Chapter 5 review: Eq. 5.3.4 (m71585/eip-465) now starts with f= and goes directly from approximation sign to 1.36 Hz. C5-FREQUENCY-CALCULATION-CLEANUP-m71585. XML checked; preview refresh deferred.


Chapter 5 review: repaired inline function-list spacing in paragraph introducing Figure 5.3.4 (m71585/import-auto-id3032532). Separate MathML expressions with ordinary prose commas/spaces/conjunction. C5-GRAPH-FUNCTION-SPACING-m71585. XML checked; preview refresh deferred.


Chapter 5 review: replaced chest-cavity/normal-breathing resonance paragraph with approved walking example, emphasizing swing-leg natural frequency and muscular effort. C5-WALKING-RESONANCE-EXAMPLE-m71586; supporting research recorded there. Paragraph ID retained; XML checked; preview refresh deferred.


Chapter 5 review: corrected frequency/wavelength parentheticals in Section 5.5, m71587/eip-904 (C5-WAVE-FREQUENCY-PARENTHETICALS-m71587). XML checked; preview refresh deferred.


Chapter 5 review: approved superposition paragraph applied in Section 5.6, m71588/import-auto-id3047262 (C5-SUPERPOSITION-EXPLANATION-m71588). Replaces force-addition rationale with pointwise disturbance addition. Term anchor and figure links preserved; XML checked; preview refresh deferred.

Chapter 5 review batch: Section 5.8 summary now uses three bullets, preserving equations and paragraph IDs (C5-SOUND-SUMMARY-BULLETS-m71589). Rebuilt course and CNX with all nine approved pending Chapter 5 corrections. Full validation and chapter browser checks passed (23 exercises unchanged); visually inspected Eqs. 5.2.2, 5.2.7, 5.3.4 and the summary bullets. Prepared refreshed preview for in-context read-through before exercises. No PDF binary rebuilt.

All pending Chapter 5 changes above published successfully as preview version 48. Ready for in-context review and then exercise review; 23 existing exercise numbers unchanged. MyOpenMath additions still pending.


Chapter 5 review after preview 48: Eq. 5.2.7 gap before 1/f traced to native MathML centering the RHS cells despite columnalign="right center left". Added equation-scoped CSS left alignment for the third column; leaves vertical spacing and other equations unchanged. Preview refresh deferred.

### 2026-09-29 — Summary equation numbers and content audit

Hide all 108 summary equation labels at render time in both numbering profiles; retain IDs and internal counters. Verified no changes to non-summary equation labels and no incoming source links to summary equations. Audited 193 displayed/inline relationship candidates; four temperature-conversion formulas in Section 8.2 require an explicit body introduction (maintainer question pending). Separately recorded loop-count N/n and proton charge-to-mass 9.57/9.58 inconsistencies for review. See reports/1.1/summary-equation-audit/review.md. Eq. 5.2.7 local alignment fix included in next publish. Both builds/full validation passed; PDF binary unchanged.

Summary labels and Eq. 5.2.7 spacing fix published successfully as preview version 49. Temperature-conversion placement decision remains pending; two summary/body consistency findings remain explicitly tracked in the audit. Chapter 5 exercises still 23, unchanged.

Maintainer requested chapter-triggered follow-ups rather than handling later-chapter content now: temperature-conversion introduction in Chapter 8, and loop-count n/N in Chapter 10. Added explicit checklist reminders to docs/exercise-revision-1.1.md; retained proton charge-to-mass discrepancy for Chapter 12. Temperature-placement question resolved as defer to Chapter 8 review. No source or preview changes in this turn.


### 2026-09-29 — Chapter 5 question additions for review

Added twenty maintainer-approved MyOpenMath-guided questions and arranged the complete set by section/topic: 43 ordinary questions, retaining all 23 prior questions unchanged. New coverage includes cycle timing, heartbeat rate, oscillator motion/energy, natural versus driving frequency, wave motion, superposition, standing-wave patterns and harmonics, sound, and Mach number. Full descriptions and assessment names are recorded in reports/1.1/chapter5-structure/exercise-additions-and-order.json. Source export, controls and solutions are not included in the public site. All 12 inline Check Your Understanding prompts retained. Both numbering builds, full validation and Chapter 5 browser checks passed (43 sequential numbers, links/images valid, no mobile overflow). Pending maintainer read-through after publication.

Chapter 5 additions published successfully as preview version 50. Ready for review of all 43 questions together.

Chapter 5 exercise review: swapped preview-50 Exercises 10 and 11. New Exercise 11 asks why larger-amplitude spring oscillations cover more distance in the same period, in terms of speed/restoring force. Former Exercise 11 is now Exercise 10, unchanged. XML validated; preview publication pending next batch.

Chapter 5 exercise review: Exercise 21 now compares the wave in Figure 5.5.3 with the position-versus-time graph in Figure 5.3.4, asking about repetition in distance/time and wavelength/period intervals. Stable figure targets and XML verified. Pending next preview refresh alongside Exercise 10/11 changes.

Chapter 5 exercise review: Exercise 30 now compares standing-wave patterns in Figures 5.6.6 and 5.6.7; Exercise 31(b) counts antinodes instead of loops. XML and stable figure targets verified. Pending next preview refresh with prior exercise edits.


### Chapter 5 review complete

Maintainer approved Chapter 5 after reviewing all 43 questions. Final batch swaps Exercises 10/11, replaces new Exercise 11 with the longer-distance/constant-frequency spring question, references Figures 5.5.3/5.3.4 in Exercise 21 and Figures 5.6.6/5.6.7 in Exercise 30, and uses antinodes in Exercise 31(b). Both numbering builds and full validation passed; browser check confirms 43 consecutive exercise labels, working links/images and no narrow-screen overflow. Section 5.7 Sound has exactly one chapter-exercise link. Ready to publish final reviewed Chapter 5 preview.

Final Chapter 5 batch published successfully as preview version 51. Chapter 5 review complete; no pending Chapter 5 edits. Next chapter in sequence: Chapter 6.


### Chapter 6 organization ready for review

Matched CNX Chapter 7 end matter (PDF pages 196–200); no placement exceptions. Collected 13 glossary definitions, five summaries and 28 unchanged questions; five inline Check Your Understanding prompts retained. Removed optional unreferenced introduction video FmnkQ2ytlO8. Both builds, full validation and chapter browser checks passed. Details: reports/1.1/chapter6-structure/review.md. No PDF binary rebuild; MyOpenMath additions not yet proposed.

Chapter 6 organization published successfully as preview version 52; ready for maintainer read-through.

Chapter 6 browser review: Eq. 6.4.6 now uses three aligned lines; Eq. 6.4.7 explicitly begins KE_trans/KE_rot. Corrected grouping so only v is squared in the kinetic-energy formula. Course build and visual check at 920px passed (equation width 296px, no MathML errors). Stable equation IDs retained. Public preview refresh pending next batch.

Chapter 6 browser review: Eqs. 6.5.23 and 6.5.25 now use stacked angular-speed/conversion fractions, preserving two aligned rows and results. Normalized KE typography. Course build and 798px visual check passed (math widths 413/420px within 620px equation containers; no MathML errors). Pending next public preview batch alongside Eqs. 6.4.6/6.4.7.

Chapter 6 Exercise 5 revised with approved uniform-rod wording, explicit same rotation axis and link to Figure 6.3.3. No new figure. XML and link target verified; public preview refresh pending next batch.

Chapter 6 Exercise 9 moved from Section 6.3 to Section 6.4 with corrected frictionless-sliding versus rolling-without-slipping wording. Temporarily first in 6.4, preserving overall exercise numbering. TODO at final Chapter 6 ordering: place this question appropriately within rotational kinetic energy. XML validated; no incoming references. Public refresh pending.

Chapter 6 Exercise 13: replaced unfamiliar car-engine rocking question with maintainer-approved handheld electric drill startup wording, asking why the body tends to twist oppositely and how the hand prevents rotation. IDs preserved; XML validated. Pending next preview refresh.

Chapter 6 Figure 6.E.3 moved inside Exercise 15, after its question text. Image, caption, IDs and reference preserved; XML nesting and single occurrence verified. Pending next preview refresh.

Chapter 6 Exercise 19 approved and applied: polar land-ice melt redistributes mass away from the rotation axis; students explain day length and atomic-time drift. Named NIST Leap Seconds FAQs link retained; NASA factual source recorded in patch. XML verified. Pending next preview refresh.

Chapter 6 Exercise 25 (football/projectile spin stability), including its figure, moved unchanged to Section 6.6. Temporarily first to preserve global numbering. XML validated; no external source links to moved IDs. Public refresh pending; final within-section order deferred.

Chapter 6: removed preview-52 Exercise 26 (motorcycle steering), as approved. 27 ordinary questions remain before additions. XML and absence of incoming references verified; validation count expectations updated. On next build, old Exercises 27/28 become 26/27 unless further reordering intervenes. Public preview refresh pending.

Chapter 6: eight approved MyOpenMath-guided additions applied; all 35 questions ordered by section topic sequence. Pending moves of rolling-energy and spin-stability questions are now incorporated in final ordering. All earlier Chapter 6 review edits included; ordinary answers remain omitted and five inline Check Your Understanding items retained. Addition provenance and order: reports/1.1/chapter6-structure/exercise-additions-and-order.json. Preview refresh in progress.

Chapter 6 additions/review batch published as Sites version 53 (2026-09-29 local): 35 questions, all eight additions, topic ordering, prior approved exercise edits. Course/CNX builds and full validation passed (pre-existing external-media finding elsewhere); chapter browser check passed 35 consecutive questions, links, images, MathML, and 390px overflow. Four edited equation layouts rechecked at 920/798px. Non-exercise changes in this batch: Eqs. 6.4.6, 6.4.7, 6.5.23, 6.5.25. Ready for final Chapter 6 exercise review.

Chapter 6 final exercise review: Exercise 28 now explicitly asks what effect the skater’s work has on her rotational kinetic energy, before asking why angular momentum does not increase. XML verified. Pending next batched preview refresh.

Chapter 6 final review complete: Exercise 28 work/rotational-kinetic-energy addition published in Sites version 54. No further maintainer notes; chapter ready for progression to Chapter 7. Course/CNX builds and full validation passed with existing external-media finding elsewhere.

Chapter 7 organization complete: CNX comparison found no placement exceptions; 11 glossary entries, seven summaries and 42 unchanged questions collected at chapter end. Section numbering retained. Both builds and browser validation passed. Ready for body/exercise review before MyOpenMath additions. Evidence: reports/1.1/chapter7-structure/review.md.

Chapter 7 reorganization is live in preview version 55; ready for maintainer review.

Chapter 7 review: removed redundant “or g/mL” from all three Table 7.3.1 column headings (including matching math annotations). Retained 10^3 kg/m^3 and all table values. XML verified; pending next batched preview refresh.

Chapter 7 review: Eq. 7.4.4 now states 1 bar = 1000 mbar = 10^5 Pa; preceding sentence uses millibars (mbar). Clean MathML replaces the inconsistent legacy annotation. XML verified; pending next batched preview refresh.

Chapter 7 Exercise 15 revised with approved density/column-height wording and moved from 7.4 to first question in 7.5. IDs retained, no incoming source references found; XML valid. Global numbering unchanged for now; final topic ordering after additions. Pending next preview refresh.

Chapter 7 Exercise 19: approved dam/atmospheric-pressure clarification applied. XML verified; pending batched preview refresh.

Chapter 7 Exercise 22: approved bathtub-plug pressure wording applied; moved from 7.6 to end of 7.5, preserving current overall numbering and IDs. No incoming source references found; XML verified. Pending next batched preview refresh and eventual topic ordering.

Chapter 7 Exercise 25: approved marbles/container wording applied, specifying flat bottom, vertical walls, no overflow and rest; prompts explanation through increased water pressure plus direct contact. XML verified; pending next batched preview refresh.

Chapter 7 Exercise 29 garden-hose question moved unchanged from 7.8 to end of 7.7, preserving overall numbering for now. XML and unique IDs verified; no incoming references found. Pending batched preview refresh and final topic ordering.

Chapter 7 Exercise 38 (keel) removed as authorized: whole-text search found no keel mention outside this question. No incoming references; XML verified. 41 chapter questions remain before additions. Validation counts updated; pending next batched preview refresh.

Chapter 7: nine approved MyOpenMath-guided questions added; all 50 ordered by topic within their sections. Earlier approved edits/moves/removal included; figures preserved. Course/CNX builds and full validation passed (existing external-media finding elsewhere); browser checks passed 50 consecutive questions, links, images, math and 390px width. Source descriptions and assessments recorded in reports/1.1/chapter7-structure/exercise-additions-and-order.json. Non-exercise changes: Table 7.3.1 headings omit or g/mL; Eq. 7.4.4 and introduction show 1 bar = 1000 mbar = 10^5 Pa. Ready for final exercise review; publishing underway.

Chapter 7 pending batch is now live in preview version 56, including all nine additions and the density-table/bar-conversion changes.

Chapter 7 Eq. 7.8.2: cleaned nested MathML grouping, separated variables and operators, and placed exponent on v only. XML verified; pending next batched preview refresh.

Chapter 7 Bernoulli glossary entries: corrected literal Latin p to Greek rho and replaced ambiguous 1/2 text formulas with structured MathML stacked fractions. XML verified; pending next batched preview refresh alongside Eq. 7.8.2.

Chapter 7 final review — approved placement plan: move current Exercise 9 (ice-water glass, source m71613/fs-id1397150) and its nested figure from Section 7.3 to Section 7.6, immediately after ex-c7-ice-density. It requires Archimedes’ principle. Preserve wording and figure; update cross-links if needed. Apply in next organization/preview batch; source has not yet been moved.

Chapter 7 final review — approved placement plan: move current Exercise 17 (floating iceberg versus land glacier, source m71615/fs-id2590796) from Section 7.4 to Section 7.6, immediately after the planned ice-in-a-glass question (m71613/fs-id1397150). Final sequence: ex-c7-ice-density, ice-in-a-glass, iceberg versus land glacier. Preserve wording. Apply with the other planned move in the next organization/preview batch; source has not yet been moved.

Chapter 7 final review: removed current Exercise 26, wine-bottle/cork question (m71623/fs-id1355852), as requested. XML and no incoming references verified; validation counts updated to 49 chapter questions. Pending next batched preview refresh; planned ice-question moves remain pending.

Chapter 7 current Exercise 27 (ex-c7-submerged-volumes): approved rewrite specifies both objects denser than water and suspended from thin strings, asking (a) buoyant forces and (b) string tensions. XML verified; pending next batched preview refresh.

Chapter 7 final refresh: both approved ice-question moves applied with the glass figure retained, after ice-density question; wine-bottle question removed; suspended-object question clarified. Eq. 7.8.2 and both Bernoulli glossary formulas repaired. 49 questions; builds and browser checks pass. Final order recorded in reports/1.1/chapter7-structure/final-review-order.json. No outstanding approved edits; awaiting user’s final visual check before closing Chapter 7.

Final Chapter 7 batch live in preview version 57; awaiting final user visual confirmation.

2026-09-30: Maintainer reviewed preview version 57 and explicitly finalized Chapter 7. Chapter organization, section corrections, glossary math, and all 49 questions are approved. No outstanding Chapter 7 review items. Next chapter: Chapter 8; consult its deferred reminders before starting.

Chapter 8 organization prepared: 47 glossary entries, 13 summaries, 105 chapter-end questions (59 conceptual, 46 numerical); five inline CYU retained. Approved hot-tub/thermos wrappers applied; legacy paragraph-numbering aliases retired. Course numbering unified by section. Builds/browser checks pass. No content pruning or MyOpenMath additions yet. Review agenda and saved reminders: reports/1.1/chapter8-structure/review.md.

Chapter 8 reorganization live in preview version 58; ready for section and exercise review.

Chapter 8 Temperature summary: replaced four display conversions with one relationship bullet and inline Kelvin-from-Celsius equation. Body unchanged, per maintainer. Deferred summary-only conversion issue resolved. XML verified; pending batched preview refresh.

2026-09-30: Preview version 59 published successfully with the approved 47 Chapter 8 questions and the Section 8.2 summary conversion revision. Both numbering builds, source/link validation, and Chapter 8 browser checks passed (47 sequential questions, intact thermos figure, no broken images/math or mobile overflow). Usual Chapter 8 reorganization was already published in version 58. Receipt: reports/1.1/chapter8-structure/preview59-receipt.json.

2026-10-04: Maintainer explicitly finalized Chapter 9 after preview 71 review. All 55 exercises, section corrections, and Figure 9.E.1 approved. Chapter 10 organization prepared for later review: 42 glossary definitions, 10 summaries, 50 unchanged questions (19 conceptual, 31 numerical). Review agenda: reports/1.1/chapter10-structure/review.md; includes saved Section 10.8 n/N reminder.

Chapter 10 reorganization is live in preview 72, ready for review when the maintainer returns.

### 2026-10-09: Appendix lettering restored

Author approved course-profile appendices A Atomic Masses, B Selected Radioactive Isotopes, C Useful Information, D Glossary of Key Symbols and Notation, replacing LibreTexts 15–18. Historical metadata retained; maintained numbering overrides drive navigation and object references. Source URLs/anchors remain stable.
Preview 96 published successfully with appendix letters A-D. Both builds and full validation passed; all 12 changed object labels are confined to appendices and all anchors unchanged.

### 2026-10-09: Stable chapter permalinks

Author requested short chapter-introduction permalinks that survive renumbering while retaining canonical section URLs. Added maintained/chapter-permalinks.json keyed by stable module IDs, using /chapters/<topic>/ for all 15 chapter entries. Static aliases retain original anchors and relative assets, with canonical metadata pointing to original section pages. Generated navigation, contents, chapter-return links, source references, and search URLs prefer these paths. Original /sections/ pages remain available; chapter numbers are not part of permalink identity.
Preview 97 published: all 15 stable chapter permalinks live. Four routing unit tests, full builds/validation, anchor/asset checks, preferred internal URLs, and search deduplication verified in both profiles.

### 2026-10-09: Section 12.2 math italics

Removed both forced italic attributes in m67250 highlighted energy-step calculation. Whole-section audit found no other forced italic overrides. XML verified; pending preview refresh. Correction C12-BLACKBODY-REMOVE-FORCED-ITALICS.

### Outstanding author photograph — remind at every chapter finalization

Figure 12.3.2 (m67251#import-auto-id1362766) needs a higher-resolution author photo of the lab photoelectric apparatus. Author will arrange Monday reminder. Keep mentioning this during every chapter finalization until the new image and its credit are updated and verified. Tracking checklist: docs/exercise-revision-1.1.md, Outstanding items to mention at every chapter finalization. Existing image/credit unchanged for now.

### 2026-10-09: Section 12.3 forced math italics

Removed all 16 forced italic attributes in m67251; XML comparison verifies only those attributes changed. Normal variable italics and prose emphasis retained. Correction C12-PHOTOELECTRIC-REMOVE-FORCED-ITALICS. Pending preview refresh. Earlier parenthesis simplification was proposed, not yet applied. Outstanding apparatus photo remains on every-chapter-finalization checklist.

2026-10-09: Removed the space between inline h and the first em dash in Figure 12.3.4 caption (m67251/import-auto-id1573454). XML verified; pending next batched preview refresh.

2026-10-09: Repaired Example 12.3.1 MathML tokens and grouping (operators, complete numbers, upright units); two photon-energy calculations now use aligned two-row layouts with results on the second row. Repeated kinetic-energy formulas corrected consistently. Values and prose retained; XML verified. Pending preview refresh.

2026-10-09: Removed all three forced italic MathML overrides in Section 12.4, The Wave Nature of Matter (m67803). XML comparison verifies only these attributes changed; normal variable styling and prose emphasis retained. Pending next preview refresh.

2026-10-09: Split Example 12.4.1 velocity substitution (m67803/eip-177) before the second equals sign into two aligned rows. Numerical values retained; XML and row structure verified. Pending next preview refresh.

2026-10-09: Corrected uncertainty-product grouping and thin spacing in equations 12.5.3 and 12.5.4 (m67804/eip-840, eip-227), including proper delta and 4 pi tokens. XML verified; pending next preview refresh.

2026-10-09: Applied uncertainty-product grouping and thin spacing to the three remaining occurrences in m67804: Example 12.5.1 strategy, its displayed minimum-uncertainty equality, and section summary. XML verified; pending preview refresh.

2026-10-09: Split Example 12.5.1 momentum uncertainty calculation (m67804/eip-810) before the final equals sign into aligned rows. Values retained; XML and row structure verified. Confirmed eip-833 product spacing already corrected. Pending next preview refresh.

2026-10-09: Moved final results to separate aligned rows in Example 12.5.1 velocity uncertainty and kinetic energy calculations (m67804/eip-899 and eip-669). Values preserved; XML and two-/four-row layouts verified. Pending preview refresh.

2026-10-09: Separated ordinary parenthetical labels from MathML in equations 12.6.3–12.6.5 (m67805/eip-479, eip-618, eip-19). Values, IDs and numbering retained; numeric/unit tokens cleaned up. XML and label separation verified. Pending preview refresh.

### 2026-10-09: Global sentence punctuation cleanup

Before resuming Chapter 12 review, added shared publishing normalization that moves terminal sentence punctuation outside MathML and excludes it from equation copy formats. Audit: 6,726 expressions, 836 normalized across 98 modules; six mathematical ellipses retained. Fixed one malformed source comma inside a fraction denominator. Block/multiline visual placement checked across the full book at phone, tablet and desktop widths. Details: reports/1.1/math-sentence-punctuation/review.md. Pending next preview refresh.

2026-10-09: Preview 98 published successfully with all saved Chapter 12 math/layout fixes and the global sentence-punctuation normalization. Both builds and full validation passed; whole-book punctuation placement checked at three viewport widths. Deployment receipt: reports/1.1/math-sentence-punctuation/preview98-receipt.json. Photoelectric apparatus photo replacement and credit update remain outstanding.

2026-10-09: Moved the two additional charge-to-mass ratio labels (electron/proton) outside MathML in Section 12.6. Summary expressions checked; no embedded copies remain. XML verified; pending next preview refresh.

2026-10-09: Completed global prose-label audit over all 6,726 expressions. Reviewed 202 prose-like candidates; moved 11 additional labels/qualifiers outside MathML across eight modules. Preserved units, word equations, counted entities, and mathematical subscripts. Saved reviewed retained cases and repeatable audit tool to flag future additions. Both builds/full validation and 22 mobile/desktop label checks pass. Details: reports/1.1/math-prose-labels/review.md. Pending next preview refresh, together with the two Section 12.6 ratio labels.

2026-10-09: Preview 99 published successfully with the 11 global prose-label fixes and the two Section 12.6 charge-to-mass ratio labels. All approved pending math/layout corrections are now live. Receipt: reports/1.1/math-prose-labels/preview99-receipt.json. Chapter 12 review may resume; apparatus photo/credit replacement remains outstanding.

### Native reading theme
Added a persistent System/Light/Dark selector to site navigation. System is the default; changes apply before page styles load. Dark colors cover prose, equations, examples, tables, search, and copy dialogs; figures retain their original colors and print keeps the light palette. Browser checks passed for five page types, mobile layout, persistence, system changes, blocked storage, equation copying, and print. Evidence: reports/1.1/native-dark-theme/validation.json.


### Bohr summary table layout
Shortened the dependence heading and replaced four proportional-to labels with the proportionality symbol. Orbital energy now has two aligned lines, no redundant parentheses, and denominator 2 n-squared hbar-squared without an explicit multiplication sign. Source correction: C12-BOHR-TABLE-COMPACT-m67807. Both builds passed; table inspected at 624px. Screenshot: reports/1.1/bohr-table/table.png.


### Bohr derivation layout
Split the Bohr radius, photon-energy substitution, and Rydberg constant at their final equals signs. Removed redundant parentheses, retained subtraction grouping, and used implied multiplication for symbolic products (including the intervening wavelength expression). Both builds and full validation pass; 520px screenshots are in reports/1.1/bohr-derivation. Source record: C12-BOHR-DERIVATION-LAYOUT-m67807.


### Wave quantization MathML cleanup
Separated allowed-n conditions into their own MathML with ordinary-text parentheses in both body equations and summary repetitions (four occurrences). Removed six forced-italic attributes throughout m67808. Both builds and validation passed; screenshots and equation-boundary checks at 520px are in reports/1.1/wave-quantization. Source record: C12-WAVE-QUANTIZATION-MATH-m67808.


### Chapter 12 glossary and summary review
Clarified hydrogen-like atom/ion definition and section discussion; rebuilt glossary energy formula with normal variable typography and a separate allowed-n condition; added prose definition for Planck's constant. Normalized summary italic overrides and upright Delta. Corrected reduced Planck constant description (Unicode U+210F verified) and showed equivalence of nh/(2pi) and n hbar in section 12.8 and its summary. Heisenberg's uncertainty principle already exists in the glossary under H; retained that entry. Both builds and full validation passed; screenshots in reports/1.1/chapter12-glossary-review.


### Bohr photon-energy equality (pending preview)
Applied the previously discussed removal of redundant parentheses in Eq. 12.7.4: hf = Delta E = E_i - E_f. Normalized upright Delta and moved trailing comma outside MathML. Source XML validated. Preview intentionally not refreshed.


### Chapter 12 exercise scope decisions (pending preview)
Removed Preview104 exercises 48-53, 60-61, and 75-78. Added a qualitative one-electron helium-ion versus neutral-helium question. Expected set: 69 exercises. Record: reports/1.1/chapter12-structure/scope-decisions.json. Keep remaining question review tied to Preview104 numbering until refresh.


### Chapter 12 exercise review preview
Removed Preview104 Exercise55 (duplicate of59), corrected65 MathML to 2 pi-squared and69 units to inverse metres. Chapter now has 68 exercises including approved scope removals and conceptual ion addition. Rebuilt both profiles and checked copied formula representations. This publication also includes the saved Eq.12.7.4 parentheses correction. Old59 becomes52; old65 becomes57; old69 becomes61.


### Hydrogen-like ion glossary (pending preview)
Renamed the glossary term to hydrogen-like ion and saved the approved definition explaining why its one remaining electron permits application of Bohr's model. Preserved definition anchors. Preview intentionally unchanged.


### Global descriptive-subscript audit (pending preview)
Reviewed editable MathML across the maintained book and corrected 191 descriptive-subscript occurrences in 32 modules, including initial/final, image/object, named forces and speeds, and particle mass/charge labels. Retained quantum indices, coordinate variables, and Greek particle-symbol subscripts; undefined E_B remains flagged. Copy LaTeX verified for E_i/E_f. Records and retained cases: reports/1.1/subscript-audit/review.json. Preview not refreshed; raster figure lettering is outside this MathML audit.


### Particle notation follow-up (pending preview)
Kept current Exercise 48's undefined E_B distractor by author decision. Corrected 27 Latin-v neutrino occurrences to Greek nu across five affected source modules (including related particle-style corrections), restored italic neutrino flavour symbols, and made descriptive mu/tau lepton-number labels upright. Recorded the PDG particle-symbol convention and NIST quantity-label distinction in the style guide. Two frequency-nu occurrences in the electromagnetic-spectrum application section remain unchanged pending context review. Audit: reports/1.1/subscript-audit/neutrino-frequency-review.json. Raster figure lettering is outside this audit.

### Particle-subscript convention reconciliation (pending preview)
Checked the saved audit against the agreed contextual convention: 81 common-particle quantity subscripts and 54 neutrino flavour subscripts conform, with no further source changes required. Coordinate and quantum indices remain italic, descriptive lepton-family labels remain upright, and the approved Exercise 48 distractor is retained. Two frequency-nu uses in Section 11.5 remain for author review. Report: reports/1.1/subscript-audit/particle-convention-review.json. No preview refresh.

### UV photodissociation notation (pending preview)
Section 11.5 now describes UV light breaking a CFC bond and places “UV light” above the reaction arrow. Removed both h-nu photon-energy references, avoiding particle notation before Chapter 12. Stable paragraph and equation IDs retained. Preview unchanged.

### Chapter 12 Exercises 1–2 wording (pending preview)
Replaced physical entity with physical property, retained quantized terminology, and requested two examples with their allowed values in Exercise 1 and continuous ranges in Exercise 2. Corrected described to describe in approved wording. Stable exercise and paragraph IDs retained; source XML validated. Preview unchanged.

### Chapter 12 redundant Exercise 7 (pending preview)
Removed the orangutan oscillator problem (Preview105 Exercise 7, m67250/fs-id1319731). Exercise 5 already covers energy spacing and n; Exercise 4 covers why everyday quantization is unobservable. Chapter 12 now has 67 exercises; bookwide projected count is 839. Continue review using unchanged public-preview numbers until the next refresh.

### Chapter 12 Exercise 8 wording (pending preview)
Replaced Preview105 Exercise 8 (m67251/fs-id874567) with the approved open-ended prompt about what determines photoelectric emission from a material and which spectral regions can cause it. Stable IDs retained; source XML validated. Preview unchanged.

### Chapter 12 redundant Exercise 10 (pending preview)
Removed Preview105 Exercise 10 (m67251/fs-id1565970), retaining Exercise 9 unchanged because it already addresses the explanatory roles of wave and photon models. Chapter 12 now has 66 exercises; bookwide projected count is 838. Continue using public-preview numbers until refresh.

### Chapter 12 Exercise 11 removal (pending preview)
Removed Preview105 Exercise 11 (m67251/fs-id1631189), which conflates photoemission thresholds with conductivity and requires solid-state concepts beyond the chapter scope. Chapter 12 now has 65 exercises; bookwide projected count is 837. Public-preview numbering remains unchanged until refresh.

### Chapter 12 Exercise 12 removal (pending preview)
Removed Preview105 Exercise 12 (m67251/fs-id1545718): thermal emission and shaking-versus-heating are outside the section development; revised Exercise 8 covers the escape-energy objective. Chapter 12 now has 64 exercises; bookwide projected count is 836. Public-preview numbering remains unchanged until refresh.

### Chapter 12 Exercises 25–26 removal (pending preview)
Removed Preview105 Exercises 25 and 26 (m67251/fs-id1555510 and fs-id1548779). Exercise 25 uses subthreshold photons; Exercise 26 claims electron kinetic energy greater than photon energy. Both are inconsistent-energy checks of the photoelectric relation. Chapter 12 now has 62 exercises; bookwide projected count is 834. Preview unchanged.

### Photoelectric calculation review and accumulated preview refresh
Applied approved work-function and wording audit for Preview105 Exercises 13–24, preserving stable IDs. Potassium now 2.30 eV; calcium 2.87 eV; sodium data consistent at 2.28 eV. Worked calcium example now uses more precise constants, photon energy 2.95 eV, maximum kinetic energy approximately 0.08 eV, stopping potential 0.08 V, and threshold wavelength 432 nm. Electron-rate/power questions state ideal upper-limit assumptions, and sunlight/recovery wording is removed. Refresh includes all pending global notation and Chapter 12 editorial changes.

### Preview106 Exercise 20 removal (pending preview)
Removed m67251/fs-id1596197 (Preview106 Exercise 20; Preview105 Exercise 24), retaining Preview106 Exercise 19 as the last photoelectric calculation. Chapter 12 now has 61 exercises; bookwide projected count is 833. Public preview remains version 106 until next requested refresh.

### Preview106 Exercise 21 wording (pending preview)
Saved approved two-part interference question (m67803/fs-id2731532), separating pattern similarity from detection and buildup with individual electrons. Stable IDs retained; source XML validated. Preview unchanged.

### Preview106 Exercises 22–23 combined (pending preview)
Combined into the approved two-part experimental-observation question at m67803/fs-id1306355; removed the separate m67803/fs-id1278570 exercise. Chapter 12 now has 60 exercises; bookwide projected count is 832. Preview remains unchanged.

### Preview106 Exercise 24 wavelength (pending preview)
Changed m67803/fs-id1308269 from 1.00 m to 1.00 mm. Nonrelativistic de Broglie calculation gives 0.727 m/s. Source XML validated; preview unchanged.

### Preview106 Exercise 26 comparison (pending preview)
Saved approved proton/electron comparison at 6.00 fm in m67803/fs-id1208943. Both calculations explicitly use p=mv and ask students to assess the approximation against c. Source XML validated; preview unchanged.

### Preview106 Exercise 27 radius comparison (pending preview)
Revised m67803/fs-id1224509 to ask for the speed at which the 0.400-kg ball has a wavelength equal to its stated 3.00-cm radius. Removed the inter-ball interference claim. Result: approximately 5.52 × 10^-32 m/s. Source XML validated; preview unchanged.

### Preview106 Exercise 27 regulation dimensions (pending preview)
Supersedes the earlier 0.400-kg, 3.00-cm billiard-ball version: approved wording now specifies a pool ball of mass 0.170 kg and radius 2.86 cm, consistent with WPA dimensions. Result approximately 1.36 × 10^-31 m/s. Source XML validated; preview unchanged.

### Preview106 Exercise 28 removal (pending preview)
Removed m67803/fs-id1655339 as repetitive of Preview106 Exercises 25 and 26. Chapter 12 now has 59 exercises; bookwide projected count is 831. Preview unchanged.

### Preview106 Exercise 30 removal (pending preview)
Removed m67803/fs-id1678654 because the nuclear-scale wavelength calculation duplicates Exercise 26 with a neutron instead of a proton. Chapter 12 now has 58 exercises; bookwide projected count is 830. Preview unchanged.

### Preview106 Exercises 24 and 33 combined (pending preview)
Merged into m67803/fs-id1308269: (a) 1.00-mm electron wavelength; (b) 1.00-μm wavelength speed and accelerating potential from rest. Removed separate fs-id1471848. Chapter 12 now has 57 exercises; projected total 829. Preview unchanged.

### Preview106 Exercises 35–36 (pending preview)
Exercise 35 now compares the nonrelativistic electron wavelength with the shortest X-ray wavelength when all kinetic energy goes to one photon. Removed Exercise 36 because revised Exercise 26 checks the same approximation failure. Chapter 12 now has 56 exercises; projected total 828. Preview unchanged.

### Preview106 Exercise 37 uncertainty wording (pending preview)
Saved approved three-part prompt at m67804/fs-id1252921, retaining the glossary term Heisenberg uncertainty principle, using atomic/nuclear length scales, and distinguishing individual uncertainties from their joint constraint. Stable IDs retained; source XML validated. Preview unchanged.

### Preview106 Exercises 38–39 comparison scale (pending preview)
Exercise 38 now supplies a concrete molecular bond-energy benchmark (H2 dissociation, 4.48 eV) and explicitly distinguishes speed from velocity uncertainty. Exercise 39 repeats all parts for chlorine using a stable cross-reference. Membrane setting retained; not explained in section prose and does not enter the calculation. Preview unchanged.

### Preview106 Exercise 39 removal (pending preview)

Removed the chlorine-ion repeat of Exercise 38 to avoid conflating whole-ion localization with electron binding. Chapter 12 now has 55 exercises; projected book total is 827. Exercise 38 wording at 0.100 nm was subsequently approved and saved (see atomic-localization entry below).

### Preview106 Exercises 40–41 removal (pending preview)

Removed the electron position-uncertainty question as redundant and the accelerator proton question for limited conceptual value. Chapter 12 now has 53 exercises; projected book total is 825.

### Preview106 Exercises 42 and 44 ordering (pending preview)

Moved the Millikan oil-drop question (44) ahead of the electron-mass evidence question (42), making it the first exercise of Section 12.6. Replaced the generic justification in 42 with the approved independent questions about combining measured quantities and Thomson’s measurement. IDs and exercise count are unchanged.

Preview106 Exercise 42 now asks for “measured quantities” instead of “pieces of evidence”; remaining wording unchanged (pending preview).

Preview106 Exercise 45 is now a single-part scale-model calculation: removed the subjective “How easy will this be to do?” follow-up and the (a) label (pending preview).

### Preview106 Exercise 47 removal (pending preview)

Removed the hydrogen-like-ion conceptual question; Bohr-model concluding prose unchanged. Chapter 12 now has 52 exercises; projected book total is 824.

### Preview106 Exercises 48–49 combined (pending preview)

Combined the first- and third-line Lyman calculations and spectral-region identification into Exercise 48. Chapter 12 now has 51 exercises; projected book total is 823.

Preview106 Exercise 55: simplified legacy MathML, using a proper fraction for (13.6 eV)/(hc), numeric tokens, and consistent number-unit spacing (pending preview).

Preview106 Exercises 56–58 (Balmer limit, Paschen range, and Balmer/Lyman overlap) moved in that order immediately after the combined Lyman-series question. Wording, IDs, and count unchanged (pending preview).

### Preview106 Exercise 59 removal (pending preview)

Removed the Balmer visible/UV line-count question as redundant. Chapter 12 now has 50 exercises; projected book total is 822.

### Preview106 Exercise 61 removal (pending preview)

Removed the Balmer wavelength percentage-difference question. Chapter 12 now has 49 exercises; projected book total is 821.

### Preview106 Exercise 38 atomic localization (pending preview)

Saved the approved 0.100 nm localization question, including minimum velocity uncertainty, the kinetic-energy scale K = (1/2) m_e (Delta v)^2, and comparison with 4.48 eV hydrogen dissociation energy. Removed the membrane setting. Exercise IDs and count unchanged.

### Chapter 12 MyOpenMath-oriented additions and topic ordering

Added seven approved exercises across Sections 12.3, 12.5, 12.6, 12.7, and 12.8; extended the sodium photoelectron question with stopping potential. The Bohr assumptions question is confined to its classical and quantum ingredients; standing-wave matching and probability-cloud interpretation are in 12.8. Reordered 12.7 to follow empirical spectra, orbital assumptions, radius and energy scales, transitions, and the Rydberg constant. Preserved oil-drop-first order in 12.6. Chapter 12 now has 56 exercises; projected book total 828. Optional blackbody/Planck-constant questions were not added. Full source provenance and answers are in reports/1.1/chapter12-structure/mom-additions-applied.json.

### 2026-10-10: Chapter 12 finalized; Chapter 13 review preparation

Maintainer finalized Chapter 12 after Preview 107 with 56 exercises and all approved MyOpenMath-oriented additions. No pending Chapter 12 wording decisions. Figure 12.3.2 apparatus photo replacement remains an explicitly deferred asset task: await maintainer photo and update its credit/caption/alt text together; continue reminders at every chapter finalization. Preparing Chapter 13 by collecting glossary, summaries, and all 94 existing chapter-end exercises in section order, preserving question content and IDs and retaining five inline Check Your Understanding prompts. Numerical-review flags: m42542/fs-id1346384 negative scientific-notation base; m42546 Equation 13.7.15 electron-mass inconsistency. Four remaining explicit Unreasonable Results exercises are flagged for upcoming review. No Chapter 13 pruning or MyOpenMath additions in this organization pass.


### 2026-10-10: Chapter 13 finalized; Chapter 14 organization

Maintainer finalized Chapter 13 after Preview 113, approving all 39 exercises and the new space-time diagram subsection. Chapter 14 prepared with 112 glossary definitions, 10 section summaries, and 195 original chapter-end exercises in section order. All exercise content and IDs preserved by the organization script; 0 inline checks retained. Section 14.12 missing objective particle name flagged for review. Figure 12.3.2 author photograph remains deferred; reminder delivered. Chapter 14 review inventory: reports/1.1/chapter14-structure/review.json.


Preview 114 published successfully: Chapter 14 organized and ready for review. Both numbering builds, full validation, and narrow/desktop browser checks passed. Receipt: reports/1.1/chapter14-structure/preview114-receipt.json. Chapter 13 finalized; no canonical GitHub push.


### 2026-10-11: Same-page numbering selector

Completed the older textbook map from the preserved PDF outline (140 labeled modules plus unnumbered preface). Added Lecture-aligned / Older textbook selection at the same page URL, with persistent preference and synchronized headings, navigation, object labels, references, and search. Per author direction, both modes retain section-based object counters; exercise numbers remain stable. Chapter introductions use chapter.0 object labels in older mode. Source CNXML and stable links are unchanged. Evidence and checks: reports/1.1/numbering-toggle/.

### 2026-10-12: Numbering and header review complete

Previews 116–118 rename the alternate mode CNX-aligned, hide duplicate introduction entries in CNX-aligned contents, and center the header with both preference menus wrapping together. User approved the preview and requested committing these updates to GitHub. Course build, numbering checks across 141 sections, and header checks at 320–1600 px passed. Publication receipts and browser evidence are in reports/1.1/numbering-toggle/.

### 2026-10-12: Figure 12.3.2 author photograph

Replaced the deferred photoelectric-tube photograph with author photo 4. Applied a deterministic crop and resize, retained the full-resolution original in local references, and updated the caption and alt text, and removed the obsolete credit. Author selected photo credit to College of Alameda Physics Department. The author identified the yellow-wire connection as the photocathode and the circular wire as the anode; uncertain routing and design intent are omitted. Browser checks verify the image at 390 and 1200 px and both numbering labels. This closes the chapter-finalization photo reminder.

### 2026-10-13: Radiation-name parentheses

Moved parentheses around the initial alpha, beta, and gamma symbols in m76584/import-auto-id3422619 into prose, leaving only the Greek letters in MathML. Added the missing spaces after the names. XML and all three math contents verified. Queued for the next preview refresh.

### 2026-10-13: Greek particle plurals

Applied the approved α’s / β’s / γ’s convention across maintained source with ’s outside MathML, including captions, exercises, and the isotope appendix. Preserved “the α’s charge to mass ratio” as requested. Recorded the convention in docs/style-guide.md and the inventory in reports/1.1/greek-particle-plurals/applied.json. Queued for next preview refresh.

### 2026-10-13: Redundant E italic attribute

Removed the sole explicit italic MathML attribute in m76584 (E in import-auto-id1177617). Default mathematical italics and prose emphasis are unchanged. XML check passed; no explicit italic MathML attributes remain in the section. Queued for next preview refresh.

### 2026-10-13: Substructure of the Nucleus italic cleanup

Removed three explicit italic MathML attributes (A, m, N) in m52466. XML validation passed; no explicit italic MathML attributes remain in the section. Default variable italics retained. Queued for next preview refresh.

### 2026-10-13: Decay-equation descriptions

Moved the four parenthetical decay descriptions in m76603 (alpha, beta-minus, beta-plus, gamma) outside reaction MathML. Parentheses and the word decay are prose; particle symbols retain separate math. IDs and reactions retained; XML validation passed. Queued for next preview refresh.

### 2026-10-13: Reaction-energy equation spacing

Cleaned up m76603/eip-241: removed explicit spacing before equals, changed Delta from an operator to an upright identifier, grouped parentheses, and moved the sentence period outside MathML. Relationship and equation ID retained. XML valid. Queued for next preview refresh.

### 2026-10-13: Nuclear decay italic cleanup

Removed all 20 explicit italic MathML attributes in m76603, including the annotated Delta m. XML valid; no explicit italic MathML attributes remain in the section. Standard mathematical styling retained. Queued for next preview refresh.

### 2026-10-13: Final-mass sum display

Replaced over-wide inline mass sum in m76603/import-auto-id2684784 with three displayed lines. Corrected decimal/operator/unit tokenization and isotope grouping; numerical values unchanged. XML valid. Queued for next preview refresh.

### 2026-10-13: Neutron-decay particle symbols

Changed n and p in m76603/eip-828 from upright text to mathematical identifiers, following the particle-symbol style convention. Included in the pending preview refresh.

### 2026-10-13: Final-mass punctuation placement

Anchored the period to the final u in the three-line mass sum; the renderer separates it from copied math and aligns it to the last row. Thus now starts a new paragraph. Queued for next preview refresh.

### 2026-10-13: Half-life calculations on two lines

Split m52471/eip-15 and eip-806 into two aligned display rows each, placing the evaluated fraction and final count on the second row. Tokens and values retained; XML and row-count checks passed. Queued for next preview refresh.

### 2026-10-13: Half-life and activity italic cleanup

Removed all six explicit italic MathML attributes on N and t in m52471. XML validation and section rescan passed; normal mathematical styling preserved. Queued for next preview refresh.

### 2026-10-13: Carbon activity calculations on two lines

Split m52471/eip-999, eip-367, eip-515, and eip-403 into two aligned rows, with each final result on its own line. The 250 Bq conversion is included; the following curie conversion (eip-172) remains on one line. Values and punctuation preserved. Queued for next preview refresh.

### 2026-10-16: Activity equation alignment

Normalized MathML in m52471/eip-515 and eip-403: dedicated equality column, consistent relation spacing, decimal numbers as single tokens, multiplication operators, and separate upright units. Both retain two lines and unchanged values. Queued for preview refresh.

### 2026-10-16: Radiation unit spacing and table wrapping

Added explicit number-unit spacing in m68327/eip-810 and made the Bq-to-Ci table conversion wrap only after the approximation sign when necessary. Queued for preview refresh.

### 2026-10-16: Proton-proton cycle energy annotations

Replaced parenthetical energies throughout the fusion section, including all ten body equations with energy annotations and four repeated summary equations, with separate Q expressions and defined Q in prose. Preserved equation numbers; reaction and Q expressions wrap as separate units on narrow screens.

### 2026-10-16: Fusion reaction-count conversion factor

Changed the Avogadro factor in m52480/eip-812 to a stacked fraction over mol, retaining the single-line calculation and numerical values. Queued for preview refresh.

### 2026-10-16: Fusion energy conversion factors

Stacked complete factors over reaction and MeV in m52480/eip-817 and aligned the two equals signs. Preserved values and two-line layout.

### 2026-10-16: Fusion power unit spacing

Reduced the explicit number-unit gaps in m52480/eip-674 from 0.25em to 0.167em, consistently for J, s, W and MW. Queued for preview refresh.

### 2026-10-16: Fission product mass multiplication

Replaced parentheses around the neutron mass with explicit multiplication in m52479/eip-319. Values and two-line layout preserved. Queued for preview refresh.

### 2026-10-16: Fission math styling and energy layout

Removed five forced italic MathML attributes throughout m52479. Split eip-179 into three aligned lines, with the final 171.2 MeV result on its own line.

### 2026-10-16: Fission percentage spacing

Removed the extra space in 0.72% in m52479. Queued for preview refresh.

### 2026-10-16: Fission energy fence spacing

Set explicit zero spacing on parentheses and the unit slash in m52479/eip-179, retaining thin number-unit spaces and aligned equals signs. Queued for preview refresh.

### 2026-10-16: Fission conservation sum spacing

Normalized numeric tokens and infix operators in both sums in m52479/import-auto-id3081841. Values unchanged. Queued for preview refresh.

### 2026-10-16: Separate breeding half-life annotations

Separated half-lives from reactions in m52479/eip-890 and eip-412, using independent MathML expressions with a visible gap and responsive wrapping. Queued for preview refresh.

### 2026-10-16: Fission atom-count conversion factor

Stacked the complete number and uranium-235 numerator over mol in m52479/eip-689. Values and remaining layout preserved. Queued for preview refresh.

### 2026-10-16: Approved operator audit D1

Corrected specific-heat units and denominator grouping in m67135/eip-333. Two aligned rows, with the approximate 162 °C result on the second; explicit thin spaces before units. D2 remains awaiting review. Queued for preview refresh.

### 2026-10-16: Approved operator audit D2

Cubed the entire length-conversion factor in m52466/eip-317. The resulting 2.2908 × 10^17 kg/m³ agrees with the existing rounded 2.3 × 10^17 kg/m³. Queued for preview refresh.


Operator audit (2026-10-16): maintainer-authorized typography pass repaired 611 expressions in 84 modules, preserving visible content and grouping. Reversal snapshots: proposals/maintainer-corrections/OPERATOR-AUDIT-STRAIGHTFORWARD.json. D3 isotope-placement question remains unchanged pending review; see reports/1.1/operator-audit/remaining-decisions.json.


D3 approved and applied (2026-10-16): carbon-14 emission exercise now shows ²²²Ra → ᴬX + ¹⁴C, retaining the unknown nuclide.


Antineutrino correction (2026-10-16): Eqs. 14.10.4–5 now use electron antineutrinos, with a brief reminder after the pair. Section 14.5 consistently calls the emitted particle an electron antineutrino and explains equal mass/spin, opposite nonzero electric charges, and neutral antiparticles with opposite electron family numbers.


Beta-decay label audit: corrected cobalt-60 introductory word label and Latin v in fusion neutrino notation. Conflicting Section 14.5 conservation exercise left for maintainer judgment. See reports/1.1/beta-decay-audit/README.md.


D4 applied: Section 14.5 exercise fs-id2460264 now consistently uses beta-plus decay, N+1, Z−1, and an electron neutrino. Approved correction to the current exercise only. This decision carries no weight in deciding whether to retain or remove the exercise in a later revision.


Section 14.12: changed the force-table entry to “Gluons (experimentally established)” and removed the obsolete conjecture footnote. No glueball discussion added.


Section 14.12: removed the inherited 1983 discovery footnote from the weak-force carrier entry; retained “(observed)” to match the photon entry.


Section 14.13 particle table: names/categories left aligned, other columns centered; four notes relocated below with numbered references; short values kept together. Screen and portrait Letter/A4 print-width checks pass. Final PDF pagination remains a release check.

Section 14.13: updated direct neutrino mass bounds to <4.5×10⁻⁷, <0.19, and <18.2 MeV/c²; removed leading zeros; added confidence levels, flavor/mass-state distinction, and separate oscillation mass-squared-difference note. All three neutrino lifetime entries now read “No decay observed,” as approved.

Section 14.13: audited all 23 particle mass entries against PDG 2025 and the previously approved KATRIN result; W updated to 80.37×10³ MeV/c², other non-neutrino values retained at existing precision. Added missing overbars to charged Xi and Omega antiparticles; all nine antibaryon labels checked.

Section 14.13: spelled out “zero” in “the total remains zero as it was before decay” to avoid ambiguity with the letter o. Pending next preview refresh.

Section 14.13: standardized particle names to Electron Neutrino, Muon Neutrino, and Tau Neutrino, preserving note 3 markers. Pending next preview refresh.

Section 14.13: grouped the four table notes and oscillation paragraph into a caption-style Table notes block below the table, with smaller sans-serif typography and an accessible table association. Pending preview refresh.

Section 14.13: restored missing space between “muon family number” and its symbol. Pending next preview refresh.

Section 14.14: removed newline-generated space after the opening parenthesis before the weak-force range. Pending next preview refresh.

Chapter 14 glossary: corrected source “1g” to “1 g” with U+00A0 in the curie definition. Pending next preview refresh.

Chapter 14 glossary: standardized electron neutrino and electron antineutrino names and changed the latter definition to “antiparticle of the electron neutrino.” Pending next preview refresh.

Chapter 14: merged gluon glossary entries using identical current definitions in both sources; one combined entry preserves both sets of anchors. Section 14.14 prose remains unchanged pending review. Pending preview refresh.

Section 14.14: applied approved gluon prose; corrected caption to explain two superpositions and explicitly flag misleading White label. Figure replacement design under discussion; image unchanged. Pending preview refresh.

Figure 14.14.2: adopted approved color-state diagram as panel (a); preserved original panel (b) through layout cropping; updated caption and alt text.

Section 14.14: updated Higgs glossary definition to established spin-0 particle associated with the Higgs field, discovered in 2012. Flagged inherited SSC-era prose and conceptual question fs-id1169738209354 for review; those remain unchanged. Pending preview refresh.

Section 14.14: applied approved Higgs prose and conceptual-question revisions. Exercise identity and ordering preserved; no renumbering.

Higgs glossary: changed "spin-0 particle" to "particle with zero spin" for readability. Pending next preview refresh.

Chapter 14 glossary: renamed photomultiplier to photomultiplier tube and clarified faint-light conversion and successive electron multiplication. Existing entry anchors preserved. Pending next preview refresh.

Section 14.14: applied approved Standard Model glossary, explanatory paragraph, and section-summary revisions. Clarified particle content, interactions, and limitations; removed proposed-gluon wording. Existing anchors preserved. Pending next preview refresh.

Section 14.13: clarified strangeness definition, conservation rules and quark interpretation; added qualified Gell-Mann maxim; corrected kaon charge accounting and signed strangeness change. Example identity preserved.

Section 14.13: applied approved antiproton storage explanation (electric and magnetic confinement, density and technical limitations) and matter-antimatter imbalance scope statement. Removed misleading magnetic-field power claim and later-chapter promise. Pending next preview refresh.

Section 14.13: applied approved hadron-lepton distinction, defining composite hadrons and elementary leptons and clarifying that both participate in weak interactions. Existing term anchors preserved. Pending next preview refresh.

Section 14.13: removed redundant zero or from boson integer-spin definition in prose and matching glossary entry; retained spin examples and markup. Pending next preview refresh.

Section 14.13 only: standardized all electron, muon and tau family subscripts on lepton numbers and neutrinos to explicit italic styling. Other sections unchanged. Pending next preview refresh.

Section 14.13: clarified that the name baryon derives from the Greek for heavy. Pending next preview refresh.

Section 14.13: reframed meson/baryon decay patterns as evidence illustrating conservation rather than definitions. Kept quark introduction later and retained baryon-number discussion. Pending next preview refresh.

Section 14.13: moved formal meson and baryon term anchors from initial decay discussion to new definitions after the quark introduction. Early mentions are plain text; glossary entries now define quark content. IDs preserved. Pending next preview refresh.

Textbook glossary: applied approved canonical definitions and introduction points; distinguished lens power, polarized light and electric polarization; replaced duplicate glossary definitions with canonical cross-references while preserving previous anchors.

G04: removed the vector addition glossary entry from Section 9.5. Section 1.3 vector coverage retained; no additional instruction or exercise changes. Pending next preview refresh.

G06: removed redundant thermal agitation glossary and formal-term styling in 11.5; earlier random thermal motion coverage confirmed in energy and heat sections. Ordinary prose and term anchor retained. Pending preview refresh.

G07: removed the double-slit interference glossary entry from Section 12.7. No prose or exercise changes. Pending next preview refresh.

G08: removed decay equation glossary entry and formal-term styling in Section 14.5. Ordinary wording, equations and exercise numbering retained. Pending next preview refresh.

G14/G15: removed eleven equation-label/procedural glossary entries and associated formal-term styling. Equations, explanations, prose anchors and exercise numbering retained. Pending preview refresh.

G19: defined electromagnets with matching glossary in 10.3; defined electromagnetism broadly with matching glossary in 11.2 at Maxwell unification discussion. Existing anchors retained. Pending preview refresh.

Glossary quality batch: applied focused definitions, canonical placements and prose consistency corrections from approved groups. G17 and G33 held for broader prose review. Equations and exercise numbering retained; pending preview refresh.

Approved glossary batch follow-up: synchronized proper-time, curie-history and approximate vacuum-permeability prose; clarified activity versus finite detector counts. Exact proposals for 14 remaining groups plus held G17/G33 are in reports/1.1/glossary-wording-decisions.md.

G20: applied approved qualitative Ampere/Biot-Savart prose and glossary definitions. Maxwell extension links to the section title using module m52443, without a section number. Pending preview refresh. After glossary review, scan hard-coded chapter/section references for renumbering resilience.

G22: applied thermal-equilibrium temperature definition and simple absolute-zero lower-limit wording in Section 8.2 and glossary. Removed all-motion-ceases claim; no quantum caveat added. Pending preview refresh.

G28: applied approved Feynman-diagram and gauge-boson explanations and glossary definitions in 14.12/14.13, retaining gauge field terminology. Anchors preserved; pending preview refresh.

Applied all remaining approved glossary groups (G05, G17, G27, G29, G33, G34, G36, G39, G42, G46, G47, G49, G51), including five G51 removals. G49 experimental milestones unchanged. Preserved IDs and exercise numbering. Pending preview refresh. Next review: hard-coded chapter/section references before renumbering.

Final glossary consistency pass synchronized quantum measurement discussion, entropy summaries/caption and model-dependent unification/proton-decay wording. No updated lifetime limit or fusion experimental milestone added. Next review remains hard-coded chapter/section references before renumbering.

- Scanned all 141 maintained modules for hard-coded chapter/section references. Replaced the garden-hose momentum question’s “Chapter 2” reference with the linked title “Newton’s Third Law of Motion: Symmetry in Forces,” preserving its target and exercise number. Retained three section numbers citing external prescribing documents.

- Chapter 14: applied the approved exercise review (19 keep, 44 revise, 132 remove), plus ten separate fixed MyOpenMath-aligned questions. Final 73 questions follow textbook topic order and, per the maintainer’s subsequent instruction, are renumbered 1–73. Eighteen optional extensions are marked. Body prose unchanged; internal crosswalk and provenance: reports/1.1/chapter14-structure/applied-question-set.json.

- Chapter 14 exercises: standardized spelled-out radiation names to native MathML α, β⁻, β⁺ and γ in 16 questions; numbers, order and remaining wording preserved.

## October 17, 2026 — Appendix A evaluated-data correction

Applied systematic Atomic Masses table corrections from AME2020/NUBASE2020/CIAAW2024: 160 original rows plus one explicitly labeled Rf-261m row. Maintainer approved separate state rows, natural-abundance ranges, and a 0.1% principal-decay-branch threshold. Precision, uncertainties, sources, and uncertain state ordering are explained in table notes. Numerical/source-ID checks and course build passed; desktop/mobile rendered checks passed. Published in preview 147. Full correction log: reports/1.1/atomic-masses-audit/applied-review.md.

- [ ] During appendix/second-pass review, check Appendix B and other repeated isotope data for consistency. Carbon-14 appendix now gives 5700(30) y; Chapter 14 Exercises 31 and 32 now use 5700 y; Section 14.6 body/worked examples remain to be reviewed.

## October 17, 2026 — carbon-14 exercise consistency

Updated Exercises 31 and 32 to use 5700 y. Exercise 32(a) now uses 11,400 y; the three-half-life answers are 17,100 y. Calculations and course build passed. Appendix A corrections and these exercise changes were published together in preview 147. The Section 14.6 body/worked examples and Appendix B retain their earlier values pending their second-pass consistency review.


## October 17, 2026 — Appendix B evaluated-data consistency and emissions audit

Updated 38 isotope half-lives using NUBASE2020, consistent with Appendix A, and audited selected radiation energies/yields against 33 DDEP evaluations, four LNHB Nucléide-Lara entries, and ICRP107 via MIRDspecs for Cs-129. Maintainer approved compact selected emissions, dominant replacements for ambiguous entries, and DDEP branching fractions used consistently with DDEP emissions while retaining NUBASE half-lives. Corrected gamma photon yields, alpha kinetic energies, beta endpoints and branching fractions; clarified selection, daughter delays, and source conventions. All existing IDs preserved. Course build passed (6430 math, issues {}, 2440 adaptations, 8424 search passages); desktop and mobile checks passed. Audit: reports/1.1/appendix-b-consistency/review.html. Published successfully as preview 148 (source c9406503d29056827b129861ed8f997fa9ed0275). Section 14.6 body/worked examples remain pending second-pass consistency review.

## October 17, 2026 — Section 14.6 carbon-14 consistency

Updated all remaining 5730 y references in Section 14.6 to 5700 y, including MathML annotations. Recalculated the simplified Shroud age to 686 y (about AD 1300 remains valid), and living-carbon activity to 7.93 × 10^9 decays/y = 251 Bq = 6.78 nCi per kilogram, or 0.251 decays/s per gram. Preserved the reviewed equation layouts and historical calibrated date range. This completes the previously pending Section 14.6 consistency update. Arithmetic, XML, and full course build checks passed (6430 math expressions; no issues); preview publication pending. Provenance: proposals/maintainer-corrections/C14-SECTION-146-HALFLIFE-5700.json.

## October 17, 2026 — Appendix C and heat convention consistency

Applied approved Appendix C updates: Avogadro constant units, Earth mass/mean radius, common-prefix title, seven SI base units, radian classification, electric potential label, pound-force/knot/torr labels, and rounded versus exact conversions. Adopted the thermochemical calorie (4.184 J exactly) in Appendix C and Heat prose; checked and corrected rounded kcal equivalents in specific-heat and latent-heat tables while retaining SI material properties and their worked calculations. Source IDs and XML/hash checks passed. Full course build: 6425 math, issues {}, 2440 adaptations, 8427 search passages. Browser checks passed for five affected sections at desktop and 430 px mobile widths. Published together with Section 14.6 carbon-14 changes in preview 149, source ae4be96589baa92a6ac2051392fb95c4f1847146. Reports: reports/1.1/appendix-c-consistency/.

## October 17, 2026 — Appendix D notation consistency

Applied the approved definition corrections and 12 missing symbol meanings, removed the orphaned energy-uncertainty entry, and replaced time uncertainty with elapsed time. Updated calorie/Avogadro conventions, relativity/quantum wording, anticolor labels, and context-dependent bar/subscript-zero conventions. Used an overbar on x as a compact example for mobile display. Preserved existing IDs and P/p distinctions. Full course build passed (6435 math, issues {}, 2440 adaptations, 8427 passages); desktop/mobile content checks passed. Published preview 150, source eea1a6abe89e964bda7e62ed9d206ada6603d0d1. Provenance: proposals/maintainer-corrections/APPENDIX-D-NOTATION-CONSISTENCY.json.

## October 17, 2026 — Appendix D symbol alignment

Explicitly centered all symbol cells, fixing inline gamma and other inline entries while preserving left-aligned definitions. Course build passed (6435 math, no issues); desktop/mobile gamma center offset verified as zero, no page overflow. Published preview 151, source 923aebc419be03069502111f7699c7f138648fc8. Provenance: proposals/maintainer-corrections/APPENDIX-D-SYMBOL-ALIGNMENT.json.

Appendix D follow-up: matched L_e, L_mu, and L_tau subscripts to the italic identifiers used in particle-physics prose; labels now read electron/muon/tau family number. Full course build passed. Pending next preview refresh. Provenance: APPENDIX-D-LEPTON-FAMILY-NOTATION.json.

Appendix D: clarified both newton-meter definitions (work/energy equivalent to joule; torque conventionally not called joule), preserving American spelling. XML validation passed. Pending next preview refresh with lepton-family notation updates.

Appendix D: fixed w_R alignment missed by the earlier plain-row matcher; its row has namespace attributes. Verified all 273 body symbol cells explicitly center their contents. Full course build passed. Pending next preview refresh with family-number and newton-meter updates.

Appendix D: tesla entry now explicitly says SI unit of magnetic field strength B. XML validation passed; pending next preview refresh.

## October 17, 2026 — Appendix D unit definitions and pending review edits

Updated 22 unit definitions to identify their measured quantities, including ampere and the work/energy newton-meter entry. Included all pending family-number notation, newton-meter, w_R alignment, and tesla corrections. Full course build passed (6435 math, issues {}, 2440 adaptations, 8427 search passages). Desktop (1100 px) and mobile (430 px) checks passed: no overflow, all symbol cells centered. Published preview 152, source 1c840dec9ce3ac8583651ef2d057bf28b200c75f. Provenance: APPENDIX-D-UNIT-DEFINITIONS.json; screenshots: reports/1.1/appendix-d-consistency/units-1100.png and units-430.png.


## October 17, 2026 — summary/prose consistency

Screened 120 section summaries and corrected mismatches in 20 modules, including the Section 10.8 coil N, permeability approximation and Ampere/Biot-Savart distinction. Full build passed (6431 math; no issues); source IDs preserved and magnetism rendering checked. Pending next requested preview refresh. Details and separate prose-review leads: reports/1.1/summary-consistency/README.md.


## October 17, 2026 — lightning rods and conductor properties

Applied approved paired paragraphs in Section 9.7, preserving the linked pointed-conductor figure. Updated both captions and section summary to distinguish corona discharge from the grounded conducting path used for lightning protection. Preserved image credits, alternative text, objectives and IDs. XML and full course build passed; rendered figure-link target verified. Pending next requested preview refresh with summary consistency changes. The separate source-of-magnetism proposal remains unapplied.


Section 10.3 magnetism follow-up: removed the absolute-current claim box and replaced the second summary bullet with approved current/orbital-motion/spin wording at the end. Surrounding prose and captions retained by maintainer decision. No incoming source references to removed box/paragraph IDs. Pending next requested preview refresh.


Section 11.5: applied the approved blackbody/emissivity paragraph and linked forward reference to Blackbody Radiation (m67250). Full build passed, rendered link verified. Pending preview refresh. Flagged the retained final sentence about 50 percent solar absorption: this refers to the surface, not the entire Earth system; proposed clarification awaits review.


## October 17, 2026 — remaining content flags after summary review

Applied approved Section 11.5 solar-absorption clarification: about half of incoming top-of-atmosphere solar energy is absorbed by the surface. Full course build passed; pending preview refresh.

Three current-source issues confirmed and presented for review (not yet changed):
- m67133/import-auto-id1169738209327: Sun yellowish because red exceeds violet; revise to combined visible sunlight appearing white, with atmospheric scattering affecting observed color. NASA: https://science.gsfc.nasa.gov/attic/eclipse2017.gsfc.nasa.gov/what-color-sun.html
- m67807/import-auto-id694489: principal quantum number described as non-negative; must be positive (1, 2, 3, ...), matching earlier prose and summary.
- m52420/import-auto-id1166991830052: tokamak particles said to follow circles and never cross field lines/escape; distinguish gyration and motion along field lines, and acknowledge drift/losses and additional confinement fields. ITER: https://www.iter.org/node/20687/searching-perfect-shape

These are current content flags, not a certification that the full book has no other errors. Historical unresolved notes elsewhere must be read with their later dispositions. Lightning-rod and magnetism-summary review leads are now resolved by approved changes; retain surrounding magnetism prose per maintainer choice.


Bohr principal quantum number: corrected non-negative to positive in m67807/import-auto-id694489, matching n = 1, 2, 3, ... elsewhere. XML valid; pending preview refresh. Solar-color and magnetic-confinement paragraphs remain under wording review.


## October 17, 2026 — approved solar color and magnetic confinement revisions

Applied both approved paragraphs in m67133 and m52420; provenance: proposals/maintainer-corrections/SOLAR-COLOR-AND-MAGNETIC-CONFINEMENT.json. The preceding positive-integer correction for Bohr n is also included. Full course build passed: 6431 math, issues {}, 2440 adaptations, 8425 search passages. All changes since preview 152 remain queued for the next requested preview refresh.

Historical flag reconciliation: Priority 2 numerical/dose work was applied under P2-01-05-coordinated and P2-06; the negative-base momentum exercise ID no longer exists in the revised Chapter 13 set; the four borderline equation-numbering decisions were resolved in the October 8 exercise-review log. One genuine outstanding numerical flag remains: m42546/eip-95 still substitutes 9.00 × 10^-31 kg for electron mass, while its displayed result 4.02 × 10^-14 J agrees with 9.11 × 10^-31 kg. Reported to maintainer for correction; unchanged in this turn. This reconciliation is not a new comprehensive numerical audit.


## October 17, 2026 — final known content-review correction

Corrected m42546/eip-95 electron-mass substitution from 9.00 to 9.11 × 10^-31 kg, as approved. The existing result 4.02 × 10^-14 J remains correct. Provenance: RELATIVISTIC-EXAMPLE-ELECTRON-MASS.json. Closed stale summary-consistency prose-review leads with their subsequent approved dispositions. No known unresolved content-review decisions remain from the tracked review; this status does not replace the maintainer second-pass review or assert an exhaustive new audit. Preview refresh and release preparation remain separate tasks; public preview remains 152.

### 2026-10-17 — Version 1.1 preface

Added the author-provided About Version 1.1 at the top of Preface, linked the five referenced sections, and renamed the existing heading Original “About This Book”. Existing content otherwise preserved. Minor grammar/typo corrections outside the Pangram sentence only; that sentence is retained as requested. Full course build passed (6431 math expressions, no issues); generated heading order, Pangram wording, and section links checked. Public preview remains unchanged. Proposal: `VERSION-1-1-PREFACE`.

### 2026-10-17 — Preview 153 published

Published the new preface and all pending corrections since preview 152. Source commit: c80fbcee1f3f1857d373b4b23d6b7f708e54f54e; deployment: appgdep_6ad37717dc0c8191b3de3c3d0dcd3f01 (succeeded). Local generated preface checks passed; direct live HTTP verification returned 403. Preface browser opening queued. Packaging used Git Bash outside sandbox with TAR_OPTIONS=--force-local for Windows drive paths.


### 2026-10-17 — Section 4.3 objectives

Applied the approved calculation-objective clarification and combined the first two objectives into one. CNXML parses; changes confined to the objective list. Provenance: OBJECTIVES-4-3-IMPULSE. Other learning-objective proposals remain under review. Pending preview refresh.


### 2026-10-17 — Section 7.5 objectives

Removed the third objective (calculate density given pressure and altitude), as approved. First two objectives retained. CNXML parses; pending preview refresh. Provenance: OBJECTIVES-7-5-REMOVE-DENSITY.


### 2026-10-17 — Section 8.11 objectives

Applied the proposed heat-engine efficiency calculation objective and the maintainer’s exact conceptual objective about why an ideal Carnot engine cannot achieve 100% efficiency. First objective retained. CNXML parses; pending preview refresh. Provenance: OBJECTIVES-8-11-CARNOT.


### 2026-10-17 — Section 8.13 objectives

Applied the reviewed entropy objectives with the approved shorter calculation wording. CNXML parses; only objective list changed. Pending preview refresh. Provenance: OBJECTIVES-8-13-ENTROPY.


### 2026-10-17 — Section 10.5 objectives

Applied the approved right-hand-rule objective revision; retained the original calculation objective as requested. CNXML parses; only second objective changed. Pending preview refresh. Provenance: OBJECTIVES-10-5-RIGHT-HAND-RULE.


### 2026-10-17 — Section 10.10 objectives

Retained the original Faraday’s law calculation objective verbatim and expanded the Lenz’s law objective into the two approved direction and energy-conservation objectives. CNXML parses; only the Lenz objective changed. Pending preview refresh. Provenance: OBJECTIVES-10-10-LENZ.


### 2026-10-17 — Section 13.4 objectives

Applied the approved third objective: Explain why length contraction is ordinarily unnoticeable in everyday life. Other objectives retained. CNXML parses; pending preview refresh. Provenance: OBJECTIVES-13-4-LENGTH-CONTRACTION.


### 2026-10-17 — Section 8.14 objectives

Applied the reviewed statistical-entropy objectives with the approved shortened final wording. CNXML parses; only objective list changed. Pending preview refresh. Provenance: OBJECTIVES-8-14-STATISTICAL-ENTROPY.


### 2026-10-17 — Section 11.7 objectives

Added the approved shortened refraction objective; existing index-of-refraction calculation objective retained. CNXML parses; pending preview refresh. Provenance: OBJECTIVES-11-7-REFRACTION.


### 2026-10-17 — Section 12.5 objectives

Retained the original first objective verbatim and applied the proposed second and third objectives. CNXML parses; pending preview refresh. Provenance: OBJECTIVES-12-5-UNCERTAINTY.


### 2026-10-17 — Section 13.3 objectives

Applied the maintainer-provided four objectives in order: simultaneity, space-time diagrams, time dilation/gamma, twin paradox. Verified this matches subsection order. Gamma retains MathML. CNXML parses; pending preview refresh. Provenance: OBJECTIVES-13-3-SIMULTANEITY-TIME.


### 2026-10-17 — Section 14.13 objectives

Applied general quark-structure wording and particle-table conservation objective. Omitted proposed strangeness/neutrino-oscillation objective per maintainer decision. First two objectives and section prose retained. CNXML parses; pending preview refresh. Provenance: OBJECTIVES-14-13-PARTICLES.


### 2026-10-17 — Remaining learning-objective proposals approved

Applied all 24 remaining section proposals, including the three emphasis choices, under the maintainer’s approval of all other revisions. All 36 reviewed sections are now resolved, preserving individual decisions recorded during review. Source objective lists matched their reviewed baselines and XML parses. Provenance: OBJECTIVES-REMAINING-APPROVED. Build verification and preview refresh pending.

Validation completed: all 36 final source objective lists match approved wording. Full course build passed: 6431 math expressions, no issues, 2440 adaptations, 8431 search passages. Public preview refresh remains pending.


### 2026-10-17 — Preview 154 published

Published the rounded white-IP favicon in CoA blue (#00539F) and all 36 sections’ approved learning-objective revisions. Both numbering builds passed (6431 math; no issues); all 174 packaged HTML pages passed favicon-reference and internal-link checks. The legacy full validator found a stale local review-items link to a removed exercise; that historical report is excluded from deployment. Source commit aaac458b8e200f7c5ff68d429353ed9b346c4893; saved version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_5bfe3782a4a48191ba0fd3b604bf9641; deployment appgdep_6ad38ac26a3c8191ba11e95b2458242a succeeded. Maintainer second-pass review and final PDF/release preparation remain.


### 2026-10-17 — Unit conversion spacing and cancellation

Corrected m67032/eip-442 number–unit spacing and consolidated 0.080 into one numeric token. Preserved the two unit-cancellation enclosures and added a currentColor CSS stroke fallback for native MathML rendering. Local browser check confirms visible cancellation; course build passed (6431 math, no issues). Public preview remains 154; pending refresh. Record: UNIT-CONVERSION-CANCELLATION.


### 2026-10-17 — Preview 155 published

Published the unit-conversion spacing and visible cancellation fix (m67032/eip-442). Both numbering builds passed with 6431 math expressions and no issues. Packaged equation and CSS checked; local browser rendering verified in the preceding turn. Commit 6160c65ab473af4d89a0ae628f619be5b62fcf9e; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_c3bd59ce54048191adc3bf8b5602bc15; deployment appgdep_6ad38dfaa16081919d2f71524fe25a01 succeeded. Preview opened at the corrected equation for maintainer review.


### 2026-10-17 — Motion graph figure sizing

Figure 1.4.4 (m71407/import-auto-id1810795): screen-only CSS sets width 300px and removes the inherited 380px height cap, which squeezed this 575x1335 image to about 164px wide. Existing responsive max-width remains; print sizing unchanged. Course build passed; generated target and rule verified. Pending preview refresh.


### 2026-10-17 — Preview 156 published

Published Figure 1.4.4 screen-sizing fix (300px wide; height cap removed; responsive width and print sizing retained). Both numbering builds passed with 6431 math expressions and no issues. Commit 5d8fe81c44559b34513c63a28e36d3277a73c504; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_057b9ab121a081918c7f02cadb760e09; deployment appgdep_6ad3978f249081919b4a74c78ac0f1fa succeeded. Opened preview at the figure for maintainer review.


### 2026-10-17 — Displacement result sign spacing

Removed explicit extra space before +2.00 km in m67033/import-auto-id2400875 and marked result signs as prefix operators with zero internal spacing in that equation and part (b), import-auto-id2589758. Values and other equation content preserved. XML parses; pending preview refresh. Record: DISPLACEMENT-RESULT-SIGN-SPACING.


### 2026-10-17 — Acceleration conversion multiline layout

Placed the final numerical result on a second, equals-aligned row in m67033/import-auto-id2596926. Mathematical tokens and values preserved; XML parses. Pending preview refresh. Record: ACCELERATION-CONVERSION-MULTILINE.


### 2026-10-17 — Train motion graph sizing

Removed the screen height cap for m67033/import-auto-id2596939 (Figure_02_03_04.jpg), using its source width of 350px. Responsive max-width and print sizing retained. Pending preview refresh.


### 2026-10-17 — Positive acceleration result layout

Moved +0.556 m/s squared to a second equals-aligned row in m67033/import-auto-id2581171, removed the explicit extra space before the positive sign, and applied prefix sign spacing. Mathematical tokens preserved; XML parses. Pending preview refresh. Record: POSITIVE-ACCELERATION-CONVERSION-MULTILINE.


### 2026-10-17 — Average velocity equation qualifier

Moved (constant a) outside the main MathML expression in m67034/import-auto-id2086556, matching prose qualifiers elsewhere; a remains inline math. Formula and equation ID preserved. XML parses; pending preview refresh. Record: AVERAGE-VELOCITY-CONSTANT-QUALIFIER.


### 2026-10-17 — Simplified motion notation row spacing

Added explicit 0.5em row spacing and equalrows to the three-line table m67034/import-auto-id2563693. Existing CSS fallback applies 0.5em top padding to subsequent rows for native MathML engines. Expressions, alignment, and brace preserved. Pending preview refresh. Record: SIMPLIFIED-MOTION-NOTATION-ROW-SPACING.


### 2026-10-17 — Final position result multiline layout

Moved = 480 m to a separate equals-aligned row in m67034/import-auto-id2300752. Mathematical tokens preserved; XML parses. Pending preview refresh. Record: FINAL-POSITION-RESULT-MULTILINE.


### 2026-10-17 — Final velocity constant-acceleration qualifiers

Separated (constant a) from the main MathML in m67034/import-auto-id1962571 and import-auto-id2168495 (Equation 1.6.3). Formula subtrees and IDs retained; a remains inline math. XML parses; pending preview refresh. Record: FINAL-VELOCITY-CONSTANT-QUALIFIERS.


### 2026-10-17 — Airplane final velocity three-line calculation

Split m67034/import-auto-id2177855 into three equals-aligned rows: formula, numerical substitution, and final result 10.0 m/s. Mathematical tokens preserved; XML parses. Pending preview refresh. Record: AIRPLANE-FINAL-VELOCITY-THREE-LINES.


### 2026-10-17 — Final position constant-acceleration qualifier

Separated (constant a) from the main MathML in m67034/import-auto-id1807031 (Equation 1.6.4). Formula and ID retained; a remains inline math. XML parses; pending preview refresh. Record: FINAL-POSITION-CONSTANT-QUALIFIER.


### 2026-10-17 — Motion equations list punctuation

Capitalized five sentence-length bullets and added missing periods to six explanatory bullets and the summary sentence ending in the notation table. Calculation fragments and the colon-introduced equation reference list retained. XML parses; pending preview refresh. Record: MOTION-EQUATIONS-LIST-PUNCTUATION.


### 2026-10-17 — Velocity squared constant-acceleration qualifier

Separated (constant a) from the main MathML in m67034/import-auto-id1659227 (Equation 1.6.5). Formula and ID retained; a remains inline math. XML parses; pending preview refresh. Record: VELOCITY-SQUARED-CONSTANT-QUALIFIER.


### 2026-10-17 — Preview 157 published

Published all pending second-pass fixes in m67033 and m67034: sign spacing, multiline calculations, train graph screen sizing, three-row notation spacing, separate constant-acceleration qualifiers, and list capitalization/punctuation. Course and CNX builds passed (6436 math expressions, no issues); packaged target anchors and CSS checked. Commit fcd513a18ed658dd4e218a4c798d11f2a7708900; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_9325e3fa7aa08191add9fbc0cd53d73b; deployment appgdep_6ad39d98cefc8191ae296514eb492e8c succeeded.


### 2026-10-17 — Falling-object position calculation layout

Changed m/s and m/s squared to stacked unit fractions and moved = 8.10 m to a separate equals-aligned row in m68876/import-auto-id2302522. Numeric and unit tokens preserved; XML parses. Pending preview refresh. Record: FALLING-POSITION-STACKED-UNITS-MULTILINE.


### 2026-10-17 — Falling-object velocity three-line calculation

Split m68876/import-auto-id1688803 into three equals-aligned rows: formula, substitution, and final result 3.20 m/s. Mathematical tokens preserved; XML parses. Pending preview refresh. Record: FALLING-VELOCITY-THREE-LINES.


### 2026-10-17 — Preview 158 published

Published falling-object position stacked-unit fractions and separate final result, plus the three-line velocity calculation. Course and CNX builds passed (6436 math expressions, no issues). Commit 1242d20a36d9601bb918ec3c0eec9303c01bdb3b; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_476628ea0eec8191aa030cad5517045c; deployment appgdep_6ad39f64aa808191935abdc75064bc53 succeeded. Equation widths await maintainer browser review.


### 2026-10-17 — Projectile vertical acceleration sign spacing

Marked both minus signs in the vertical acceleration expression in m67038/import-auto-id1696126 as prefix operators with zero internal spacing. Mathematical content and number-unit spacing preserved. XML parses; pending preview refresh. Record: PROJECTILE-VERTICAL-ACCELERATION-SIGNS.


### 2026-10-17 — Summary motion notation row spacing

Applied the same rowspacing=0.5em and equalrows=true settings as the section-body equation to m67034/import-auto-id2168257 in the chapter summary. Expressions, brace, and punctuation preserved. XML parses; pending preview refresh. Record: SUMMARY-MOTION-NOTATION-ROW-SPACING.


### 2026-10-17 — Bacteria speed parenthetical

Separated the two equivalent speed quantities in m52314/import-auto-id2173366 into independent math expressions, with parentheses in prose. Values and wording preserved. XML parses; pending preview refresh. Record: BACTERIA-SPEED-PARENTHETICAL.


### 2026-10-17 — System 1 acceleration single-line calculation

Combined m68330/eip-id1741589 into one equality chain, removing the repeated a and intervening comma. Fractions, values, units, and equation ID preserved. XML parses; pending preview refresh. Record: SYSTEM-ONE-ACCELERATION-SINGLE-LINE.


### 2026-10-17 — Preview 159 published

Published projectile acceleration sign spacing, chapter-summary notation row spacing, separated bacteria-speed parenthetical, and single-line System 1 acceleration calculation. Course and CNX builds passed (6437 math expressions, no issues); all four target anchors verified in packaged HTML. Commit cf8a3715560fa6b0011f6ea16d6b615dd36d29db; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_dfebdebf4ef4819183acbc091b5b9c1d; deployment appgdep_6ad3a209d81c81918d3d6001f51a5b29 succeeded.


### 2026-10-17 — Elevator example vector notation

Replaced bold-plus-arrow vector notation with bold symbols in m68329/fs-id1165038187326, including caption, prose, and vector equation. The scale reading F_p is now scalar where explicitly defined as a magnitude. Descriptive subscripts remain upright and normal weight. Flattened JPEG retained; arrow-label retouching deferred. XML parses; pending preview refresh. Record: ELEVATOR-EXAMPLE-VECTOR-NOTATION.


### 2026-10-17 — Elevator net force equality chain

Replaced nested Content MathML equalities in m68329/fs-id1165037151851 with the direct presentation chain F_net = F_s - w = ma, removing renderer-generated parentheses. Scalar notation, upright descriptive subscripts, and source ID retained. XML parses; pending preview refresh. Record: ELEVATOR-NET-FORCE-EQUALITY-CHAIN.


### 2026-10-17 — Elevator weight prose spacing

Changed the concluding comparison to "his weight of 735 N (165 lb)", using nonbreaking number-unit spaces in both quantities. XML parses; pending preview refresh. Record: ELEVATOR-WEIGHT-NUMBER-UNIT-SPACES.


### 2026-10-17 — Elevator figure vector labels

Added image-tool-edited PNG with small vector-notation arrows removed. Visually checked force-arrow directions, broken arrows, labels and diagram structure. Original JPEG retained. Source references the new PNG. Supersedes earlier artwork deferral. Pending preview refresh. Record: ELEVATOR-FIGURE-BOLD-VECTORS.


### 2026-10-17 — Preview 160 published

Published elevator example vector-notation corrections, edited figure, simplified force equality, and weight prose with nonbreaking spaces. Both builds passed (6437 math expressions, no issues). Commit acb82bc50a29ebc7c1313a76b428295a1b11de17; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_3fc82ddc819c8191aa24eae5697f19e3; deployment appgdep_6ad3a47c547c81918b649b64508928cc succeeded.


### 2026-10-17 — Hooke law figure height cap

Figure 2.7.3 (m67044/import-auto-id2404473), source image 875 by 945, has an intended width of 375px. The 380px screen height cap reduced it to about 352px wide. Added a screen-only scoped override for width 375px and no height cap; responsive max-width and print styling retained. Pending preview refresh.


### 2026-10-17 — Gravitational force three-line calculation

Split m71410/eip-625 into three equals-aligned rows: formula, substitution, and final result 20.0 N. Mathematical tokens and displaystyle preserved; XML parses. Pending preview refresh. Record: GRAVITATIONAL-FORCE-THREE-LINES.


### 2026-10-17 — Preview 161 published

Published Hooke law figure screen height-cap correction and three-line gravitational-force calculation. Both builds passed (6437 math expressions, no issues). Commit 42c4e6a28991eec09b91786fc59fbb1833785d87; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_e2f6df7c02f88191aa174b48a38d345b; deployment appgdep_6ad3a63de5c48191bea6824b76d9938d succeeded.


### 2026-10-17 — Gravitational force unit spaces and inline formula

Replaced four empty operators before units with explicit thin spaces and added a thin space before the compound unit of G in m71410/eip-625. First row now uses GmM/r squared with a solidus instead of a stacked fraction. Three-row layout and numerical values retained. XML parses; pending preview refresh. Record: GRAVITATIONAL-FORCE-THIN-SPACES.


### 2026-10-17 — Centripetal force figure height cap

Figure 2.10.1 (m67036/import-auto-id1581195) is 554 by 941 pixels; the global 380px height cap limits screen width to about 224px. Added a screen-only width of 350px with no height cap. Responsive max-width and print styling retained. Pending preview refresh.


### 2026-10-17 — Negative work parentheses

Removed parentheses from the first inline quantity in m67539/eip-663, now -470 J with prefix minus spacing and a thin number-unit space. The subsequent total-work expression is unchanged. XML parses; pending preview refresh. Record: NEGATIVE-WORK-PARENTHESES.


### 2026-10-17 — Numbered compact work-energy theorem

Promoted the bare block MathML in m71411/import-auto-id2069888 to a standalone numbered equation, work-energy-theorem-compact, with standard display margins. Split surrounding prose into paragraphs and retained the original paragraph ID. Removed the stray comma after "as" and placed punctuation after the display. XML parses; pending preview refresh. Record: WORK-ENERGY-COMPACT-NUMBERED-EQUATION.


### 2026-10-17 — Preview 162 published

Published gravitational formula thin spaces and solidus, centripetal figure sizing, negative-work parentheses removal, and numbered compact work-energy theorem with display spacing. Both builds passed (6437 math expressions, no issues). Commit b1273eeb207141f0b12db26c3bbb0509ef0f0d69; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_72546525c6b881918563081052b0d133; deployment appgdep_6ad3a8ad1fe081918f98877066c38f5a succeeded.


### 2026-10-17 — Work-energy display punctuation

Removed redundant MathML display=block from work-energy-theorem-compact so the equation wrapper controls the display layout and the external comma stays beside the formula. Numbering and display margins retained. Pending preview refresh. Record: WORK-ENERGY-DISPLAY-PUNCTUATION.


### 2026-10-17 — Potential energy change two-line expression

Split m71414/eip-306 before = mg(h_f - h_i), keeping that expression and = mg Delta h together on the second equals-aligned row. Mathematical tokens and source ID preserved. XML parses; pending preview refresh. Record: POTENTIAL-ENERGY-CHANGE-TWO-LINES.


### 2026-10-17 — Knee force three-line calculation

Split m71414/eip-118 into three equals-aligned rows: formula, substitution, and final result 3.53 times 10^5 N. Mathematical tokens preserved; XML parses. Pending preview refresh. Record: KNEE-FORCE-THREE-LINES.


### 2026-10-17 — Final fall speed result line

Moved = 19.8 m/s to its own equals-aligned row in m71414/eip-230. Square roots, mathematical tokens, and ID preserved. XML parses; pending preview refresh. Record: FALL-FINAL-SPEED-TWO-LINES.


### 2026-10-17 — Preview 163 published

Published compact work-energy theorem comma fix and gravitational potential-energy layouts: eip-306 two rows, eip-118 three rows, and eip-230 separate final result. Both numbering builds passed (6437 math expressions, no issues). Commit 9059b30ae70b5313002d1e18708e707c2bbf9504; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_9bcddc9b9ac48191989e9886f1b9b8a7; deployment appgdep_6ad3aa2521208191878140fccf8419c1 succeeded.


### 2026-10-17 — Potential energy caption parentheses

Moved parentheses around Delta PE_g into caption prose in m71414/import-auto-id1556510. Quantity and remaining caption preserved. XML parses; pending preview refresh. Record: POTENTIAL-ENERGY-CAPTION-PARENTHESES.


### 2026-10-17 — Roller coaster speed stacked units

Changed the two unit ratios on the first row of m71414/eip-388 to stacked fractions. The second-row result and all numerical values remain unchanged. XML parses; pending preview refresh. Record: ROLLER-COASTER-SPEED-STACKED-UNITS.


### 2026-10-17 — Potential energy abbreviation parentheses

Moved parentheses around PE into prose in m67037/import-auto-id1532141. Abbreviation and surrounding wording preserved. XML parses; pending preview refresh. Record: CONSERVATIVE-FORCES-PE-PARENTHESES.


### 2026-10-17 — Mechanical energy grouping spacing

Kept the grouping parentheses around KE + PE in m67037/eip-784 and set their inner and outer MathML operator spacing to zero. Removed redundant imported wrappers; normal spacing around the plus sign is preserved. XML parses; pending preview refresh. Record: MECHANICAL-ENERGY-GROUPING-SPACING.


### 2026-10-17 — Power unit equivalence parentheses

Moved the parentheses and sentence period around 1 W = 1 J/s into prose in m71415/import-auto-id2265352. Unit equivalence and existing thin spaces preserved. XML parses; pending preview refresh. Record: POWER-UNIT-EQUIVALENCE-PARENTHESES.


### 2026-10-17 — Power calculation stacked units

Changed m/s and m/s squared on the first row of m71415/fs-id1008855 to stacked fractions. Values, remaining rows, and thin spaces preserved. XML parses; pending preview refresh. Record: POWER-CALCULATION-STACKED-UNITS.


### 2026-10-17 — Monthly power cost on two lines

Moved the final monthly cost in m71415/eip-110 onto a second equals-aligned row. Mathematical tokens and values preserved. XML parses; pending preview refresh. Record: POWER-COST-TWO-LINES.


### 2026-10-17 — Summary work-energy numbered display

Promoted the work-energy theorem in m71411/fs-id2019226 to a display equation, aliasing its number to the original fs-id2771768 and adding a source cross-reference. Formula preserved. Pending preview refresh. Record: SUMMARY-WORK-ENERGY-NUMBERED-DISPLAY.


### 2026-10-17 — Summary potential energy parentheses

Moved the parentheses around PE into prose in the second item of m67037/fs-id1337667. Remaining text and gravitational potential-energy expression preserved. XML parses; pending preview refresh. Record: SUMMARY-POTENTIAL-ENERGY-PARENTHESES.


### 2026-10-17 — Mechanical energy definition

Corrected m67037 summary definition: mechanical energy is the sum of kinetic and potential energy, without a conservative-force condition. The section body and glossary already state the definition correctly; no prose correction needed there. Pending preview refresh. Record: MECHANICAL-ENERGY-DEFINITION-SUMMARY.


### 2026-10-17 — Hooke law summary spacing

Reduced vertical margins around m67045/import-auto-id3385046 to 0.4em and removed the following paragraph top margin. Scoped to this equation; content and number unchanged. Pending preview refresh. Record: HOOKE-SUMMARY-EQUATION-SPACING.

### 2026-10-17 — Preview 164 published

Published all pending parentheses, unit-fraction, calculation layout, work-energy summary numbering/link, mechanical-energy definition, and Hooke summary spacing corrections. Both profiles passed (6437 math expressions, no issues). Commit 75c20c3f48bab256c300b0ad0bdbb40acbfdc94a; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_8aeab18393348191ac20bcbfa4258bec; deployment appgdep_6ad3add9f4c8819189c15f1fbd809323 succeeded. Reloaded the existing work-and-energy review tab; live DOM confirms corrected mechanical-energy definition and 7.2px Hooke equation margins.


### 2026-10-17 — Summary work equation reference

Wrapped summary W = Fd in a numbered display, reusing the original fs-id1536731 label and adding a cross-reference to it. Formula preserved. Pending preview refresh. Record: SUMMARY-WORK-NUMBERED-DISPLAY.


### 2026-10-17 — Momentum force equality chain

Flattened the nested equality in m71582/eip-844 into one three-term equality, removing renderer-added parentheses. Vectors, fractions, and values preserved. XML parses; pending preview refresh. Record: MOMENTUM-FORCE-EQUALITY-CHAIN.


### 2026-10-17 — Elastic collision equation conditions

Separated the F_net = 0 conditions from the main math in m67042/eip-545 and eip-485, with prose parentheses and punctuation. Removed imported spacer runs. Formulas and labels preserved. XML parses; pending preview refresh. Record: ELASTIC-COLLISION-CONDITIONS.


### 2026-10-17 — Elastic collision energy description

Moved the two-object elastic-collision description from Equation 4.5.3 into the following sentence (import-auto-id1704032), preserving the formula. Record: ELASTIC-COLLISION-ENERGY-DESCRIPTION.

### 2026-10-17 — Preview 165 published

Published summary W = Fd numbering and original-equation link, momentum equality parentheses removal, separated elastic-collision conditions, and kinetic-energy equation description moved into prose. Both profiles passed (6439 math expressions, no issues). Commit 9bc86cfc273863f91dceeec6be18695913e13773; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_ff2595bf46888191b921528228786cca; deployment appgdep_6ad3afb160308191ba5cead9deaf5492 succeeded. Reloaded existing elastic-collisions tab and verified the new description in live page text.


### 2026-10-17 — Elastic collision second velocity layout

Split m67042/eip-560 before the numerical substitution into two equals-aligned rows. Formula, values, and separate final-result equation preserved. XML parses; pending preview refresh. Record: ELASTIC-COLLISION-SECOND-VELOCITY-TWO-LINES.


### 2026-10-17 — Elastic collision condition spacing

Added a prose em space before the parenthetical condition in m67042/eip-545 and eip-485, visually separating each condition from the main equation. Math and numbering unchanged. XML parses; pending preview refresh. Record: ELASTIC-COLLISION-CONDITION-SPACING.


### 2026-10-17 — Inelastic collision velocity layout

Moved the final result in m67043/eip-777 to a second equals-aligned row. Mathematical tokens and values preserved. XML parses; pending preview refresh. Record: INELASTIC-COLLISION-VELOCITY-TWO-LINES.


### 2026-10-17 — Inelastic collision energy layout

Reformatted m67043/eip-440 into three equals-aligned rows: formula, numerical substitution, and final result. Mathematical tokens and values preserved. XML parses; pending preview refresh. Record: INELASTIC-COLLISION-ENERGY-THREE-LINES.


### 2026-10-17 — Cart velocity substitution fraction

Combined the second-row terms in m67043/eip-999 over their common 0.50 kg denominator, and stacked all three m/s unit ratios in the numerator. Symbolic row and final result preserved. XML parses; pending preview refresh. Record: INELASTIC-CART-VELOCITY-COMBINED-FRACTION.


### 2026-10-17 — Initial collision energy stacked units

Changed both m/s unit ratios in the second row of m67043/eip-530 to stacked fractions. Values, symbolic row, and result preserved. XML parses; pending preview refresh. Record: INELASTIC-INITIAL-ENERGY-STACKED-UNITS.


### 2026-10-17 — Final collision energy stacked units

Changed both m/s unit ratios in the second row of m67043/eip-626 to stacked fractions. Values, symbolic row, and result preserved. XML parses; pending preview refresh. Record: INELASTIC-FINAL-ENERGY-STACKED-UNITS.

### 2026-10-17 — Preview 166 published

Published all pending elastic and inelastic collision equation layouts: eip-560 two rows, condition em-space separation, eip-777 two rows, eip-440 three rows, eip-999 common denominator and stacked units, eip-530 and eip-626 stacked units. Both profiles passed (6439 math expressions, no issues). Commit eda344fa3f38ca0631701dee66ce971c73729809; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_e9c88bd5690481918e50f07cb1ff8a1f; deployment appgdep_6ad3b2bc1fdc81919fc65b18f24f82c0 succeeded. Reloaded current inelastic-collisions tab and verified updated second-row fractions in eip-626.


### 2026-10-17 — Hertz definition anchor location

Removed the duplicate hertz definition after the questions in m71584 and moved canonical-hertz to the existing explanation in import-auto-id2402363. Existing wording and glossary definition preserved; anchor remains unique. Pending preview refresh. Record: HERTZ-DEFINITION-ANCHOR-LOCATION.


### 2026-10-17 — SHM time argument spacing

Replaced the eight imported fenced time arguments in m71585/eip-1 with the compact presentation markup used in the following paragraph. Function names sin and cos remain upright; prose and mathematical meaning preserved. XML parses; pending preview refresh. Record: SHM-TIME-ARGUMENT-SPACING.


### 2026-10-17 — Redundant resonate pointer

Removed the trailing definition-pointer sentence in m71586 and relocated its two legacy anchors to the existing sentence defining resonate. Definition and primary resonance anchor preserved. Pending preview refresh. Record: RESONATE-REDUNDANT-DEFINITION-LINK.


### 2026-10-17 — Introduction definition reminders

Removed the standalone quantum mechanics and relativity reminders from m52310, preserving inline links and relocating legacy anchors alongside them. Record: INTRO-REDUNDANT-DEFINITION-REMINDERS.

### 2026-10-17 — Preview 167 published

Published hertz duplicate removal and anchor relocation, SHM time-argument spacing, redundant resonate pointer removal, and introduction quantum mechanics/relativity reminder removal. Inline links and legacy anchors preserved. Both profiles passed (6439 math expressions, no issues). Commit ea9706142d5f64295270c4e5ea426c2f633a72f4; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_e27fca9d1d748191a5be4985c3280f67; deployment appgdep_6ad3b518cfc4819184e746e8ef336aa8 succeeded. Reloaded introduction tab and verified no standalone definition reminders remain.


### 2026-10-17 — Wavelength adjacent definition link

Removed the redundant wavelength link to the immediately preceding definition in m71587/import-auto-id1375143. Word, legacy ID, and canonical definition anchor preserved. Pending preview refresh. Record: WAVELENGTH-ADJACENT-DEFINITION-LINK.


### 2026-10-17 — Term-link direction cleanup

Removed 26 inline same-page/backward term links and 22 standalone definition reminders. Preserved legacy anchors and three forward cross-page term links. Equation, figure, exercise, and section references unchanged. Pending preview refresh. Record: TERM-LINK-DIRECTION-CLEANUP; audit: reports/1.1/term-link-direction-cleanup.md.


### 2026-10-17 — Standing-wave figure widths

Matched fundamental and overtone panels to available figure width on screen, preserving aspect ratios. Record: STANDING-WAVE-FIGURE-WIDTHS.

### 2026-10-17 — Preview 168 published

Published standing-wave figure width matching, adjacent wavelength unlinking, and term-link direction cleanup (26 inline links and 22 reminders). Both profiles passed: 6439 math expressions, no issues. Commit 942ed079bf2ecd7ca4af397ea0c528a1ba776a41; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_08b2d0559450819195746e6dfc2a3348; deployment appgdep_6ad3b8b6b2e4819186b36b0514717e30 succeeded. Reloaded standing-waves browser tab; both figures measure 504.8px wide at the current viewport.


### 2026-10-17 — SHM summary time-argument spacing

Matched sin(t) and cos(t) in m71585/import-auto-id1860331 to the compact presentation markup already used in the main prose. Pending preview refresh. Record: SHM-SUMMARY-TIME-ARGUMENT-SPACING.


### 2026-10-17 — Angular-velocity chained equalities

Flattened nested equalities in m71592/eip-121 and eip-582 to remove unnecessary parentheses. Equation IDs, values, and numbering preserved. Pending preview refresh. Record: ANGULAR-VELOCITY-CHAINED-EQUALITIES.


### 2026-10-17 — Short angular-acceleration calculation

Joined m71592/eip-272 into one line, preserving both fractions, values, and punctuation. Pending preview refresh. Record: ANGULAR-ACCELERATION-SHORT-CALCULATION-ONE-LINE.


### 2026-10-17 — Angular-acceleration result in two lines

Combined symbolic and numerical substitution rows in m71592/eip-899; final result remains on its own aligned row. Pending preview refresh. Record: ANGULAR-ACCELERATION-RESULT-TWO-LINES.


### 2026-10-17 — Stopping-time calculation on one line

Joined m71592/eip-455 into one line. Fraction, signs, units, result, and punctuation preserved; math token sequence checked. Pending preview refresh. Record: ANGULAR-STOPPING-TIME-ONE-LINE.


### 2026-10-17 — Tangential-acceleration calculation in two lines

Combined first two rows of m71592/eip-20; final result retains its own aligned row. Math token sequence preserved. Pending preview refresh. Record: TANGENTIAL-ACCELERATION-TWO-LINES.


### 2026-10-17 — Motorcycle angular-acceleration calculation in two lines

Combined first two rows of m71592/eip-155; final result retains its own aligned row. Math token sequence preserved. Pending preview refresh. Record: MOTORCYCLE-ANGULAR-ACCELERATION-TWO-LINES.

### 2026-10-17 — Preview 169 published

Published SHM summary time-argument spacing and all pending angular-acceleration equation layouts (eip-121, eip-582, eip-272, eip-899, eip-455, eip-20, eip-155). Both profiles passed: 6439 math expressions, no issues. Commit 16f570db66e4240118630a4230e5a3d32d91008c; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_369c759878e481918085bdc420b957ea; deployment appgdep_6ad3bb09191081918a1364b70b882c6f succeeded. Reloaded angular-acceleration tab and verified requested row counts and no equation-container overflow at the current viewport.


### 2026-10-17 — Rotational-inertia figure width

Made m71593/fs-id1655769 fill available figure width on screen, removing the height cap while preserving aspect ratio. Pending preview refresh. Record: ROTATIONAL-INERTIA-FIGURE-FULL-WIDTH.


### 2026-10-17 — Angular-velocity conversion in two lines

Moved final result of m67046/eip-583 onto its own aligned row. Values, units, and math token sequence preserved. Pending preview refresh. Record: ROTATIONAL-ENERGY-ANGULAR-VELOCITY-TWO-LINES.


### 2026-10-17 — Rotor-inertia calculation in two lines

Combined first two rows of m67046/eip-897; final result retains its own aligned row. Math token sequence preserved. Pending preview refresh. Record: ROTOR-INERTIA-TWO-LINES.


### 2026-10-17 — Rotor-energy height calculation in two lines

Moved final result of m67046/eip-232 onto its own aligned row. Values, units, and math token sequence preserved. Pending preview refresh. Record: ROTOR-ENERGY-HEIGHT-TWO-LINES.


### 2026-10-17 — Rolling-cylinder speed in two lines

Moved final result of m67046/eip-191 onto its own aligned row. Values, units, and math token sequence preserved. Pending preview refresh. Record: ROLLING-CYLINDER-SPEED-TWO-LINES.


### 2026-10-17 — Stacked revolutions per day

Changed the 1 rev/d factor in m71594/eip-195 to a stacked fraction. Values and surrounding calculation preserved. Pending preview refresh. Record: EARTH-ANGULAR-MOMENTUM-STACKED-REV-PER-DAY.


### 2026-10-17 — Lazy-Susan angular-momentum typography

Corrected upright rF text to separate italic variables in m71594/eip-911, consolidated decimal tokens, grouped parenthesized factors, and normalized spacing. Values, units, and two-line layout preserved. Pending preview refresh. Record: LAZY-SUSAN-ANGULAR-MOMENTUM-TYPOGRAPHY.


### 2026-10-17 — Lazy-Susan angular velocity in two lines

Moved final result of m71594/eip-98 onto its own aligned row. Values, units, and math token sequence preserved. Pending preview refresh. Record: LAZY-SUSAN-ANGULAR-VELOCITY-TWO-LINES.


### 2026-10-17 — Net-torque zero spacing

Replaced trailing text whitespace with explicit 0.25em math spacing between net and tau in m71594/eip-283. Pending preview refresh. Record: NET-TORQUE-ZERO-SPACING.


### 2026-10-17 — Separate angular-momentum conservation conditions

Moved net torque zero conditions into separate math expressions with prose parentheses and an em space after the main formula in m71594/eip-10 and eip-67. Added explicit net/tau spacing. IDs, numbers, and punctuation preserved. Pending preview refresh. Record: ANGULAR-MOMENTUM-CONSERVATION-CONDITIONS.

### 2026-10-17 — Preview 170 published

Published all pending rotational-inertia figure sizing, rotational-energy equation layouts, and angular-momentum typography, line breaks, unit fractions, and separated conditions. Both profiles passed: 6441 math expressions, no issues. Commit 66acf2542df4d6ede66af750da20bf1645e904d4; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_5e4d316c5404819180fbf6c75ebd08c9; deployment appgdep_6ad3bd8afb948191b351895472a67c27 succeeded. Reloaded angular-momentum section and verified changed equation structure and no equation-container overflow at the current viewport.


### 2026-10-17 — Rotation exercise emphasis

Changed bold emphasis to italics for the same rotation axis in rotation Exercise 8, preserving the wording. Pending preview refresh. Record: ROTATION-EXERCISE-AXIS-EMPHASIS.


### 2026-10-17 — Reservoir volume in three lines

Moved final result of m71613/eip-289 onto a third aligned row. Values, units, and math token sequence preserved. Pending preview refresh. Record: RESERVOIR-VOLUME-THREE-LINES.


### 2026-10-17 — Atmospheric-pressure definition layout

Led m71623/eip-820 with P_atm = 1 atmosphere (atm), with both SI equivalents on the second aligned row. Values, units, and equation ID preserved. Pending preview refresh. Record: ATMOSPHERIC-PRESSURE-DEFINITION-TWO-LINES.


### 2026-10-17 — Water-pressure depth in two lines

Moved final result of m71623/eip-169 onto its own aligned row. Values, units, and math token sequence preserved. Pending preview refresh. Record: WATER-PRESSURE-DEPTH-TWO-LINES.

### 2026-10-17 — Preview 171 published

Published rotation Exercise 8 italic emphasis, reservoir-volume three-line layout, atmospheric-pressure definition reordering and two-line layout, and water-pressure depth two-line layout. Both profiles passed: 6441 math expressions, no issues. Commit 2891cc725b413f4d263d8be33d7d423af7fd9b18; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_647cd1c9652081919308070c3b75452f; deployment appgdep_6ad3c00dcb6c8191a1ad8d00cd41506f succeeded. Reloaded fluid-pressure section and verified both edited equations have two rows without equation-container overflow at the current viewport.


### 2026-10-17 — Steel volume in two lines

Moved final result of m71624/eip-29 onto its own aligned row. Values, units, and math token sequence preserved. Pending preview refresh. Record: STEEL-VOLUME-TWO-LINES.


### 2026-10-17 — Displaced-water mass in three lines

Separated symbolic expression, substitution, and final result in m71624/eip-383 into three aligned rows. Values, units, and math token sequence preserved. Pending preview refresh. Record: DISPLACED-WATER-MASS-THREE-LINES.


### 2026-10-17 — Steel buoyant force in three lines

Separated symbolic equalities, numerical substitution, and final result in m71624/eip-164 into three aligned rows. Values, units, and math token sequence preserved. Pending preview refresh. Record: STEEL-BUOYANT-FORCE-THREE-LINES.


### 2026-10-17 — Boat displaced-water mass in three lines

Separated symbolic expression, substitution, and final result in m71624/eip-902 into three aligned rows. Values, units, and math token sequence preserved. Pending preview refresh. Record: BOAT-DISPLACED-WATER-MASS-THREE-LINES.


### 2026-10-17 — Maximum boat buoyant force in three lines

Separated symbolic equalities, numerical substitution, and final result in m71624/eip-606 into three aligned rows. Values, units, and math token sequence preserved. Pending preview refresh. Record: BOAT-MAXIMUM-BUOYANT-FORCE-THREE-LINES.


### 2026-10-17 — Aorta flow speed in two lines

Moved final result of m71625/fs-id3104729 onto its own aligned row. Values, units, and math token sequence preserved. Pending preview refresh. Record: AORTA-FLOW-SPEED-TWO-LINES.


### 2026-10-17 — Capillary count in two lines

Moved final result of m71625/fs-id3175565 onto its own aligned row. Values, units, and math token sequence preserved. Pending preview refresh. Record: CAPILLARY-COUNT-TWO-LINES.

### 2026-10-17 — Preview 172 published

Published all pending Archimedes-principle layouts (eip-29, eip-383, eip-164, eip-902, eip-606) and flow-rate result line breaks (fs-id3104729, fs-id3175565). Both profiles passed: 6441 math expressions, no issues. Commit b34f2ab8d1b150e54acdca3a928c2993146bb8f6; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_ab3ba6da0af4819194d72b8f9d6b82ee; deployment appgdep_6ad3c21a1868819192eb2f4b367bbc96 succeeded. Reloaded flow-rate section: both revised calculations have two rows and no scrolling; math widths 294.2px and 315.2px within 437px available.


### 2026-10-17 — Temperature-range figure size

Set m52364/import-auto-id1961424 to 350px wide on screen with no height cap, retaining responsive max-width and aspect ratio. Source is 490 by 1483 pixels. Pending preview refresh. Record: TEMPERATURE-RANGE-FIGURE-SIZE.


### 2026-10-17 — Ideal-gas final pressure in two lines

Moved final result of m67122/import-auto-id2677638 onto its own aligned row. Values, units, and math token sequence preserved. Pending preview refresh. Record: IDEAL-GAS-FINAL-PRESSURE-TWO-LINES.


### 2026-10-17 — Ideal-gas molecule count in two lines

Moved final result of m67122/import-auto-id2887530 onto its own aligned row. Values, units, and math token sequence preserved. Pending preview refresh. Record: IDEAL-GAS-MOLECULE-COUNT-TWO-LINES.


### 2026-10-17 — Inline volume-conversion spacing

Replaced operator-tagged units with upright unit text and standard equals-sign spacing in both conversions in m67122/import-auto-id3224684. Values preserved. Record: IDEAL-GAS-INLINE-VOLUME-CONVERSION-SPACING.

### 2026-10-17 — Preview 173 published

Published temperature-range figure sizing, both ideal-gas final-result line breaks, and inline volume-conversion spacing fixes. Both profiles passed: 6441 math expressions, no issues. Commit 72c258769e6be361d19a64978e25240bc3f71ae7; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_0d26ff6a83288191bf15be4eb093c581; deployment appgdep_6ad3c45c501c81918fff20fa1918f79e succeeded. Reloaded ideal-gas section; verified correct unit markup in conversions and two-row calculations without horizontal scrolling.


### 2026-10-17 — Total transferred heat in two lines

Moved final result of m67622/eip-229 onto its own aligned row. Displayed values, units, and math token sequence preserved; obsolete source annotation removed. Pending preview refresh. Record: TOTAL-TRANSFERRED-HEAT-TWO-LINES.


### 2026-10-17 — Calorimetry stacked specific-heat units

Changed all four J/(kg dot degrees C) units in the first row of m67622/eip-274 to stacked fractions, in both numerator and denominator. Numerical values and remaining rows preserved. Pending preview refresh. Record: CALORIMETRY-FINAL-TEMPERATURE-STACKED-UNITS.

### 2026-10-17 — Preview 174 published

Published the total-heat final-result line break and four stacked specific-heat unit fractions in the calorimetry substitution. Both profiles passed: 6441 math expressions, no issues. Commit 624332e01dbb96bdfdf3f729494874ba4c500843; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_e71cd3f5672c8191adcf57657ad8b00f; deployment appgdep_6ad3c5cb6da4819182236938283b409d succeeded. Reloaded heat-capacity section; verified total heat uses two rows without scrolling and calorimetry has four stacked unit fractions. The long calorimetry substitution still requires horizontal scrolling at the current narrow viewport.


### 2026-10-17 — Soda numerator term in three lines

Added the descriptive label Soda term to m67124/eip-96, with symbolic expression, numerical substitution, and result on separate aligned rows. Avoids reusing Q_soda, which denotes a different quantity in this example. Values and units preserved. Pending preview refresh. Record: SODA-NUMERATOR-TERM-THREE-LINES.

### 2026-10-17 — Ice latent-heat result in two lines

Moved the final 6012 J result in m67124/eip-291 to a second aligned row. Displayed tokens preserved; obsolete annotation removed. Pending preview refresh. Record: ICE-LATENT-HEAT-RESULT-TWO-LINES.

### 2026-10-17 — Mixture denominator in three lines

Added the label Denominator to m67124/eip-649 and separated the symbolic expression, substitution, and 1122 J/degree C result into three aligned rows. Values and units preserved. Pending preview refresh. Record: MIXTURE-DENOMINATOR-THREE-LINES.

### 2026-10-17 — Preview 175 published

Published the Soda term and Denominator three-line layouts and ice latent-heat two-line result. Both profiles passed: 6441 math expressions, no issues. Commit ac2c585b181b9053561f21ddd7f07f28c443495e; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_f9fbf5d09b4c8191993f97653bab7fae; deployment appgdep_6ad3c820972481919dea7525fb62ee67 succeeded. Reloaded phase-change section and verified row counts 3, 2, 3. Soda term and ice calculation fit; denominator still requires horizontal scrolling at the current narrow viewport.


### 2026-10-17 — Short denominator label

Abbreviated the m67124/eip-649 label to denom, preserving the three-line calculation. Pending preview refresh. Record: MIXTURE-DENOMINATOR-SHORT-LABEL.

### 2026-10-17 — Piston-cycle figure sizing

Set Figure 8.9.3 to 350 px wide on screen, with no height cap and the existing responsive max-width constraint. Source is 516 by 1250 px. Pending preview refresh. Record: HEAT-ENGINE-PISTON-FIGURE-SIZE.

### 2026-10-17 — Thermodynamic-process plots sizing

Set Figure 8.9.5 to 350 px wide on screen, with no height cap and the existing responsive max-width constraint. Source is 625 by 1127 px. Pending preview refresh. Record: THERMODYNAMIC-PROCESS-PLOTS-FIGURE-SIZE.

### 2026-10-17 — Inline latent-heat summary

Moved Q = mL inline in the phase-change summary bullet, removing the introductory colon and retaining both source anchors. Record: LATENT-HEAT-SUMMARY-INLINE.

### 2026-10-17 — Preview 176 published

Published the inline latent-heat summary, shortened denom label, and Figure 8.9.3/8.9.5 sizing. Both profiles passed: 6441 math expressions, no issues. Commit 604daee1deaebbc3ad736444597cef0fd94c857d; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_2d9e5a08ed308191a63ca89781eccc97; deployment appgdep_6ad3ca6626408191a88205a32da96917 succeeded. Reloaded thermal-physics review; verified the latent-heat bullet is one continuous sentence with inline math and no equation block.


### 2026-10-17 — Van de Graaff figure sizing

Set Figure 9.7.8 to 350 px wide on screen, with no height cap and the existing responsive max-width constraint. Source is 361 by 634 px. Pending preview refresh. Record: VAN-DE-GRAAFF-FIGURE-SIZE.

### 2026-10-17 — Simple circuit figure sizing

Set Figure 9.8.2 to 350 px wide on screen, with no height cap and the existing responsive max-width constraint. Source is 574 by 959 px. Pending preview refresh. Record: SIMPLE-CIRCUIT-FIGURE-SIZE.

### 2026-10-17 — Electron-symbol parentheses

Moved the parentheses around the electron symbol into prose in m67130/import-auto-id2052846. Also corrected the adjacent sentence spacing before Since. Pending preview refresh. Record: ELECTRON-SYMBOL-PROSE-PARENTHESES.

### 2026-10-17 — Series resistance row spacing

Added the standard 0.5em row spacing to m42356/eip-138. Existing unit spacing and content preserved. Pending preview refresh. Record: SERIES-RESISTANCE-ROW-SPACING.

### 2026-10-17 — Series voltage sum in two lines

Moved the final 12.0 V result in m42356/eip-359 to its own aligned row. All displayed tokens preserved. Pending preview refresh. Record: SERIES-VOLTAGE-SUM-TWO-LINES.

### 2026-10-17 — Series power sum in two lines

Moved the final 7.20 W result in m42356/eip-698 to its own aligned row. Displayed tokens preserved. Pending preview refresh. Record: SERIES-POWER-SUM-TWO-LINES.

### 2026-10-17 — Parallel circuits figure width

Set Figure 9.11.3 to fill the available figure width on screen and removed the height cap. Aspect ratio preserved. Source is 1000 by 1002 px. Pending preview refresh. Record: PARALLEL-CIRCUITS-FIGURE-FULL-WIDTH.

### 2026-10-17 — Parallel power sum in two lines

Moved the final 179 W result in m42356/eip-286 to its own aligned row. All displayed tokens preserved. Pending preview refresh. Record: PARALLEL-POWER-SUM-TWO-LINES.

### 2026-10-17 — Scalar electric-field magnitude in summary

Changed E to a scalar math variable in m52385/eip-915 and its introductory prose, which now reads The magnitude E of the electric field. Preserved vector E in the subsequent vector-addition statement and preceding vector definition. Pending preview refresh. Record: ELECTRIC-FIELD-SUMMARY-SCALAR-MAGNITUDE.

### 2026-10-17 — Magnetic recording figure width

Set Figure 10.3.6 to fill the available figure width on screen and removed the height cap. Aspect ratio preserved. Source is 1001 by 1319 px. Pending preview refresh. Record: MAGNETIC-RECORDING-FIGURE-FULL-WIDTH.

### 2026-10-17 — Magnetic-force display spacing

Wrapped the four standalone display expressions in m52414/eip-673 in standard unnumbered equation blocks to provide consistent vertical margins. Existing prose, math, and anchors preserved. Pending preview refresh. Record: MAGNETIC-FORCE-DISPLAY-SPACING.

### 2026-10-17 — Preview 177 published

Published pending electrostatics/current figure sizing and electron-symbol punctuation, series/parallel equation spacing and final-result line breaks, parallel-circuit figure sizing, scalar electric-field magnitude notation, magnetic-recording figure sizing, and magnetic-force display spacing. Both profiles passed: 6441 math expressions, no issues. Commit 689af9f78b4781e90f958f1bc6d5e3a361039ed6; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_fe18ff7c68388191a1c98c11e998756d; deployment appgdep_6ad3cf0cbf508191a008957e9f12f283 succeeded. Reloaded the magnetic-force section and verified all four expressions have 18px top and bottom margins.


### 2026-10-17 — Straight-wire field diagram sizing

Set Figure 10.8.1 to 350 px wide on screen, with no height cap and the existing responsive max-width constraint. Source is 624 by 1048 px. Pending preview refresh. Record: STRAIGHT-WIRE-RIGHT-HAND-RULE-FIGURE-SIZE.

### 2026-10-17 — Redundant Maxwell forward reminder

Removed the standalone definition reminder at the bottom of m52420. Preserved its legacy anchors and the existing forward section link in the prose. Pending preview refresh. Record: MAXWELL-REDUNDANT-FORWARD-REMINDER.

### 2026-10-17 — Transformer secondary turns in two lines

Combined the symbolic and substitution rows of m52427/eip-757, retaining the final result on the second aligned row. Displayed tokens preserved. Pending preview refresh. Record: TRANSFORMER-SECONDARY-TURNS-TWO-LINES.

### 2026-10-17 — Transformer secondary current in two lines

Combined the symbolic and substitution rows of m52427/eip-361, retaining 12.0 mA on the second aligned row. Displayed tokens preserved. Pending preview refresh. Record: TRANSFORMER-SECONDARY-CURRENT-TWO-LINES.

### 2026-10-17 — Step-down transformer turns in two lines

Combined the symbolic and substitution rows of m52427/eip-63, retaining 25 on the second aligned row. Displayed tokens preserved. Pending preview refresh. Record: STEP-DOWN-TRANSFORMER-TURNS-TWO-LINES.

### 2026-10-17 — Step-down transformer current in two lines

Combined the symbolic and substitution rows of m52427/eip-981, retaining 2.00 A on the second aligned row. Displayed tokens preserved. Pending preview refresh. Record: STEP-DOWN-TRANSFORMER-CURRENT-TWO-LINES.

### 2026-10-17 — Inline magnetic-force summary

Made F = qvB inline in the first summary bullet of m52414. The matching formula in the section is unnumbered. Added sentence punctuation outside math. Pending preview refresh. Record: MAGNETIC-FORCE-SUMMARY-INLINE.

### 2026-10-17 — Preview 178 published

Published the straight-wire/right-hand-rule figure sizing, redundant Maxwell reminder removal, four transformer calculations with combined first rows, and inline magnetic-force summary. Both profiles passed: 6441 math expressions, no issues. Commit d6d2a575957d9af62e17dd9b1e55864453cca7bb; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_8259b15f979081918504aae228a8430b; deployment appgdep_6ad3d195d078819181a8bd50ce8d1e9b succeeded. Reloaded magnetism review and verified the maximum-force summary formula renders inline.


### 2026-10-17 — Michelson rotating-mirror figure width

Set Figure 11.7.2 to fill the available figure width on screen and removed the height cap. Aspect ratio preserved. Source is 1000 by 1078 px. Pending preview refresh. Record: MICHELSON-ROTATING-MIRROR-FIGURE-FULL-WIDTH.

### 2026-10-17 — Rainbow formation figure sizing

Set Figure 11.8.5 to 350 px wide on screen, with no height cap and the existing responsive max-width constraint. Source is 530 by 1250 px. Pending preview refresh. Record: RAINBOW-FORMATION-FIGURE-SIZE.

### 2026-10-17 — Thin-lens ray-tracing figure sizing

Set Figure 11.9.7 to 350 px wide on screen, with no height cap and the existing responsive max-width constraint. Source is 664 by 1450 px. Pending preview refresh. Record: THIN-LENS-RAY-TRACING-FIGURE-SIZE.

### 2026-10-17 — Converging-lens virtual-image figure sizing

Set Figure 11.9.11 to 350 px wide on screen, with no height cap and the existing responsive max-width constraint. Source is 1019 by 1600 px. Pending preview refresh. Record: CONVERGING-LENS-VIRTUAL-IMAGE-FIGURE-SIZE.

### 2026-10-17 — Diverging-lens ray-tracing figure sizing

Set Figure 11.9.13 to fill the available figure width on screen and removed the height cap. Aspect ratio preserved. Source is 1000 by 1208 px. Pending preview refresh. Record: DIVERGING-LENS-RAY-TRACING-FIGURE-SIZE.

### 2026-10-17 — Concave mirror area in three lines

Separated m67135/eip-48 into formula, numerical substitution, and final result on three aligned rows. Displayed tokens preserved. Pending preview refresh. Record: CONCAVE-MIRROR-AREA-THREE-LINES.

### 2026-10-17 — Stacked mineral-oil density unit

Changed kg/m^3 to a stacked fraction in m67135/eip-677. Numerical values and equation layout preserved. Pending preview refresh. Record: MINERAL-OIL-DENSITY-STACKED-UNIT.

### 2026-10-17 — Magnifying mirror figure width

Set Figure 11.10.6 to fill the available figure width on screen and removed the height cap. Aspect ratio preserved. Source is 919 by 1250 px. Pending preview refresh. Record: MAGNIFYING-MIRROR-FIGURE-FULL-WIDTH.

### 2026-10-17 — Convex mirror figure width

Set Figure 11.10.7 to fill the available figure width on screen and removed the height cap. Aspect ratio preserved. Source is 759 by 1250 px. Pending preview refresh. Record: CONVEX-MIRROR-FIGURE-FULL-WIDTH.

### 2026-10-17 — Preview 179 published

Published seven optics figure sizing corrections, three-line mirror area calculation, and stacked mineral-oil density units. Both profiles passed: 6441 math expressions, no issues. Commit 331ce920089e00f3c352497fed25ac8bec37b5ba; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_bbfc6abe73508191925b9d741605ea34; deployment appgdep_6ad3d45d1ea08191b5a5a52bb194ec6c succeeded. Reloaded mirror section; both changed calculations have three rows and no horizontal scrolling at the current viewport.


### 2026-10-17 — Photoelectric potential-energy parentheses

Replaced nested content MathML in m67251/import-auto-id1488065 with explicit presentation markup for Delta PE = (-e)(-3.00 V) = 3.00 eV. Removed redundant inner and result parentheses; preserved signs and values. Pending preview refresh. Record: PHOTOELECTRIC-POTENTIAL-ENERGY-PARENTHESES.

### 2026-10-17 — Lorentz factor in two paired lines

Combined rows 1 and 2, and rows 3 and 4, of m42531/eip-216. Added standard row spacing; displayed tokens preserved. Pending preview refresh. Record: LORENTZ-FACTOR-PAIRED-LINES.

### 2026-10-17 — Length contraction in two lines

Combined the symbolic and substitution rows of m42535/eip-535, retaining 0.1433 ly on the second aligned row. Displayed tokens preserved; obsolete layout annotation removed. Pending preview refresh. Record: LENGTH-CONTRACTION-TWO-LINES.

### 2026-10-17 — Photomultiplier figure sizing

Set Figure 14.3.3 to 350 px wide on screen, with no height cap and the existing responsive max-width constraint. Source is 550 by 764 px. Pending preview refresh. Record: PHOTOMULTIPLIER-FIGURE-SIZE.

### 2026-10-17 — Nuclide chart figure width

Set Figure 14.4.3 to fill the available figure width on screen and removed the height cap. Aspect ratio preserved. Source is 575 by 773 px. Pending preview refresh. Record: NUCLIDE-CHART-FIGURE-FULL-WIDTH.

### 2026-10-17 — Uranium decay-series figure width

Set Figure 14.5.1 to fill the available figure width on screen and removed the height cap. Aspect ratio preserved. Source is 550 by 809 px. Pending preview refresh. Record: URANIUM-DECAY-SERIES-FIGURE-FULL-WIDTH.

### 2026-10-17 — Figure 14.11.5 display sizing

Set the existing figure to 350 px wide on screen, with no height cap and the existing responsive max-width constraint. Source is 450 by 785 px. Pending preview refresh. Record: FIGURE-14-11-5-DISPLAY-SIZE.

### 2026-10-17 — Figure 14.11.6 display sizing

Set the existing chart to 350 px wide on screen, with no height cap and the existing responsive max-width constraint. Source is 438 by 1250 px. Pending preview refresh. Record: FIGURE-14-11-6-DISPLAY-SIZE.

### 2026-10-17 — Preview 180 published for widescreen review

Published the photoelectric parentheses cleanup, Lorentz-factor and length-contraction line combinations, and five nuclear-physics figure sizing adjustments. Both profiles passed: 6441 math expressions, no issues. Commit 60e9189452d4d25e317972bcadede62de7e6048f; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_8a53bc3d80e0819195b41eb082433bda; deployment appgdep_6ad3d8126d4c8191982dfbd21fb2336d succeeded. Reloaded the user's Chapter 14 review tab for their third, widescreen layout pass.


### 2026-10-17 — Falling-objects widescreen figure cap

Limited Figure 1.7.1 to 450 px wide on screen, shrinking to fit narrower containers, to bring embedded labels closer to caption text size. Aspect ratio preserved. Pending preview refresh. Record: FALLING-OBJECTS-FIGURE-WIDESCREEN-CAP.

### 2026-10-17 — Falling-rock graph sizing

Set Figure 1.7.3 to 400 px wide on screen with no height cap, shrinking to fit narrower containers, to bring graph labels closer to caption size. Source is 640 by 1233 px. Pending preview refresh. Record: FALLING-ROCK-GRAPHS-DISPLAY-SIZE.

### 2026-10-17 — Falling-rock comparison sizing

Set Figure 1.7.5 to 600 px wide on screen with no height cap, shrinking to fit narrower containers, to bring the small labels closer to caption size. Source is 946 by 1248 px. Pending preview refresh. Record: FALLING-ROCK-COMPARISON-DISPLAY-SIZE.

### 2026-10-17 — Falling-ball graph and table sizing

Set Figure 1.7.6 to 650 px wide on screen with no height cap, shrinking to fit narrower containers, to bring graph and table labels closer to caption size. Source is 1196 by 1437 px. Pending preview refresh. Record: FALLING-BALL-GRAPHS-DISPLAY-SIZE.

### 2026-10-17 — Preview 181 published

Published the four falling-objects figure adjustments for widescreen review. Both profiles passed: 6441 math expressions, no issues. Commit 0e2c4c5d51d9b4e4a5d6a47b3ae45c2d1257937a; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_576dca124f9081919d74a06bf757614b; deployment appgdep_6ad3da225714819191ba0f00542bf875 succeeded. Reloaded falling-objects section and verified image widths of 450, 400, 600, and 650 px.


### 2026-10-17 — Projectile components figure sizing

Set Figure 1.8.1 to 550 px wide on screen with no height cap, shrinking to fit narrower containers, to bring vector labels closer to caption size. Source is 937 by 1383 px. Pending preview refresh. Record: PROJECTILE-COMPONENTS-FIGURE-DISPLAY-SIZE.

### 2026-10-17 — Newton second-law figure display size

- Figure 2.4.1: enlarge the wagon and free-body diagrams to a 650 px screen width cap, constrained to the available width, with automatic height and no height cap. This brings the force labels closer to caption size.
- Correction record: `NEWTON-SECOND-LAW-WAGON-FIGURE-DISPLAY-SIZE`.
- Pending preview refresh.

### 2026-10-17 — Rocket-sled figure display size

- Figure 2.4.4: enlarge the rocket-sled and free-body diagram to a 550 px screen width cap, constrained to the available width, with automatic height and no height cap, bringing force labels closer to caption size.
- Correction record: `ROCKET-SLED-FIGURE-DISPLAY-SIZE`.
- Pending preview refresh.

### 2026-10-17 — Normal-force comparison figure display size

- Figure 2.6.1: enlarge the normal-force comparison and free-body diagrams to a 500 px screen width cap, constrained to available width, with automatic height and no height cap. This brings the force labels closer to caption size.
- Correction record: `NORMAL-FORCE-COMPARISON-FIGURE-DISPLAY-SIZE`.
- Pending preview refresh.

### 2026-10-17 — Friction surface figure widescreen cap

- Figure 2.8.1: reduce the surface-friction illustration to a 450 px screen width cap, constrained to available width and preserving its aspect ratio, so the embedded text is closer to caption size.
- Correction record: `FRICTION-SURFACE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Friction contact-area figure widescreen cap

- Figure 2.8.3: reduce the small/large normal-force comparison to a 325 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `FRICTION-CONTACT-AREA-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Earth radius figure widescreen cap

- Figure 2.9.3: reduce the Earth-radius illustration to a 375 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `EARTH-RADIUS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Lunar tides figure widescreen cap

- Figure 2.9.4: reduce the lunar-tide illustration to a 425 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `LUNAR-TIDES-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Impulse force-time graph widescreen cap

- Figure 4.3.1: reduce the force-time graph to a 300 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `IMPULSE-FORCE-TIME-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Spring recording figure widescreen cap

- Figure 5.3.3: reduce the spring and moving-paper illustration to a 180 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `SPRING-RECORDING-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Harmonic-motion graphs figure display size

- Figure 5.3.4: enlarge the spring-motion and position/velocity/acceleration graphs to a 400 px screen width cap, constrained to available width, with automatic height and no height cap. This brings the small labels closer to caption size.
- Correction record: `HARMONIC-MOTION-GRAPHS-FIGURE-DISPLAY-SIZE`.
- Pending preview refresh.

### 2026-10-17 — Transverse-wave figure widescreen cap

- Figure 5.5.3: reduce the transverse-wave illustration to a 425 px screen width cap, constrained to available width and preserving its aspect ratio, so the amplitude label is closer to caption size.
- Correction record: `TRANSVERSE-WAVE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Longitudinal-wave figure widescreen cap

- Figure 5.5.4: reduce the longitudinal-wave illustration to a 425 px screen width cap, matching Figure 5.5.3 above it. Constrain to available width and preserve its aspect ratio, bringing embedded labels closer to caption size.
- Correction record: `LONGITUDINAL-WAVE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Fundamental standing-wave figure widescreen cap

- Figure 5.6.6: replace its full-width screen presentation with a 350 px width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `FUNDAMENTAL-STANDING-WAVE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Standing-wave overtone figure width match

- Figure 5.6.7: set a 350 px screen width cap to match Figure 5.6.6 above it, constrained to available width and preserving its aspect ratio.
- Correction record: `STANDING-WAVE-OVERTONES-FIGURE-WIDTH-MATCH`.
- Pending preview refresh.

### 2026-10-17 — Sound compression figure widescreen cap

- Figure 5.7.2: reduce the vibrating-string compression illustration to a 200 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `SOUND-COMPRESSION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Leftward vibrating-string figure width match

- Figure 5.7.3: set a 200 px screen width cap to match resized Figure 5.7.2 above it, constrained to available width and preserving its aspect ratio.
- Correction record: `SOUND-LEFTWARD-STRING-FIGURE-WIDTH-MATCH`.
- Pending preview refresh.

### 2026-10-17 — Speaker frequency figure widescreen cap

- Figure 5.8.4: reduce the speaker frequency/wavelength illustration to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `SPEAKER-FREQUENCY-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Stationary sound-source figure widescreen cap

- Figure 5.9.1: reduce the stationary sound-source illustration to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so observer labels are closer to caption size.
- Correction record: `STATIONARY-SOUND-SOURCE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Moving sound-source figure widescreen cap

- Figure 5.9.2: reduce the moving sound-source illustration to a 300 px screen width cap, constrained to available width and preserving its aspect ratio, so wavefront and observer labels are closer to caption size.
- Correction record: `MOVING-SOUND-SOURCE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Moving sound-observers figure widescreen cap

- Figure 5.9.3: reduce the moving-observers illustration to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so observer labels are closer to caption size.
- Correction record: `MOVING-SOUND-OBSERVERS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Sonic-boom wavefront figure widescreen cap

- Figure 5.9.4: reduce the sonic-boom wavefront illustration to a 275 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `SONIC-BOOM-WAVEFRONTS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Circular acceleration components figure widescreen cap

- Figure 6.2.3: reduce the centripetal/tangential acceleration diagram to a 200 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `CIRCULAR-ACCELERATION-COMPONENTS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Bike-wheel acceleration figure widescreen cap

- Figure 6.3.1: reduce the bike-wheel angular-acceleration illustration to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `BIKE-WHEEL-ACCELERATION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Rotating mass tabletop figure widescreen cap

- Figure 6.3.2: reduce the rotating-mass tabletop illustration to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `ROTATING-MASS-TABLETOP-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Angular-momentum right-hand-rule figure widescreen cap

- Figure 6.6.1: reduce the angular-momentum right-hand-rule illustration to a 375 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `ANGULAR-MOMENTUM-RIGHT-HAND-RULE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Torque direction figure widescreen cap

- Figure 6.6.2: reduce the torque-direction and merry-go-round illustration to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `TORQUE-DIRECTION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Pressure contact-area figure widescreen cap

- Figure 7.4.1: reduce the pressure/contact-area comparison to a 500 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `PRESSURE-CONTACT-AREA-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Atmospheric air-column figure widescreen cap

- Figure 7.5.3: reduce the atmospheric air-column illustration to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `ATMOSPHERIC-AIR-COLUMN-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Hydrometer figure widescreen cap

- Figure 7.6.5: reduce the hydrometer illustration to a 275 px screen width cap, constrained to available width and preserving its aspect ratio, so scale numerals are closer to caption size.
- Correction record: `HYDROMETER-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Flow-rate figure widescreen cap

- Figure 7.7.1: reduce the flow-rate illustration to a 275 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels and equations are closer to caption size.
- Correction record: `FLOW-RATE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Narrowing-tube continuity figure widescreen cap

- Figure 7.7.2: reduce the narrowing-tube continuity illustration to a 500 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `NARROWING-TUBE-CONTINUITY-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Vehicle airflow figure widescreen cap

- Figure 7.8.1: reduce the vehicle-airflow illustration to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so pressure and speed labels are closer to caption size.
- Correction record: `VEHICLE-AIRFLOW-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Entrainment devices figure widescreen cap

- Figure 7.8.2: reduce the entrainment-device illustration to a 625 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `ENTRAINMENT-DEVICES-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Levee and sandbags figure widescreen cap

- Figure 7.E.1: reduce the levee and sandbags illustration to a 300 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `LEVEE-SANDBAGS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Venturi constriction figure widescreen cap

- Figure 7.E.3: reduce the Venturi constriction illustration to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `VENTURI-CONSTRICTION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — First-law energy-transfer figure widescreen cap

- Figure 8.8.2: reduce the energy-transfer illustration to a 500 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `FIRST-LAW-ENERGY-TRANSFER-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Entropy paths figure widescreen cap

- Figure 8.13.2: reduce the reversible/irreversible entropy-path illustration to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `ENTROPY-PATHS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Melting entropy figure widescreen cap

- Figure 8.13.4: reduce the ice-to-water entropy illustration to a 375 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `MELTING-ENTROPY-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Amber and cloth charge-separation figure widescreen cap

- Figure 9.2.6: reduce the amber-and-cloth charge-separation illustration to a 600 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `AMBER-CLOTH-CHARGE-SEPARATION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Pair creation and annihilation figure display size

- Figure 9.2.7: enlarge the pair-creation/annihilation illustration to a 325 px screen width cap, constrained to available width, with automatic height and no height cap, so embedded labels are closer to caption size.
- Correction record: `PAIR-CREATION-ANNIHILATION-FIGURE-DISPLAY-SIZE`.
- Pending preview refresh.

### 2026-10-17 — Coulomb force-pairs figure widescreen cap

- Figure 9.3.2: reduce the like/unlike charge-force illustration to a 400 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `COULOMB-FORCE-PAIRS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Test-charge forces figure widescreen cap

- Figure 9.4.1: reduce the test-charge force illustration to a 175 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `TEST-CHARGE-FORCES-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Electric-field representations figure widescreen cap

- Figure 9.5.1: reduce the electric-field representations illustration to a 450 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `ELECTRIC-FIELD-REPRESENTATIONS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Two-positive-charge field figure widescreen cap

- Figure 9.5.3: reduce the two-positive-charge field illustration to a 200 px screen width cap, constrained to available width and preserving its aspect ratio, so field-vector labels are closer to caption size.
- Correction record: `TWO-POSITIVE-CHARGES-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Negative and opposite charge fields figure display size

- Figure 9.5.4: enlarge the negative/opposite-charge field illustration to a 400 px screen width cap, constrained to available width, with automatic height and no height cap, so charge and panel labels are closer to caption size.
- Correction record: `NEGATIVE-OPPOSITE-CHARGE-FIELDS-FIGURE-DISPLAY-SIZE`.
- Pending preview refresh.

### 2026-10-17 — Potential-energy analogy figure widescreen cap

- Figure 9.6.1: reduce the electric/gravitational potential-energy illustration to a 275 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `POTENTIAL-ENERGY-ANALOGY-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Battery and headlight figure widescreen cap

- Figure 9.6.2: reduce the battery-and-headlight illustration to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `BATTERY-HEADLIGHT-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Polarized spherical conductor figure widescreen cap

- Figure 9.7.2: reduce the polarized spherical-conductor illustration to a 350 px screen width cap, constrained to available width and preserving its aspect ratio, so charge symbols are closer to caption size.
- Correction record: `POLARIZED-SPHERICAL-CONDUCTOR-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Parallel charged plates figure widescreen cap

- Figure 9.7.4: reduce the parallel-plate field illustration to a 450 px screen width cap, constrained to available width and preserving its aspect ratio, so charge symbols are closer to caption size.
- Correction record: `PARALLEL-CHARGED-PLATES-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Uneven conductor surfaces figure widescreen cap

- Figure 9.7.5: reduce the uneven-conductor surface illustration to a 650 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `UNEVEN-CONDUCTOR-SURFACES-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Lightning rod and Van de Graaff photos widescreen cap

- Figure 9.7.7: reduce the photo pair to a 475 px screen width cap, constrained to available width and preserving its aspect ratio, so panel labels are closer to caption size.
- Correction record: `LIGHTNING-ROD-VAN-DE-GRAAFF-PHOTOS-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Van de Graaff figure widescreen cap

- Figure 9.7.8: reduce the existing 350 px screen width to 250 px, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size. Retain removal of the height cap.
- Correction record: `VAN-DE-GRAAFF-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Xerography stages figure widescreen cap

- Figure 9.7.9: reduce the xerography-stage illustration to a 575 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `XEROGRAPHY-STAGES-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Laser-printer figure widescreen cap

- Figure 9.7.10: reduce the laser-printer illustration to a 575 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `LASER-PRINTER-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Inkjet-printer figure widescreen cap

- Figure 9.7.11: reduce the inkjet-printer illustration to a 475 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `INKJET-PRINTER-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Current charge-flow figure widescreen cap

- Figure 9.8.1: reduce the current/charge-flow illustration to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `CURRENT-CHARGE-FLOW-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Simple circuit figure widescreen cap

- Figure 9.8.2: reduce the existing 350 px screen width to 300 px, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size. Retain removal of the height cap.
- Correction record: `SIMPLE-CIRCUIT-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Ohm law circuit figure widescreen cap

- Figure 9.9.1: reduce the simple-circuit schematic to a 225 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `OHMS-LAW-CIRCUIT-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Resistor voltmeter figure widescreen cap

- Figure 9.9.2: reduce the resistor-voltmeter illustration to a 325 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `RESISTOR-VOLTMETER-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Series and parallel resistors figure widescreen cap

- Figure 9.11.1: reduce the series/parallel resistor illustration to a 275 px screen width cap, constrained to available width and preserving its aspect ratio, so resistor labels are closer to caption size.
- Correction record: `SERIES-PARALLEL-RESISTORS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Equivalent series resistance figure widescreen cap

- Figure 9.11.2: reduce the equivalent-series-resistance illustration to a 400 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `EQUIVALENT-SERIES-RESISTANCE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Combination resistor example figure widescreen cap

- Figure 9.11.5: reduce the combination-circuit illustration to a 475 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `COMBINATION-RESISTOR-EXAMPLE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Fuse and circuit-breaker figure display size

- Figure 9.12.2: enlarge the fuse/circuit-breaker illustration to a 350 px screen width cap, constrained to available width, with automatic height and no height cap, so component labels are closer to caption size.
- Correction record: `FUSE-CIRCUIT-BREAKER-FIGURE-DISPLAY-SIZE`.
- Pending preview refresh.

### 2026-10-17 — Fuse circuit schematic figure widescreen cap

- Figure 9.12.3: reduce the fuse-circuit schematic to a 175 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `FUSE-CIRCUIT-SCHEMATIC-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Electric shock effects figure widescreen cap

- Figure 9.12.4: reduce the electric-shock effects illustration to a 500 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `ELECTRIC-SHOCK-EFFECTS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Shock sensitivity graph widescreen cap

- Figure 9.12.5: reduce the shock-sensitivity graph to a 375 px screen width cap, constrained to available width and preserving its aspect ratio, so axis and curve labels are closer to caption size.
- Correction record: `SHOCK-SENSITIVITY-GRAPH-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Battery and bulb open-circuit figure widescreen cap

- Figure 9.E.1: reduce the battery-and-bulb illustration to a 600 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `BATTERY-BULB-OPEN-CIRCUIT-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Magnet shapes figure widescreen cap

- Figure 10.2.1: reduce the magnet-shapes illustration to a 300 px screen width cap, constrained to available width and preserving its aspect ratio, bringing pole labels closer to caption size.
- Correction record: `MAGNET-SHAPES-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Earth magnetic poles figure widescreen cap

- Figure 10.2.2: reduce the Earth-and-magnet illustration to a 325 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `EARTH-MAGNETIC-POLES-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Iron-core electromagnet figure widescreen cap

- Figure 10.3.5: reduce the iron-core electromagnet illustration to a 100 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `IRON-CORE-ELECTROMAGNET-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Magnetic recording figure widescreen cap

- Figure 10.3.6: reduce the magnetic recording panels to a 400 px screen width cap, constrained to available width and preserving their aspect ratio, so embedded labels are closer to caption size.
- Correction record: `MAGNETIC-RECORDING-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Electron magnetism models figure widescreen cap

- Figure 10.3.7: reduce the electron magnetism models to a 550 px screen width cap, constrained to available width and preserving their aspect ratio, so embedded labels are closer to caption size.
- Correction record: `ELECTRON-MAGNETISM-MODELS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Magnetic force on a wire figure widescreen cap

- Figure 10.6.1: reduce the current-carrying wire diagram to a 500 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `MAGNETIC-FORCE-ON-WIRE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Magnetohydrodynamic pump figure widescreen cap

- Figure 10.6.3: reduce the magnetohydrodynamic pump diagram to a 350 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `MAGNETOHYDRODYNAMIC-PUMP-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — MHD propulsion figure widescreen cap

- Figure 10.6.4: reduce the MHD propulsion diagram to a 475 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded annotations are closer to caption size.
- Correction record: `MHD-PROPULSION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Current-loop torque figure widescreen cap

- Figure 10.7.1: reduce the current-loop torque diagram to a 300 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `CURRENT-LOOP-TORQUE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Motor brushes figure widescreen cap

- Figure 10.7.2: reduce the motor-and-brushes diagram to a 500 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `MOTOR-BRUSHES-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Moving-coil meter figure widescreen cap

- Figure 10.7.3: reduce the moving-coil meter diagram to a 325 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `MOVING-COIL-METER-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Faraday apparatus figure widescreen cap

- Figure 10.9.1: reduce Faraday’s apparatus diagram to a 500 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `FARADAY-APPARATUS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Magnetic flux components figure widescreen cap

- Figure 10.9.4: reduce the magnetic-flux diagram to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `MAGNETIC-FLUX-COMPONENTS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Power distribution figure widescreen cap

- Figure 10.11.2: reduce the power-distribution diagram to a 650 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `POWER-DISTRIBUTION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Transformer construction figure widescreen cap

- Figure 10.11.3: reduce the transformer construction diagram to a 275 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `TRANSFORMER-CONSTRUCTION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — AC and DC graphs figure widescreen cap

- Figure 10.12.1: reduce the AC/DC voltage-and-current graphs to a 225 px screen width cap, constrained to available width and preserving their aspect ratio, so embedded labels are closer to caption size.
- Correction record: `AC-DC-GRAPHS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — AC circuit and waveform figure widescreen cap

- Figure 10.12.2: reduce the AC circuit-and-waveform diagram to a 275 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `AC-CIRCUIT-WAVEFORM-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — AC power graph figure widescreen cap

- Figure 10.12.3: reduce the AC power graph to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `AC-POWER-GRAPH-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Magnetic force direction exercise figure widescreen cap

- Figure 10.E.2: reduce the magnetic-force direction exercise diagram to a 425 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `MAGNETIC-FORCE-DIRECTION-EXERCISE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Force and velocity exercise figure widescreen cap

- Figure 10.E.3: reduce the force-and-velocity exercise diagram to a 275 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `FORCE-VELOCITY-EXERCISE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Stretched coil exercise figure widescreen cap

- Figure 10.E.5: reduce the stretched-coil exercise diagram to a 475 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `STRETCHED-COIL-EXERCISE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Hertz apparatus figure widescreen cap

- Figure 11.2.2: reduce the Hertz apparatus diagram to a 550 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `HERTZ-APPARATUS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Antenna electric and magnetic fields figure widescreen cap

- Figure 11.3.2: reduce the antenna-and-fields diagram to a 650 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `ANTENNA-ELECTRIC-MAGNETIC-FIELDS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Electromagnetic wave figure widescreen cap

- Figure 11.3.3: reduce the electromagnetic-wave diagram to a 450 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `ELECTROMAGNETIC-WAVE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Electromagnetic wave momentum figure widescreen cap

- Figure 11.3.4: reduce the electromagnetic-wave momentum diagram to a 400 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `ELECTROMAGNETIC-WAVE-MOMENTUM-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Radiation pressure apparatus figure widescreen cap

- Figure 11.3.5: reduce the radiation-pressure apparatus diagram to a 300 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `RADIATION-PRESSURE-APPARATUS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Submarine ELF radio wave figure widescreen cap

- Figure 11.5.3: reduce the submarine radio-wave diagram to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so its embedded label is closer to caption size.
- Correction record: `SUBMARINE-ELF-RADIO-WAVE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — AM modulation figure widescreen cap

- Figure 11.5.4: reduce the AM modulation diagram to a 400 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `AM-MODULATION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Nuclear materials figure widescreen cap

- Figure 14.4.1: reduce the coal, uranium, and cesium panels to a 675 px screen width cap, constrained to available width and preserving their aspect ratio, so embedded panel labels are closer to caption size.
- Correction record: `NUCLEAR-MATERIALS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — FM modulation figure widescreen cap

- Figure 11.5.5: reduce the FM modulation diagram to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `FM-MODULATION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Antenna towers figure widescreen cap

- Figure 11.5.6: reduce the antenna-tower photos to a 300 px screen width cap, constrained to available width and preserving their aspect ratio, so embedded panel labels are closer to caption size.
- Correction record: `ANTENNA-TOWERS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Visible spectrum figure widescreen cap

- Figure 11.5.8: reduce the visible-spectrum diagram to a 575 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `VISIBLE-SPECTRUM-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Law of reflection figure widescreen cap

- Figure 11.6.1: reduce the law-of-reflection diagram to a 225 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `LAW-OF-REFLECTION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Diffuse reflection figure widescreen cap

- Figure 11.6.2: reduce the diffuse-reflection diagram to a 470 px screen width cap, approximately 75 percent of its previous 627 px width at the 380 px height cap, constrained to available width and preserving its aspect ratio.
- Correction record: `DIFFUSE-REFLECTION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Paper diffuse reflection figure widescreen cap

- Figure 11.6.3: reduce the flashlight-and-paper illustration to a 410 px screen width cap, approximately 75 percent of its previous 547 px width at the 380 px height cap, constrained to available width and preserving its aspect ratio.
- Correction record: `PAPER-DIFFUSE-REFLECTION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Mirror reflection figure width match

- Figure 11.6.4: set the mirror-reflection illustration to a 410 px screen width cap, matching Figure 11.6.3 above, constrained to available width and preserving its aspect ratio.
- Correction record: `MIRROR-REFLECTION-FIGURE-WIDTH-MATCH`.
- Pending preview refresh.

### 2026-10-17 — Rotating mirror light speed figure widescreen cap

- Figure 11.7.2: reduce the rotating-mirror diagram to a 500 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `ROTATING-MIRROR-LIGHT-SPEED-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Lawn-mower refraction figure widescreen cap

- Figure 11.7.3: reduce the lawn-mower refraction analogy to a 575 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `LAWN-MOWER-REFRACTION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Dispersion visible spectrum figure widescreen cap

- Figure 11.8.2: reduce the visible-spectrum diagram to a 575 px screen width cap, matching Figure 11.5.8, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `DISPERSION-VISIBLE-SPECTRUM-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Water-droplet rainbow figure widescreen cap

- Figure 11.8.4: reduce the water-droplet rainbow diagram to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `WATER-DROPLET-RAINBOW-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Converging lens refraction figure widescreen cap

- Figure 11.9.1: reduce the converging-lens refraction diagram to a 500 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `CONVERGING-LENS-REFRACTION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Diverging lens refraction figure widescreen cap

- Figure 11.9.3: reduce the diverging-lens refraction diagram to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `DIVERGING-LENS-REFRACTION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Light source at lens focus figure widescreen cap

- Figure 11.9.4: reduce the light-bulb and lens illustration to a 430 px screen width cap, approximately 75 percent of its previous 573 px width at the 380 px height cap, constrained to available width and preserving its aspect ratio.
- Correction record: `LIGHT-SOURCE-LENS-FOCUS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Lens ray-tracing steps figure widescreen cap

- Figure 11.9.7: reduce the ray-tracing steps diagram from 350 px to a 275 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `LENS-RAY-TRACING-STEPS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Diverging lens ray-tracing figure widescreen cap

- Figure 11.9.13: reduce the diverging-lens ray-tracing diagram to a 350 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `DIVERGING-LENS-RAY-TRACING-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Virtual image ray-tracing figure widescreen cap

- Figure 11.9.11: reduce the virtual-image ray-tracing diagram from 350 px to a 275 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `VIRTUAL-IMAGE-RAY-TRACING-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Bulb and screen ray diagram figure widescreen cap

- Figure 11.9.9: reduce the bulb-and-screen ray diagram to a 475 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `BULB-SCREEN-RAY-DIAGRAM-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Spherical mirror focus figure widescreen cap

- Figure 11.10.2: reduce the spherical-mirror focus diagram to a 550 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `SPHERICAL-MIRROR-FOCUS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Concave mirror real image figure widescreen cap

- Figure 11.10.4: reduce the concave-mirror real-image ray diagram to a 275 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `CONCAVE-MIRROR-REAL-IMAGE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Concave mirror virtual image figure widescreen cap

- Figure 11.10.6: reduce the concave-mirror virtual-image figure to a 350 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `CONCAVE-MIRROR-VIRTUAL-IMAGE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Convex mirror image figure widescreen cap

- Figure 11.10.7: reduce the convex-mirror image figure to a 275 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `CONVEX-MIRROR-IMAGE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Polarization glare comparison figure widescreen cap

- Figure 11.11.1: reduce the polarization comparison photos to a 550 px screen width cap, constrained to available width and preserving their aspect ratio, so panel labels are closer to caption size.
- Correction record: `POLARIZATION-GLARE-PHOTOS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Polarization direction figure widescreen cap

- Figure 11.11.2: reduce the polarization-direction diagram to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `POLARIZATION-DIRECTION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Rope polarization figure widescreen cap

- Figure 11.11.3: reduce the rope-polarization diagram to a 600 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `ROPE-POLARIZATION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Random polarization figure widescreen cap

- Figure 11.11.4: reduce the random-polarization diagram to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `RANDOM-POLARIZATION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Polarizing filter figure widescreen cap

- Figure 11.11.5: reduce the polarizing-filter diagram to a 475 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `POLARIZING-FILTER-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Polarization component figure widescreen cap

- Figure 11.11.7: reduce the polarization-component diagram to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `POLARIZATION-COMPONENT-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Scattering polarization figure widescreen cap

- Figure 11.11.11: reduce the scattering-polarization diagram to a 375 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `SCATTERING-POLARIZATION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — LCD polarization figure display size

- Figure 11.11.12: enlarge the LCD polarization diagram to a 300 px screen width, constrained to available width and preserving its aspect ratio, with the height cap removed so embedded labels are closer to caption size.
- Correction record: `LCD-POLARIZATION-FIGURE-DISPLAY-SIZE`.
- Pending preview refresh.

### 2026-10-17 — Optical activity figure widescreen cap

- Figure 11.11.13: reduce the optical-activity diagram to a 425 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `OPTICAL-ACTIVITY-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Birefringence figure widescreen cap

- Figure 11.11.15: reduce the birefringence diagram to a 350 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `BIREFRINGENCE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Atom and nucleus introduction figure widescreen cap

- Figure 12.1.2: reduce the atom-and-nucleus illustration to a 477 px screen width cap, approximately 60 percent of its previous 795 px width at the 380 px height cap, constrained to available width and preserving its aspect ratio.
- Correction record: `ATOM-NUCLEUS-INTRO-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Flashlight photons figure widescreen cap

- Figure 12.3.3: reduce the flashlight-and-photons diagram to a 400 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `FLASHLIGHT-PHOTONS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Photoelectron energy graph figure widescreen cap

- Figure 12.3.4: reduce the photoelectron-energy graph to a 225 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `PHOTOELECTRON-ENERGY-GRAPH-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Crossed-fields CRT figure widescreen cap

- Figure 12.6.4: reduce the crossed-fields CRT diagram to a 575 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `CROSSED-FIELDS-CRT-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Thomson CRT figure widescreen cap

- Figure 12.6.3: reduce the Thomson CRT diagram to a 400 px screen width cap, constrained to available width and preserving its aspect ratio, so charge symbols are closer to caption size.
- Correction record: `THOMSON-CRT-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Rutherford scattering figure widescreen cap

- Figure 12.6.5: reduce the Rutherford scattering diagram to a 600 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `RUTHERFORD-SCATTERING-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Gold foil atoms figure widescreen cap

- Figure 12.6.6: reduce the gold-foil atom diagram to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so its scale label is closer to caption size.
- Correction record: `GOLD-FOIL-ATOMS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Planetary atom model figure widescreen cap

- Figure 12.6.7: reduce the planetary atom diagram to a 300 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `PLANETARY-ATOM-MODEL-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Hydrogen spectrum series figure widescreen cap

- Figure 12.7.3: reduce the hydrogen-spectrum diagram to a 600 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `HYDROGEN-SPECTRUM-SERIES-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Bohr energy transition figure widescreen cap

- Figure 12.7.4: reduce the Bohr transition diagram to a 300 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `BOHR-ENERGY-TRANSITION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Hydrogen energy levels figure display size

- Figure 12.7.6: enlarge the hydrogen energy-level diagram to a 350 px screen width, constrained to available width and preserving its aspect ratio, with the height cap removed so embedded labels are closer to caption size.
- Correction record: `HYDROGEN-ENERGY-LEVELS-FIGURE-DISPLAY-SIZE`.
- Pending preview refresh.

### 2026-10-17 — Standing-wave electron orbits figure widescreen cap

- Figure 12.8.1: reduce the standing-wave orbit diagram to a 575 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `STANDING-WAVE-ELECTRON-ORBITS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Quantized orbit wavelengths figure widescreen cap

- Figure 12.8.2: reduce the quantized-orbit wavelength diagram to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `QUANTIZED-ORBIT-WAVELENGTHS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Hydrogen probability cloud figure widescreen cap

- Figure 12.8.3: reduce the hydrogen probability-cloud diagram to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `HYDROGEN-PROBABILITY-CLOUD-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Moving charged particle figure widescreen cap

- Figure 13.4.4: reduce the moving charged-particle field diagram to a 350 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `MOVING-CHARGED-PARTICLE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Spaceship laser velocities figure widescreen cap

- Figure 13.5.4: reduce the spaceship-and-laser diagram to a 350 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `SPACESHIP-LASER-VELOCITIES-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Relativistic momentum graph widescreen cap

- Figure 13.6.2: reduce the relativistic-momentum graph to a 300 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `RELATIVISTIC-MOMENTUM-GRAPH-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Sun and nuclear power station figure display size

- Figure 13.7.2: enlarge the Sun-and-power-station figure to a 375 px screen width, constrained to available width and preserving its aspect ratio, so panel labels are closer to caption size.
- Correction record: `SUN-NUCLEAR-POWER-STATION-FIGURE-DISPLAY-SIZE`.
- Pending preview refresh.

### 2026-10-17 — Relativistic kinetic energy graph widescreen cap

- Figure 13.7.3: reduce the relativistic and classical kinetic-energy graph to a 300 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `RELATIVISTIC-KINETIC-ENERGY-GRAPH-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Matter substructure figure widescreen cap

- Figure 14.1.2: reduce the matter-substructure diagram to a 650 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `MATTER-SUBSTRUCTURE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Pocket dosimeter figure widescreen cap

- Figure 14.2.3: reduce the pocket-dosimeter figure to a 400 px screen width cap, constrained to available width and preserving its aspect ratio, so panel labels are closer to caption size.
- Correction record: `POCKET-DOSIMETER-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Geiger counter figure display size

- Figure 14.3.2: enlarge the Geiger-counter figure to a 475 px screen width, constrained to available width and preserving its aspect ratio, so diagram labels are closer to caption size.
- Correction record: `GEIGER-COUNTER-FIGURE-DISPLAY-SIZE`.
- Pending preview refresh.

### 2026-10-17 — Nuclear stability chart widescreen cap

- Figure 14.4.3: reduce the nuclear-stability chart from full available width to a 425 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `NUCLEAR-STABILITY-CHART-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Nuclear decay chain figure widescreen cap

- Reduce the nuclear-decay chain chart (media `import-auto-id1825282`) from full available width to a 450 px screen width cap, constrained to available width and preserving its aspect ratio, so isotope and half-life labels are closer to caption size.
- Correction record: `NUCLEAR-DECAY-CHAIN-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Alpha decay figure widescreen cap

- Figure 14.5.2: reduce the alpha-decay diagram to a 300 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `ALPHA-DECAY-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Beta-minus decay figure widescreen cap

- Figure 14.5.4: reduce the beta-minus decay diagram to a 275 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `BETA-MINUS-DECAY-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Beta-plus decay figure widescreen cap

- Figure 14.5.5: reduce the beta-plus decay diagram to a 275 px screen width cap, matching the beta-minus diagram, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `BETA-PLUS-DECAY-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Gamma camera figure widescreen cap

- Figure 14.7.2: reduce the gamma-camera diagram to a 425 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `GAMMA-CAMERA-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Ionization density figure widescreen cap

- Figure 14.8.1: reduce the ionization-density diagram to a 600 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `IONIZATION-DENSITY-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Dental X-ray shielding figure widescreen cap

- Figure 14.8.2: reduce the dental X-ray shielding diagram to a 325 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `DENTAL-XRAY-SHIELDING-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Fusion potential energy figure widescreen cap

- Figure 14.9.3: reduce the fusion potential-energy graph to a 325 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `FUSION-POTENTIAL-ENERGY-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Fusion collisions figure widescreen cap

- Figure 14.9.4: reduce the fusion-collision diagram to a 550 px screen width cap, constrained to available width and preserving its aspect ratio, so panel labels are closer to caption size.
- Correction record: `FUSION-COLLISIONS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Solar fusion figure widescreen cap

- Figure 14.9.5: reduce the solar-fusion diagram to a 275 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `SOLAR-FUSION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Figure 14.11.1 widescreen cap

- Figure 14.11.1: reduce the image to a 350 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `NUCLEAR-WEAPONS-INTRO-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Figure 14.11.5 widescreen cap

- Figure 14.11.5: reduce the image from 350 px to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `NUCLEAR-WEAPONS-FIGURE-14-11-5-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Energy output charts widescreen cap

- Figure 14.11.6: reduce the image from 350 px to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so chart labels are closer to caption size.
- Correction record: `ENERGY-OUTPUT-CHARTS-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Virtual photon exchange figure widescreen cap

- Figure 14.12.1: reduce the virtual-photon exchange figure to a 400 px screen width cap, constrained to available width and preserving its aspect ratio, so panel labels are closer to caption size.
- Correction record: `VIRTUAL-PHOTON-EXCHANGE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Feynman photon exchange figure widescreen cap

- Figure 14.12.2: reduce the Feynman diagram to a 225 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `FEYNMAN-PHOTON-EXCHANGE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Feynman pion exchange figure widescreen cap

- Figure 14.12.3: reduce the pion-exchange diagram to a 225 px screen width cap, matching the photon-exchange diagram, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `FEYNMAN-PION-EXCHANGE-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Particle annihilation figure widescreen cap

- Figure 14.13.2: reduce the particle-annihilation diagram to a 225 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `PARTICLE-ANNIHILATION-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Particle table rest-mass header layout

- Table 14.13.1: place the rest-mass unit on a second line below the heading so the column can narrow. Preserve all table values and units.
- Correction record: `PARTICLE-TABLE-REST-MASS-HEADER-LAYOUT`.
- Pending preview refresh.

### 2026-10-17 — Weak-force Feynman figure widescreen cap

- Figure 14.14.1: reduce the weak-force Feynman diagram to a 250 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `WEAK-FORCE-FEYNMAN-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Gluon states panel (a) widescreen cap

- Figure 14.14.2(a): reduce the gluon-states panel from full available width to a 600 px width cap, constrained to available width and preserving its aspect ratio, so main labels are closer to caption size.
- Correction record: `GLUON-STATES-PANEL-A-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Gluon exchange panel (b) widescreen cap

- Figure 14.14.2(b): reduce the panel viewport from 450 px to 300 px, constrained to available width, preserving its existing crop and aspect ratio so labels are closer to caption size.
- Correction record: `GLUON-EXCHANGE-PANEL-B-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Force unification graph widescreen cap

- Figure 14.14.4: reduce the force-unification graph to a 450 px screen width cap, constrained to available width and preserving its aspect ratio, so embedded labels are closer to caption size.
- Correction record: `FORCE-UNIFICATION-GRAPH-FIGURE-WIDESCREEN-CAP`.
- Pending preview refresh.

### 2026-10-17 — Preview 182 published; website review checkpoint

- Published all queued website layout corrections since preview 181, including responsive figure sizing and the particle-table rest-mass header. Supersedes pending-preview notes in this batch.
- Both course and CNX builds passed: 6441 mathematical expressions, no reported issues, 2413 adaptations; search passages 8435/8608. Export: 757 files, 131725625 bytes.
- Sites source commit: `4195284975e9758b05ef590aa7ca8612eb481f1b`. Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_0474a71c77108191b92e50d2ed1ebad1`. Deployment: `appgdep_6ad40eeb5318819184eeeffd72c9b559` (succeeded).
- Archive SHA-256: `2f4a591daf5d4e761ce89451c4a48f8b76bd2ca672cf1a41dfcac25f1ade8074`.
- Refreshed the maintainer's existing live preview tab successfully. Final visual acceptance remains the maintainer's last preview pass.
- Main remaining work: PDF layout and production, followed by v1.1 release metadata, packaging and archival bookkeeping. Published v1.0 remains frozen.

### 2026-10-17 — Nucleus model legend sizing

- Figure 14.4.2: reduce the nucleus model to a responsive 180 px screen width so its Proton and Neutron labels approach caption text size. Preserve the image and its aspect ratio.
- Pending preview refresh; print sizing remains independent.

### 2026-10-17 — Forced oscillation diagram sizing

- Figure 5.4.2: reduce the driven paddle-ball diagram to a responsive 500 px screen width so frequency and amplitude labels approach caption size. Preserve its aspect ratio.
- Pending preview refresh; print sizing remains independent.

### 2026-10-17 — Dissimilar-wave superposition sizing

- Figure 5.6.4: reduce the superposition diagram to a responsive 275 px screen width so embedded labels approach caption size and the preceding interference figures. Preserve its aspect ratio.
- Pending preview refresh; print sizing remains independent.

### 2026-10-17 — Beats diagram sizing

- Figure 5.6.8: reduce the beats diagram to a responsive 475 px screen width so its wave, interference, and time labels approach caption size. Preserve its aspect ratio.
- Pending preview refresh; print sizing remains independent.

### 2026-10-17 — Circular-motion diagram sizing

- Figure 6.2.1: reduce the circular-motion diagram to a responsive 250 px screen width so embedded labels approach caption size. Preserve its aspect ratio.
- Pending preview refresh; print sizing remains independent.

### 2026-10-17 — Tangential-acceleration diagram sizing

- Figure 6.2.2: reduce the tangential-acceleration diagram to a responsive 200 px screen width, matching Figure 6.2.3 and bringing embedded labels toward caption size. Preserve its aspect ratio.
- Pending preview refresh; print sizing remains independent.

### 2026-10-17 — Image alternative-text review

- Reviewed 548 distinct rendered image/description pairs; inspected 70 flagged figures visually.
- Corrected 69 distinct descriptions in 70 source media elements across 50 modules, including displacement signs, standing-wave harmonics, heat-pump reservoirs, speaker labels, and relativistic-energy behavior.
- Both full build profiles pass: 573 image occurrences each, no missing or empty alt attributes, and all revised descriptions present. Source validation confirms alt-only edits and preserved IDs.
- Evidence: `reports/1.1/image-alt-audit/verification.json`; approved change: `proposals/maintainer-corrections/IMAGE-ALT-REVIEW.json`.
- Pending preview refresh. This is an editorial alt-text review, not a complete accessibility certification.

### 2026-10-17 — Preview 183 publication checkpoint

- Published the queued image sizing and alt-text corrections to https://intro-1-1.coaphys.xyz/; Sites deployment succeeded for version 183.
- Verified the corrected fundamental and overtone image descriptions in the live browser accessibility tree. Both full build profiles pass.
- Cover/title-page and publication-credits generators and the two-column thermodynamics trial are checkpointed for continued PDF authoring.

### 2026-10-17 — Chapter 0 print-layout proof

- User approved the publication/credits draft and selected two-column US Letter layout, developed one chapter at a time.
- Print rules: chapters start on recto; Section 1 is a single-page chapter opener with chapter image and compact contents; Section 2 begins on its verso; remaining sections start on fresh pages. Prefer figures at column tops and wide tables at page tops.
- Three-ring-binder margins: mirrored 1-inch inner and 0.65-inch outer margins; duplex long-edge printing. Main text 10.5 pt; opener prose 9.7 pt.
- Generated `output/pdf/v1.1-chapter-0.pdf` (18 pages) with `prototype/tools/render-chapter-zero.cjs`. Section starts: 0.1 page 1, 0.2 page 2, 0.3 page 9; review page 15; source credits page 18.
- All 18 images preserved; block-text and MathML preservation checks pass; no detected layout overflow or broken images. Canonical textbook source is unchanged. This proof awaits author review; section-ending white space and figure sizing remain adjustable.

### 2026-10-17 — Chapter 0 revised print proof and layout lessons

- Supersedes the one-page opener rule: retain the normal-size chapter image, float compact chapter contents in a corner, and let single-column introduction prose continue onto the next page. Section 0.2 begins below its end on the same page when space permits. No learning objectives belong in the chapter introduction. Later sections retain fresh-page starts.
- Schedule figures by their first prose reference, allowing modest look-ahead to place them on the same page. Prefer column corners and distribute illustrations across pages; aim to leave at least half the regular page available for prose and equations. Large tables are exceptions.
- Treat substantial optional boxes as floats. In this proof the Scientific Method occupies a full-width, single-column box atop page 7; the main prose continues uninterrupted at its former location. Keep Check Your Understanding in the prose sequence.
- Revised proof: `output/pdf/v1.1-chapter-0-revised.pdf`, 18 pages. The original proof remains available separately. Figures 0.2.3 and 0.2.4 now share page 3 with their first reference; Figures 0.2.5 and 0.2.6 occupy opposite columns on page 4.
- Verified all block text, unchanged MathML, all 18 images, Letter geometry, mirrored binder margins, and no content beyond margins. Visually reviewed all pages. This remains an author-review proof; the generated PDF and its layout do not change canonical web content.

### 2026-10-17 — Chapter 0 print punctuation and table-note revision

- Restored web inline-MathML and punctuation-group CSS in the separate print renderer. The paginator now treats these groups as indivisible when splitting paragraphs, so parentheses and trailing punctuation cannot detach at column or page boundaries. Carry this rule into subsequent chapter renderers.
- Moved table-header footnotes intact beneath their tables in 7.5 pt type. Table 0.3.2 now has a compact Value heading; the Appendix A note is below the table. Canonical web source is unchanged.
- Regenerated `output/pdf/v1.1-chapter-0-revised.pdf` (18 pages). Visually checked all pages and the three annotated cases on pages 11–12. Text, MathML, punctuation-group preservation, images, and mirrored margin checks pass. Awaiting author final acceptance before Chapter 1.

### 2026-10-17 — Chapter 0 aligned conversion and reference wrapping
- Combined the two conversion equations in maintained m67032 into an equals-aligned derivation with one Average speed label and inline m/s in the result; retained the old result anchor.
- Shared HTML rendering keeps reference labels with their numbers; web and Chapter 0 print CSS prevent wrapping, and print splitting respects these groups.
- Added print alignment for two-column MathML tables and remeasured terminal punctuation after pagination.
- Full course build: 6,440 math expressions, no issues. Chapter 0 remains 18 Letter pages, with no layout/content failures, missing images, or characters outside binding margins. Visually checked the changed reference and equation in PDF and the equation in local web output. Web preview has not been published for this pass.

### 2026-10-17 — Chapter 1 first print review
- Chapter 0 accepted by author. Chapter 1 proof uses Letter paper, mirrored 1-inch inner/.65-inch outer margins, 10.5pt body text, two columns, single-column introduction with corner contents and chapter image, and fresh-page section starts.
- Chapter 1 starts at book page 19; 39-page proof ends at 57. Reserve blank verso 58 before the next chapter in the assembled book.
- Added render-chapter-one.cjs. Preserves all 45 images and source math; chapter review contains section summaries once. Four wide equations use 8.5–9pt print sizing; two tall graph figures are enlarged to 3 inches. Source content unchanged.
- Improved print splitting between complete equation/figure blocks, kept captions with figures, retained punctuation and cross-reference rules, and recomputed punctuation positions after pagination.
- QA: no horizontal/vertical overflows, detached captions, content failures, missing images, or out-of-margin characters. 39 Letter pages. Chapter 1 awaits author review; Chapter 0 proof unchanged.

### 2026-10-17 — Chapter 1 readability revision
- Fixed column/page splitting to break only on ordinary whitespace, preserving NBSP and narrow NBSP groups. Added protected-word-group audit. Applied splitter correction to Chapter 0 renderer without regenerating its approved PDF.
- Enlarged flagged Figures 1.4.4, 1.5.5, 1.5.6, 1.5.9, 1.7.3, 1.7.5, 1.7.6, 1.8.1, and 1.8.2. Tall figures use individual widths rather than a shared height cap; four dense figures span columns at intermediate widths. Worked-example figures and captions move intact, with nearby prose below.
- Regenerated stable Chapter 1 PDF: 42 Letter pages, book pages 19–60. Next chapter can start at page 61. This supersedes the first-proof page range and blank-verso plan.
- Visual review of all pages plus detailed checks of revised figures. All 45 images preserved; mathematics, content, nonbreaking word groups, and captions pass validation. No horizontal/vertical overflows or out-of-margin characters. Source images and prose unchanged. Awaiting author review.

### 2026-10-17 — Unit 1 heading and Chapter 2 first proof
- Author accepted the Chapter 1 readability revision. Added Unit 1: Mechanics I — Motion and Forces above its chapter title, with no separate divider page. Chapter 1 remains 42 pages, book pages 19–60.
- Added render-chapter-two.cjs and generated Chapter 2: Dynamics with the same Letter, duplex binder-margin, two-column conventions. This first proof has 44 pages, book pages 61–104; the next chapter can start at 105.
- The single-column introduction retains both illustrations and its concluding note. Enlarged detailed Figures 2.2.1, 2.4.1, and 2.7.3 across columns, with nearby prose below. One wide equation uses 9pt print sizing. Source content and images unchanged.
- QA: all 35 images present; content, math, punctuation groups and nonbreaking word groups preserved; no horizontal/vertical overflows, detached captions, or out-of-margin PDF characters. Reviewed rendered pages and revised figure placements. Chapter 2 awaits author review.

### 2026-10-17 - Chapter 2 heading correction and Chapter 3 proof
- Chapter 2 accepted subject to keeping headings with following content. Updated its pagination to carry trailing headings across column/page breaks, including intervening empty elements. Verified 2.8: Friction now starts the right column with Exercise 28 on book page 101. Pagination remains 61-104 (44 pages).
- Added render-chapter-three.cjs using the corrected conventions. Chapter 3: Work and Energy begins Unit 2 with the unit heading on its opener; 28 Letter pages, book pages 105-132. The next chapter can begin at 133.
- Allowed prose inside equation containers to wrap in print, fixing an out-of-margin sentence in Example 3.2.1 without changing source mathematics or prose.
- Both PDFs pass content, math, punctuation, protected-word, image, stranded-heading, and horizontal/vertical overflow checks. PDF character bounds stay within mirrored margins. All 35 Chapter 2 and 16 Chapter 3 images retained. Rendered pages inspected; Chapter 3 awaits author review.

### 2026-10-17 - Chapter 3 review corrections and Chapters 0-2 layout audit
- Applied print-only fixes across all four chapter renderers: honor left-aligned MathML tables; insert real whitespace between glossary terms and meanings; place learning objectives first beneath section titles; reserve the opening left column for objectives and prose. Figures float to the right column, and wide figures wait for a later page rather than intervene between title and objectives.
- Chapter 3 Equation 3.5.2 now places its conservative-forces qualifier on a separate line. The source equation and mathematical tokens remain unchanged. Added explicit objective-placement and equation-label-collision audits.
- Propagated the heading/empty-element keep-together correction to earlier renderers. Chapter starts now derive from the preceding chapter report, with blank versos supplied when required.
- Regenerated all four PDFs. Chapters 0 and 1 remain pages 1-18 and 19-60. Chapter 2 is pages 61-106 (45 content pages plus blank verso 106); Chapter 3 is pages 107-134. Next chapter starts at 135. These ranges supersede the earlier proof ranges.
- QA: visually inspected every section opening, chapter review/glossary openings, and the flagged Chapter 3 equations. All 114 images retained; content, mathematics, and punctuation preserved. No objective-placement failures, equation-label collisions, reported overflows, or out-of-margin PDF characters. All pages are Letter size with mirrored binder margins. Revised PDFs await author review.

### 2026-10-17 - Bottom wide figures and Chapter 4 first proof
- Wide floats now try the remaining space beneath both columns at the end of a section before being deferred. Figure 2.2.1 and its caption fit at the bottom of book page 63, with objectives still immediately below the section title.
- Regenerated Chapter 2: 44 pages, book pages 61-104, no blank verso. Regenerated Chapter 3: 28 pages, book pages 105-132. These supersede the previous ranges.
- Prepared Chapter 4: Impulse and Momentum, using the established Letter/two-column/binder-margin rules. 19 content pages, book pages 133-151, followed by blank verso 152. Next chapter begins at 153.
- Enlarged the goalie diagram (Figure 4.6.2) across columns near its example. Three long calculations use 8.5pt print mathematics; the given-value list in Example 4.5.1 wraps between complete expressions. Source mathematics and prose unchanged.
- QA: all 8 Chapter 4 images retained; text, mathematics, punctuation groups and protected word groups preserved. No overflow, detached captions, stranded headings, objective placement failures, equation-label collisions, or out-of-margin characters. Rendered Chapter 4 pages reviewed, including the final modified example layouts. Chapter 4 awaits author review.


### 2026-10-17 - Chapter 4 final corrections and Chapter 5 first proof
- Added the missing sentence-ending period to source equation eip-844 in m71582 and rebuilt the course output. The source change is one line; Chapter 4 retains its accepted equation sizing.
- Blank verso pages now retain the running header and folio in the Chapter 4 and Chapter 5 renderers. Chapter 4 remains book pages 133-152, including the numbered blank page 152.
- Added render-chapter-five.cjs and generated Chapter 5: Oscillations and Waves with the established Letter, duplex binder margins, intro, objectives, and two-column conventions. The review proof is 36 pages, book pages 153-188 (35 content pages and a numbered blank verso). Chapter 6 can start at 189.
- Figures 5.3.1 and 5.6.5 use intermediate widths across columns; tall Figure 5.3.4 has an individual width without the general height cap. Multiple small floats can share a column, and remaining figures try available space below prose before a new page, reducing isolated figure pages.
- QA: all 39 Chapter 5 images retained; content, mathematics, punctuation groups, and nonbreaking word groups preserved. No horizontal/vertical overflow, detached captions, stranded headings, objective-placement failures, equation-label collisions, or out-of-margin PDF characters in either PDF. All pages are Letter size. Rendered page layouts and enlarged diagrams reviewed. Chapter 5 awaits author review.


### 2026-10-17 - Chapter 5 image reductions and Chapter 6 first proof
- Reduced Figures 5.3.3, 5.6.4, 5.7.2, 5.7.3, and 5.8.4 using individual print widths. Caption sizes are unchanged; wave labels match the preceding figure more closely, and the vibrating-string heights are comparable. Chapter 5 remains 36 pages, book pages 153-188.
- Prepared Chapter 6: Rotation, 28 Letter pages, book pages 189-216. Section 6.2 follows the intro continuation on page 190. Chapter 7 can begin at 217.
- Enlarged the rotational-inertia chart across columns near its first discussion, with no empty continuation box. Three slightly over-wide calculations use 9.5pt print mathematics. Reduced two oversized diagram labels through individual image sizing. No source content changes.
- QA: 39 Chapter 5 images and 25 Chapter 6 images retained. Content, math, punctuation and protected word groups preserved. No reported overflow, equation-label collisions, detached captions, stranded headings, objective-placement failures, or out-of-margin PDF characters. Rendered pages and revised figures inspected. Both PDFs await author review.


### 2026-10-17 - Chapter 6 compact table revision
- Table 6.2.1 now fits one column at the top right of book page 193 beside its prose reference. Removed the separate table page. Subsequent sections move one page earlier; content ends at 215, followed by numbered blank verso 216. Chapter 7 still begins at 217.
- Regenerated Chapter 6 and inspected the table and repaginated pages. All 25 images, source text, mathematics, punctuation groups, and protected word groups retained. No overflow, margin violations, detached captions, stranded headings, objective-placement failures, or equation-label collisions.


### 2026-10-17 - Chapter 7 first proof, completing Unit 2
- Prepared Chapter 7: Fluids with the established Letter, mirrored binder margins, two-column layout, and intro conventions. Section 7.2 begins below the short introduction on page 217. The PDF has 30 pages, book pages 217-246, including numbered blank verso 246. Unit 3 and Chapter 8 can begin at 247.
- Figures 7.6.7, 7.8.2, and 7.8.4 use wider print layouts for readable labels. Figure 7.7.1 has a smaller individual width. Equations 7.6.5 and 7.6.6 use 9pt text to clear their equation numbers. The chapter-review source note uses compact print styling to avoid an otherwise empty continuation page. Source content unchanged.
- QA: all 27 images retained; text, math, punctuation groups, and protected word groups preserved. No overflow, equation-label collisions, detached captions, stranded headings, objective-placement failures, or out-of-margin characters. Rendered pages inspected. Chapter 7 awaits author review.


### 2026-10-17 - Chapter 7 review revisions
- Section 7.2 starts on page 218: a one-page introduction always gets its own page. It continues on 219. Intro continuation pages may still share space with Section 2.
- Summary lists now split between whole list items, keeping equations with their original bullet. Glossary emphasized inline expressions stay together, including Q = V/t. Reduced Figure 7.E.3 to match body-text label sizing.
- Figure 7.8.4 follows 7.8.3 and sits across the bottom of page 240 with the Velocity measurement discussion above it. Reserved bottom space avoids a separate figure-only page.
- Chapter 7 remains 30 pages, book pages 217-246; the previous blank verso is now used by content. Chapter 8 can still start at 247. All 27 images and source text/math preserved; layout and PDF margin checks pass. Rendered revision reviewed; awaiting author review.


### 2026-10-17 - Chapter 7 Connections sidebar trial
- Tried the Section 7.2 Connections box as a 1.7-inch right-floating sidebar below the objectives, with prose wrapping alongside and beneath it. Text size and content unchanged. Narrower and wider trials also did not eliminate the continuation page.
- The retained trial reduces the spill to four lines on page 219, but Section 7.2 still occupies two pages. Chapter 7 remains pages 217-246. No other layout rules changed. Content, image, math, overflow and PDF margin checks passed; sidebar page and continuation inspected.

### 2026-10-17 - Shorter caption for Figure 7.2.1
- Shortened the maintained source caption to three panel descriptions, retaining the spring analogy and removing explanations repeated in the prose. Rebuilt web and Chapter 7 PDF.
- With the Connections sidebar retained, Section 7.2 now fits on page 218. Section 7.3 begins on 219; sources move to 245, with the usual blank verso on 246. Chapter range remains 217-246. Rendered page inspected and layout/content checks passed.

### 2026-10-17 - Chapter 7 accepted and Chapter 8 print proof
- Author accepted Chapter 7 with the normal full-column Connections box and shortened source caption. Section 7.2 fits page 218; Chapter 7 remains pages 217-246.
- Prepared Chapter 8: Thermal Physics, starting Unit 3 on page 247. The proof has 62 Letter pages, ending with numbered blank verso 308; Chapter 9 can start at 309. Uses the current objectives, margins, reference/punctuation, heading, list-splitting, and figure-placement conventions.
- Four wide equations use print-only math sizing (8-9.5pt); source mathematics and prose are unchanged. Existing multiline equations retained. Tall temperature and process diagrams enlarged individually; Otto-cycle and reactor diagrams span columns at intermediate widths. Opener contents use concise labels.
- All 54 images and 47 sequential exercises retained. Content, math, punctuation, protected-word, heading, objective, equation-label and overflow checks pass. PDF Letter geometry and mirrored margins verified. Page layouts and changed equations/figures visually reviewed. Chapter 8 awaits author review, including print readability of the longest calculation on book page 262.

### 2026-10-17 - Chapter 8 accepted and Chapter 9 print proof
- Chapter 8 accepted after reducing Figure 8.13.2 to 2.45 inches. Chapter 8 remains pages 247-308.
- Prepared Chapter 9: Electricity, 56 Letter pages, book pages 309-364, including numbered blank verso 364. Chapter 10 can start at 365. Established layout conventions retained; source text and mathematics unchanged.
- Two Coulomb-law calculations use 9.5pt and 8.5pt print math. Xerography and parallel-circuit diagrams use intermediate widths across columns; the Van de Graaff diagram is enlarged and several oversized labels reduced through individual image sizing. Tightened paragraph/equation spacing in Example 9.6.3 to avoid a three-line continuation page, retaining body font size.
- All 50 images and 55 sequential exercises retained. Content, math, punctuation, protected-word, heading, objective, equation-label and overflow checks pass; PDF Letter geometry and mirrored margins verified. Rendered layouts and changed equations/figures inspected. Chapter 9 awaits author review.

### 2026-10-17 - Chapter 9 review revision
- Started Section 9.2 on page 311; subsequent sections through 9.7 retain their starts. Reduced Figures 9.4.1, 9.5.3, 9.8.1, and 9.11.1; enlarged 9.5.4 to coordinate charge labels. Captions unchanged.
- Corrected six padded variable tokens and the combined minus-W token in maintained m75427. Audited all ten W occurrences; rebuilt web output with no build issues.
- Deferred the full-column Misconception box in 9.7 so following prose fills earlier gaps, retaining figure order and no side wrapping. Chapter 9 now has 54 pages, book pages 309-362.
- All 50 images and 55 sequential exercises retained; layout/content/math checks and PDF margin checks pass. Changed layouts visually inspected. Revised proof awaits author review.


### 2026-10-18 - Chapter 9 accepted and Chapter 10 print proof
- Author accepted the revised Chapter 9, pages 309-362. Prepared Chapter 10: Magnetism, continuing Unit 3 on page 363. The proof has 38 Letter pages through 400, including a numbered blank verso; Chapter 11 can begin on 401.
- Retained established section starts, objectives placement, mirrored margins, figure placement, and math/punctuation conventions. Existing multiline equations fit without additional math shrinking; source text and mathematics unchanged. Moved the exercise source note into Sources and adaptations to avoid an isolated provenance page.
- All 45 images and 46 sequential exercises retained. Content, math, punctuation, protected-word, heading, objective, equation-label and overflow checks pass. PDF Letter geometry and mirrored margins verified; rendered page layouts and calculation detail inspected. Chapter 10 awaits author review.


### 2026-10-18 - Chapter 10 review revision
- Started Section 10.2 below the introduction on page 364 and reduced its four figures; the section now ends on 365 and Section 10.3 begins on 366.
- Reduced Figures 10.12.1-3 for label sizing and Figures 10.E.2-3 to coordinate with 10.E.1. Captions and source content unchanged.
- Revised proof is 36 pages, book pages 363-398, with no blank final verso. All 45 images and 46 sequential exercises retained; layout, content, math and PDF margin checks pass. Changed figure layouts visually inspected; awaiting author review.


### 2026-10-18 - Chapter 10 accepted and Chapter 11 print proof
- Author accepted Chapter 10, pages 363-398. Prepared Chapter 11: Light, the last chapter of Unit 3, beginning on page 399. The proof has 66 Letter pages through numbered blank verso 464; Chapter 12 can begin on 465.
- Retained established objectives, margins, heading, list, punctuation, and intro-continuation conventions. Spectrum charts span both columns; selected dense ray diagrams are enlarged and oversized diagram labels reduced with individual print sizing. Two equations use print-only sizing at 8.5pt and 9.5pt. Source text, mathematics, and captions unchanged.
- All 75 images and 57 sequential exercises retained. Content, math, punctuation, protected-word, heading, objective, equation-label and overflow checks pass; PDF Letter geometry and mirrored margins verified. Rendered page layouts, spectrum charts, and adjusted equations reviewed. Chapter 11 awaits author review.


### 2026-10-18 - Chapter 11 review revision
- Table 11.7.1 now fits one column. Enlarged Figure 11.8.5; reduced Figures 11.9.3 and 11.9.4 with coordinated lens scale. Captions unchanged.
- Reserved bottom space on page 438 for Table 11.9.1 and reflowed the last lens page, modestly tightening equation/paragraph spacing in Example 11.9.4 while retaining its font sizes. The experiment box also fits, removing the isolated table page.
- Figure 11.11.6 now spans both columns. Adjusted the polarization float queue and note splitting to retain figure order and let text use available space.
- Revised proof: 64 pages, book pages 399-462, including numbered blank verso 462. All 75 images and 57 exercises retained. Content, math, layout and PDF margin checks pass; revised tables, diagrams and polarization flow visually reviewed. Awaiting author review.


### 2026-10-18 - Chapter 11 second review revision
- Reduced Figure 11.5.10 and allowed its note to split, keeping the image and caption at the bottom left of page 417. Example 11.7.1 now begins on page 423 before the independently placed table. Shortened the maintained Figure 11.7.3 caption to preserve the lawnmower analogy, bending directions and reversibility without repeating the prose; web build passed (6440 math expressions, no issues). Refraction still ends on 425 with the take-home experiment.
- Enlarged Figure 11.8.5 to a 5.5-inch height limit and placed the remaining prose at the top of the right column below the table.
- Reserved the opening polarization page bottom-right for Figure 11.11.3. Stacked Figures 11.11.4 and 11.11.5 at the next page upper-left and reduced Figure 11.11.4. Main narrative flows ahead of the independent atomic-explanation box; its Figures 11.11.9-10 remain with the box, which now follows the main section prose.
- Revised proof remains 64 pages, book pages 399-462, with numbered blank verso 462. All 75 images and 57 exercises retained. Content, math, layout and PDF margin checks pass; affected layouts visually reviewed. Awaiting author review.


### 2026-10-18 - Chapter 11 third review revision
- Placed Figure 11.7.3 below the one-column refraction table with a 2.4-inch image width limit. All remaining Refraction prose and the take-home experiment now fit on page 424; Section 11.8 begins on 425.
- Liquid Crystals and Other Polarization Effects in Materials starts on a new page (447), following the figures at its top. The atomic-explanation box starts in the right column of page 448 below Figure 11.11.15 and continues on 449.
- Revised proof: 62 pages, book pages 399-460. All 75 images and 57 sequential exercises retained. Content, math, layout, Letter geometry and mirrored-margin checks pass; affected layouts visually reviewed. Awaiting author review.


### 2026-10-18 - Chapter 11 final polarization revision
- On page 446 (PDF page 48), reserved the right column below wide Figure 11.11.6 for Figures 11.11.7 and 11.11.8 in that order. Reduced Figure 11.11.7 to a 2.2-inch width limit. Remaining prose and the complete take-home experiment fit on the left; later figures stay on subsequent pages.
- Full revised chapter remains 62 pages, book pages 399-460. All 75 images and 57 sequential exercises retained. Content, mathematics, layout, page geometry and margin checks passed; revised page and subsequent flow visually reviewed. User requested finalization with this change.


### 2026-10-18 - Chapter 11 accepted and Chapter 12 print proof
- Author accepted Chapter 11, book pages 399-460. Added render-chapter-twelve.cjs and prepared Chapter 12: Quantum Mechanics with the Unit 4 Modern Physics heading on its opener. Proof: 34 Letter pages, book pages 461-494, including numbered blank verso 494; Chapter 13 can begin at 495.
- Preserved the established duplex margins, objectives, introduction, punctuation, math splitting and review conventions. Blackbody Radiation starts on a fresh page after the two-page introduction. One wide blackbody calculation uses 9.5pt print math. Source text and mathematics unchanged.
- Enlarged the SEM, Rutherford-scattering, hydrogen-spectrum and matter-wave diagrams across columns at individual widths. Kept figure order while allowing prose to flow beneath wide figures. Adjusted selected Bohr diagrams and the probability-cloud figure; placed the Bohr summary table in one column and slightly tightened paragraph/equation spacing in that section, retaining font sizes and eliminating an isolated final paragraph page.
- All 29 images and 56 sequential exercises retained. Content, math, punctuation, protected-word, heading, objective, equation-label and overflow checks passed. PDF Letter geometry and mirrored margins verified; page layouts and adjusted figures, table and equations visually reviewed. Chapter 12 awaits author review.


### 2026-10-18 - Chapter 12 figure revision and Chapter 13 print proof
- Rebuilt Chapter 12 with Figures 12.3.4, 12.6.6 and 12.8.2 limited to 2.5-inch widths. Captions unchanged. Pagination remains 34 pages, book pages 461-494, and every section start is unchanged. All 29 images and 56 sequential exercises retained; adjusted pages visually reviewed and full checks passed.
- Added render-chapter-thirteen.cjs and prepared Chapter 13: Special Relativity, continuing Unit 4 without a repeated unit heading. Proof: 38 Letter pages, book pages 495-532, including numbered blank verso 532. Chapter 14 can begin at 533.
- Retained established duplex margins, objectives, introduction flow, math/punctuation protection and figure-order conventions. Enlarged the space-time diagram within its column and the light-clock and muon length-contraction diagrams across columns for label readability. Existing multiline mathematics fit without extra print font reductions. Source text and mathematics unchanged.
- All 24 images and 39 sequential exercises retained. Content, math, punctuation, protected-word, heading, objective, equation-label and overflow checks passed. PDF Letter geometry and mirrored margins verified. Chapter 13 layouts and adjusted diagrams visually reviewed; awaiting author review.


### 2026-10-18 - Chapters 12 and 13 accepted; Chapter 14 print proof
- Author accepted Chapters 12 and 13. Added render-chapter-fourteen.cjs and prepared Chapter 14: Nuclear and Particle Physics, continuing Unit 4. Proof: 76 Letter pages, book pages 533-608, including numbered blank verso 608. Whole-book assembly remains separate.
- Retained duplex margins, objectives, figure order, review conventions and protected math/punctuation. Enlarged selected nuclear charts and diagrams for readability, used wide figures where needed, and placed compact radiation tables in one column. Adjusted the particle table spacing to retain all notes and modestly tightened Fusion/Fission paragraph spacing.
- Moved the electron-capture prose qualifier onto its own print line and reduced selected long calculations to fit their columns. Source text and mathematics unchanged.
- All 59 images and 70 sequential exercises retained. Content, mathematics, punctuation, protected-word, heading, objective, equation-label and overflow checks passed. PDF Letter geometry and mirrored margins verified; rendered layouts and corrected equations visually reviewed. Chapter 14 awaits author review.


### 2026-10-18 - Chapter 14 beta-decay figure pairing
- Scheduled Figure 14.5.5 together with Figure 14.5.4, placing it immediately below that figure in the right column of book page 547. Figure sizes and captions unchanged.
- Rebuilt proof: 74 pages, book pages 533-606. Content and math checks, PDF margins, and all 70 exercise numbers pass. Paired diagrams visually reviewed; author review continues.


### 2026-10-18 - Chapter 14 embedded-figure paragraph repair
- Fixed print flattening of paragraphs containing figures: the previous child-element traversal discarded plain text nodes while retaining formatted terms. The beta-plus paragraph on page 548 is restored in full. Applied the text-preserving extraction to all such Chapter 14 paragraphs and added an explicit text-integrity assertion before pagination; prior content audits began too late to detect this loss.
- Rebuilt proof: 76 pages, book pages 533-608. Beta-decay figure pairing retained. Rendered restored paragraph reviewed; content/math checks, PDF margins and all 70 exercise numbers pass.


### 2026-10-18 - Whole-book embedded-figure prose audit
- Audited all 15 chapter print outputs (Chapters 0-14) against current book and review sources. Checked 33 embedded-figure paragraph occurrences and 60 adjacent paragraphs, reassembling split print blocks by audit key to avoid false positives from intervening floats. No additional missing prose found. Only the previously repaired Chapter 14 beta-plus paragraph contains prose outside its embedded figure; all other embedded-figure wrappers contain figures alone.
- Applied the text-preserving embedded-figure extraction and pre-pagination integrity assertion to all earlier chapter renderers and the Chapter 10 flow-trial renderer. No earlier PDF rebuild was needed: the affected structure has no surrounding prose in those sources, so their existing output is unchanged.
- Added audit_embedded_figure_prose.py and check-embedded-figure-prose.cjs. Browser regression checks passed for all 16 renderers, each using the 31 current source wrappers plus a two-figure fixture with plain and formatted prose before, between and after the figures. Reports: reports/1.1/embedded-figure-prose-audit.json and embedded-figure-regression.json.


### 2026-10-18 - Chapter 14 Example 14.5.2 continuation
- Allowed the split-point search for Example 14.5.2 to continue beyond a heading candidate that fits geometrically, rather than prematurely treating that heading as the column height limit. The full Solution now follows Strategy and Concept in the left column of page 548; Discussion and Implications begins at the top right.
- Section 14.5 ends one page earlier, on 549; Section 14.6 begins on 550. Revised chapter: 74 pages, book pages 533-606, with the previously blank final verso no longer needed. Source content unchanged. Rendered example reviewed; content, math, layout, margin and 70-exercise sequence checks pass.


### 2026-10-18 - Chapter 14 acute-exposure table placement
- Floated Table 14.8.3 to the top of the right column on book page 561, above the continuing paragraph. The prose now runs continuously below the table. Content, captions and table dimensions unchanged.
- Chapter remains 74 pages, book pages 533-606. Content, mathematics and layout checks pass; revised page visually reviewed and PDF margins checked.


### 2026-10-18 - Chapter 14 diagnostic-dose table and reaction-energy spacing
- Moved Table 14.8.5 to the upper-right column of book page 564, allowing Risk versus Benefit to finish uninterrupted on the left.
- Added a 12pt gap between reaction equations and their separate Q values through the reaction-energy print class, including all ten fusion reactions, repeated review equations and the two matching fission equations. Long pairs can wrap the Q value to a second line without changing mathematics or font sizes.
- Rebuilt proof remains 74 pages, book pages 533-606. Revised table and fusion pages visually reviewed; content/math, overflow, equation-label, margin and 70-exercise sequence checks pass.


### 2026-10-18 - Chapter 14 energy-output chart enlargement
- Increased Figure 14.11.6's print height limit from 4 to 6.4 inches within its existing column, bringing its internal labels closer to body-text size. Caption unchanged; following prose reflows onto the next page.
- Chapter remains 74 pages, book pages 533-606. Enlarged chart visually reviewed; content/math/layout checks and affected PDF page margins pass.


### 2026-10-18 - Chapter 14 annihilation diagram reduction
- Limited Figure 14.13.2 to 2.4 inches wide, bringing its internal labels close to body-text size. Caption unchanged. Revised figure on page 583 visually reviewed.
- Chapter remains 74 pages, book pages 533-606. Content, math and layout checks pass; affected section PDF margins checked.


### 2026-10-18 - Chapter 14 particle-table page
- Reserved book page 584 for Table 14.13.1 and its notes. The short prose continuation previously below the table now starts on page 585, with subsequent text flowing normally.
- Chapter remains 74 pages, book pages 533-606. Table and following page visually reviewed; content/math/layout checks and affected PDF margins pass.


### 2026-10-18 - Chapter 14 revised gluon figure assembly
- Restored the existing web-layout viewport crop in the Chapter 14 print CSS so Figure 14.14.2 shows only panel (b) of the old image. The old panel (a) is no longer visible; original image pixels remain intact.
- Reduced replacement panel (a) from 5.8 to 4 inches wide, centered its separate label, and set the cropped panel (b) viewport to 2.6 inches wide. Caption unchanged.
- Figure assembly on book page 589 visually reviewed. Chapter remains 74 pages, book pages 533-606; content/math/layout checks and affected PDF margins pass.


### 2026-10-18 - Chapter 14 final review rebuild
- Replaced the three mfenced decay-symbol expressions in maintained m76603 with explicit non-stretching parentheses. Grouped the signed +1 in all three matching baryon-number expressions in maintained m42674. Recorded source snapshots and hashes in CH14-INLINE-MATH-SPACING proposals; no values or prose changed.
- Full course build passed: 6440 math expressions, zero issues. Rebuilt Chapter 14 with all accumulated figure, table, flow, spacing and source corrections: 74 pages, book pages 533-606; 59 images and 70 sequential exercises retained.
- Full layout/content/math checks, Letter geometry, mirrored PDF margins and exercise sequence passed. Re-ran the whole-book embedded-figure audit: no missing prose in 33 embedded-figure paragraphs or 60 adjacent paragraphs. Corrected source expressions visually reviewed in the final PDF. Delivered for final author acceptance.


### 2026-10-18 - Book-wide definition styling and activity-unit source corrections
- Added bold, upright dfn styling to all chapter print renderers (including the Chapter 10 trial), matching the web treatment. Rebuilt Chapters 0-14 in order; Chapter 0 retains its established v1.1-chapter-0-revised.pdf output. Ordinary emphasis markup remains unchanged.
- Normalized the Bq definition (body and review) and MBq-to-microcuries conversion in maintained m52471: explicit numbers, upright units including microcurie prefix, consistent number-unit spacing and relation spacing. Saved before/after source snapshots and hashes in CH14-ACTIVITY-UNIT-SPACING-m52471.json. Full course build: 6440 expressions, zero issues.
- All chapter page counts and section starts remain unchanged. Chapter 14 remains 74 pages, book pages 533-606. All 15 PDFs pass layout, content/math, page geometry, mirrored-margin and exercise-sequence checks. Whole-book embedded-figure audit again passes. Representative term styling and the revised activity expressions visually reviewed; no earlier-chapter author re-review required by these checks.
- Reports: definition-style-before.json, definition-style-pagination.json and definition-style-pdf-check.json under reports/1.1. Chapter 14 review continues.


### 2026-10-18 - Chapter 14 boson-list punctuation spacing
- Corrected the source MathML comma between W-plus and W-minus from an identifier to a separator with zero leading space and 0.25em trailing space; removed the empty identifier. Saved source snapshots/hashes in CH14-BOSON-LIST-SPACING-m42680.json.
- Full course build passed with 6440 expressions and zero issues. Rebuilt Chapter 14 remains 74 pages, book pages 533-606. Corrected list on page 588 visually reviewed; content/math/layout checks and affected PDF margins pass.

## October 18, 2026 - Appendix A print proof

- Added `prototype/tools/render-appendix-a.cjs`, using the current maintained Atomic Masses module (m42699) from the full course build.
- Produced `output/pdf/v1.1-appendix-a.pdf`: six Letter pages, book pages 607-612, following the accepted Chapter 14 pagination.
- Full-width table repeats its caption/header; all 161 isotope/state rows remain in order and all 110 element groups stay together. No scientific data or source prose changed.
- Table notes and source attribution remain on the final page. Existing chapter credits and chapter pagination are unchanged.
- Checked all six rendered pages visually. DOM comparison preserves every table row; cell overflow checks and PDF mirrored-margin checks pass. Reports: `reports/1.1/appendix-a-print/layout.json` and `pdf-check.json`.
- Status: Appendix A PDF ready for user review; whole-book assembly and remaining appendices are separate work.

## October 18, 2026 - Appendix B print proof

- Appendix A accepted by the user.
- Added `prototype/tools/render-appendix-b.cjs` using maintained module m42702 from the current full course build.
- Produced `output/pdf/v1.1-appendix-b.pdf`: content on book pages 613-615, with a blank verso at 616 to keep Appendix C on a recto.
- Preserved all 70 emission rows for 38 isotopes, all introductory prose, source notes, attribution, and table MathML. Isotope groups stay together and table headers repeat.
- Visually checked all four pages. Cell overflow, Letter geometry, mirrored margins, source-prose preservation, and table MathML comparisons pass. Reports: `reports/1.1/appendix-b-print/layout.json` and `pdf-check.json`.
- Ready for user review; earlier PDFs and scientific source data unchanged.

### Appendix B beta-sign correction

- Replaced baseline beta-minus and positron-emission signs in the introductory paragraph with MathML superscripts in maintained module m42702. Source snapshot and hashes: `reports/1.1/appendix-b-print/beta-signs-source.json`.
- Full course build passed (6,442 expressions, no issues); rebuilt Appendix B and visually verified the corrected first page. Pagination and row distribution unchanged: pages 613-616, 70 rows in 38 intact groups.

## October 18, 2026 - Appendix C print proof

- Appendix B accepted by the user after the beta-sign correction.
- Added `prototype/tools/render-appendix-c.cjs`, using maintained module m78798 from the current full course build.
- Produced `output/pdf/v1.1-appendix-c.pdf`: content on book pages 617-621, blank verso at 622. All nine reference tables remain intact; Useful Formulae and source attribution share the final content page.
- Preserved all 98 table body rows, all source prose, notes, and MathML. No scientific source edits.
- Visually reviewed the rendered layout; cell-overflow, source-content, MathML, Letter geometry, and mirrored-margin checks pass. Reports: `reports/1.1/appendix-c-print/layout.json` and `pdf-check.json`.
- Ready for user review. Earlier PDF pagination remains unchanged.

## October 18, 2026 - Appendix D print proof

- Appendix C accepted by the user.
- Added `prototype/tools/render-appendix-d.cjs`, using maintained symbol glossary module m42709 from the current full course build.
- Produced `output/pdf/v1.1-appendix-d.pdf`: content on book pages 623-631, blank verso at 632. Repeated column headers; all 273 entries remain intact and in source order. Source credits fit on the final content page.
- Preserved table content, MathML, introductory prose, and attribution. No scientific source edits.
- Visually checked all ten pages; cell overflow, source preservation, MathML, Letter geometry, and mirrored-margin checks pass. Reports: `reports/1.1/appendix-d-print/layout.json` and `pdf-check.json`.
- Ready for user review; earlier PDF pagination unchanged.

## October 18, 2026 - Subject index print proof

- Appendix D accepted by the user.
- Built `output/pdf/v1.1-index.pdf`: eight pages, book pages 633-640. Earlier accepted PDFs are unchanged.
- Index contains 624 alphabetized entries: marked key terms, all 498 unique chapter glossary terms, major section topics, appendix reference tables, and 16 explicit see cross-references. Straightforward variants are consolidated through the reviewable `prototype/tools/print-index-editorial.json` mapping. Definitions themselves are not repeated.
- Page references derive from accepted explicit-page print HTML, with matching folios and PDF page counts checked across all 632 source pages. Every source term/reference string was independently found on its assigned PDF page; zero unresolved glossary terms or page-text mismatches.
- Standalone page links use relative PDF GoToR destinations to the adjacent chapter/appendix files. Keep those files together to use the links. The whole-book assembly must convert these to internal destinations using `reports/1.1/index-print/link-manifest.json`; it must also adjust the index's standalone-specific introductory sentence. This is not yet a whole-book assembly.
- Tools: `build-print-index.py`, `render-print-index.cjs`, `link-print-index.py`, `check-print-index.py` in `prototype/tools/`.
- Visually reviewed all eight pages. Verified all 624 rendered entries, 1,109 page-link destinations, 18 internal cross-reference annotation rectangles (16 cross-references, two wrapped), mirrored margins, and Letter geometry. Evidence in `reports/1.1/index-print/`.
- Ready for user review. Next end-matter item remains book-wide licensing/attribution; retain existing chapter credits as agreed.

## October 18, 2026 - Book-wide licensing and attribution proof

- Index accepted by the user.
- Added `prototype/print-content/book-wide-licensing.html` and `prototype/tools/render-book-licensing.cjs`; produced `output/pdf/v1.1-licensing-attribution.pdf`, book pages 641-642.
- Explicit copyright notice: Copyright 2018-2026 Andrew Park, covering the collection and original adaptations and revisions; upstream copyright notices retained. Book-wide CC BY 4.0 statement, reuse summary, suggested attribution, item-specific credit guidance, and source/adaptation history included.
- User clarified that omitting self-credit concerns item-level credit such as images, not book-wide authorship/copyright. Updated the scope and authorization text in `metadata/public-attribution.json`; retained its existing item-level omission list. Do not omit Andrew Park from book-wide copyright or adaptation attribution.
- Sources: current preface, public-attribution metadata, publication policy, license-source audit, and pinned CC BY reference documentation. License summary checked against the official CC BY 4.0 deed. No blanket claim is made about differently licensed individual items.
- Existing chapter and appendix credits and pagination unchanged. Source history includes OpenStax/Rice University, Bobby Bailey, James Rittenbach, Andrew Park, and the credited University Physics Carnot passage.
- Both pages visually reviewed; source-to-PDF text, mirrored margins, and six link annotations pass. Reports in `reports/1.1/book-licensing-print/`. Ready for user review; full-book assembly remains pending.

## October 18, 2026 - Copyright page proof

- Added `prototype/print-content/copyright-page.html` and `prototype/tools/render-copyright-page.cjs`; generated `output/pdf/v1.1-copyright-page.pdf`.
- One page, designed for the verso after the existing title page, without a visible folio. Final front-matter numbering is deferred to assembly.
- Reuses the approved 2018-2026 Andrew Park copyright assertion, CC BY 4.0 statement, and upstream attribution; includes website/repository links and a reference to detailed licensing on book pages 641-642.
- Existing cover/title PDF, approved chapters, appendices, index, and end-matter pagination unchanged.
- Rendered and visually checked. Full source text, Letter geometry, verso margins, and three link annotations pass; evidence in `reports/1.1/copyright-page-print/`. Ready for user review.

## October 18, 2026 - Contents and preface proof

- Copyright page accepted. User authorized laying out TOC and preface together and iterating their Roman pagination.
- Produced `output/pdf/v1.1-toc-and-preface.pdf`: eight pages, TOC iii-viii and preface ix-x. Title and copyright count as i-ii with suppressed folios; cover excluded. Body remains Arabic 1-642.
- Preface uses maintained m67030 wording unchanged: Version 1.1 introduction on ix; historical prefaces, About OpenStax College, and source credit together on x. Historical page uses 10-point text to retain the credits on the same page.
- TOC includes all 15 chapters, 166 section/review/credit rows, appendices A-D, index, and licensing. Units preserved. All 166 section titles verified against their target PDF pages. Pagination stabilized after two passes.
- Tools: `build-front-matter-data.py`, `render-front-matter.cjs`, `link-front-matter.py`, and `check-front-matter.py` in `prototype/tools/`.
- Verified 187 body-page link annotations, five internal preface links, nine external links, full source-text preservation, Letter geometry, and mirrored margins. All eight pages visually reviewed; reports in `reports/1.1/front-matter-print/`.
- Standalone proof links to adjacent PDFs. Assembly must convert GoToR actions to internal destinations using `link-manifest.json` and retain internal preface destinations. Full-book assembly is still pending; no accepted PDF components were changed.
- Ready for user review.

### Preface section links for whole-book assembly

- User confirmed that the five section titles in the Version 1.1 preface must become internal full-book links.
- Verified source anchors: Einstein's Postulate `#m42528` -> body page 496; Biological Effects of Ionizing Radiation `#m68327` -> 559; Uncertainty Principle `#m67804` -> 472; Statistical Interpretation of Entropy `#m42238` -> 294; GUTs: The Unification of Forces `#m42680` -> 588.
- These fragment targets are outside the standalone TOC/preface document, so Chrome omits their PDF annotations. During assembly, explicitly create their internal link annotations from the preface DOM link rectangles (or render them first as resolvable body placeholders and remap). Converting existing GoToR links alone is insufficient. Verify all five in the assembled PDF.

## October 18, 2026 - Complete book review PDF

- User approved the contents and preface and authorized full-book assembly.
- Produced `output/pdf/v1.1-complete-book.pdf`: 654 physical pages, including cover and blank cover verso, Roman i-x, and Arabic 1-642. Title/copyright folios remain suppressed. The blank cover verso preserves recto/verso parity.
- Added 202 hierarchical bookmarks and 2,615 internal link annotations (2,455 logical source links), including contents, index, cross-chapter references, and all five requested preface section links. Retained 775 external link annotations. No unresolved source links or remote-PDF actions remain.
- Approved chapter and appendix PDFs were reused. All 653 imported pages retain identical content streams and extracted text to their assembly components; the additional page is blank. The assembled index alone uses a revised introductory sentence describing within-book navigation, with unchanged pagination.
- Reopened the saved PDF and verified all link and bookmark destinations and Roman/Arabic page labels. Rendered and visually checked cover/title, copyright, TOC, both preface pages, body opening, index opening, and both licensing pages.
- Assembly tools: `prepare-book-assembly.py`, `extract-book-links.cjs`, and `assemble-full-book.py`. `render-print-index.cjs` supports a separate BOOK_ASSEMBLY variant without replacing the approved standalone index.
- Evidence: `reports/1.1/full-book/components.json`, `assembly-check.json`, `saved-pdf-check.json`, DOM link geometry, and rendered review samples. Full-book proof is ready for user review; no publication or commit performed.

## October 18, 2026 - Screen-optimized complete PDF

- User approved the complete book and requested a separate smaller PDF suitable for screen reading through 200% zoom, retaining the original.
- Created `output/pdf/v1.1-complete-book-screen.pdf`: 68,732,028 bytes (68.7 MB), down from 123,666,314 bytes (123.7 MB), a 44.4% reduction. The full-resolution original is unchanged (SHA-256 verified).
- Conservative image-only optimization: preserve every image's pixel dimensions; use lossless PNG prediction or high-quality JPEG without chroma subsampling when smaller. Strict decoded-pixel error bounds for diagrams and mixed figures; separately reviewed photographic images use a photographic threshold. Keep original image streams when candidates do not qualify. No downsampling, text rasterization, repagination, or source edits.
- Text/vector page content streams, all link annotations, bookmark hierarchy, page labels and page geometry match the original across all 654 pages.
- Rendered 12 representative/worst-error/large-savings sample pages at 192 dpi (200% at 96-dpi screen scale) and visually compared image crops, including fine lines, small labels, photos, quantum orbit diagrams and the gluon figure. No conspicuous additional loss observed in these samples; ready for user review.
- Tools: `prototype/tools/optimize-screen-pdf.py`, `prototype/tools/check-screen-pdf.py`. Evidence and comparisons: `reports/1.1/screen-pdf/`. This remains a review candidate, not a published replacement.
