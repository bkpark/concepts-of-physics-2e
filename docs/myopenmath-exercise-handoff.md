# MyOpenMath follow-up guidance (working document)

This document collects recommendations for a separate course-maintenance task. It does not authorize changes to the live course. Baseline: Physics 10 full export dated 2026-09-27, checksummed in the exercise-planning inventory.

For each future entry record: learning objective; source unique IDs and assessment context; corresponding textbook section/exercise stable IDs; existing coverage; proposed addition or correction; conceptual vs numerical intent; randomization constraints; answer/distractor rationale; image/provenance requirements; priority; and review status. Use export-local IDs only as locators within the frozen export, not assumed live MyOpenMath database IDs.

## Initial leads

- **Radiation framing:** review question unique ID 1543705851125192 (radiation essay, also reused elsewhere). Its broad safe/unsafe distinction needs reconciliation with the revised textbook. Preserve its useful aim of distinguishing meanings of radiation. This is a review lead, not an applied correction.
- **Thermodynamics alignment:** compare heat-engine/heat-pump, entropy and work-convention question families and their answer explanations with approved 1.1 text. Do not infer that all such questions are wrong.
- **Link maintenance — intentionally deferred to winter break:** the maintainer prioritized assessment-setting links because they were quick to update. Question-level hints remain a known follow-up, delayed to avoid changing questions used by other instructors mid-semester. The maintainer plans a manual pass, followed by a scan of a fresh export for missed links, potentially in another project. Current question links may be read as mapping evidence, but this textbook task must not update the live questions or treat those links as an urgent defect.
- **New questions:** identify actual coverage gaps after the textbook/MyOpenMath crosswalk. Prioritize prediction, comparison, proportional reasoning, graph interpretation and explanation of misconceptions. No claim of missing coverage is made solely because a topic was absent from the small sample.

Do not copy textbook fixed values straight into every algorithmic template. Define valid parameter ranges, avoid unintended ties or ambiguous distractors, and test representative and boundary variants. Lecture fill-in-the-blank prompts identify topics; they should not dictate the wording of new independent questions.

## Chapter 9 review leads — preview 68 exercise proposal

Review-only; no live course edits. Fixed textbook variants are in reports/1.1/chapter9-structure/question-set-proposal.json.

### Potential versus kinetic energy

Source: **Introduction to Physics - Electric Potential - Calculations - Q1 (updated to LibreTexts version)**; Question Set 8: Electricity and Circuits; Question Set 8 Assessment. Internal export locator: 1531333047872425.

Evidence: The question describes motion from a positive electrode to a negative electrode and asks how much energy an electron gains. That direction raises electron potential energy; electric-force-only acceleration is the opposite direction.

Recommendation: Specify which energy changes and the physical cause. Proposed question 20 uses motion from 0 V to +100 V and asks both potential-energy decrease and kinetic-energy gain. No external figure reuse is proposed; compare any revised distractors and randomization against this stated model. Status: maintainer follow-up, not applied.

### Battery capacity and unstated voltage

Source: **Introduction to Physics - Electric Power - Units - Q2 (updated to LibreTexts version)**; Question Set 8: Electricity and Circuits; Question Set 8 Assessment. Internal export locator: 1531361791123523.

Evidence: The prompt calls mA·h an energy rating and asks energy without supplying voltage; control assumes 1.5 V.

Recommendation: Distinguish charge capacity from energy; supply a constant-voltage approximation. Proposed question 42 does so. No external figure reuse is proposed; compare any revised distractors and randomization against this stated model. Status: maintainer follow-up, not applied.

### Charge carriers depend on material

Source: **Introduction to Physics - Circuits - Current Descriptions - Q1 (updated to LibreTexts version)**; Question Set 8: Electricity and Circuits; Question Set 8 Assessment. Internal export locator: 1531358805127996.

Evidence: The wording says conductor generally, while its keyed answer assumes mobile electrons only.

Recommendation: Specify a metal wire; ionic conductors need not fit that model. Proposed question 28 specifies metal. No external figure reuse is proposed; compare any revised distractors and randomization against this stated model. Status: maintainer follow-up, not applied.

### Branch circuit versus one outlet

Source: **Introduction to Physics - Electric Power - Calculations - Q1 (updated to LibreTexts version)**; Question Set 8: Electricity and Circuits; Question Set 8 Assessment. Internal export locator: 1531360478839544.

Evidence: The prompt treats a 15-A circuit-breaker rating as a power allowance for any one outlet and an exact trip threshold.

Recommendation: Account for combined loads on the same branch circuit and avoid claiming an exact trip point/time. Proposed question 48 uses a simplified comparison. No external figure reuse is proposed; compare any revised distractors and randomization against this stated model. Status: maintainer follow-up, not applied.

### Universal safe-current categories

Source: **Introduction to Physics - Circuits - Electrical Safety - Q1 (updated to LibreTexts version)**; Question Set 8: Electricity and Circuits; Question Set 8 Assessment. Internal export locator: 1531363207805516.

Evidence: The matching labels include maximum harmless current and a categorical claim that touching a high-voltage generator is safe.

Recommendation: Review against current electrical-safety guidance; include path, duration and conditions. Do not encode a universally safe current or a generator-touch guarantee. Proposed questions 52–55 use mechanisms rather than threshold matching. No external figure reuse is proposed; compare any revised distractors and randomization against this stated model. Status: maintainer follow-up, not applied.

### Insulator charge transfer

Source: **Introduction to Physics (Essay Questions) - Electricity - Bouncing Tab**; Essay Timed Assessment for Chapter 9. Internal export locator: 1541304862189399.

Evidence: The essay answer says a styrofoam ball does not gain charge because it is an insulator and must remain stuck.

Recommendation: Insulators can acquire charge; whether sustained bouncing occurs depends on charge transfer and geometry. No adaptation proposed without specifying the model. No external figure reuse is proposed; compare any revised distractors and randomization against this stated model. Status: maintainer follow-up, not applied.

Safety reference: OSHA 1910.333(b)(2)(iv), https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.333 ; OSHA basic electricity training, https://www.osha.gov/sites/default/files/2019-04/Basic_Electricity_Materials.pdf . These support the safety review, not numerical medical thresholds.
