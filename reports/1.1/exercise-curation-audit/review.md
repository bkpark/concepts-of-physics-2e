# Historical exercise-curation audit

Date: 2026-09-27. Read-only inventory of the recovered CNX 12.1 exercises, compared with the maintained draft and the pinned CC BY College Physics 2e reference. No textbook exercises changed.

## Conclusion

**The strongest sustained boundary is the end of Chapter 7, Fluids.** Chapters 0–7 are consistently conceptual, with four deliberately modest-looking displacement/path problems in 1.2 as the only exercises still classified as Problems & Exercises. Eight unclassified ordinary exercises in 1.6, 2.6 and 5.2 are qualitative prompts on acceleration, normal force/tension, and period/frequency, rather than overlooked numerical sets.

**This is a completion boundary, not proof of the chronological stopping point.** Later chapters contain substantial selection and adaptation too. Chapter 8 is already patchy, and Chapter 11 is heavily pruned. The available final snapshot cannot establish the last section edited or distinguish an intentional retained numerical problem from unfinished curation.

## Chapter counts in the historical source

Numbers use current course chapter labels. Counts are exercise elements, not lettered subparts. Category names describe source markup, not an independent pedagogical classification: conceptual questions can still contain numbers, and some numerical problems may suit this course. Inline Check Your Understanding prompts are separated.

| Chapter | Conceptual-tagged | Problems-tagged | Unclassified | Inline CYU |
|---|---:|---:|---:|---:|
| 0. Introduction | 12 | 0 | 0 | 3 |
| 1. Kinematics | 30 | 4 | 4 | 6 |
| 2. Dynamics | 38 | 0 | 2 | 1 |
| 3. Work and Energy | 20 | 0 | 0 | 2 |
| 4. Impulse and Momentum | 19 | 0 | 0 | 0 |
| 5. Oscillations and Waves | 21 | 0 | 2 | 12 |
| 6. Rotation | 28 | 0 | 0 | 5 |
| 7. Fluids | 42 | 0 | 0 | 0 |
| 8. Thermal Physics | 57 | 46 | 0 | 5 |
| 9. Electricity | 62 | 94 | 0 | 1 |
| 10. Magnetism | 19 | 31 | 0 | 0 |
| 11. Light | 44 | 8 | 0 | 0 |
| 12. Quantum Physics | 19 | 61 | 0 | 0 |
| 13. Special Relativity | 22 | 72 | 4 | 2 |
| 14. Nuclear and Particle Physics | 61 | 134 | 0 | 0 |

## Evidence at the boundary and beyond

- **1.2 Displacement:** the four Problems & Exercises ask for distance, displacement magnitude and displacement for paths A–D in a diagram. Their limited character fits selective retention; their presence does not contradict a conceptual curation pass.
- **7.2–7.8 Fluids:** 42 conceptual-tagged questions, no Problems & Exercises. The mapped later reference contains extensive numerical sets. The conceptual-only pattern extends across all substantive fluid sections, not just a chapter opening.
- **8.2 Temperature:** all 13 exercise IDs match the later reference, including eight temperature-conversion problems, four conceptual questions and one inline check. This is the clearest first return of a full numerical set.
- **8.3 Ideal Gas Law:** 11 numerical problems remain, versus 17 in the mapped reference. Examples include tire pressure as temperature changes, gauge-pressure conversion and gas-filled bulbs. Already selected, but still substantially quantitative.
- **8.6–8.10:** no numerical sets remain, although the mapped reference has them. These sections show selection later than the first two substantive thermal sections.
- **8.11 Carnot engines and 8.12 Heat pumps:** retain all nine and ten numerical problems respectively, and all exercise IDs from their mapped reference sections.
- **8.13 Entropy:** no numerical set; **8.14 Statistical interpretation:** eight numerical problems remain. Thus there is no clean stopping line even within Chapter 8.
- **9 Electricity:** 94 numerical-tagged exercises remain, but the chapter also contains conceptual-only sections. Do not assume every part needs the same treatment.
- **10 Magnetism:** numerical sets remain in force, transformer and AC/DC sections, while induction sections are more selective; some sections have no exercises.
- **11 Light:** only eight numerical-tagged exercises remain, seven in Refraction and one in Dispersion. Lenses, mirrors and polarization are conceptual-only despite numerical sets in the reference. This is strong evidence of later selective curation.
- **12–14:** large numerical sets survive: 61, 72 and 134 respectively. These are likely the largest remaining curation workload. Four unclassified exercises in Relativity are not included in the numerical-tagged count; they require individual classification.

## Limits and provenance

Historical source: untouched `modules/*/index.cnxml` from recovered CNX 12.1. Current maintained source was checked separately: only 13.2 has a different exercise-element count (the approved removal of the general-relativity Check Your Understanding). Other repairs changed wording or subparts without changing exercise counts, so equal counts do not imply identical content.

Reference: pinned CC BY 4.0 OpenStax College Physics 2e commit `f98d7a792138a6133fe7267d17e70aa04e9ccbed`, using the explicit section mappings in `metadata/upstream-map.1.1.json`. It is a later comparison snapshot, not necessarily the exact edition adapted originally. Counts from overlapping upstream mappings must not be summed as unique chapter inventories. Shared IDs support continuity, not unchanged wording or chronology. Missing upstream problems may reflect removal of associated coverage as well as deliberate exercise curation.

`inventory.json` records each historical and maintained exercise ID, source category and extracted question text, plus mapped reference exercises. Extracted text includes legacy MathML annotations; use the textbook for readable equations. The inventory is an audit artifact, not a replacement source.

## Suggested exercise-revision approach

Use this as a workload map, not a deletion instruction. Start the MyOpenMath alignment pilot with a chapter at the boundary (Thermal Physics), then address the large later sets while preserving evidence of earlier selection. Earlier chapters still need a suitability check against current course questions, but should not be reset to upstream. Identify retain/adapt/remove/add decisions individually and keep stable exercise identities where possible. Keep ordinary exercises at chapter ends and inline checks in place. No exercise decisions have been made by this audit.
