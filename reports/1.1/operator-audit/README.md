# Operator typography audit

Read-only structural triage of all maintained textbook modules. No textbook source was changed.

{
  "modules": 141,
  "math_expressions": 6699,
  "flagged_expressions": 1133,
  "confidence": {
    "review": 713,
    "low": 330,
    "high": 90
  },
  "rules": {
    "mixed-text-and-math-token": 346,
    "numeric-text-near-operator": 459,
    "explicit-operator-spacing": 467,
    "operator-at-nested-group-edge": 188,
    "symbol-in-nonoperator-token": 123,
    "split-decimal": 22,
    "function-typography": 2,
    "explicit-edge-form-between-operands": 2,
    "large-or-negative-explicit-space": 3,
    "number-in-operator": 1
  },
  "render_errors": [],
  "source_unchanged": true
}

Open review.html for filterable, paginated current-renderer previews. audit.json contains every finding and exact source hashes. symbol-inventory.json inventories all detected symbols and token types, including those not flagged.

Start with high confidence, especially symbol-in-nonoperator-token, number-in-operator, and split-decimal. Review grouped binary operators next. Low-priority manual spacing is often intentional. All labels denote heuristic confidence, not approval to change. Repeated expressions remain separate because their source contexts differ.

Limitations: no semantic proof, no exhaustive visual detection, and uncommon non-Unicode/custom operators can require manual review. Greek identifiers are not treated as operators. Source annotations are excluded from expression previews and token rules. Browser previews use the current renderer without the textbook page CSS; use the context link for final page layout.
