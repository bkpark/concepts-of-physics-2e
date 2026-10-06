# Exercise revision for 1.1: proposed action plan

Prepared September 27, 2026 from the maintainer's fresh MyOpenMath export and the recovered exercise-curation audit. This is a proposal, not approval of individual question additions or removals.

## What the export provides

The export contains 105 assessments, 1,642 question-instance records and 1,012 question definitions. Pool members and repeated assignment uses are not 1,642 distinct exercises, and multipart definitions can contain several prompts. The file is JSON containing question source and configuration; no code was executed.

| Role, determined from course organization | Assessments | Distinct definitions within role |
|---|---:|---:|
| Lecture comprehension | 30 | 166 |
| Weekly homework | 12 | 296 |
| Weekly spot-check assessments | 12 | 293 |
| Timed multiple-choice | 12 | 379 |
| Timed essay | 13 | 55 |
| Explicitly unused final-exam folder | 1 | 4 |
| Explicitly archived content | 25 | 448 |

These definition counts overlap between roles and must not be added. Folder placement identifies intended course roles, not proof of individual student usage. All referenced question-set records resolve. Definition types are 472 choices, 216 multipart, 171 essay, 79 multiple-answer, 40 matching, 32 number and 2 string. A multipart lecture question often mixes a quotation blank with conceptual choices; the type alone cannot determine suitability.

The original export is preserved outside the publishing repository in `../reference-inputs/phys-10-full-export-2026-09-27.imas`. Its checksum and a metadata-only inventory are in `reports/1.1/mom-exercise-planning/inventory.json`. The export contains grading code, answer material and course configuration; it is not a website asset. No student submissions or grade-record collections are present in its top-level structure. Do not publish the raw export or assessment answer material as part of this task.

## Editorial direction

- **Chapters 0–7: additions first.** Preserve the earlier conceptual curation. Add missing reasoning tasks when they contribute something beyond the existing set; correct or consolidate individual existing questions only where needed.
- **Chapters 8–14: retain, revise, remove and add.** Use the historical inventory to identify dense inherited numerical sets, but do not blanket-delete by source classification. Simple proportional reasoning, graph reading, unit sense and a short calculation that exposes a physical relationship can fit conceptual physics.
- Homework is the primary source of useful tasks; timed questions expose misconceptions and short contrasts; essays supply synthesis/explanation tasks. Lecture comprehension supplies a topic-coverage check. Quotation completion is not a textbook exercise template.
- Keep the textbook self-contained: no video, lecture timestamp, answer box, randomized variable, button, online grading rule or required MyOpenMath account. Preserve useful multiple-choice/ranking formats where the choices carry pedagogical value; do not mechanically turn every question into an essay.
- Do not use question frequency as a proxy for importance: the same family can recur in homework, spot-checks, timed pools and archived assignments.

## Proposed sequence and review deliverables

1. **Build a topic/family crosswalk.** For each chapter, map maintained exercises and MyOpenMath families to section IDs and learning objectives. Deduplicate exact uses by source unique ID, then identify semantic variants by inspection. Keep the export-local IDs as locators, not new textbook identities. Separate current, archived and unused contexts.
2. **Prepare a bounded two-part pilot.** A small Dynamics addition sample demonstrates how early-chapter enrichment works; one coherent Thermal Physics cluster demonstrates removal/revision/addition in a later chapter. Temperature, ideal gas and heat/phase-change reasoning are good starting material. Present proposed wording, existing counterpart, disposition, rationale, provenance, selected fixed values if any, and an internal answer/rationale. No whole-chapter rewrite or automatic import.
3. **Agree on the resulting style from that pilot.** Review the level of calculation, whether to request explanations with selections/rankings, and the usefulness of grouping. Decide public answer/solution policy before packaging answers; internal correctness checking does not require publishing an answer key.
4. **Extend in batches.** Finish additions for Chapters 0–7, then complete Chapters 8–11 and 12–14 in reviewable chapter batches. Large chapters may need several packets. Preserve sections already carefully curated rather than rebuilding from upstream.
5. **Apply reviewed decisions and validate.** Use stable exercise IDs and reversible editorial records. Keep a disposition for removed questions and redirect or explain old anchor destinations where feasible. Verify diagrams, fixed numerical variants, MathML, subparts, cross-references, numbering and answers. Ordinary exercises appear only in chapter-end collections in both HTML and PDF; Check Your Understanding remains inline. Resolve the known website duplication during integration.
6. **Maintain a separate MyOpenMath handoff.** Record gaps and corrections as they emerge, with concrete evidence, without editing the live course or creating another task automatically. This is useful parallel documentation, not a prerequisite that should delay the textbook release.

## Concrete candidates seen in the export

These are candidate families, not approved new textbook questions. Check existing textbook counterparts before adding.

| Source family | Potential textbook use |
|---|---|
| Force categorization, unique ID 1529635023176840 | Distinguish forces from objects, motions and events; ask for a reason rather than reproducing the grading interface. |
| Rotational-inertia ranking, 1530595062523426 | A small fixed set of arrangements to rank and explain, with a self-contained diagram if necessary. |
| Ideal-gas predictions, 1531146385628727 | Predict changes and recognize insufficient information; state what is held constant. |
| Latent-heat descriptions, 1531210918392542 / 1531211425943691 | Distinguish temperature change from phase change and reason about energy transfer. |
| Heat-pump coefficient-of-performance essay, 1541302000672805 | Explain why delivered heat can exceed work input without violating energy conservation; reconcile with the revised chapter. |
| Refrigerators and second law, 1544147916517086 | A short explanation connecting work input and heat transfer. |
| Half-life, 1543209909022825 | Select transparent fixed values supporting repeated halving rather than requiring logarithms. |

## Conditions to check during adaptation

The full bank has not been independently fact-checked or rendered. Sampling already shows why it should be compared with the revised textbook rather than treated as a new authority: an older radiation essay (1543705851125192) calls some radiation safe even in large quantities. Its distinction between ionizing and nonionizing radiation remains useful, but the broad safety framing needs review. Thermodynamic explanations and relativity variants also need comparison with the new wording.

All 1,012 definitions list Park,Andrew and license code 1; some preserve OpenStax attribution. The numeric code has not yet been interpreted against the platform's license definition, and author metadata alone does not establish rights to every embedded figure. Verify the declaration and inherited credits when selecting actual material; preserve the book's CC BY 4.0-only policy. No external prose or images have been imported by this inventory.

Fifty-six definitions have an image flag; inspect actual image/link dependencies and any dynamically generated diagrams before selecting candidates. Answers may live in control code (including showanswer), even when the separate solution field is empty. Randomization can encode several genuinely different situations; choose representative fixed cases deliberately and check distractors and answer keys after doing so. No MyOpenMath code should be run blindly as part of source inspection.

## Scope of this first look

Inventory covers the entire export structure and assessment membership. Content review sampled lecture, homework and timed/essay material across mechanics, thermal physics and modern physics; it is not a completed 1,012-definition content review. The next concrete deliverable is the crosswalk and bounded pilot described above. Textbook source, the public preview and the live MyOpenMath course remain unchanged.

