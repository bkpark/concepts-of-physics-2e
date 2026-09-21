# cp2e-ver1.1 planning

## Current status and remaining work

The scoped CC BY upstream comparison/backport pass is complete: all 140 mapped sections have recorded dispositions, with zero unresolved comparison differences. The local Preface has no upstream counterpart. Published 1.0 remains frozen.

The first focused factual-review cycle is applied (September 20, 2026): **35 approved items (FC01–FC34 plus FC28b)**, bringing the maintained corpus to 203 editorial records. The updated preview is at http://127.0.0.1:8765/course-full/; before/approved comparisons remain at http://127.0.0.1:8765/review-1.1/fact-check-review/. Application records, source hashes and factual references are in the editorial ledger and proposals/1.1/fact-check.json. This does not certify all textbook claims. The next cycle will address remaining radiation/medical and electrical-safety claims first, then tables and summaries, conceptual qualifications, and historical/current-technology leads. See proposals/1.1/fact-check-followups.json. Start that cycle when the author returns; it is not a scheduled/background task.

The author is updating MyOpenMath assessment settings to reference the **published 1.0** section links and will provide a fresh export for the conceptual exercise revision. The export is not a dependency for factual review. No course settings or published website files are changed by this work.

Work order approved by the author:

1. **Immediate next task: focused factual audit.** Independently check historical dates, discovery/attribution and Nobel claims; medical, environmental and safety claims; constants, definitions and potentially outdated assertions. Produce a source-linked, side-by-side review packet with minimal proposed corrections. Separate confirmed errors from uncertainty and broader editorial preferences. Preserve existing prose where possible; substantial rewriting remains author-led. Agreement with upstream is not evidence of independent verification. This is the next work item, not a timed/background automation.
2. **Conceptual chapter-end exercise revision.** Request an up-to-date MyOpenMath export for this project when starting the exercise pilot. Inventory provenance and suitability, develop an author-review pilot, then extend across chapters. Resolve explicitly deferred exercise issues and review answer/solution policy. Keep ordinary PDF exercises at chapter ends and Check Your Understanding inline.
3. **Website exercise placement and publication artwork/front matter.** Near the end of content work, resolve the reported duplicate ordinary exercises at section ends: display them only in the chapter-end collection in static HTML as well as PDF. Keep Check Your Understanding inline. Add a website favicon. Present optional simple PDF cover and reusable front matter for author review; see scope below.
4. **Equation-copy interface (last feature task).** Assess LaTeX as the useful primary copy format and AsciiMath where faithful; provide explicit handling of unsupported constructs. Preserve canonical MathML and symbol-level selection. See the detailed scope below.
5. **Release-candidate build and verification.** Generate fresh 1.1 PDF and static HTML; verify equations, figures/tables, cross-references, exercise placement, numbering, stable URLs/anchors, accessibility and page layout. Retain support for both numbering profiles while prioritizing lecture-aligned presentation.
6. **Release and archival bookkeeping.** Finalize substantive change log, attribution/provenance, 1.1 metadata and filenames; package the website and linked PDF with crawler rules; record checksums, reproducible build instructions, Git tag/release assets and publication handoff. Preserve all 1.0 artifacts and tags. Do not publish an unreviewed release candidate.

Before producing release artifacts, deliberately prepare metadata/release.json for cp2e-ver1.1 with new filenames, candidate status, and artifacts_frozen=false. Do not repurpose the 1.0 output directory.

Broader prose/pedagogy revisions, plasma coverage decisions and the author's careful full-book read-through remain planned for the interval between 1.1 and 1.2.

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
