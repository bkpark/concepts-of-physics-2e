# CC BY upstream backport for 1.1

The author authorized backporting **all applicable OpenStax College Physics corrections** that can be included in a CC BY 4.0 textbook. This is broader than Special Relativity. It is not authorization to replace the adaptation wholesale or extensively rewrite prose.

## Current state

- SR01 and SR02 are applied, with the two approved SR01 typo fixes.
- Seven additional small corrections are applied in `proposals/1.1/upstream-batch-01.json`: Isaac Newton's name; radium-doped luminous paint; magnification discussion 3 to 4; two friction-paragraph typos; a missing closing quotation mark; displacement magnitude; and specifying each resistor in an exercise.
- The 4x magnification correction agrees with the existing example's object distance 7.50 cm, focal length 10.0 cm, image distance -30.0 cm, and calculated magnification 4.00. No equation was changed.
- All 141 maintained sections were inventoried against the 283-module pinned CC BY collection. 140 have supported candidate correspondences. The local Preface has no supported match.
- Mapping evidence includes exact shared IDs, source hashes, and unmatched IDs. Combined energy and electrostatics sections have multiple upstream modules; the two electromagnetic-spectrum sections map to one upstream module. These are correspondences, not determinations that every difference is a correction.
- The full backport is **not complete**. Unreviewed differences remain in every category. The report must not be presented as a completed physics, accessibility, exercise, or licensing audit.

## Provenance and workflow

The only update source is `f98d7a792138a6133fe7267d17e70aa04e9ccbed`, already verified as CC BY 4.0 in the license, README, collection and preface. `tools/review_upstream_book.py` rechecks those evidence files and the full archive checksum. It restricts matching to the College Physics 2e collection, excluding other modules bundled in the repository.

The script writes `metadata/upstream-map.1.1.json` and `reports/1.1/upstream-book/`, plus a development preview. It never writes textbook content. Every applied correction is a small literal patch in the ordered `maintained/editorial-changes.json` ledger, with before/after hashes, upstream module/commit, rationale, and authorization. The ledger verifier reconstructs the entire maintained corpus from the preserved historical source and approved changes.

Review pages:

- http://127.0.0.1:8765/review-1.1/upstream-book/applied.html — manageable list of applied changes.
- http://127.0.0.1:8765/review-1.1/upstream-book/ — full comparison index and machine-readable section evidence.

## Remaining work and acceptance criteria

1. Review chapter by chapter, tracking decisions per stable difference ID. Use earlier upstream history where needed to separate actual upstream corrections from adaptation differences. Two-way matching alone is insufficient.
2. Preserve the author's terminology, omitted coverage, rearrangements, prior reference repairs, and extensive MathML work. For example, upstream `deceleration`, `emf`, or `internal kinetic energy` cannot simply replace local wording without examining why it differs. Defer broader prose revisions.
3. Prioritize changed equation tokens, numerical results and figure descriptions. Identical token lists do not establish equivalence: fractions, scripts, grouping, accents, and layout can change. Review unmatched equation owners and shifted ordinals separately. Do not mass-normalize MathML.
4. Examine upstream-only and local-only objects for applicability. Shared-ID comparisons can miss corrections where objects were replaced or IDs changed. Do not restore omitted sections, AP exercises, or cross-references merely because upstream includes them.
5. Review figure content, resolution and credit independently. Different hashes can mean recompression; identical filenames do not prove unchanged artwork. Check individual third-party restrictions before importing any image or attributed material; exclude NC/SA content.
6. Exercise **corrections remain in scope**. Defer conceptual exercise redesign until the MyOpenMath pilot. Check changed problem data against solutions rather than updating only one side.
7. Record each difference as applied, intentionally retained, not applicable, duplicate/format-only with evidence, or pending author decision. No chapter is complete until all relevant categories and unmatched objects are resolved.
8. After content review, regenerate and check both output formats, numbering and anchors. Do not overwrite the frozen 1.0 artifacts, tag or live website.

The current generated inventory contains unreviewed differences, not thousands of confirmed errors. It separates prose, references, accessibility, media, MathML token changes, identical-token markup changes, and unmatched MathML structure. Counts can overlap within an object.