## Maintainer-facing question references

Use the full MyOpenMath question description together with an assessment title (and folder where useful). Prefer current homework or another current assessment over archived uses. Export source IDs are internal provenance only: they do not match the identifiers the maintainer sees on the platform. Apply this convention in review pages, proposals and chat references.


## Workflow revised after maintainer discussion — September 27

The separate Dynamics/Thermal Physics pilot is superseded by chapter-by-chapter review starting with Chapter 0. Fold structural restoration against the original CNX PDF into each chapter packet, alongside exercises, glossary and summaries. First structure comparison: reports/1.1/chapter0-structure/review.md. The initial crosswalk and sampled relationships remain useful reference work, not an instruction to start elsewhere.


## Initial five findings — carry-forward checklist

Check this list when preparing each chapter; the maintainer need not reintroduce the earlier plan. The separate pilot was superseded, but these findings were not dropped. Machine-readable status is in `reports/1.1/exercise-crosswalk/reviewed-relationships.json`.

- [x] Force classification (2.2): implemented as `cnx:m78923#ex-identifying-forces`, Exercise 1 in preview version 24. Chapter 2 reviewed and approved.
- [ ] Ideal gas (8.3): prediction/insufficient-information tasks, coordinated with pruning inherited numerical questions.
- [ ] Heat capacity / latent heat (8.6–8.7): compare Oakland/Orinda and San Francisco/Sacramento climate questions; assess placement and overlap before adding.
- [ ] Latent heat (8.7): evaluate a foundational heat-absorbed/released classification question against existing applications.
- [ ] Heating curve (8.7): consider energy-input ranking; inspect diagram dependency and specify sample/pressure assumptions.

Bring the four outstanding findings into the Chapter 8 review packet with explicit proposed dispositions. These remain candidates, not approval to insert every one.

- Chapter 13: review m42542 exercise fs-id1346384, momentum with negative scientific-notation base (−10)^(−19). Flagged during minus typography audit; mathematical value intentionally unchanged pending exercise review. See reports/1.1/minus-sign-audit/applied-audit.json.

## Summary-equation audit — reminders for upcoming chapter reviews

Check these items when preparing the named chapter, and bring them to the maintainer before considering its review complete. These are chapter-triggered reminders, not scheduled notifications. Maintainer deferred the temperature-conversion and loop-count matters on September 29; no source content correction is applied yet.

- [x] **Chapter 8, Section 8.2 (Temperature), m52364:** resolved 2026-09-30 by maintainer direction: retain body unchanged; replace summary conversion list with a Kelvin–Celsius relationship bullet and only inline T_K = T_°C + 273.15. Pending next preview refresh.
- [ ] **Chapter 10, Section 10.8, m52420:** summary item `import-auto-id1166991832296` uses lowercase n in the circular-loop field formula; body `import-auto-id1166991833146` uses N for total turns, while n is turns per unit length for a solenoid. Remind maintainer and reconcile during Chapter 10 review.
- [ ] **Chapter 11, Section 11.5, m67133:** review the early uses of blackbody radiation and emissivity in the microwave/infrared/visible-light discussion. These concepts are not developed in Chapter 8; the substantive blackbody introduction is in Chapter 12, Section 12.2 (m67250). At the maintainer’s request (2026-09-30), consider a brief explanation and forward reference to Section 12.2 so the terminology does not appear unexplained. Check whether emissivity needs its own short explanation rather than assuming the Chapter 12 reference covers it. Bring this up during Chapter 11 review; no section wording change approved yet.
- [ ] **Chapter 12, Section 12.6, m67805:** summary equation `eip-115` gives proton charge-to-mass ratio as 9.57 × 10^7 C/kg; body `eip-62` gives 9.58 × 10^7 C/kg. Carry forward for reconciliation during Chapter 12 review.

Evidence and equation inventory: `reports/1.1/summary-equation-audit/review.md` and `relationships.json`. Hiding summary equation numbers is already published; these content follow-ups remain open.


### 2026-09-29 — Chapter 5 question additions for review

Added twenty maintainer-approved MyOpenMath-guided questions and arranged the complete set by section/topic: 43 ordinary questions, retaining all 23 prior questions unchanged. New coverage includes cycle timing, heartbeat rate, oscillator motion/energy, natural versus driving frequency, wave motion, superposition, standing-wave patterns and harmonics, sound, and Mach number. Full descriptions and assessment names are recorded in reports/1.1/chapter5-structure/exercise-additions-and-order.json. Source export, controls and solutions are not included in the public site. All 12 inline Check Your Understanding prompts retained. Both numbering builds, full validation and Chapter 5 browser checks passed (43 sequential numbers, links/images valid, no mobile overflow). Pending maintainer read-through after publication.


### Chapter 5 review complete

Maintainer approved Chapter 5 after reviewing all 43 questions. Final batch swaps Exercises 10/11, replaces new Exercise 11 with the longer-distance/constant-frequency spring question, references Figures 5.5.3/5.3.4 in Exercise 21 and Figures 5.6.6/5.6.7 in Exercise 30, and uses antinodes in Exercise 31(b). Both numbering builds and full validation passed; browser check confirms 43 consecutive exercise labels, working links/images and no narrow-screen overflow. Section 5.7 Sound has exactly one chapter-exercise link. Ready to publish final reviewed Chapter 5 preview.

Final Chapter 5 batch published successfully as preview version 51. Chapter 5 review complete; no pending Chapter 5 edits. Next chapter in sequence: Chapter 6.


### Chapter 6 organization ready for review

Matched CNX Chapter 7 end matter (PDF pages 196–200); no placement exceptions. Collected 13 glossary definitions, five summaries and 28 unchanged questions; five inline Check Your Understanding prompts retained. Removed optional unreferenced introduction video FmnkQ2ytlO8. Both builds, full validation and chapter browser checks passed. Details: reports/1.1/chapter6-structure/review.md. No PDF binary rebuild; MyOpenMath additions not yet proposed.

- [ ] Chapter 6 final ordering: place the sliding-versus-rolling ramp question (fs-id1401566, moved to m67046) at the appropriate point in Section 6.4. Currently first to preserve review numbering.

- [ ] Chapter 6 final ordering: place spin-stability question eip-746 and its figure (now m71595, Section 6.6) in topic order. Currently first to preserve review numbering.

Chapter 6: eight approved MyOpenMath-guided additions applied; all 35 questions ordered by section topic sequence. Pending moves of rolling-energy and spin-stability questions are now incorporated in final ordering. All earlier Chapter 6 review edits included; ordinary answers remain omitted and five inline Check Your Understanding items retained. Addition provenance and order: reports/1.1/chapter6-structure/exercise-additions-and-order.json. Preview refresh in progress.

Chapter 6 final review complete: Exercise 28 work/rotational-kinetic-energy addition published in Sites version 54. No further maintainer notes; chapter ready for progression to Chapter 7. Course/CNX builds and full validation passed with existing external-media finding elsewhere.

Chapter 7 organization complete: CNX comparison found no placement exceptions; 11 glossary entries, seven summaries and 42 unchanged questions collected at chapter end. Section numbering retained. Both builds and browser validation passed. Ready for body/exercise review before MyOpenMath additions. Evidence: reports/1.1/chapter7-structure/review.md.

