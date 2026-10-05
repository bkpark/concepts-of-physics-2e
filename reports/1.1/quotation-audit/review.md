# Quotation typography audit

Read-only scan of 141 maintained CNXML modules, September 27, 2026. No historical or maintained textbook content changed in this audit. Machine-readable candidates are in inventory.json. Prose counts exclude XML syntax, metadata and MathML; block-level candidates were reviewed in context.

## Findings

- Confirmed reversed opening double quote: m71410 subsection title `”Weightlessness” and Microgravity`. Correct form: `“Weightlessness” and Microgravity`. This is the only mismatched curly-double-quote sequence found in the examined prose blocks.
- Mixed straight and curly double quotes: 146 straight double-quote characters (73 pairs) in 45 prose blocks. Examples include normal-force summary `"apparent weight"`, third-law `"action"`/`"reaction"`, and optics using straight `"wave optics"` alongside curly `“geometric optics”`. The pairs are balanced; this is typography consistency, not missing wording.
- Straight apostrophes mixed with curly apostrophes: 79 ASCII apostrophe characters in non-MathML prose, including possessives/contractions such as Newton's, Hooke's, person's, doesn't, and can't. Of these, one is explicitly a prime marker and two occur in the plural g's; do not blindly convert all as apostrophes.
- Single quotation marks: two curly opening marks occur in `‘thrown’` (centripetal-force question) and an attribution nickname `Jon ‘ShakataGaNai’ Davis`. Both are paired; the nickname can stay. Whether to use double quotes for `‘thrown’` is house style, not a correction of a mismatch.
- Prime notation: m67042 says `where the primes (') indicate values after the collision`. The displayed marker should be a prime (′), not a curly apostrophe.
- Two `g's` plural usages in m67530 could be typeset as `g`s without apostrophes; this is a minor notation/wording choice rather than an opening/closing quote error.
- Placement of punctuation is mixed: e.g. `"Fusion",` versus `"conceptual physics,"`. This is a house-style choice; punctuation belonging to a quoted question or title needs individual treatment.

## Suggested scope

Fix the reversed heading mark; normalize ordinary prose quotation marks and apostrophes while preserving wording. Treat prime notation separately. Exclude source-code attributes, URLs, MathML primes, and StarMath annotations from any automatic smart-quote replacement. Preserve historical files. This audit does not independently authenticate quotations or their attributions and does not establish what characters are drawn into image assets.

## Applied after maintainer approval

The maintainer approved curly prose quotes/apostrophes and logical punctuation. See docs/style-guide.md, tools/normalize_prose_quotes.py and applied.json. Changes span 65 modules. All MathML subtrees and XML attributes were checked unchanged. The earlier findings above describe the pre-edit baseline. The two plural g’s instances retain their wording (only the apostrophe typography changed).
