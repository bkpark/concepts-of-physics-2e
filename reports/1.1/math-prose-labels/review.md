# Whole-book prose-label audit

Reviewed 202 expressions flagged for prose-like tokens across all 6,726 source MathML expressions. Shorter alphabetic tokens were also inspected for missed qualifiers; these were units, symbols, functions, chemical elements, or descriptive mathematical subscripts.

Moved 11 additional explanatory labels/qualifiers outside MathML in eight modules:

- Proposed proton decay (m42680).
- On dry concrete and on wet concrete (m67034).
- Conservative forces only (m67037).
- Two-object elastic collision (m67042).
- Melting/freezing and vaporization/condensation (m67124).
- Isobaric process (m67126).
- Two occurrences of cyclical process (m67127).
- Exactly, in the inch-to-centimeter conversion (m78798).

Source IDs, numbers, relations, units, and visible wording were preserved. Each correction has a before/after record in the editorial ledger. Existing display-style math with attached prose now uses inline MathML within its numbered equation container, keeping the label beside the formula.

Retained word equations, named quantities, descriptive subscripts, probability-table outcomes, unit names/conversions, and counts of physical entities. For example, `wall on feet` is part of a force subscript, `constant` is the value in an equality, and `gravitational acceleration` is a quantity in a chained equality. Stripping these would change the mathematics. After the fixes, 193 expressions still match the candidate pattern: two repaired expressions also contain legitimate mathematical words and thus remain candidates.

The before-audit inventory is `candidates.json`; the reviewed retained cases and reasons are in `reviewed-retained.json`. Run `python tools/audit_math_prose_labels.py` to flag new, unreviewed prose-like tokens instead of removing text automatically. This is a heuristic review aid, not a guarantee that all future prose can be identified mechanically.

Both numbering builds and full source/link/content validation pass. Browser checks at 375 and 1024 px verified that all 11 labels remain visible outside MathML and absent from copied equation content. Screenshots of the phase-change formula, braced conservation equations, and unit conversion were inspected.

These changes and the two Section 12.6 ratio-label corrections made after preview 98 are pending the next preview refresh.

Published successfully in preview 99, 2026-10-10 UTC (2026-10-09 Pacific). See preview99-receipt.json.
