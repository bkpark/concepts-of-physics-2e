# Exercise revision for 1.1: proposed action plan

## Outstanding items to mention at every chapter finalization

- [ ] **Replace Figure 12.3.2 photoelectric-apparatus photograph.** Author will take a higher-resolution photo of their lab apparatus (plans to take it Monday and will set their own reminder). At every chapter finalization, remind the author while this remains open, even after Chapter 12. Stable target: m67251 figure import-auto-id1362766, media import-auto-id953716. Replace the photo, revise its alt text/caption as needed, and update the image credit together when the author supplies it. Current credit is P.P. Urone; keep it until the replacement is made. No scheduled notification requested. Mark complete only after the replacement and credit update are verified.


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
- [x] **Chapter 12, Section 12.6, m67805:** resolved during global equation review (2026-10-08); both now 9.58 × 10^7 C/kg. Historical discrepancy: summary equation `eip-115` gives proton charge-to-mass ratio as 9.57 × 10^7 C/kg; body `eip-62` gives 9.58 × 10^7 C/kg. Carry forward for reconciliation during Chapter 12 review.

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

Section 3.4: Removed 11 explicit MathML italic style overrides at maintainer request. Mathematical tokens and prose are unchanged; natural variable italics remain. Reversible source patch: MATH-C3-4-REMOVE-FORCED-ITALICS.

Equations 3.4.13 and 3.4.14: Removed explicit thin spaces between g and h_f in source and consequently copied LaTeX. Number-unit spaces retained.

Section 10.4: Removed three plain-text italic B emphasis wrappers, including two B-field terms. Text and MathML are unchanged.

Responsive math overflow: Removed the legacy below-650px blanket scroll rule. All math wrappers now use visible overflow unless genuinely too wide; explicit display equations retain block layout. Extended existing punctuation overflow sizing to standalone math wrappers, avoiding nested scroll containers. Checked five widths in light/dark color schemes, horizontal overflow and resize recovery; math-copy UI regression passed. Local only, awaiting batched preview refresh.

Preview 80: LaTeX now copies the parallel relation as \parallel; ASCIIMath retains Unicode. All 11 converter tests pass. Published with the pending plain-text B and responsive overflow fixes; see preview80-receipt.json.

Inline math baseline: Changed shared equation and punctuation wrappers from vertical-align:middle to baseline. Visually compared the right-hand-rule paragraph before/after; short symbols now align with prose without per-expression offsets. Responsive overflow and copy-interface regressions pass. Pending the next batched preview refresh.

Eq. 10.8.2: Three aligned lines separate the algebraic formula, numerical substitution, and 25 A result. Original fractions preserved. Course build and three-row LaTeX copy check pass. Pending batched preview refresh.

Section 10.8: Removed all five forced italic overrides. Opening parentheses before n=N/l are now prose in both body and glossary, excluded from math copying. XML and focused copy checks pass; pending batched preview refresh.

Equations 10.8.5 and 10.8.6: Added requested breaks before =1000 m^-1 and after mu_0 n I respectively, producing two and three aligned lines. Mathematical tokens and operand subtrees preserved. Pending batch preview refresh.

Preview 82: Shared CSS honors right-center-left MathML columns. Eq. 10.8.6 now uses stacked T m/A and 1000/m. Browser alignment and visual checks passed for 10.8.2, 10.8.5, and 10.8.6 at 650px; no equation-container width overflow. Both builds succeeded; published.

Section 10.10: Removed all ten explicit MathML italic overrides (seven fontstyle and three mathvariant) and associated mathit classes, including glossary markup. XML parses and text/tokens are unchanged. Pending batch preview refresh.

Eq. 10.11.7: Final numerical result moved to third aligned line. XML, operand preservation, and three-row LaTeX copy checks pass. Pending batch preview refresh.

Three-column alignment audit: Standardized all 85 remaining lll tables to rcl (84 equation chains and one nuclear reaction array). No exceptions required. Only columnalign attributes changed; full XML comparison verifies all other content unchanged. Inventory: reports/1.1/three-column-alignment.json. Pending batch refresh.

Alignment audit follow-up: Two unspecified three-column tables also copied as lll. Both now explicitly rcl, bringing total to 87 in 38 modules. No exceptions.

Eqs. 10.11.8–10: Final numerical results on separate third lines with rcl alignment. Mathematical operand preservation and three-row copy checks passed. Pending batch refresh.

Section 10.12: Removed all three forced italic MathML wrappers (V/R and two IV expressions). XML parses; all text and mathematical tokens preserved. Pending batch preview refresh.

Average abbreviation: Changed all 14 P_ave occurrences in Section 10.12 to upright P_avg, including legacy annotations; no other ave/avg subscripts found in maintained source. Recorded avg as the future house convention in docs/style-guide.md. XML and upright LaTeX-copy check pass. Pending batch refresh.

Eqs. 10.12.6–7: Three aligned lines for 10.12.6; corrected operator/text separation and numerical/unit tokens in 10.12.7. XML and focused copy checks passed. Pending batch refresh.

Section 10.8 applicability labels: Standardized gap before parentheses to 0.50em for all six body/summary instances. XML, text-content, and spacing checks pass. Pending batch refresh.

- 2026-10-06: Chapter 10 Exercise 2 reworded to state explicitly that magnetic field lines cannot cross, retaining the direction-at-a-point reasoning prompt. Pending next preview refresh.

- 2026-10-06: Chapter 10 Exercise 3 replaced with the approved compare-and-contrast prompt: two similarities and two differences, including one of each about interaction with matter. Pending next preview refresh.

- 2026-10-06: Chapter 10 Exercise 5 revised with the approved field-direction, field-strength, and horizontal-compass questions. Retains the rhetorical strength question. Pending next preview refresh.

- 2026-10-06: Using preview 83 numbering throughout the current review: removed Exercises 8, 10, 12; retained 7, 9, 11 and added the sign-reversal comparison to 7. Replaced Exercise 13 with maximum magnetic force and acceleration for a laboratory electron beam (8.0e6 m/s, 1.0e-3 T), with electron constants supplied. Internal numerical answers and physical-scale checks recorded in chapter10-structure/review-round-exercise-changes.json. Pending next preview refresh.

- 2026-10-06: Added approved circular-path radius part (c) to preview 83 Exercise 13; verified r = 0.04555 m, rounded to 4.6 cm. Maintainer identifies this problem as approximately the upper end of Chapter 10 calculation difficulty. Pending next preview refresh.

- 2026-10-06: Removed preview 83 Exercise 18 (refrigerator AC versus car-starting DC compass comparison), as approved. Continue using preview 83 numbers for this review round. Pending next preview refresh.

- 2026-10-06: Removed preview 83 Exercises 20 and 21 as approved, retaining 19. Continue using preview 83 numbers for this review round. Pending next preview refresh.

