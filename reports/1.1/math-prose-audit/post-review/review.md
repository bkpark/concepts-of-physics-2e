# Embedded prose in MathML — global scan

Scanned 6738 expressions across 141 modules. Found 8 flags. No source changes applied.

Presentation text only; legacy annotations excluded. Snippets flatten fractions and scripts and are for identification, not copying. Individual letters and the chemical symbol At are not treated as prose. The scan cannot guarantee detection of words split across separate letter tokens.

## Inline expressions likely worth splitting


## Displayed connectors requiring layout judgment

- **8.6 — Temperature Change and Heat Capacity**; `eip-508`; `m67622-math-0024`
  - Embedded text: `Percentage for pan`
  - Expression: `Percentage for pan=QAlQtotal×100%=27.0kJ89.8kJ×100%=30.1%,`
- **8.6 — Temperature Change and Heat Capacity**; `eip-686`; `m67622-math-0025`
  - Embedded text: `Percentage for water`
  - Expression: `Percentage for water=QwQtotal×100%=62.8kJ89.8kJ×100%=69.9%.`

## Descriptive labels: not automatically errors

- **7.6 — Archimedes’ Principle**; `eip-251`; `m71624-math-0042`
  - Embedded text: `apparent weight loss = weight of fluid displaced`
  - Expression: `apparent weight loss = weight of fluid displaced`
- **7.6 — Archimedes’ Principle**; `eip-249`; `m71624-math-0043`
  - Embedded text: `apparent mass loss = mass of fluid displaced.`
  - Expression: `apparent mass loss = mass of fluid displaced.`
- **14.9 — Fusion**; `import-auto-id3418170`; `m52480-math-0033`
  - Embedded text: `8 mol of reactants`
  - Expression: `(1000g)/(5.03g/mol)=198.8 mol of reactants`
- **17 — Useful Information**; `import-auto-id1528540`; `m78798-math-0157`
  - Embedded text: `minute of arc`
  - Expression: `1 minute of arc(')=1/60 degree`
- **17 — Useful Information**; `import-auto-id1528540`; `m78798-math-0158`
  - Embedded text: `second of arc`, `minute of arc`
  - Expression: `1 second of arc('')=1/60 minute of arc`
- **17 — Useful Information**; `import-auto-id1528540`; `m78798-math-0166`
  - Embedded text: `millimeter of mercury`
  - Expression: `1 millimeter of mercury(mmHg)=133.3 Pa`

## Editorial notes

- The two isotope alternatives in Atomic Masses should preserve leading mass-number scripts when split around “or”.
- The 9.6 voltage/potential-energy identity pair occurs three times; any later layout decision should be applied consistently.
- Formula applicability labels (for example “at center of loop”), percentage labels, and conversion descriptions may legitimately remain in MathML.
- The reported 11.9 lens givens and 11.5 photon-energy parentheses were already corrected before this scan and are not counted.
