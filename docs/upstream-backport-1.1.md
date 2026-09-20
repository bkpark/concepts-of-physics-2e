# CC BY upstream backport for 1.1

The author authorized backporting **all applicable OpenStax College Physics corrections** that can be included in a CC BY 4.0 textbook. This is broader than Special Relativity. It is not authorization to replace the adaptation wholesale or extensively rewrite prose.

## Current state

- Unit 3 comparison pass: 49 sections, 50 applied correction records in batch 05, and six held author-review items. Review at http://127.0.0.1:8765/review-1.1/unit3-review/ . Holds concern the incubator example, helium-balloon exercise, ozone/CFC update, power-line health wording, generator-current arrows, and the broad electron-transition claim. None of these held changes is applied. The packet includes per-section rationales, fingerprinted shared-object dispositions and 369 unmatched-content boundaries; absent exercises are not independently re-solved.
- Units 1–2 are author-approved, including the scoped conservative-force heuristic. Plasma remains optional future coverage, potentially only a sentence explaining its omission.


- The requested Units 1–2 comparison pass now covers 55 sections: the remaining Kinematics differences, all Dynamics, and all five Unit 2 chapters. Batch 04 records 35 scoped corrections, including MathML/numerical repairs, minimal physics wording corrections, three exact pinned media imports, and three verified alt descriptions. See `proposals/1.1/upstream-batch-04.json` and `reports/1.1/unit12-review/`.
- All shared-object differences in those units have fingerprinted dispositions, with plasma explicitly deferred by the author to broader revision. The 466 upstream-only objects/changed wrappers have explicit coverage dispositions. This is a comparison/applicability pass, not independent revalidation of every exercise or a claim that all author-added material is error-free.
- The batch review is at http://127.0.0.1:8765/review-1.1/unit12-review/ . No chapter/section structure, stable IDs, slugs, numbering profiles, or exercise organization changed. The development website is rebuilt; the frozen 1.0 outputs are unchanged. Release PDF/layout verification follows the full-book backport.

- SR01 and SR02 are applied, with the two approved SR01 typo fixes.
- Seven additional small corrections are applied in `proposals/1.1/upstream-batch-01.json`: Isaac Newton's name; radium-doped luminous paint; magnification discussion 3 to 4; two friction-paragraph typos; a missing closing quotation mark; displacement magnitude; and specifying each resistor in an exercise.
- Batches 02 and 03 add thirteen checked corrections in the opening chapters: a duplicated caption word; a missing space; the four-fundamental-quantities qualification; atomic diameter order 10^-10 m; graph alt text 3 km; the odometer question; acceleration-versus-velocity signs; rock apex time 1.33 s; Alan Shepard's name; displacement/average-velocity graph labels; Isaac Newton's name in a caption; Earth's-surface qualification; and acceleration magnitude in the weight derivation.
- The graph-label update is an exact pinned CC BY media replacement, checked visually and for individual credit. Its local path and IDs are retained. Binary before/after bytes are stored in the same editorial ledger using explicit base64 encoding; the verifier reconstructs these bytes as well as text patches. Historical media remain untouched.
- `proposals/1.1/backport-decisions.json` records the first prose/reference/media pass through course chapters 0 and 1, plus two upstream regressions found in chapter 2. This records the earlier opening pass; the later Units 1–2 batch includes mathematical and unmatched-object review as described above.
- `reports/1.1/math-representation-decisions.json` retains 6,413 MathML representations after a conservative tree comparison proves that differences are limited to attribute-free redundant rows or equivalent decimal spellings of em spacing. Fractions, scripts, accents, grouping, attributes and token text remain significant. Six safety tests cover this method. This is not a physics-proof claim.
- BR01 is applied: past-tense wording, the definition in effect since May 2019, and the approving body corrected to the General Conference on Weights and Measures. The author’s exact Planck-constant addition and all MathML are preserved. BR02 is also applied: position-axis label and alt text corrected while retaining the original paths and answers. See `proposals/1.1/opening-review.json`.
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
- http://127.0.0.1:8765/review-1.1/backport-review/ — BR01/BR02 decisions and the thirteen corrections from batches 02/03.