- 2026-10-06: Removed preview 83 Exercise 22 (lightning force). Plasma current does experience magnetic force, but the calculation does not establish visible bending; research nuance recorded in the review-round report. Pending next preview refresh.

- 2026-10-06: Replaced preview 83 Exercise 24 MHD-drive calculation with MRI gradient-coil segment force (100 A, 5.0 cm, 1.5 T perpendicular; answer 7.5 N). Acoustic-noise context checked against Siemens description; no scanner-specific specifications implied. Pending next preview refresh.

- 2026-10-06: Replaced preview 83 Exercise 26 with approved two-coil switching question. Pending next preview refresh.

- 2026-10-06: Removed preview 83 Exercises 30 and 31 as approved. For the later MyOpenMath-oriented addition pass, aim for at least one conceptual question per section, with more where natural; Section 10.10 now needs coverage. Keep current preview numbering during review. Pending next preview refresh.

- 2026-10-06: Replaced preview 83 Exercise 36 with conceptual transformer inefficiency question on winding resistance, eddy currents, and insulated laminations; classified as conceptual. Other proposed transformer removals remain pending approval. Pending next preview refresh.

- 2026-10-06: Approved transformer selection: retain old 32/33 with ideal-model wording, retain conceptual 36, replace 38 with conceptual transmission question; remove 34/35/37/39. Rebuild and refresh with automatic renumbering; subsequent review uses updated numbers.

- 2026-10-06: Replaced preview 84 Exercise 27 with approved AC-grid question emphasizing transformers for high-voltage transmission and lower-voltage supply to users. Pending next preview refresh.

- 2026-10-06: Replaced preview 84 Exercise 29 with indoor-light stroboscopic effect on a rapidly moving hand or meter stick. Verified against DOE hand-waving demonstration: https://www.energy.gov/cmei/ssl/flicker-demonstration . Bright phases emphasize successive positions; dim intervals create less visible intervening motion. Constant illumination does not produce this illumination-driven effect. Pending next preview refresh.

- 2026-10-06: Simplified preview 84 Exercise 29 closing prompt to “Explain this effect.” Removed brightness-variation hints. Pending next preview refresh.

- 2026-10-06: Replaced Section 10.12 unfulfilled superconductivity forward reference with approved standalone maximum-current statement. Pending next preview refresh.

- 2026-10-06: Updated preview 84 Exercise 33 office AC schedule to 8.0 hours/workday for 22 workdays and assumed electricity price 35.0 cents/kWh. Verified 176 h, 8800 kWh, $3080 unrounded cost; effective resistance unchanged at 3.32928 ohms. Pending next preview refresh.

- 2026-10-06: Preview 84 Exercise 33 now uses 208 V and asks for rms current, with explicit single-phase/in-phase approximation to support P_avg = V_rms I_rms. Verified current 240.3846 A (240 A to three significant figures); cost unchanged. Pending next preview refresh.

- 2026-10-06: Explicitly labeled Exercise 33 supply as 208 V rms. Pending next preview refresh.

- 2026-10-06: Applied approved Exercise 33 wording: resistor approximation in part (a), replacing separate single-phase/in-phase sentence; smoothed schedule wording in part (b). Answers unchanged. XML validated; pending next preview refresh.

- 2026-10-06: Applied Chapter 10 conceptual-gap pass: nine additions (eight aligned with frozen MyOpenMath objectives and one introduction overview), geology moved to 10.3, transformer conceptual-first ordering, and approved heater merger. 45 questions; every section has a conceptual question. See reports/1.1/chapter10-structure/mom-review-question-set.md for numbering, source locators and new/merged internal answers. Pending preview refresh.

- 2026-10-06: Chapter introductions are excluded from the at-least-one-conceptual-question goal. Moved preview 85 Exercise 1 to 10.2 Magnets, removing its reference to this introduction. Audit of all Chapter.1 pages (0.1 through 14.1): no other exercises on those pages. Numbering remains unchanged; pending batch preview refresh.

- 2026-10-06: Approved preview 85 Exercise 25 split into three parts: straight wire, circular loop compared with bar magnet, and long-solenoid interior. Updated internal answer; XML valid. Pending batch refresh.

- 2026-10-06: Added approved eddy-current question after preview 85 Exercise 31, now Exercise 32; following questions shift by one. Total 46. Internal answer and MyOpenMath provenance recorded. Refresh includes Exercise 1 relocation and three-part Exercise 25.

## Chapter 10 finalized; Chapter 11 prepared (2026-10-06)

Maintainer finalized Chapter 10 after preview 86, including all 46 exercises. Chapter 11 structural organization authorized: collect glossary and summaries, normalize question group headings, preserve all existing exercise content and IDs. Chapter introductions remain excluded from exercise coverage targets. Deferred Section 11.5 blackbody/emissivity reminder carried into chapter11-structure/review.md.

Preview 87 published successfully: Chapter 11 organized, 52 questions with sequential numbering verified, 74 glossary definitions and 10 summaries. Course/CNX builds and source/link validation passed. Chapter 10 finalized. No canonical GitHub push.

- [ ] 2026-10-06: Chapter 11 duplicate glossary review deferred by maintainer. Check definitions in 11.4/11.6 and repetition in 11.5/11.10; nine duplicate terms, six identical pairs and three differing pairs (radio waves, infrared, gamma ray). No consolidation authorized at this stage. Details: reports/1.1/chapter11-structure/review.md.

- 2026-10-08: Approved demotion of model in Section 1.4: removed duplicate glossary definition and changed body term to ordinary inline text, preserving its anchor. Chapter 0 definition unchanged. No references to removed definition IDs found; XML validated. Pending batch preview refresh.

- 2026-10-08: Glossary headings disambiguated: meter (unit of length) in 0.3, moving-coil meter in 10.7 with approved concise definition. First relevant body term now Moving-coil meters; Motors and Meters title and later meter shorthand preserved. XML validated; pending batch preview refresh.

- 2026-10-08: Removed redundant vector glossary entry in 9.5 and acceleration/free-fall entries in 2.4. Body term markup demoted where present; earlier definitions in 1.3, 1.5, and 1.7 retained. Vector addition remains a distinct glossary entry. XML validated; pending batch refresh.

- 2026-10-08: Removed duplicate deformation glossary entry in 3.6 and demoted corresponding body term markup; Section 2.7 definition retained. XML validated; pending batch refresh.

- 2026-10-08: Removed mechanical energy glossary duplication in 9.6; Chapter 3 definition retained. Body and summary conservation wording need review: definition currently conflates KE+PE with conservation; summary says this sum is a constant without conditions. Prose not yet changed. Pending batch refresh.

- 2026-10-08: Applied approved combined conservation paragraph in 9.6, preserving wording where possible and qualifying mechanical energy conservation. Removed redundant inline equation; displayed equations and source anchors retained. Summary bullet still awaiting review. XML validated; pending preview refresh.

- 2026-10-08: Approved 9.6 summary bullet now states that mechanical energy is constant when only conservative forces do work. Conservation prose/summary review resolved. XML validated; pending batch preview refresh.