Chapter 7: nine approved MyOpenMath-guided questions added; all 50 ordered by topic within their sections. Earlier approved edits/moves/removal included; figures preserved. Course/CNX builds and full validation passed (existing external-media finding elsewhere); browser checks passed 50 consecutive questions, links, images, math and 390px width. Source descriptions and assessments recorded in reports/1.1/chapter7-structure/exercise-additions-and-order.json. Non-exercise changes: Table 7.3.1 headings omit or g/mL; Eq. 7.4.4 and introduction show 1 bar = 1000 mbar = 10^5 Pa. Ready for final exercise review; publishing underway.

Chapter 7 final review — approved placement plan: move current Exercise 9 (ice-water glass, source m71613/fs-id1397150) and its nested figure from Section 7.3 to Section 7.6, immediately after ex-c7-ice-density. It requires Archimedes’ principle. Preserve wording and figure; update cross-links if needed. Apply in next organization/preview batch; source has not yet been moved.

Chapter 7 final review — approved placement plan: move current Exercise 17 (floating iceberg versus land glacier, source m71615/fs-id2590796) from Section 7.4 to Section 7.6, immediately after the planned ice-in-a-glass question (m71613/fs-id1397150). Final sequence: ex-c7-ice-density, ice-in-a-glass, iceberg versus land glacier. Preserve wording. Apply with the other planned move in the next organization/preview batch; source has not yet been moved.

Chapter 7 final refresh: both approved ice-question moves applied with the glass figure retained, after ice-density question; wine-bottle question removed; suspended-object question clarified. Eq. 7.8.2 and both Bernoulli glossary formulas repaired. 49 questions; builds and browser checks pass. Final order recorded in reports/1.1/chapter7-structure/final-review-order.json. No outstanding approved edits; awaiting user’s final visual check before closing Chapter 7.

2026-09-30: Maintainer reviewed preview version 57 and explicitly finalized Chapter 7. Chapter organization, section corrections, glossary math, and all 49 questions are approved. No outstanding Chapter 7 review items. Next chapter: Chapter 8; consult its deferred reminders before starting.

Chapter 8 organization prepared: 47 glossary entries, 13 summaries, 105 chapter-end questions (59 conceptual, 46 numerical); five inline CYU retained. Approved hot-tub/thermos wrappers applied; legacy paragraph-numbering aliases retired. Course numbering unified by section. Builds/browser checks pass. No content pruning or MyOpenMath additions yet. Review agenda and saved reminders: reports/1.1/chapter8-structure/review.md.

2026-09-30: Chapter 8 exercise selection approved and applied: 47 chapter-end questions (35 retained/revised, 12 MyOpenMath-based additions), replacing 105. Ordered by section and topic. Approved Oakland/Orinda context, equilibrium ice/water wording, simplified thermos with existing figure, irreversible free-expansion entropy question, and three-coin microstate task included. Five inline CYU retained. Section body unchanged; pending temperature-summary Celsius-to-kelvin revision included in next refresh. See reports/1.1/chapter8-structure/applied-question-manifest.json and section-change-check.json.

2026-09-30: Preview version 59 published successfully with the approved 47 Chapter 8 questions and the Section 8.2 summary conversion revision. Both numbering builds, source/link validation, and Chapter 8 browser checks passed (47 sequential questions, intact thermos figure, no broken images/math or mobile overflow). Usual Chapter 8 reorganization was already published in version 58. Receipt: reports/1.1/chapter8-structure/preview59-receipt.json.

2026-09-30: Approved textbook-wide math-italic audit repaired 495 expressions in 68 modules; 226 potential issues remain flagged for contextual review, primarily compound script bases. Both full builds and link/source checks passed, and browser checked all affected section pages without math errors. Pending batched preview refresh with Section 8.6 equation repairs. See reports/1.1/math-italic-audit/review.md and audit.json. Consult the section-specific flags during subsequent chapter reviews.

### MathML contextual review completed (2026-09-30)

Following the user's decisions for R001–R055 and authorization to resolve the rest by context, all 190 gallery expressions are now resolved locally. R056–R190 covered variable products, script attachment, operator tokenization, upright COP labeling, and punctuation. Related clear fixes include radius squares in R068, latent-heat punctuation in R093, and the 4π² factor in R119/R120. The gallery renderer now expands legacy mfenced elements so parentheses appear correctly in Chromium. Details: reports/1.1/math-italic-audit/remaining-review-decisions.json and resolutions.json.

Both course and CNX builds pass with no unresolved math. Full source/link validation passes apart from the pre-existing external-media notice. All 190 gallery cards and 37 affected section pages were browser-checked without math-error markers. Public preview has not been refreshed.

Later Chapter 13 numerical review: R159 / Equation 13.7.15 uses 9.00 × 10^-31 kg for the electron while nearby calculations use 9.11 × 10^-31 kg; its stated 4.02 × 10^-14 J agrees with 9.11. This is outside the typography corrections and remains for that chapter's review.

### Preview 60 published (2026-10-01)

Published all pending Section 8.6 equation corrections and the textbook-wide MathML audit fixes, including the 190 contextual-review expressions and subsequent alignment/spacing adjustments. Course/CNX builds have zero unresolved math; source/link validation and the 37 affected-section browser math checks passed. Existing external-media notice remains unchanged. Receipt: reports/1.1/math-italic-audit/preview60-receipt.json. Source commit: 98ff6b2b72c5d3df5afa2a9c178282b722dd62f4. Continue review at Section 8.6 or 8.7.

### Pending after preview 60: Equation 8.6.13 left-hand alignment

Chromium reported text-align:right on the first MathML table column but left-aligned its mathematical contents. Verified text-align:-webkit-right correctly places the three left-hand sides flush against the equals column. Added this browser-specific fallback to two-column equation CSS and the review gallery, retaining standard right alignment as fallback. Course build passes; visually checked Eq. 8.6.13. Awaiting next preview refresh.

### Preview 61 published (2026-10-01)

Includes all post-preview-60 Chapter 8 corrections: Eq. 8.6.13 left-hand alignment; Eqs. 8.7.6 and 8.7.8 line breaks; Section 8.9 and summaries 8.3/8.6/8.7 formula styles; Exercise 19 ΔT; Exercise 36 direct drinking-bird figure reference. Course/CNX builds and source/link validation passed with only the pre-existing external-media notice. Receipt: reports/1.1/chapter8-structure/preview61-receipt.json. Chapter 8 awaits the user's final spot check before finalization and Chapter 9 work.

