# Full course-numbered PDF review build

The complete PDF is `output/pdf/introduction-to-physics-course.pdf` (1,151 Letter pages, approximately 141 MB). This supersedes the six-module PDF samples. It is a review edition, not a claim of completed publication certification.

## Assembly and preservation

The renderer consumes the full maintained HTML build and verifies its module hashes against current maintained XML before printing. It does not edit canonical or historical source. All 141 modules, 7,391 native MathML expressions, 563 image references, and original object anchors are retained.

- 952 ordinary exercises are grouped at the ends of their 15 course chapters, in section order, conceptual questions before problems. Solutions remain with their questions.
- 41 embedded Check Your Understanding prompts remain inline, as the author requested.
- Three unclassified source blocks, containing eight conceptual questions, are recognized by their exact Conceptual Questions headings and moved alongside the classified blocks. Their existing section-based labels are retained; no later exercise counters are renumbered. This is a PDF placement rule, not an editorial reclassification of source XML.
- The linked contents and PDF outline navigate to section and exercise pages. Original internal references still point to the preserved object IDs after relocation.
- Short tables stay together with captions; long tables can span pages with repeated headers.
- Full historical section credits are collected in an attribution appendix, avoiding isolated credit-only spillover pages. Figure credits remain with figures. Only obsolete generated prototype commentary was updated; author prose was not changed.
- Native MathML remains text in the PDF. It has character-level mathematical text, rather than equation images. Copying a whole equation as plain PDF text still cannot preserve every two-dimensional relationship; structured MathML copying remains available on the website.

## Rebuild

From the repository root, with Python 3.10+, Node, Playwright 1.62.1, and Chrome:

```powershell
python prototype/build.py course --all
# Use the installed Playwright node_modules location for this machine:
$env:NODE_PATH='C:/Users/a/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules'
node prototype/tools/render-full.cjs
# pdfplumber and pypdf must be available to this Python:
python prototype/tools/audit_full_pdf.py
```

`PROTOTYPE_CHROME` can override the Chrome executable. `render-full.cjs --check` performs the DOM assembly and checks without replacing the PDF. It also writes `prototype/dist/course-full/print-full.html` for inspection. The renderer starts a private local static server, blocks external requests, and closes its browser and server afterward.

Generated PDF and temporary raster files are excluded through this checkout's `.git/info/exclude`; the baseline `.gitignore` remains unchanged. They are build artifacts, not canonical source. No remote repository or publication settings changed.

## Validation

- Complete DOM inventory comparison before/after exercise relocation; zero lost or duplicated anchors, broken internal links, missing images, unresolved expressions, or print-width overflow.
- Complete PDF character-position scan across all 1,151 pages; zero body text characters outside the checked margins.
- All 1,027 PDF internal link annotations resolve. There are 293 external link annotations (including attribution links); their remote availability is not guaranteed.
- 53,393 mathematical-font characters are present in the PDF text layer. PDF tagging and outline are present; this is not a PDF/UA certification or a new end-user clipboard test.
- Poppler visual review of 54 selected pages in the penultimate layout and 13 focused pages in the delivered revision, including the revised exercise order, dense table, corrected M01/M02 equations, contents, and credits. This is visual sampling, not manual proofreading of every page.
- Historical baseline and exact maintained editorial ledger verification pass.

Machine-readable records: `prototype/qa/course-full-print.json`, `course-full-pdf.json`, and `course-full-visual-review.json`. The PDF record includes its SHA-256. Poppler rasterizations remain in ignored `tmp/pdfs/` for this review.

## Remaining publication work

The layout is deliberately a spacious one-column review edition. Section starts can leave white space at the previous page's end, and inherited exercise/appendix labels remain provisional where historical numbering evidence was incomplete. The eight formerly unclassified conceptual questions retain their existing labels to avoid cascading renumbering during the deferred exercise revision. Website exercise projections are unchanged by this PDF-only placement step.

Chrome 153.0.8010.50 and Windows Cambria Math were used. Font/renderer packaging and timestamp control are still required for byte-reproducible releases. Tagged output does not establish accessibility compliance. Three external media resources still need internet access. Browser/OS font behavior, comprehensive object numbering review, and final publication packaging remain separate work.