- 2026-10-08: Removed repeated Ohm’s law and resistance glossary entries in 9.11; body term markup demoted, earlier 9.9 definitions retained. Inconsistent resistance wording appeared only in the removed definition, not prose. XML validated; pending batch refresh.

- 2026-10-08: Preview 88 published: all approved glossary demotions/disambiguation and 9.6 conservation prose/summary corrections; added Chapter contents return links below all 15 exercise-page headings. Builds/source/link checks passed. Chapter 11 duplicate terms remain untouched for review. No canonical GitHub push.

- 2026-10-08: Extended shared inline-math punctuation grouping to opening parentheses/brackets immediately preceding math, including preceding-sibling tails and math-only inline wrappers. Existing closing punctuation handling retained; MathML/copy payloads unchanged. Nine unit regressions pass; generated 11.2 hertz example confirms opening parenthesis inside group. Pending batch preview refresh.

- 2026-10-08: Normalized 11.5 inline photon energy: moved parentheses to prose, removed forced italic wrapper, changed Latin v to Greek nu. Adjacent Eq. 11.5.5 photon term likewise uses variable h and nu. XML validated; pending batch refresh.

- 2026-10-08: Removed remaining forced-italics MathML in 11.5: LC resonance in opening microwave paragraph. Natural variable italics retained. Section scan confirms no remaining explicit italic MathML attributes; XML valid. Pending batch refresh.

- 2026-10-08: Table 11.7.1 gas heading: 1 atm converted to inline MathML with thin number-unit spacing and upright unit. XML validated; pending batch preview refresh.

- 2026-10-08: Split 11.9 lens-example givens into separate d_o = 0.750 m and f = 0.500 m math expressions with prose and. XML valid; queued for batch refresh.

- 2026-10-08: Global embedded-prose MathML scan completed (tools/audit_math_prose.py): 6,721 expressions, 28 flags: six inline split candidates, fourteen displayed connector cases, eight descriptive-label cases. No source changes from audit. Review report: reports/1.1/math-prose-audit/review.md.

- 2026-10-08: Split Eq. 4.5.4 example givens into four expressions with commas/and outside math; normalized decimals and units. Display anchor and current numbering retained pending the next audit. XML validated; pending batch refresh.

## Next after connector review: equation-numbering audit (approved 2026-10-08)

Perform immediately after the current embedded-connector review. Policy: number important laws, definitions, reusable results and explicitly referenced equations; normally leave lists of givens, routine substitutions, intermediate arithmetic and repeated summary formulas unnumbered. Review derivations and worked-example results individually. Check internal references before removing numbers, preserve stable anchors, and validate shifted numbering. Eq. 4.5.4 is an approved example of a givens list suitable for unnumbered display. Author accepts numbering shifts in major revision 1.1 and will check outside references, especially MyOpenMath, after this revision. Do not change live MyOpenMath content. This is workflow sequencing, not a scheduled automation.

- 2026-10-08: Eq. 5.2.2 split into two hertz definitions with prose or, replacing manual MathML connector spacing. Stacked fractions and current equation number retained. XML valid; pending batch refresh.

- 2026-10-08: Section 7.4 pressure alternatives: lb/in^2 and psi are separate inline MathML expressions; or and both parentheses moved to prose. XML validated; pending batch refresh.

- 2026-10-08: Eq. 8.10.9 now uses 0.408 = 40.8%. Removed ten conflicting forced-italic wrappers around upright Eff across four modules, including formula appendix; natural variable styling retained. XML validated; pending batch refresh.

- 2026-10-08: Eq. 8.11.4 now gives 0.476 = 47.6%, replacing the prose connector; numeric tokens normalized and stale annotation removed. XML validated; pending batch preview refresh.

- 2026-10-08: Split five composite expressions in 9.6: both displayed potential-energy relationships and their summary repeat, four initial/final energy values, and q/V/m list. Connectors and sentence punctuation now prose; equation IDs/numbers retained. XML and expression counts validated. Loop applicability note in 10.8 left pending discussion. Pending batch preview refresh.

- 2026-10-08: Moved 10.8 straight-wire, loop-center, and solenoid applicability labels to prose within their equation containers, in body and summary (six occurrences). Removed stale annotations; formulas and IDs preserved. XML validated.

- 2026-10-08: Preview 89 published successfully with all batched corrections since preview 88, including connector splits and six 10.8 applicability labels outside MathML. Course/CNX builds and source/link checks passed; generated label placement checked. Fresh visual browser QA not performed. No canonical GitHub push.

- 2026-10-08: Eq. 11.5.6 split into two reaction expressions with prose and and terminal punctuation. Chemical tokens normalized, stale annotation removed; equation ID/number preserved. XML and expression boundaries validated. Pending batch preview refresh.

- 2026-10-08: Eq. 12.4.1 applicability note moved to prose; Eq. 12.4.2 uses stacked h/p and numerical quotient with normalized numeric/unit tokens. Values, IDs, and numbering preserved. XML and fraction structure validated. Pending batch preview refresh.

- 2026-10-08: Split Eq. 12.5.2 with prose comma/where and terminal period; removed 33 explicit italic MathML attributes throughout m67804, including summary/exercises. Natural variable italics retained. XML, expression boundaries, and absence of remaining explicit italic attributes verified. Pending batch preview refresh.

- 2026-10-08: Eq. 12.7.2 now specifies R = 1.097 x 10^7 m^-1 directly, with upright unit and thin number-unit spacing. Redundant alternate notation and stale annotation removed; value and numbering unchanged. XML validated. Pending batch preview refresh.

- 2026-10-08: Eq. 14.5.21 electron-capture note moved outside MathML with ordinary prose spacing; stale annotation removed. Formula and numbering preserved; XML valid.

- 2026-10-08: Preview 90 published with batched corrections since 89: ozone reaction split, matter-wave label/fractions, uncertainty connector/italic cleanup, Rydberg unit, electron-capture note. Course/CNX builds and source/link validation passed; generated note outside MathML verified. Fresh visual browser QA not performed. No canonical GitHub push.

- 2026-10-08: Section 14.10 uranium-235 parenthetical now has only the nuclide in MathML, with article and parentheses in prose. Prescript retained, stale annotation removed; XML valid. Pending batch preview refresh.

- 2026-10-08: Atomic Masses table: deuterium and tritium alternatives now separate MathML symbols with prose or within each cell. Upright chemical symbols and proper mass-number prescripts retained; stale annotations removed. XML valid. Pending batch preview refresh.

- 2026-10-08: Connector review closed. Follow-up scan: 6,738 expressions / 141 modules; eight remaining flags all approved word equations, quantity labels, or unit names. Recorded dispositions in reports/1.1/math-prose-audit/post-review/disposition.md. No unresolved scan flags. Original review snapshot preserved. Fission and Atomic Masses fixes await next refresh. Equation-numbering audit is next approved work.

