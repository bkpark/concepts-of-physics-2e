# Operator audit triage

No textbook edits. Two maintainer decisions, both dimensional-consistency corrections.

## D1: Specific-heat units in the solar-heating example

Correct the specific-heat unit to J/(kg·°C), and write the first line as Q/(mc)?

Recommendation: Yes. Keep 1670 and the stated 162 °C result; change the unit and make the denominator grouping explicit.

1130 × 60.0 / (0.251 × 1670) = 161.748… °C, which rounds to the existing 162 °C.

## D2: Missing cube in the nuclear-density unit conversion

Cube the entire femtometre-to-metre conversion factor?

Recommendation: Yes. Add an exponent 3 to the whole factor (1 fm / 10⁻¹⁵ m); retain the existing 2.3 × 10¹⁷ kg/m³ result.

0.138 × 1.66×10⁻²⁷ × (10¹⁵)³ = 2.2908×10¹⁷ kg/m³, consistent with the existing rounded result.

## Routing counts

{
  "contextual-technical-review": 323,
  "mechanical-review": 443,
  "preserve-unless-rendering-defect": 364,
  "maintainer-decision": 2,
  "already-addressed": 1
}

Triage routes are not a claim that all 1133 expressions were individually browser-verified. Unique suspicious token patterns and grouped-operator contexts were inspected; mechanical cases still require technical and rendering checks before edits. Additional semantic ambiguities discovered during those checks will be escalated. No source changes are approved by this report.
