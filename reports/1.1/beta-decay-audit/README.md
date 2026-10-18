# Beta-decay label audit

Scanned all 141 maintained modules, including body, summaries and exercises. Inspected 34 reaction expressions involving beta/neutrino labels, including fusion and particle-decay cross-checks. The two beta-decay diagrams were visually checked and correct. This checks labels, not every numerical value or reaction property.

## Corrections published in preview 130

- m76603 eip-799: introductory cobalt-60 reaction now says electron antineutrino. Kept the word label because the symbol is introduced later.
- m52480 eip-983: replaced Latin v in 2v_e with Greek nu and a separate coefficient: 2ν_e. These are neutrinos, not antineutrinos.

## Maintainer decision

Section 14.5 exercise fs-id2460264 / para import-auto-id3246240 mixes β− in the prompt and emitted particle, Z−1 and N−1 in the daughter, and ν_e. The preceding exercise already covers β− and the following exercise covers electron capture. Recommend making this the β+ conservation exercise: β+ in prompt and reaction, daughter Z−1 and N+1, keeping ν_e. Approved and applied in preview 130. This correction carries no weight in later decisions to retain or remove the exercise.
