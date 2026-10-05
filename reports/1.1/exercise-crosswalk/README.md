# Exercise coverage crosswalk — September 27, 2026

The first whole-export coverage map is complete as an inventory. It is not a completed semantic review of every question or an approved selection for the textbook.

Open `index.html` for chapter tables, expandable section details, MyOpenMath family descriptions and links to existing textbook exercises. Local preview: http://127.0.0.1:8765/review-1.1/exercise-crosswalk/ . The report is not published on Sites, and it contains no MyOpenMath answer keys or full assessment prompts.

## Coverage and confidence

- All 1,012 source definitions have a record with source unique ID, export locator, assessment roles and mapping evidence.
- 268 have explicit section-hint links. These establish the original intended section, not question correctness or suitability.
- 356 inherit candidate destinations from a normalized description family with an explicit link.
- 135 have topic/title-based candidate destinations (40 topic rules, 95 title matches).
- 234 are mapped only to assessment chapter context; 19 remain unresolved. All 19 unresolved definitions occur in the archived branch. Broad lecture, synthesis and chapter-overview prompts often have no sensible single-section destination.
- 437 provisional description families group variants for inspection. They are not 437 independently verified learning objectives. Different phrasings can still belong to the same conceptual family; members grouped together may still test different skills.
- The current maintained source contains 956 ordinary exercises and 36 tagged inline checks. The 12 unclassified ordinary exercises remain visible for individual review.

Candidate exercise matches use wording overlap within mapped sections and are explicitly marked unverified. No similarity threshold authorizes deletion, merging or addition. Cross-section semantic overlap requires reading: the climate example below illustrates why.

## Initial content-level findings

Five source questions and their relevant existing section sets were examined more closely; exact IDs and findings are in `reviewed-relationships.json`.

1. **Dynamics 2.2:** distinguishing a force from an object or event adds a different task from the existing force-standard/vector questions. Good addition-pilot candidate.
2. **Ideal gas 8.3:** prediction and insufficient-information cases complement the two current conceptual questions. They should be considered together with pruning the eleven numerical problems, not simply appended to them.
3. **Heat capacity / latent heat 8.6–8.7:** the MyOpenMath Oakland/Orinda example overlaps a textbook San Francisco/Sacramento question in a different section. Review placement and consolidation before adding another climate question.
4. **Latent heat 8.7:** a phase-change heat-transfer classification could provide foundational practice, but existing application questions already cover the topic. Addition is not automatic.
5. **Latent heat 8.7:** heating-curve energy ranking is a promising different representation/task. Check the figure and physical assumptions when drafting.

## Next step

Use these findings to produce the bounded Dynamics/Thermal Physics pilot, with existing/proposed wording, rationale, provenance and internal answers. Resolve candidate matching as each chapter is prepared; the maintainer does not need to review hundreds of inventory rows before seeing useful proposals. Do not treat blank coverage rows as instructions to fill every section with new questions.

The winter-break question-link maintenance is intentionally outside this work. Existing links were read as evidence only. No textbook exercises, MyOpenMath questions or public preview content were changed.

## Reproduction

Run `python tools/inventory_mom_export.py` and `python tools/build_exercise_crosswalk.py` against the frozen export in the sibling `reference-inputs` directory. The latter checks its checksum and builds the machine-readable map, chapter summary and local HTML report. The content-level findings are separately maintained editorial judgments, preserved across regeneration.