- 2026-10-08: Read-only equation-numbering audit produced tools/audit_equation_numbering.py and reports/1.1/equation-numbering-audit/. Inventory: 1,488 display objects across 141 modules, including 877 visible numbered equations and 478 table-math displays. Found 103 hidden summary labels still consuming course counters; 8 equation targets have structured incoming references. Editorial triage groups 340 worked calculations as likely number-removal candidates, 153 worked symbolic steps/results for individual review, and 28 unnumbered non-table displays for inspection. These are provisional recommendations, not approved bulk removals. No source numbering, build, or preview changes.

- 2026-10-08: Implemented summary-number reuse through maintained/numbering.json stable-ID aliases: 38 unique exact same-section matches; 67 unmatched/ambiguous summary displays left unnumbered and flagged in reports/1.1/equation-numbering-audit/summary-review.md. Summary equations excluded from counters in both profiles, and renderer displays aliased labels. Dynamic alias regression passes; course/CNX builds and source/link validation pass. No preview refresh. Next suggested policy example: dragster displacement Eqs. 1.6.18-21 (repeated law, simplified relation, substitution, final numerical result).

- 2026-10-08: Approved removal of numbers from current-preview Eqs. 1.6.18-21: four dragster displacement displays now class unnumbered. Math and anchors unchanged. Continue referring to published preview numbers during body-numbering review; local subsequent labels shift. Summary aliases reviewed after body decisions. No preview refresh.

- 2026-10-08: Approved removal of numbers from preview Eqs. 1.6.15-16; 1.6.17 result retains numbering. XML valid; no summary aliases target removed numbers. Section 1.6 italic scan found 35 explicit attributes across 28 expressions (24 mi, 11 mstyle); reported, not changed. Preview unchanged.

- 2026-10-08: Section 1.6 removed 35 explicit italic attributes; replaced 31 hyphen accents with stretchy U+00AF overbars. XML valid and all overbars verified to copy as LaTeX overline / ASCIIMath bar. No preview refresh; visual rendering awaits batch review.

- 2026-10-08: Book-wide overbar scan: fixed 47 remaining hyphen accents in five modules (m42674:18, m42680:5, m67033:18, m71407:4, m76603:2), in addition to 31 prior Section 1.6 fixes. Only mover accent encoding changed; variable/particle identity preserved. XML and LaTeX/ASCIIMath overbar conversion verified; no hyphen/minus mover accents remain. Preview unchanged.

- 2026-10-08: Authorized book-wide body-numbering pass complete: 615 additional displays unnumbered across 78 modules, 256 numbered body displays remain. Four borderline worked-example results retained pending judgment; two optional unnumbered-body additions flagged. Eight internal equation-reference targets retained. Recomputed summary aliases: 91 clear matches, 14 review cases. Full preview/local crosswalk and dispositions in reports/1.1/equation-numbering-audit/. XML content/anchors preserved; both builds, source/link validation, alias regression and all body/summary-label checks passed. Preview unchanged; ready for summary-number match review after small body exception list.