2026-10-01: User finalized Chapter 8 after preview 61. Chapter 9 structural organization authorized next; preserve existing questions for subsequent review.
`n2026-10-01: Preview 62 published. Chapter 9 initial reorganization complete: 56 glossary definitions, 11 section summaries, 156 questions (62 conceptual, 94 numerical), with inline CYU retained. All original exercise content preserved; selection awaits review. Course/CNX builds and source/link/browser checks pass, apart from the existing unrelated external-media notice. Receipt: reports/1.1/chapter9-structure/preview62-receipt.json.

2026-10-01: Preview 63 published. Removed eight forced italic attributes in six Section 8.6 expressions: Figure 8.6.1 caption, Eqs. 8.6.2/8.6.9/8.6.10, inline Mgh before 8.6.8, and inline heat-transfer formula before 8.6.11. Natural mathematical italics retained. Course/CNX builds and source/link checks passed apart from existing external-media notice; rendered equations checked. Receipt: reports/1.1/chapter8-structure/preview63-receipt.json.

2026-10-02: Fixed stale Chapter Exercises navigation labels for reorganized chapters 4-9; navigation now uses the same review_chapters settings as collection. Standardized browser titles and removed legacy (Exercise)/(Exercises) title suffixes for chapters 0-9. Both builds pass; all ten chapter navigation labels and page titles verified. Pending next preview refresh.

2026-10-02: Preview 64 published successfully with the pending chapter-review navigation and browser-title naming fixes for Chapters 0-9. Existing student URL unchanged. Receipt: reports/1.1/preview64-receipt.json. No pending approved edits.

2026-10-03: Preview 65 published. Section 9.2: corrected all six absolute-value charge expressions (body, summary, exercise), three forced italic mass expressions, numeric/punctuation markup in Eq. 9.2.1 and summary, and two-line mobile layout for Eq. 9.2.2. Course/CNX builds and source/link validation passed apart from existing unrelated external-media notice; mobile render checked at 390px. Receipt: reports/1.1/chapter9-structure/preview65-receipt.json.

2026-10-03: Eq. 9.3.7 split over three lines; G units now a stacked fraction. All values unchanged. Course build and 390px mobile rendering checked; pending next preview refresh.

2026-10-03: Eq. 9.4.2 absolute-value delimiters given explicit prefix/postfix forms, zero spacing, and asymmetric stretch to match enclosed fractions; display-style fractions enabled. Course build and mobile rendering checked. Pending preview refresh alongside Eq. 9.3.7; Exercise 18 forced italics deliberately deferred to exercise review.

2026-10-03: Eq. 9.3.4 Coulomb constant units changed to a stacked fraction, values unchanged. Course build checked. Pending next preview refresh.

2026-10-03: Removed whitespace inside G identifier in Eq. 9.3.6 for normal variable formatting. Course build and rendered equation checked. Pending next preview refresh.

2026-10-03: Section 9.5 forced-italic scan found one expression: inline E=k|Q|/r-squared in paragraph import-auto-id3424254 (field-line density discussion). Removed the forced italic style on k|Q|; no other forced-italic attributes in this module. Course build passes. Pending next preview refresh.

2026-10-03: Removed forced italic styling from 15 Section 9.6 expressions (14 body/example expressions and one summary copy), including Eqs. 9.6.6/7; trimmed identifier whitespace. Removed PE-specific italic ancestors in Sections 9.10 and 9.11. Other expressions in those later sections and exercise review remain deferred. Both builds pass; PE browser styles verified normal. Pending next preview refresh.

2026-10-03: Preview 66 published all pending section math changes: 9.3.4 unit fraction, 9.3.6 G token, 9.3.7 multiline/unit fraction; 9.4.2 fences and vertical room; 9.5 inline forced italics and absolute-value spacing; 15 Section 9.6 expressions including summary; upright PE in 9.10 and 9.11. Both builds and source/link checks pass with existing unrelated external-media notice. Receipt: reports/1.1/chapter9-structure/preview66-receipt.json. Exercise 18 forced italics remains explicitly deferred.

2026-10-03: User prefers Eq. 9.2.2 as a single line despite slight mobile width overflow. Restored single-line layout, keeping cleaned number/unit markup. Course build passed. Pending next preview refresh.

2026-10-03: Combined former Eqs. 9.3.3 and 9.3.4 into aligned Eq. 9.3.3. Former 9.3.5-9.3.9 now 9.3.4-9.3.8. Old eip-947 anchor retained inside merged equation. No source links or literal equation-number references require editing. Both builds and source/link validation passed apart from existing unrelated media notice; rendered alignment checked. Reference audit: reports/1.1/chapter9-structure/equation-merge-reference-check.json. Pending preview refresh.

2026-10-03: Applied three annotated requests: former Eq. 9.3.7 (now 9.3.6) has substitution on one line and result on second, aligned at equals signs; Eq. 9.4.4 Coulomb constant units stacked; all three remaining Section 9.4 forced-italic expressions cleaned (math 29,32,40). Both builds pass and layouts visually checked at 712px. Pending next preview refresh.

2026-10-03: Approved inline slash convention: no added spacing on division slashes, including text units. Preserve explicit grouping; use parentheses for compound denominators, and flag ambiguity rather than infer grouping. Do not affect nonmathematical slashes or displayed fractions. Applied spacing-only patches to 209 expressions in 49 modules; 407 slash-containing inline expressions audited. Display equations and expression content verified unchanged by this pass. Grouping-review inventory: reports/1.1/inline-slash-audit/grouping-review.json. Future edits should follow this convention. Full builds/source-link checks and all 49 affected section pages pass, apart from the existing external-media notice.

2026-10-03: Preview 67 published: inline slash-spacing audit plus all pending Chapter 9 section corrections since 66 (9.2.2 one line; merged 9.3.3 with renumbering; gravitational calculation two aligned lines; 9.4.4 unit fraction and three inline forced italic fixes). Receipt: reports/1.1/inline-slash-audit/preview67-receipt.json. Ambiguous grouping left unchanged for review; Exercise 18 forced italics still deferred.

2026-10-03: Section 5.6 inline v_w/2L changed to v_w/(2L), resolving its slash-audit grouping flag. Eq. 5.6.1 absolute-value signs changed from relation operators to opening/closing fences with zero spacing. Course build and rendering checked. Pending preview refresh.

2026-10-03: Bookwide vertical-bar audit checked all maintained MathML, including summaries and exercises. All 25 absolute-value pairs in 23 expressions now use explicit opening/closing stretchy fences with zero operator spacing; corrected 14 expressions across seven modules, including three number-token bar pairs and two mismatched-row groupings. Preserved parallel notation and normalized two F-parallel subscripts from adjacent single bars to U+2225. No ambiguous mathematical uses remain in this audit; a Flickr contributor name containing bars was preserved. Both full builds and source/link validation completed (only existing external-media notice); all 16 changed expressions rendered without MathML errors and visually checked. Pending preview refresh.

2026-10-03: Section 6.2 slash-audit flag was a false positive: MathML mfenced parentheses were lost in plain-text extraction. Preserve pedagogical (rad/s)/s; explicit compact parentheses and slash operators now replace mfenced/text-slash markup. Removed redundant individual-variable italic overrides in 19 expressions (ordinary variable italics retained), and changed number-token Delta to upright identifiers. No whole-expression italic wrappers found. Pending preview refresh.

2026-10-03: Author requests retaining Section 8.6 compact specific-heat unit table headings without added parentheses for width. Audit also finds cal/g·°C in Table 8.6.1 footnote eip-id1169738163557 (math 36), reported for author review; unchanged. Body kcal/(kg·°C) is already explicitly grouped.

2026-10-03: Author confirms Section 8.6 unit footnote is rendered in the column heading and should remain unchanged. In Section 8.7, grouped and tidied all three paragraph specific-heat units: 0.50, 1.00, and 0.482 cal/(g·°C). Numerical values preserved. Pending preview refresh.

2026-10-03: Important Constants table now uses stacked fractions for compound quotient units in both numerical columns: G, R, Stefan-Boltzmann sigma, Coulomb k, epsilon0, and mu0 (12 expressions). Simple m/s and J/K retain inline slashes. Numerical values preserved. Pending preview refresh.
The permeability footnote also uses a stacked T·m/A unit, completing all compound quotients in the table.

2026-10-03 — NEXT PREVIEW REFRESH REMINDER (delivered with preview 68): When reporting the next successful preview refresh, explicitly remind the author to review the Important Constants table in the constants appendix, especially the newly stacked compound-unit fractions in both value columns and the permeability footnote. Author is resuming Chapter 9 review from the beginning. Mark this reminder delivered after including it in that refresh response.

2026-10-03: Section 9.6 opening conservative-force paragraph now marks d and F in the parenthetical explanation as vectors, matching W = F dot d. Previously they were plain prose letters. Pending preview refresh.

2026-10-03: Section 9.6 inline Delta V = -E dot d now uses upright Delta rather than content-MathML variable styling. PE in the Potential Energy callout phrase "a loss in PE" is plain upright prose, not bold markup; retained. Pending preview refresh.

2026-10-03: Section 9.6 annotated spacing fixes: removed extra 0.25em spaces around the inline VB minus VA; added 1em each side of and in Eqs. 9.6.6/7 and matching summary, with proper math tokens; nonbreaking number/unit spaces in battery problem including 60,000 C. Pending preview refresh.

2026-10-03: Section 9.6 further annotations: subtraction is now between VB and VA rather than embedded in VA subscript base; Delta PE = -30.0 J uses proper tokens and infix equality; Eq. 9.6.13 now has explicit 1 eV tokens and three aligned lines. Pending preview refresh.

2026-10-03: Section 9.6 molecular-energy calculation parentheses now live inside the math box, preventing a break after the opening parenthesis. Inline KE + PE = constant and Eq. 9.6.14 use upright identifiers and normal infix operator spacing. Pending preview refresh.

2026-10-03: Adopted upright descriptive subscripts as textbook convention (initial, final, image, object, etc.); recorded in style guide. Fixed lone italic image i in Section 11.9, math 79. Earlier inventory is a before-change snapshot. Pending preview refresh.

2026-10-03: Eqs. 9.6.15/16 now use standalone infix plus/equality tokens and upright KE/PE and i/f identifiers. Previously equality was embedded in the KE base text, with inconsistent whitespace and number/operator tokens for subscripts. Pending preview refresh.

2026-10-03: Bookwide Van de Graaff capitalization audit: standardized lone Van De Graaff variant in Section 9.7 figure alt text; all other occurrences already use Van de Graaff. Recorded convention in style guide. Pending preview refresh.

2026-10-03: Section 9.8 forced-italic cleanup in 14 body/summary expressions, including Eq. 9.8.1 and repeated current definitions; Delta now upright identifier. Three italic micro-prefix instances in chapter exercises (math 26-28) remain for exercise review, consistent with author deferral. Pending preview refresh.

2026-10-03: Eq. 9.8.2 now has numerical/unit tokens and explicit infix equality for standard spacing. Inline Delta t = t already uses a normal relation operator after the preceding italic cleanup; no extra spacing override added. Pending preview refresh.

2026-10-03: Section 9.9: removed forced italics in 11 body/summary expressions; repaired ohm-definition equality in Eq. 9.9.4 and summary; corrected four resistance-range units where Omega was incorrectly an operator adding spacing. Exercises remain deferred. Pending preview refresh.

2026-10-03: Standardized IR drop(s) as plain prose throughout maintained textbook, including summaries and exercises. First introduction in Section 9.9 quoted; nearby later occurrences in Sections 9.9 and 9.11 unquoted. Equation products unchanged. Pending preview refresh.

2026-10-03: Section 9.10 body/summary forced italics removed in 19 expressions; parenthetical P was already math but had a trailing prose space, now removed with parentheses included in math. Exercise cleanup deferred. Pending preview refresh.

2026-10-03: Example 9.10.1 section reference now links internally to Section 9.9. Eq. 9.10.10 rate uses stacked $0.12 over kW·h. Pending preview refresh.

2026-10-03: Section 9.11 parenthetical ohm unit changed to plain upright (Ω), matching (A) in same paragraph. Pending preview refresh.

2026-10-03: Section 9.11 remaining forced italics removed in 14 expressions (none in exercises). Defined total dissipated energy E_diss in preceding prose and added E_diss = to Eq. 9.11.2. Pending preview refresh.

2026-10-03: Bookwide ohm-operator audit normalized 73 Omega unit tokens in 62 expressions across seven modules, including exercises. Preserved three Omega particle symbols and one Greek-alphabet Omega. Confirmed annotated Section 9.11 IR drop is already plain prose in pending edits. Pending preview refresh.

- Section 9.11 author correction: rebuilt Eq. 9.11.33 with complete numeric tokens, upright W units, thin number-unit spaces, and standard infix operators. Removed redundant Problem-Solving Strategies for Series and Parallel Resistors box (fs-id2401854) and the directions pointing to it in two exercises; retained the exercise questions. Saved for next preview refresh.

- Section 9.12: confirmed ordinary 0.100 ohm unit spacing is covered by the bookwide correction; additionally removed residual explicit gaps around the hyphen in 0.100-ohm resistance (import-auto-id2514512). Pending preview refresh.

- Table 9.12.1: put (6 A) on a new line after 6000, with a nonbreaking number-unit space. Pending preview refresh.

- Fixed annotated 20 mA prose gap with NBSP; established bookwide number-unit nonbreaking-space convention in style guide. Initial prose-only audit reports 1,019 candidates across 101 modules, 307 flagged for context review. Inventory is not yet applied; markup-boundary cases need a supplemental pass. See reports/1.1/prose-unit-space-audit/.

- Bookwide prose number-unit spacing completed: 1,338 occurrences / 1,346 gaps across 113 modules, including 24 prose/MathML boundaries. MathML unchanged. Three occurrences in two author decisions remain in reports/1.1/prose-unit-space-audit/review.md. Builds/full validation and viewport wrapping checks passed apart from existing external-media notice. Pending next preview refresh.

- Author resolved number-unit review: Section 13.7 1 TeV typo/NBSP corrected; Section 2.4 both 45g references made single mathematical products, without space or apostrophe-s. Removed seven forced-italic attributes in Section 2.4. Pending preview refresh.

- Ohm glossary definition (m52401, fs-id1917197): inserted missing NBSP in 1 Ω; earlier global audit protected existing spaces and did not insert missing ones. Pending preview refresh.

- Section 9.6 summary: electron-volt conversion eip-998 now matches the corrected body equation in three rows with aligned equals signs. KE + PE uses upright identifiers and standard infix-plus spacing; sentence period moved outside math. Pending preview refresh.

- Section 9.8 summary: corrected equality spacing in 1 A = 1 C/s. Confirmed forced italics in 9.8/9.9 summaries and ohm-identity equality spacing were already corrected. Pending preview refresh.

- Section 9.10 summary: confirmed forced italics already removed; moved the period inside E = Pt math so punctuation remains attached. Pending preview refresh.

- Preview 68 published successfully (2026-10-04 UTC / 2026-10-03 Pacific), commit d729705050c190af55076be37aa54c5286861ab9. Includes all pending corrections through Section 9.10 summary punctuation, global ohm and prose number-unit spacing, Section 2.4 corrections, and constants table unit fractions. Full course/CNX checks passed with the existing external-media notice. Receipt: reports/1.1/preview68-receipt.json. Constants-table review reminder delivered with publication handoff.

- Author approved the Important Constants table with stacked fractions after preview 68. Constants-table review is complete.
- Chapter 9 exercise-selection proposal prepared against preview 68: 55 proposed questions (46 retained/revised + 9 new), all 156 current questions assigned a disposition (5 retain, 41 revise, 12 merge, 98 remove). 76 MyOpenMath crosswalk records reviewed by family/context; source decisions and six course follow-up leads saved. 33 independent numerical checks passed. Proposal and internal answers: reports/1.1/chapter9-structure/question-set-proposal.md and answer-checks.md. No selection applied; live preview remains 68 pending author review.

- Post-preview-68 annotation: left-aligned RHS cells of the electron-volt conversion in body eip-829 and summary eip-998. MathML already specified right/center/left columns, but native rendering ignored the third-column setting; added scoped CSS matching earlier alignment fixes. Pending refresh.
- AFTER CURRENT ANNOTATION BATCH: discuss a bookwide policy/fix for punctuation immediately after math. Author explicitly deferred discussion until other easy fixes in this batch are complete. Example: Section 9.8 calculator-electron-rate strategy paragraph, period stranded before “Since each electron”. Do not apply a global punctuation transformation yet.

## Global inline-math punctuation protection (2026-10-03)

Implemented in prototype/math_punctuation.py and shared renderer/CSS, covering section pages, chapter reviews, and book output in both numbering profiles. Closing punctuation remains outside the MathML copying payload, but shares one nonbreaking layout group with the equation; oversized groups scroll. Also handles math-only inline wrappers and long emphasized phrases ending in math without making the whole phrase unbreakable. No canonical CNXML changes required.

Validation: six regression tests; 656 browser geometry checks across 320, 375, 650, 712, and 1024 px viewports and 186 forced wrap thresholds; full source fidelity validation passes (6821 expressions and 10642 prose fragments). Existing unrelated external-media notice remains. Built locally; publication deferred until requested.

## Section 9.10 follow-up annotations (2026-10-03)

Applied MATH-C9-10-POWER-SPACING-ANNOTATIONS: removed whitespace after the opening parenthesis before the kilovolt-ampere identity and before the closing parenthesis after E; rewrote the conversion's 3.6 and Eq. 9.10.9's 60.0 as single mn tokens with proper operator/unit markup; inserted a newline before the take-home activity's second numbered instruction. Existing punctuation inside MathML remains unchanged. Both numbering profiles rebuilt; browser checks confirm all five corrections and full fidelity validation passes. Pending next requested preview publication.

## Equation 9.11.11 spacing (2026-10-03)

Applied MATH-C9-11-VOLTAGE-SUM-SPACING to m42356/eip-359. Replaced fragmented decimal markup with complete number tokens, flattened infix operators, and used one thin space before each upright V unit. Browser geometry confirms equal 5 px spacing on both sides of both equals signs at 712 px viewport. Both profiles rebuilt; full fidelity validation passes. Pending next preview refresh.

## Equation 9.11.23 fraction-unit spacing (2026-10-03)

Applied MATH-C9-11-PARALLEL-INVERSE-UNIT-SPACING: added a single thin space between the reciprocal fraction and upright ohm unit, consolidated decimal tokens, and normalized the remaining spacing in this expression. Browser check measures a 3 px fraction-to-unit gap at 712 px. Both profiles rebuilt and full source fidelity validation passes. Pending next preview refresh.

## Example 9.11.3 IR Drop title (2026-10-03)

Applied PROSE-C9-11-IR-DROP-EXAMPLE-TITLE: IR Drop is ordinary heading text, retaining heading capitalization and weight. A textbook-wide XML scan found this was the only remaining MathML expression immediately followed by drop/Drop. Both profiles rebuilt and source fidelity validation passes (6820 mathematical expressions after removing the prose-only IR title expression). Pending next preview refresh.

## Section 9.12 forced italic audit (2026-10-03)

Applied MATH-C9-12-FORCED-ITALIC: removed the one remaining fontstyle="italic" attribute from V/R in import-auto-id2400011. Entire module checked for fontstyle, mathvariant, and style italic overrides; no other occurrences found. Normal variable italics and prose emphasis retained. Both numbering profiles rebuilt; source fidelity validation passes. Pending next preview refresh.

## Preview 69: approved Chapter 9 questions (2026-10-03)

Published the approved 55-question Chapter 9 set, with 46 existing IDs retained and nine new IDs. Moved battery capacity to 9.10 and two-contact potential difference to 9.12. The inline 9.11 Check Your Understanding and non-exercise source content are preserved. All pending Chapter 9 math corrections and global punctuation wrapping protection are included. Answers and review rationale remain in repository reports only, excluded from the hosted preview; author accepts that these records can later be public on GitHub. Canonical GitHub repository was not pushed.

Validation: all 55 approved prompts match after typography normalization; numbering 1–55 verified at 375, 712, and 1024 px without page overflow; full source/link validation passes. Deployment succeeded; receipt reports/1.1/preview69-receipt.json. Chapter 9 awaits the author's final review.

## Exercise 6 Coulomb-constant units (2026-10-03)

Applied MATH-C9-EX6-INLINE-COULOMB-UNITS: use inline slash units instead of stacked unit fraction. Browser checks at 375 and 712 px show equal client/scroll heights (no vertical overflow). Both profiles rebuild and source validation passes. Pending preview refresh. Suggested placement for a conceptual polar-molecule explanation: Section 9.3 after the attraction/repulsion and distance discussion, before the worked comparison of electrostatic and gravitational forces; no new explanatory prose applied yet.

## Section 2.9 forced italic audit (2026-10-04)

Applied MATH-C2-9-FORCED-ITALICS: removed five forced italic mstyle attributes for mM and mg in m71410 (eip-492, import-auto-id2611373, eip-171, eip-143). No forced italic fontstyle/mathvariant/style attributes remain in the module's MathML. Both profiles rebuilt and full fidelity validation passes. Pending next requested preview refresh.

## Punctuation-group scrollbar regression (2026-10-04)

Confirmed overflow-x:auto implicitly enabled vertical auto overflow on every math-with-punctuation wrapper. Full-book checks reproduced 159 vertically overflowing groups at desktop widths. Changed ordinary wrappers to overflow:visible; ResizeObserver now enables horizontal scrolling only for groups wider than their available line. Wide groups have vertical math-ink padding and hidden vertical overflow. Punctuation remains in its nonbreaking group.

Validation: all 1844 current full-book groups checked at 375, 712, and 1024 px: zero vertical scrollbar candidates and zero clipped math bounding boxes. Eight wide groups scroll horizontally at 375 px; none need scrolling at the two desktop widths. Existing punctuation placement regression checks and full source validation pass. Pending next preview refresh.

## Section 9.3 conceptual paragraph (2026-10-04)

Applied TEXT-C9-3-INVERSE-SQUARE-POLARIZATION with the exact approved paragraph between Figure 9.3.2 and Example 9.3.1. Proportionality is native MathML; gravitation reference is a title-only internal link to m71410. Browser check confirms placement immediately before Example 9.3.1 and correct link destination. Both numbering profiles rebuilt; full source/link validation passes. Included in next preview with pending scrollbar, Section 2.9 italic, and Exercise 6 unit fixes.

Preview 70 published successfully with the Section 9.3 paragraph and all pending fixes above. Receipt: reports/1.1/preview70-receipt.json. Canonical GitHub repository not pushed.

## Exercise 16 charge scale (2026-10-04)

Applied EX-C9-16-MICROCOULOMB-SCALE: 2.0 μC replaces 2.0 C, retaining a nonbreaking number-unit space. Internal answer updated to +24 μJ in proposal/answer records and the proposal generator; numerical check now uses 2e-6 × 12 = 24e-6 J. All 33 numerical checks pass; both profiles rebuilt and source validation passes. Pending next preview refresh.

## Exercise 21 equilibrium focus (2026-10-04)

Applied EX-C9-21-EQUILIBRIUM-FOCUS: removed the final question about whether perpendicular field lines establish conductivity. Exercise now ends with the explanation of mobile-charge motion. Internal answer and proposal records updated to match. Both profiles rebuilt; full validation passes. Pending next preview refresh.

## Exercise 22 field-line interpretation (2026-10-04)

Applied EX-C9-22-FIELD-LINE-INTERPRETATION: replaced the plate-separation comparison with the approved question about uniform strength/direction and breakdown near the edges in Figure 9.7.4. Figure reference is a real internal link. Updated internal answer, proposal wording/rationale, and manifest title. Both profiles rebuilt; source/link validation passes. Pending next preview refresh.

## Exercise 27 net-charge wording (2026-10-04)

Applied EX-C9-27-NET-CHARGE: replaced total charge with net charge, clarifying that neutrality does not imply an absence of charged particles. Proposal records and generator updated; existing internal answer already explains cancellation of mobile-electron and positive-lattice charges. Both profiles rebuilt and full validation passes. Pending next preview refresh.

## Exercise 29 battery/bulb illustration (2026-10-04)

Added original vector art maintained/assets/aa-battery-bulb-open-circuit.svg, with source/provenance in proposals/1.1/assets and registry entry in maintained/added-assets.json. Shows a horizontal AA battery, bulb bottom contact touching the positive button, and clearly labeled unconnected shell/negative contacts. Applied EX-C9-29-BATTERY-BULB-ILLUSTRATION to add figure and alternative text, and align prompt wording with direct contact instead of one wire. No external artwork used. Rendered illustration visually inspected; loaded without page overflow at 375 and 712 px. Both profiles rebuilt; source/link validation passes. Pending next preview refresh.

Exercise 29 figure follow-up: removed parenthetical touching/unconnected notes per author approval; four contact labels remain. Approved prompt and descriptive alternative text unchanged. Pending next build/preview refresh.

Exercise 30: applied EX-C9-30-CURRENT-UNITS to specify average current in amperes. Proposal records updated; XML parsed successfully. Pending next preview refresh.

## Exercise 39 link to earlier cords exercise (2026-10-04)

Applied EX-C9-39-CORD-CROSS-REFERENCE. Opens with a stable internal link to Exercise 36 and repeats the resistance/current values for independent use. Proposal records updated; both profiles rebuilt and source/link validation passes. Pending next preview refresh.

Exercise 44: applied EX-C9-44-SHORTED-TERMINOLOGY, specifying an ideal wire connecting the bulb's two terminals. Proposal records updated; numerical answer unchanged. XML validation passes. Pending next preview refresh.

Exercise 48: applied EX-C9-48-PRACTICAL-PARENTHETICAL. Replaced the disclaimer with the approved parenthetical note about outlets sharing a circuit, following part (b). Proposal records updated; XML validation passes. Pending next preview refresh.

## Preview 71 published (2026-10-04)

Published all pending exercise-review edits (16, 21, 22, 27, 29, 30, 39, 44, 48), including original Figure 9.E.1 with simplified contact labels, caption, alt text, and asset provenance. All 55 questions retained. Both builds, source/link checks, 33 numerical checks, and browser checks at 375/712 px pass. Answer records remain excluded from preview. Receipt reports/1.1/preview71-receipt.json. Awaiting author's final Chapter 9 approval; canonical GitHub repository not pushed.

## Chapter 9 finalized; Chapter 10 organization (2026-10-04)

Author finalized Chapter 9 after preview 71. Chapter 10 prepared using the established collected-review structure: 42 alphabetized definitions, 10 summaries, 50 original questions (19 conceptual and 31 numerical), ordered by section with continuous numbering. No question pruning/rewording/additions in this pass. All exercise content preserved by source comparison; section bodies unchanged. Full builds/source/link validation pass. Browser review page checks at 390/1024 px: 50 sequential exercise numbers, 42 definitions, zero broken images/math issues/page overflow. Saved n/N reminder carried into reports/1.1/chapter10-structure/review.md. Publishing preview now.

Preview 72 published successfully: Chapter 10 organized and ready for review. Receipt reports/1.1/chapter10-structure/preview72-receipt.json. No canonical GitHub push. Chapter 9 remains finalized.

## Section 0.3 Planck constant spacing (2026-10-04)

Applied MATH-C0-3-PLANCK-UNIT-SPACING: explicit thin spaces before kg and between unit factors, upright units and complete exponent tokens, replacing Content MathML factors rendered with invisible multiplication. Numerical value unchanged. Both profiles rebuilt; full validation passes. Pending next preview refresh.

Table 0.3.2: applied TABLE-C0-3-REMOVE-UNITY-ASIDE, removing (=1) after the 10^0 entry. Math unchanged; XML verified. Pending next preview refresh.

Equations 0.3.2, 0.3.3, and 0.3.4: applied MATH-C0-3-SPEED-EQUATION-SPACING. Replaced text-embedded equals signs with operators, consolidated decimal tokens, and added thin spaces before units and unit fractions. Values, stacked fractions, and punctuation preserved. Both profiles rebuilt and full validation passes. Pending next preview refresh.

Equation 0.3.5: applied MATH-C0-3-UNIT-CHECK-ALIGNMENT. Removed asymmetric leading spaces in unit fraction tokens, empty identifiers, and redundant groups; added explicit quantity/unit gaps. Retained the unit-only inverted-conversion demonstration. Both builds and validation completed with only the known external-media issue. Pending next preview refresh.

Equations 0.3.6 and 0.3.7: applied MATH-C0-3-SI-SPEED-SPACING. Consolidated numeric tokens, removed empty identifiers and redundant operator grouping, and standardized thin spacing before units and unit fractions. Values and stacked fractions preserved. Both builds and validation completed with only the known external-media issue. Pending next preview refresh.

Preview 73 published (2026-10-04 Pacific): all pending Chapter 0 corrections included, plus MATH-C0-EX15-CONVERSION-SPACING for explicit quantity/unit gaps. Both builds and full validation completed with only the known external-media issue. Receipt reports/1.1/preview73-receipt.json. Canonical GitHub not pushed; last locally recorded push is 2026-09-21 10:03:09 -0700, d3e0e27. Remote check failed with local TLS credentials error.

## GitHub synchronization (2026-10-04)

Maintainer requested committing and pushing all work through preview 73. Includes reviewed textbook revisions, Chapter 9 finalization, Chapter 10 organization, Chapter 0 math corrections, supporting tools, provenance, and internal textbook answer records (approved for the GitHub reports folder, excluded from the rendered textbook). Raw MyOpenMath export remains outside this repository. Both course/CNX builds and full validation already completed for this source state, with the known unrelated external-media finding. GitHub HTTPS works using the repository-local OpenSSL backend with certificate verification enabled.

## Browser-only textbook search (2026-10-05)

Added Search navigation and a static passage index rebuilt from rendered sections and exercise pages only. No PHP, search service, or query logging: JavaScript fetches the index on demand, searches locally, highlights excerpts, and links to existing anchors. Multiple words must all match; quoted phrases are contiguous. Twenty results per batch; shareable query URLs, responsive controls, live status, empty/no-result and retry states. Reports/internal answer records are not indexed.

Both builds and full validation pass apart from the known external-media finding. Verified all 10,081 course passage anchors, Curie and exact Marie Curie results, no results for madame curie/Noether, mobile width, safe query rendering, pagination, and failed-load retry (prototype/tools/test_search.cjs). Canonical GitHub sync remains explicit and has not been requested for this addition.

Preview 74 published successfully with browser-only textbook search. Receipt reports/1.1/preview74-receipt.json. No canonical GitHub commit/push.

## Math copy format inventory (2026-10-05)

Inventoried 6,727 source expressions through native MathML for LaTeX/ASCIIMath copy planning. Reproducible tool: tools/inventory_math_copy.py. Report: reports/1.1/math-copy-inventory/index.html and inventory.json. Structural audit only, not round-trip conversion certification. 897 expressions flagged for overlapping special-handling categories; most are representable legacy notation, not mathematical defects. Three detached nonnuclear subscripts warrant source normalization (1.6.40, 1.7.5, 3.3.4). Author-policy items include multiline layout, nuclear scripts, script ell, and alphabet-reference fidelity. The standalone ASCIIMath source defines hbar and minus-or-plus, but subsequent author testing found hbar does not render correctly in the asciimath.org MathJax 4 demo. hbar is therefore flagged as renderer-dependent; source-table presence is not conversion validation. No textbook/interface/source changes or preview/GitHub publication.

## Structural MathML normalization (2026-10-05)

Applied reversible MATH-COPY-NORMALIZE patches and targeted MATH-COPY-FOLLOWUP patches: 1156 unique expressions in 82 modules. Three verified detached subscripts, primed collision variables, explicit quantity tokens/spacing, decimal fragments, unit exponent scope, and nuclear left scripts repaired. Textbook values, non-MathML prose, source IDs, and legacy annotations preserved. Both builds/full validation and six regression tests pass (known external-media warning unchanged). Native before/after render pairs checked; representative samples inspected. Original copy inventory preserved as before-normalization.json, current inventory refreshed. Unicode hbar exception remains approved for future ASCIIMath copying; no copy-interface change yet. Reports: reports/1.1/math-source-normalization/. No preview refresh or GitHub sync.

Section 10.6 flagged degree symbol: applied MATH-C10-6-ATTACH-DEGREE, moving 90 into MathML and replacing the empty-base superscript with a postfix degree symbol. Pending preview refresh.

Section 14.4 isotope list: each of hydrogen-1, hydrogen-2, and hydrogen-3 is a separate MathML expression, with commas in prose and proper nuclear prescripts. MATH-C14-4-SEPARATE-HYDROGEN-ISOTOPES. Pending preview refresh.

- 2026-10-05: Split the Section 14.4 summary nuclide notation into two inline math symbols, with “or simply” and punctuation in prose; retained the eip-107 anchor.

- 2026-10-05: Table 18.1 now uses x_0 to illustrate an initial-value subscript, replacing an isolated subscript zero.

- 2026-10-05: Section 1.7 approximate gravitational acceleration now explicitly squares only s and includes a thin space after 10.

- 2026-10-05: Equation 1.7.7 now uses two aligned lines, stacked units, complete decimal tokens, and thin number-unit spaces.

- 2026-10-05: Equation 3.4.3 uses three aligned lines and correct acceleration-unit exponent scope. Equation 3.6.4 was verified as already correctly laid out; its parenthesized unit-ratio power is valid.

- 2026-10-05: Equation 14.4.9 cube-root exponent now applies only to 56. Author approved ASCIIMath named symbols where clearly supported, otherwise Unicode fallback (including Greek variants); preserve character identity, with the prior Unicode hbar exception retained.

- 2026-10-05: Final copy-inventory source cleanup corrected 10 expressions in 9 modules (unit powers, scientific notation, electron superscript, inequality and ratio scope, quantity tokens, and padding). Reviewed 13 explicitly parenthesized powers as valid. Both builds and full validation completed, retaining the existing unrelated external-media issue; all ten changed expressions visually checked in Chrome. Remaining inventory flags are converter handling. Preview and GitHub unchanged.

- 2026-10-06: Implemented LaTeX/ASCIIMath copy dialog for equations, with keyboard activation, text preview, clipboard fallback, grouped fractions, nuclear scripts, multiline arrays/matrices and approved Unicode fallback. Copy strings derive from rendered MathML; no legacy annotation reliance. Ten converter tests passed; all 6,729 expressions parsed in both formats in MathJax 4.1.3, retaining multiline structures. Desktop/mobile interaction checks and representative visual comparisons passed. Preview refresh follows separately; GitHub sync remains manual.
- 2026-10-06: Published preview 75 with equation copying and the reviewed MathML corrections. Sites source commit 8e3e3acbaa15f85c2825d2159ec4b75022a76c5d; deployment succeeded. Canonical GitHub repository was not pushed.
- 2026-10-06: Equation copying now uses a separate Copy button revealed by hover, keyboard focus, or tap. Equation clicks do not open the dialog. The button is out of flow, preserves equation geometry, supports keyboard Tab/Enter and two-step touch activation, dismisses outside, and tracks its equation during scrolling. Updated desktop and touch interaction tests passed.

Preview 77: Removed the top equation-copy instruction banner at the author's request. Verified that the banner is absent and the revealed Copy button still opens the dialog. Published successfully; see reports/1.1/preview77-receipt.json.