The comparator now includes unnumbered captions by matching their owning figure ID. The initial ID-only prose inventory missed these captions; the added comparison found the second occurrence of the misspelled Newton name and the duplicated caption word.

Known pinned-upstream problems excluded from the backport: the path-C figure ends at 10 m while its solution still uses 11 m; the second-law glossary says force is inversely proportional to mass; and an alt-text change introduces “X-x rays.” These observations refer to the pinned CC BY snapshot, not a claim about the current public OpenStax site or its errata list.

Reproduce current reports with `python tools/triage_upstream_math.py`, `python tools/review_upstream_book.py`, and `python tools/render_backport_review.py`. Rerun the triage after inventory changes. Dispositions are accepted only when their stored content fingerprints match; changed text returns to review rather than inheriting an obsolete decision.

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


### Unit 3 author decisions (September 19, 2026)

- H01 applied: upstream metal-block example, omitting an unnecessary Thermodynamics aside; coverage is not missing.
- H02 deferred by author to the exercise revision.
- H03 figure applied from the pinned CC BY archive, with the 2020 caption, NASA credit and corrected color-scale alternative text. Paragraph also applied with author-approved limited factual adjustments: omit the undated country ranking and replace the incorrect 2020 record claim with “large and long-lasting.”
- H04 prose applied with the author-approved limited qualification: studies have not established that power-line fields cause cancer, rather than upstream’s blanket absence-of-risk statement.
- H05 upstream generator arrows applied, with synchronized alternative text.
- H06 applied: retain the electron-transition explanation and tie the majority claim explicitly to table categories, infrared through X-rays. Author completed a quick review of the remaining Unit 3 changes; no Unit 3 backport holds remain. H02 stays deferred to exercise revision.

Evidence for approved H03/H04 qualifications: [NASA 2020 ozone map and account](https://science.nasa.gov/earth/climate-change/ozone-layer/large-deep-antarctic-ozone-hole-in-2020-147465/), [NCI electromagnetic fields fact sheet](https://www.cancer.gov/about-cancer/causes-prevention/risk/radiation/electromagnetic-fields-fact-sheet). These sources support factual checking; prose backports and figure bytes come from the recorded CC BY snapshot.


## Unit 4 backport review packet

The Unit 4 packet covers 29 textbook sections and four supporting appendices. Eight correction records are applied in `proposals/1.1/upstream-batch-06.json`: the electron/photon diagram and caption, thorium notation, proton-rich beta-plus sign, ion-pair clarification, programmed-cell-death wording, and matching dosimeter image/caption/credit. Source: the existing pinned CC BY 4.0 archive only.

Review: http://127.0.0.1:8765/review-1.1/unit4-review/ . Rebuild the packet with `python tools/render_unit4_review.py`; rebuild the development textbook with `python prototype/build.py course --all`.

U4-H01 holds the reactor-safety generalization and obsolete next-chapter promise for author choice. Other shared problems and optional coverage additions are visible in the page and recorded in `reports/1.1/unit4-review/followups.json`; they have not been silently changed or certified by upstream agreement. The author can prioritize them before 1.1 or during the planned full read-through/exercise revision.

The packet records 191 unmatched upstream boundaries and row-by-row comparisons of supporting tables. It preserves custom quantum explanations, previous relativity/reference repairs, newer local constants, and repaired nuclide notation. Upstream-only AP exercises and broader history/coverage are not restored.

Validation: maintained-source ledger reconstructs 955 files with four initial repairs and 154 editorial changes; historical baseline still verifies 959 files and preservation tags. Desktop/mobile review checks and all eight change anchors pass. The development build has 7389 equations and only the three known external-media notices. No new release PDF or public deployment was produced.

Before declaring the full backport finished, resolve U4-H01 and reconcile eleven remaining opening-chapter math-ordinal differences in m67032 (separate from Unit 4), then complete final PDF/layout and release checks. An applicability review is not independent validation of every inherited exercise or scientific/historical claim.

### Unit 4 factual follow-up

Applied U4-12 (Stefan–Boltzmann units and vacuum permeability approximation) and U4-13 (tau-decay neutrinos), as approved. U4-H02 contains a shorter medical-imaging-dose proposal beside the unchanged paragraph; awaiting author review. Values are factual references, not imported external prose.