- 2026-10-08: Author retains preview Eq. 2.10.8 (m67036#eip-99); body decision and crosswalk updated. Removed all three explicit italic MathML overrides in Section 2.10; normal variable italics retained. XML valid. Preview unchanged. Three borderline body formulas remain.

- 2026-10-08: Author retains preview Eq. 4.6.4 and removes number from 6.4.17. Removed all twelve explicit italic MathML overrides in Section 6.4; normal variable italics retained. XML, both numbering profiles, and summary aliases validate; local crosswalk refreshed. Preview unchanged. Only 9.6.18 remains among four borderline body formulas.

- 2026-10-08: Author retains preview Eq. 9.6.18 for recurring quantitative use. All four borderline numbered body formulas resolved: retain 2.10.8, 4.6.4, 9.6.18; unnumber 6.4.17. Source already retained 9.6.18; dispositions updated. Ready for 14 summary-number review cases. Preview unchanged.

- 2026-10-08: Summary review #1-10 resolved. #1-7/#9 remain unnumbered. #8 parallel-resistance body and summary normalized (R_3, ellipsis, upright p), with shared number. #10 summary proton q/m corrected to 9.58 x 10^7 C/kg and linked to body; stale annotations removed. Summary aliases now 93. #11 angular-momentum summary pending discussion; #12-14 pending. XML valid; preview unchanged.

- 2026-10-08: Summary review #11 resolved: Section 12.7 summary now L = n hbar and aliases m67807#eip-866. Section 12.8 expanded expression and alias retained. XML and both numbering profiles validated; 94 aliases total. #12-14 remain. Preview unchanged.

- 2026-10-08: Summary review #12 resolved: m42535#eip-584 shares number with m42535#eip-772 (preview 13.4.7), retaining both square-root and gamma-factor forms in summary. Both numbering profiles validate. 95 summary aliases; #13-14 remain. Preview unchanged.

- 2026-10-08: Summary review #13 resolved: m52466#eip-120 uses 931.5 MeV/c^2 instead of 931.46; combined conversion remains unnumbered. XML valid; no summary alias assigned. Only #14 remains. Preview unchanged.

- 2026-10-08: Summary review #14 resolved: m52471#eip-705 now matches both forms from body eip-732 (exact ln(2), approximate 0.693) and reuses its number. All 14 summary-review cases resolved; 96 aliases. XML valid. Preview unchanged.

- 2026-10-08: Equation-numbering global review closed. Final checks: course/CNX builds, source/link validation and alias regression pass; 877 body dispositions and 96 summary aliases verified in both profiles. All author decisions resolved; nine summary displays intentionally unnumbered. Preview unchanged. External MyOpenMath reference checks remain for author after publication, as agreed.

### 2026-10-08 — Preview 91 refreshed

Published the completed equation-numbering review and pending MathML corrections as Sites version 91 (commit fb1e978333f37b4cd49ea7612bde81cf9d7f4341). Publication succeeded. Body equations now have 255 retained numbers and 622 removed numbers; 96 summary displays reuse body labels and nine remain intentionally unnumbered. Both builds, full validation, summary-numbering regression tests, and audit verification passed before packaging. Receipt: reports/1.1/preview91-receipt.json. Resume review at Section 11.9, Image Formation by Lenses.


### 2026-10-08 — Equation display-style default

Global audit found 1000 math expressions inside equation blocks: 953 omitted display settings and 47 explicitly used block display; none explicitly requested compact style. Renderer now supplies displaystyle=true within equation ancestry, retaining inline layout for separated formulas and prose connectors. Paragraph math stays inline; explicit style overrides are preserved. Source MathML and numbering are unchanged. Added regression coverage for equation versus paragraph style, source preservation, and explicit compact overrides. Audit: reports/1.1/equation-display-style-audit.json. Preview publication deferred until requested.


### 2026-10-08 — Preview 92 refreshed

Published the global equation display-style renderer correction as Sites version 92, commit 91fb307ceceb561d67a28134634a07afacc38da2. Deployment succeeded. Numbering unchanged. Receipt: reports/1.1/preview92-receipt.json. Opened Section 11.10 for user visual review.


### 2026-10-08 — Section 11.10 forced italics

Removed five explicit MathML fontstyle="italic" attributes on R, T, and m in m67135. Native variable italics and prose emphasis remain. Source correction: C11-MIRRORS-FORCED-ITALICS. Pending next preview refresh.

### 2026-10-08 — Remove inherited PhET explorations

Removed Radioactive Dating Game from Radiation Detection and Detectors (m42627) and Simplified MRI from Medical Imaging and Diagnostics (m42649), including their box content and external links. No incoming source references target removed IDs. Historical Preface note retained. Corrections: C14-REMOVE-PHET-M42627 and C14-REMOVE-PHET-M42649. Pending next preview refresh.

### 2026-10-08 — Polarization caption spacing

Figure 11.11.7: reduced two explicit 0.25em spaces around cos to normal 0.167em thin spaces. Correction C11-POLARIZATION-CAPTION-COS-SPACING. XML verified; pending preview refresh.

### 2026-10-08 — Chapter 11 glossary duplicates

Removed the later electromagnetic spectrum, microwaves, ultraviolet radiation, visible light, X-ray, and law of reflection definitions at author request. Gamma ray, infrared radiation, and radio waves pairs left unchanged pending discussion. Pending preview refresh.

### 2026-10-08 — Gamma-ray terminology in prose

Applied the two approved Section 11.5 prose edits distinguishing nuclear-transition terminology from astronomical usage. Applications discussion retained. Correction C11-GAMMA-RAY-NAMING-CONVENTIONS. Radio-wave prose and three glossary consolidations remain pending. XML validated; preview refresh pending.

### 2026-10-08 — Radio-wave introduction

Applied the approved first two sentence replacements in Section 11.5, retaining the astronomical example and remainder of the paragraph and term anchor. Correction C11-RADIO-WAVES-INTRODUCTION. XML validated; pending preview refresh.

### 2026-10-08 — Complete Chapter 11 glossary consolidation

Updated the first-introduction definitions in m67132 for gamma ray (nuclear convention with astronomical clarification), infrared radiation, and radio waves. Preserved earlier definition and meaning IDs; removed the three later copies from m67133. Pending preview refresh.

### 2026-10-08 — Remove analog-TV audio exercise

Removed m67133#fs-id1169737739134 (previous Chapter 11 Exercise 1) at author request. Remaining exercises renumber through the existing renderer. Correction C11-REMOVE-ANALOG-TV-AUDIO-EXERCISE. Pending preview refresh.

### 2026-10-08 — Remove cataract UV exercise

Removed m67133#fs-id1169737770298 (published Chapter 11 Exercise 2) at author request. Updated expected projected exercise total to 845. Correction C11-REMOVE-CATARACT-UV-EXERCISE. Pending preview refresh.

### 2026-10-08 — Focus wavelength/detail exercise

Replaced the prompt in m67133#fs-id1169737895295 with the approved comparison of ultraviolet and visible-light microscopes. Exercise identity and numbering retained. Correction C11-MICROSCOPE-WAVELENGTH-EXERCISE. XML validated; pending preview refresh.

### 2026-10-08 — MRI spatial-resolution exercise

Replaced m67133#fs-id1169737979416 (published Exercise 11) with a question about resolving details smaller than the radio wavelength by varying magnetic field with position and distinguishing signals. Supported by the existing MRI aside; exercise IDs retained. Correction C11-MRI-SPATIAL-RESOLUTION-EXERCISE. XML validated; pending preview refresh.

MRI exercise follow-up: replaced the second sentence with "Explain how this is possible." to remove the answer hint. Correction C11-MRI-EXERCISE-REMOVE-HINT; XML validated.

### 2026-10-08 — Lightning delay question

Replaced only the second part of m52454#fs-id1553873 (published Exercise 16) with the approved question asking whether the flash/thunder delay suffices and what additional information is needed. Intended answer: sound speed and independently measured distance, assuming simultaneous emission. First part and IDs unchanged. Correction C11-LIGHTNING-SPEED-QUESTION. XML validated; pending preview refresh.

### 2026-10-08 — Remove thermometer exercise and figure

Removed m52454#fs-id2104353 (published Exercise 20) and its enclosed figure/image/caption. No incoming source references. Expected exercise total now 844. Correction C11-REMOVE-THERMOMETER-EXERCISE. Pending preview refresh.

### 2026-10-08 — Remove negative-index exercise

Removed m52454#fs-id1692299 (published Exercise 21) at author request. Expected projected exercise total now 843. Correction C11-REMOVE-NEGATIVE-INDEX-EXERCISE. Pending preview refresh.

### 2026-10-08 — Lunar ranging atmospheric model

Revised m52454#fs-id1574374 to use an 8.0 km equivalent uniform atmospheric layer, Moon overhead, station-to-reflector distance 3.84e8 m, and an explicit percentage distance overestimate. Model yields 2.344 m excess inferred distance and 6.10417e-7 percent (two significant figures: 6.1e-7 percent). Correction C11-LUNAR-RANGING-ATMOSPHERE. Pending preview refresh.

### 2026-10-09 — Submerged converging lens exercise

Replaced m67134#fs-id3094309 (published Exercise 34) with the approved wording specifying a converging glass lens moved from air into water and asking how its focal length changes. IDs retained. Correction C11-SUBMERGED-LENS-EXERCISE. XML validated; pending preview refresh.

### 2026-10-09 — Chapter 11 review pause and handoff

Publish current approved edits before pausing. Resume after the submerged converging glass lens question (old preview Exercise 34, m67134#fs-id3094309); next section is 11.10 Image Formation by Mirrors (old Exercise 35). Remaining work: finish Chapter 11 exercise review, incorporate selected MyOpenMath questions, and consider question additions for sections with no questions. No automatic MyOpenMath edits authorized. A second visual pass of the whole book is planned after the first pass. Earlier blanket refractive-index-at-least-one wording remains a potential follow-up, not yet revised.


### 2026-10-09 — Preview 93 published

Published all approved edits since preview 92. Sites commit e421891747d7696108636e1024f1775dab6cc6d3; deployment succeeded. Both full builds and validation passed with zero reported issues (6731 math expressions, 548 images, 11173 source IDs). Receipt: reports/1.1/preview93-receipt.json. Resume Chapter 11 review at Section 11.10, newly numbered Exercise 31 (formerly 35), following the submerged-lens question now numbered 30. Remaining review, MyOpenMath incorporation, and possible additions for sections without questions are deferred until the user returns.


### 2026-10-09 — Seeing a real image

Reworded m67135#fs-id1622392 (preview 93 Exercise 33) to ask whether a real image can be seen without projecting it onto a screen, with an explanation. Correction C11-SEEING-REAL-IMAGE-EXERCISE. XML validated; pending preview refresh.

### 2026-10-09 — Remove image-distance notation recall

Removed m67135#fs-id1677882 (preview 93 Exercise 34) with author approval; retained the following focal-point question. Expected exercise total now 842. Correction C11-REMOVE-IMAGE-DISTANCE-RECALL. Pending preview refresh.

### 2026-10-09 — Real-image magnification wording

Replaced case 1 image with real image in m67135#fs-id1362775 (preview 93 Exercise 37), removing the unnecessary always qualifier. Correction C11-REAL-IMAGE-MAGNIFICATION-WORDING. XML validated; pending preview refresh.

### 2026-10-09 — Two-part mirror magnification question

Replaced m67135#fs-id1362775 (preview 93 Exercise 37) with approved parts (a) and (b): interpret negative magnification for the larger image in Figure 11.10.4, then draw a ray diagram showing a smaller real image with the same mirror. Figure linked through source ID import-auto-id3163149; no arbitrary case label. Correction C11-MIRROR-MAGNIFICATION-TWO-PART. XML and link target verified; pending preview refresh.

### 2026-10-09: Remove unsupported reflection-phase exercise

Removed m52456#fs-id1169737764823 (preview 93 Exercise 43) with author approval. The text does not supply the reflection-phase material needed to answer it. Correction C11-REMOVE-REFLECTION-PHASE-EXERCISE. Updated expected projected exercise count from 842 to 841. Pending preview refresh.

### 2026-10-09: Complete Chapter 11 existing-exercise review

Combined preview 93 Exercises 47 and 48 into approved three-part scattering question: demonstrate polarization with a filter, interpret wavelength dependence to explain blue sky, and explain sunset color with atmospheric path-length information supplied. Correction C11-COMBINE-SCATTERING-COLOR-EXERCISES. Expected exercise count 840. Existing Chapter 11 exercise review complete; next stage is review/adaptation of MyOpenMath candidates and coverage gaps, including sections without questions. Pending preview refresh.

### 2026-10-09: First Chapter 11 MyOpenMath additions

Applied all five approved candidates: Maxwell laws (11.2); accelerating charges and transverse fields (11.3); frequency/wavelength comparison and red/blue light (11.4). Stable provenance and internal answers are in reports/1.1/chapter11-structure/mom-empty-section-candidates.json. Expected projected count 845. Section 11.1 is a chapter introduction and excluded from substantive-section coverage gaps. Radiation-pressure application remains a proposal, not an approved addition. Pending preview refresh.

### 2026-10-09: IKAROS application

Added approved two-part IKAROS radiation-pressure question in 11.3, avoiding rest-mass terminology. New textbook prompt motivated by lecture 577 momentum objective, not a copied MOM application. Correction C11-IKAROS-RADIATION-PRESSURE. Expected count 846; pending preview refresh. Next candidate review: reflection/dispersion, then remaining optics and polarization families, screened against retained exercises.

### 2026-10-09: Reflection and dispersion additions

Added approved curved-mirror local-normal question (MOM locator 606) to 11.6 and prism color separation question (607) to 11.8. Expected exercise count 848; pending preview refresh.

### 2026-10-09: Remaining approved optics additions

Added windowpane ray tracing (11.7), lens classification/rays (11.9), and polarization/glare (11.11). Expected count 851. Prism question still under discussion; no prism candidate or live MOM edits applied. Pending preview refresh.

### 2026-10-09: Complete Chapter 11 MyOpenMath review

Added approved transparent-prism diagram question with newly drawn SVG and no glass specification. Author reports live MOM 604/699 wording fixed. Excluded additive color mixing, Cherenkov radiation, and Fresnel lenses by author decision. Expected count 852. Preparing preview refresh.

Preview 94 published successfully on 2026-10-09 (Pacific), including completed Chapter 11 existing-exercise and MyOpenMath review. Full builds and validation passed; 852 projected exercises, 549 images. Receipt: reports/1.1/preview94-receipt.json. New prism SVG rendered and visually checked; local browser preview could not connect, so browser-page QA was unavailable.

### 2026-10-09: Chapter 11 finalized; Chapter 12 organization

Author finalized Chapter 11 after Preview 94; retain current set without length-driven cuts. Chapter 12 organization collects 27 glossary terms, seven summaries, and 80 existing exercises at chapter end in section order. All exercise wording/figures/IDs preserved. No duplicate glossary terms found. See reports/1.1/chapter12-structure/review.json for section inventory and follow-ups. Section 12.1 is the introduction and not an exercise gap. Author section review starts next; MyOpenMath and exercise selection follow later.
Preview 95 published successfully: Chapter 12 organization ready for section review. Both builds, source/link validation, and sequential numbering of all 80 Chapter 12 exercises passed. No new browser visual audit performed for this organization-only change.

### 2026-10-10: Chapter 12 finalized; Chapter 13 review preparation

Maintainer finalized Chapter 12 after Preview 107 with 56 exercises and all approved MyOpenMath-oriented additions. No pending Chapter 12 wording decisions. Figure 12.3.2 apparatus photo replacement remains an explicitly deferred asset task: await maintainer photo and update its credit/caption/alt text together; continue reminders at every chapter finalization. Preparing Chapter 13 by collecting glossary, summaries, and all 94 existing chapter-end exercises in section order, preserving question content and IDs and retaining five inline Check Your Understanding prompts. Numerical-review flags: m42542/fs-id1346384 negative scientific-notation base; m42546 Equation 13.7.15 electron-mass inconsistency. Four remaining explicit Unreasonable Results exercises are flagged for upcoming review. No Chapter 13 pruning or MyOpenMath additions in this organization pass.

2026-10-10: Removed all 80 forced italic MathML attributes throughout Section 13.3 (m42531), including repeated summary/glossary and exercise expressions. XML comparison confirms only these attributes changed; natural variable styling retained. Pending next preview refresh.

2026-10-10: Section 13.3 low-speed-limit paragraph now uses the proper much-less-than MathML operator (v ≪ c), replacing literal doubled less-than text; annotation synchronized. Pending next preview refresh.

2026-10-10: Math copying maps much-less/greater-than operators to LaTeX ll/gg; ASCIIMath retains Unicode under existing fallback policy. Unmapped Unicode operators now trigger the copy-dialog compatibility note. Focused conversion checks passed; pending preview refresh.

2026-10-10: Section 13.3 particle-lifetime solution (import-auto-id1744942) split before final equals sign into two aligned rows. Mathematical tokens unchanged. Pending next preview refresh.

2026-10-10: Removed all 16 forced italic MathML attributes throughout Section 13.4 Length Contraction (m42535). XML comparison confirms only those attributes changed; natural variable styling retained. Pending next preview refresh.

2026-10-10: Both opening muon distance calculations in Section 13.4 now use three aligned rows (formula, substitution, result). Mathematical tokens preserved; pending next preview refresh.

2026-10-10: Corrected minus to equals in Section 13.4 Alpha Centauri example known value L_0 = 4.300 ly. XML valid; pending next preview refresh.

2026-10-10: Fixed Chromium native MathML rcl table alignment globally: added -webkit-right/-webkit-center fallbacks, matching the existing two-column workaround. Source columnalign was already correct. Browser verification of m42535 eip-115 at 487px shows gamma and 30.00 right edges both 240.890625px (previously gamma 206.796875px). Screenshot: reports/1.1/chapter13-structure/rcl-alignment.png. Pending preview refresh.

2026-10-10: Section 13.4 low-velocity discussion now uses v ≪ c with proper MathML operator. XML and LaTeX/ASCIIMath conversion checks passed; pending next preview refresh.

2026-10-10: Section 13.4 Check Your Understanding solution now has three aligned rows (formula, substitution, result). Mathematical tokens preserved; pending next preview refresh.

2026-10-10: Removed all 30 forced italic MathML attributes throughout Section 13.5 (m42540). XML comparison confirms only those attributes changed; natural variable styling retained. Pending next preview refresh.

2026-10-10: Corrected Section 13.5 backward-snowball sum MathML grouping and operator forms for proper binary plus/equality and unary minus spacing. Tokens preserved; pending next preview refresh.

2026-10-10: Fixed MathML grouping and sign spacing in Section 13.5 canister part (b) substitution (eip-115). Mathematical tokens and four-row layout preserved; pending preview refresh.

2026-10-10: Removed stray leading equals sign from Eq. 13.5.3 (eip-158); lambda is now a proper MathML identifier. XML valid; pending next preview refresh.

2026-10-10: Section 13.5 space-probe Doppler check solution now uses three aligned rows. Source-frequency equality grouping corrected; tokens preserved. Pending preview refresh.

2026-10-10: Removed all eight forced italic MathML attributes throughout Section 13.6 (m42542). XML comparison confirms only those attributes changed; natural variable styling retained. Pending next preview refresh.

2026-10-10: Section 13.6 electron momentum check solution split into three aligned rows before last two equals signs. Mathematical tokens preserved; pending preview refresh.

2026-10-10: Section 13.7 fourth learning objective now uses lowercase mathematical c for the speed of light. Pending preview refresh.

2026-10-10: Book-wide learning-objective audit inspected 321 objective items across the 140-module course map. Converted F and E in 9.4 and gamma in 13.3 to MathML; c in 13.7 was already corrected. Wording unchanged. Flagged missing particle name in 14.12 for review. Report: reports/1.1/objectives-math-audit.json. Pending preview refresh.

2026-10-10: Example 13.7.2 battery statement now renders (A·h) as plain text, consistent with other units. XML and text-preservation checks passed; pending preview refresh.

2026-10-10: Removed all 20 forced italic MathML attributes throughout Section 13.7 (m42546). XML comparison confirms only those attributes changed; natural variable styling retained. Pending next preview refresh.

2026-10-10: Battery unit-conversion calculation eip-835 now closes the initial factor after h and stacks C/s, keeping multiplication by hours outside the fraction. Pending preview refresh.

2026-10-10: Net-work derivation eip-888 now breaks before final equality into two aligned lines. Tokens preserved; pending preview refresh.

2026-10-10: Added approximation signs to three low-speed expansion/kinetic-energy steps and five rounded final evaluations in the following comparison example. Exact algebraic equalities preserved. Pending preview refresh.

2026-10-10: Section 13.7 classical-limit paragraph now uses proper much-less-than operator v ≪ c. XML and both copy formats verified; pending preview refresh.

2026-10-10: Wrapped long substitution in eip-971 before squared c value, with indented multiplication continuation row. Values preserved; pending preview refresh.

2026-10-10: Classical kinetic-energy substitution eip-95 wrapped before squared speed-of-light factor using indented multiplication continuation. Pending preview refresh. Existing 9.00 vs 9.11 electron-mass review flag remains.

2026-10-10: Removed standalone Problem-Solving Strategies for Relativity box fs-id2607341 from 13.7. Worked-example Strategy subsections retained; these also occur throughout earlier chapters. Pending preview refresh.

2026-10-10: Energy check solution eip-id1537888 wrapped before numerical c-squared factor with indented multiplication continuation; final equality on separate row. Pending preview refresh.

2026-10-10: Preview 109 published all pending Chapter 13 section corrections and learning-objective MathML changes. Both profiles and full validation passed. Receipt: reports/1.1/chapter13-structure/preview109-receipt.json.

2026-10-10: Section 13.4 final velocity eip-842 retains preceding precision: v = 0.99944c. XML and numerical rounding checked; pending next preview refresh.

2026-10-10: Combined light-velocity calculation eip-898 from six into three aligned rows, retaining all steps. Pending preview refresh.

2026-10-10: Combined forward-canister calculation eip-609 from four into two rows, retaining all steps. Pending preview refresh.

2026-10-10: Combined backward-canister calculation eip-115 from four into two rows, retaining all steps and sign-spacing corrections. Pending preview refresh.

2026-10-10: Combined first three symbolic rows in battery calculation eip-951 into one, leaving numerical substitution on second row. Pending preview refresh.

2026-10-10: Standalone battery mass result import-auto-id1998022 now uses centered unnumbered equation markup, retaining stable ID and expression. Pending preview refresh.

2026-10-10: Gamma calculation eip-54 condensed from four rows to two; all steps and final approximation sign retained. Pending preview refresh.

2026-10-10: Corrected energy-momentum equation eip-832 square grouping: outer exponents now apply to complete parenthesized expressions, not closing parentheses. Copy formats checked; pending preview refresh.

- 2026-10-10: Corrected two inline energy–momentum parenthesis groups in 13.7. Audit found 45 additional affected expressions / 63 faulty bases across 140 numbered modules, including 14 expressions / 22 bases in 13.7, excluding the main equation previously repaired. Two expressions fixed in this pass; remaining audit findings retained for review. Report: `reports/1.1/closing-delimiter-script-audit.json`. Pending preview refresh.

- 2026-10-10: Fixed all remaining inventoried closing-delimiter scripts: 43 expressions / 61 groups. Mathematical tokens and annotations preserved. Rescan of all 140 numbered modules found zero remaining instances. Grouped LaTeX verified and recorded in `reports/1.1/closing-delimiter-repair-verification.json`. Pending preview refresh.

- 2026-10-10: Chapter 13 exercise proposal expanded, at maintainer request, to 41 review candidates (19 additions), including five gamma–beta number-sense questions and eight further conceptual prompts from MyOpenMath. Momentum remains one question and energy four. Reviewed 56 export records including take-home variants. All 94 current-exercise dispositions updated. Proposal only; maintained exercises unchanged. Review: `reports/1.1/chapter13-structure/question-set-proposal.html`.

- 2026-10-10: Applied the approved expanded Chapter 13 set: 41 chapter-end exercises (22 retained IDs with revised/merged wording; 19 new IDs), ordered by textbook topics. All five inline checks and section body content preserved. Added native MathML for variables, relations, scientific notation and complete grouped powers. Internal answers/provenance and old/draft/new numbering are recorded in `reports/1.1/chapter13-structure/applied-question-set.json` and `applied-number-crosswalk.json`. Projected book exercise count: 775. Pending preview refresh and maintainer question review.

- 2026-10-10: Preview 110 published the approved 41-question Chapter 13 set and all pending MathML/formatting repairs. Both builds, full validation and mobile exercise-page QA passed. Receipt: reports/1.1/chapter13-structure/preview110-receipt.json. Chapter 13 exercises are ready for maintainer review.

- 2026-10-10: Corrected remaining Chapter 13 glossary text-token << to native MathML ≪ in m42540/fs-id1291443. Checked all Chapter 13 modules for double-angle text/operator tokens; no other instances found. Pending next preview refresh.

- 2026-10-10: Exercise 13.3 (current Chapter 13 Exercise 3, c13-mom-c13-p05): replaced rhetorical ending with a brief sourced example of a significant null-result experiment. Internal guidance lists Pasteur, proton decay searches and dated WIMP searches, with limits of inference. Pending preview refresh.


### 2026-10-10: Space-time diagram for Chapter 13

Added an original SVG figure and introductory subsection after simultaneity in m42531. The graph uses equal x and ct scales, rest, 0.4c motion, light, and a horizontal simultaneity line. OpenStax University Physics Volume 3 section 5.5 was consulted (https://openstax.org/books/university-physics-volume-3/pages/5-5-the-lorentz-transformation); its light-cone and transformed-axis figures exceed the scope of this introductory exercise, so no OpenStax artwork was reused. Removed Extension from Exercise 11 and restored plain-text part (c).


### 2026-10-10: Train-and-flashes space-time diagram

Revised Figure 13.3.3 to illustrate the preceding simultaneity scenario. All coordinates are in the station frame, with symmetric lamp positions at emission, a centered ct axis, station and train world lines, two inward light paths, and numbered reception events. Text explains the train observer’s emission-time inference from equal source distances and equal light speeds without transformed axes. Geometry uses x_A=0.4ct and emissions x=±180 at ct=0; reception times are 180/1.4, 180, and 180/0.6. Original artwork; no reused OpenStax image.


### 2026-10-10: Space-time glossary and Exercise 11

Defined space-time diagram and worldline in the running text and chapter glossary. Standardized worldline to one word in the section and Exercise 11. Removed the original-art caption note. Exercise 11 now applies the introduced terminology rather than reintroducing it; it retains the sketching and simultaneity questions without an Extension label.


### 2026-10-10: Exercise 12 light-clock wording

Removed the redundant final question about the pulse slowing down and specified light pulse in the opening sentence. The remaining question asks students to explain greater elapsed time from a longer light path at unchanged light speed. Pending preview refresh.


### 2026-10-10: Exercise 14 parts

Labeled the three beta/gamma questions (a), (b), and (c), preserving the introductory definitions and mathematical markup. Source XML parses. Pending preview refresh.


### 2026-10-10: Exercise 24 length measurement

Reordered into (a) proper length and contraction and (b) a concrete two-student endpoint measurement. Students identify the missing timing information, explain the necessary procedure, and predict the error from recording the leading end later. Removed the leading yes/no simultaneity question. Updated internal answer guidance. XML parses; pending preview refresh.


### 2026-10-10: Exercise 26 reciprocal contraction

Replaced the confusing question about damage/compression of one’s own stick with an explicit question about how reciprocal shorter-length measurements can be consistent. Updated answer guidance to distinguish the endpoint simultaneity conditions in the two frames. Source XML parses; pending preview refresh.


### 2026-10-10: Exercise 31 pitcher

Corrected the subject throwing the ball to a baseball pitcher standing in the truck bed, consistent with the scenario in section 13.2. Explicitly identified the ground frame for truck speed. Numerical values and calculation unchanged. XML parses; pending preview refresh.


### 2026-10-10: Exercise 32 absolute-value spacing

Grouped the absolute-value expression and marked its bars as prefix/postfix fences with zero spacing. The less-than relation retains normal operator spacing. Pending preview refresh.


### 2026-10-10: Exercise 35 parts

Labeled the momentum questions (a), (b), and (c), preserving the introductory formula and mathematical markup. Source XML parses; pending preview refresh.


### 2026-10-10: Exercise 37 rest energy in MeV

Added part (b) asking for rest energy in MeV and supplying 1 MeV = 1.602e-13 J as MathML. Existing questions labeled (a) and (c). Checked supplied rounded inputs: 8.20e-14 J and 0.512 MeV, with total energy 2.00E0 and kinetic energy 1.00E0. XML parses; pending preview refresh.


### 2026-10-10: Remove Chapter 13 summary essays

Removed Exercises 40 and 41 (C13-A7/A8), retaining 39 questions with existing numbering unchanged. Updated the applied inventory, crosswalk, and projected book exercise count (773). Archived removed prompts and internal answers in removed-chapter-essays.json. Pending preview refresh.


### 2026-10-10: Chapter 13 finalized; Chapter 14 organization

Maintainer finalized Chapter 13 after Preview 113, approving all 39 exercises and the new space-time diagram subsection. Chapter 14 prepared with 112 glossary definitions, 10 section summaries, and 195 original chapter-end exercises in section order. All exercise content and IDs preserved by the organization script; 0 inline checks retained. Section 14.12 missing objective particle name flagged for review. Figure 12.3.2 author photograph remains deferred; reminder delivered. Chapter 14 review inventory: reports/1.1/chapter14-structure/review.json.


Preview 114 published successfully: Chapter 14 organized and ready for review. Both numbering builds, full validation, and narrow/desktop browser checks passed. Receipt: reports/1.1/chapter14-structure/preview114-receipt.json. Chapter 13 finalized; no canonical GitHub push.


### 2026-10-11: Same-page numbering selector

Completed the older textbook map from the preserved PDF outline (140 labeled modules plus unnumbered preface). Added Lecture-aligned / Older textbook selection at the same page URL, with persistent preference and synchronized headings, navigation, object labels, references, and search. Per author direction, both modes retain section-based object counters; exercise numbers remain stable. Chapter introductions use chapter.0 object labels in older mode. Source CNXML and stable links are unchanged. Evidence and checks: reports/1.1/numbering-toggle/.

### 2026-10-12: Numbering and header review complete

Previews 116–118 rename the alternate mode CNX-aligned, hide duplicate introduction entries in CNX-aligned contents, and center the header with both preference menus wrapping together. User approved the preview and requested committing these updates to GitHub. Course build, numbering checks across 141 sections, and header checks at 320–1600 px passed. Publication receipts and browser evidence are in reports/1.1/numbering-toggle/.
