# Global sentence punctuation outside published MathML

Requested during Chapter 12 review on 2026-10-09; completed before resuming that review.

The shared publication adapter separates trailing sentence punctuation after native MathML normalization and before LaTeX/ASCIIMath copy generation. This applies to both numbering profiles, section pages, collected chapter reviews, and the complete book. Original maintained XML remains available as source evidence; this publishing normalization also covers future source edits automatically.

- Audited 6,726 source expressions.
- Separated sentence punctuation from 836 expressions across 98 modules.
- Corrected one additional source defect: the sentence comma was inside the denominator of E = F/q (m52385/eip-652). It now follows the MathML in the source.
- The six remaining terminal-punctuation candidates are mathematical ellipses in series, decimal expansions, or quantum-number lists. They were reviewed and retained.
- Decimal points, coordinate/list separators, unknown placeholders, and punctuation inside fractions/scripts/fences are protected by structural boundaries. The single malformed denominator was corrected explicitly rather than weakening those boundaries.
- External punctuation stays in a nonbreaking HTML group with the equation. Block layout and display style are retained. Multiline tables reserve an empty spacing anchor at the last result, allowing HTML punctuation to follow that result rather than the widest row or the table's vertical center.
- Numerical values, equation numbering, source anchors, and mathematical relations are unchanged.

Validation: unit tests cover mathematical punctuation, copy output, decimal values, ellipses, structural boundaries, one-/two-/three-column tables, idempotence, display style, and question marks. Browser checks cover every moved sentence mark in the whole book at 375, 768, and 1280 px (2,508 placement checks), plus the existing punctuation/wrapping suite at five widths and 186 wrap thresholds. Local screenshots `bohr.png` and `multiline.png` were visually inspected.

Reproduce the inventory with `python tools/audit_math_sentence_punctuation.py`. See `audit.json` and `browser-validation.json` for the itemized decisions and browser results. Pending the next preview refresh.

Published in preview 98 on 2026-10-10 UTC (2026-10-09 Pacific). See preview98-receipt.json.
