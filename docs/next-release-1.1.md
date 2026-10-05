# cp2e-ver1.1 planning

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
`n- Preview version 23 published: pending Exercise 25 wording and tape-question removal are now live; 39 Chapter 2 exercises. Continue batching future edits until requested refresh or chapter completion.

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
