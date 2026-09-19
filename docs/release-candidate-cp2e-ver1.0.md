# cp2e-ver1.0 release-candidate pass

The visible title is **Introduction to Physics**. `cp2e-ver1.0` identifies the content release in filenames and metadata, not a separate numbering edition. A future change of numbering presentation does not change section URLs or create a separate edition automatically.

## Outputs

Under `output/releases/cp2e-ver1.0/`:

- `cp2e-ver1.0.pdf`: complete 1,149-page textbook with native mathematical text.
- `cp2e-ver1.0-static-html.zip`: ordinary static hosting package, including the PDF download. Extract at the domain root; no PHP or server application is required.
- `public/`: the same publishable file tree.
- `artifact-manifest.json` and `SHA256SUMS.txt`: artifact and source checksums.

The status is **release-candidate**, not a published GitHub release. No remote repository, final release tag, or deployment was created.

## Changes in this pass

- Added `metadata/release.json`; title and release identity remain separate from numbering.
- Public HTML excludes prototype banners, review navigation, experimental-label wording, and internal correction-approval language. Canonical URLs use `https://intro.coaphys.xyz/sections/{stable-slug}/`.
- Corrected continuous versus restarted chapter exercise counters, using observed July 2026 PDF pages. Normalized the recovered singular `problem-exercises` type only in presentation logic.
- Recognized eight conceptual questions in three source sections lacking class tags, and two existing Heat Transfer question paragraphs. The PDF now has 954 ordinary chapter-end questions plus 41 inline Check Your Understanding exercises; the XML exercise-element count has not changed. No question text was rewritten or new exercise content backported.
- Wrapped long URLs and scrollable equations on narrow screens. Six missing figure descriptions fall back to their existing captions. Existing table header rows now use HTML column-header semantics.
- Added renderer/font/runtime hash verification before release printing. Windows fonts and Chrome are required at the locked versions; they are not bundled or redistributed.

## Results

- 141 modules; 7,391 equations; 563 image references; 12,234 canonical source IDs preserved.
- 157 public HTML pages checked at 1280px and 390px widths: no script errors, broken images, missing image descriptions, unnamed links, duplicate IDs, unresolved source placeholders, external rendering requests, or root horizontal overflow. Whole-equation MathML clipboard check passes.
- All local package links/anchors/assets validated. Full PDF internal-link and character-margin scans pass; PDF has tagged content and mathematical character text.
- 21 final PDF pages visually inspected, focusing on changed exercise numbering, tables, corrected equations, cover, and credits.
- Twelve adapter tests and 23 selected historical numbering fixtures pass. Historical baseline and maintained editorial-ledger verification pass.

## Deferred exercise alignment and limits

701 of 803 uniquely text-matched exercises have the July reference's labels. The remaining 102 differences fall in four groups: Dynamics (17), Thermal Physics (7), Electricity (37), and Nuclear and Particle Physics (41). Some reference questions are split or grouped differently, and its nuclear-radius sequence omits an intervening number. No content splits, merges, deletions, or additions were made to force agreement. Other exercises lack a unique automatic match.

The detailed internal report is `reports/release-review.html`, also served at `http://127.0.0.1:8765/course-full/release-review/`. These findings belong to the fuller exercise revision already deferred by the author. The candidate is not represented as a complete object-numbering match to the later LibreTexts PDF.

Caption-count comparison is diagnostic only: graphical number labels, captionless illustrations, and repeated table captions prevent a text-only count from proving correctness. Figure/example/equation display rules have selected historical fixtures and visual checks, not exhaustive reference-label certification. Accessibility checks are practical structural/browser checks, not PDF/UA certification or a full screen-reader audit. Three external video/simulation links require internet access.

The font/runtime lock prevents accidental rendering-environment drift but is Windows-specific; PDF metadata/timestamps are not normalized, so byte-identical PDF reproducibility is not claimed. ZIP entry timestamps are normalized; all delivered artifacts have exact checksums.

## Rebuild

From repository root, with the locked Chrome/Node/Playwright runtime and Python with pypdf/pdfplumber:

```powershell
$env:NODE_PATH='C:/Users/a/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules'
python prototype/build.py course --all --release
node prototype/tools/render-full.cjs --release
python prototype/tools/audit_full_pdf.py output/releases/cp2e-ver1.0/cp2e-ver1.0.pdf
python tools/check_release_numbering.py
python prototype/tools/package_release.py
node prototype/tools/audit-release.cjs --public
```

`site/` is a staging directory with internal build files; publish `public/` or the ZIP contents, not `site/`. Source provenance and source file checksums are included in the artifact manifest. Versioned filenames remain independent of the active numbering profile.
