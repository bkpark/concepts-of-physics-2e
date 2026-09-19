# Native MathML selection experiment

## Finding

Native MathML is promising for symbol selection and text-bearing PDF output.
It does not, by itself, solve structured whole-equation copying through ordinary
Ctrl+C. Keep it as a candidate pending broader compatibility and fidelity tests.
The existing SVG preview and all historical source remain unchanged.

Eight expressions were drawn from the existing six-module prototype: a fraction
with an overbar and Greek delta, combined subscripts/superscripts, a radical,
an aligned array with a brace, a two-line temperature calculation, a bold vector,
Greek pi, and a relativistic expression with a radical. This is not a full-book
test and does not claim coverage of all matrices or legacy MathML constructs.

## Measured results

Test environment: Chrome 153.0.8010.50 on Windows, Playwright 1.62.1, native
MathML with the installed Cambria Math font. No MathJax runs on this test page.

| Check | Result |
|---|---|
| DOM-range selection followed by actual Ctrl+C and clipboard read | 104/104 token tests passed, including scripts, Greek letters, and operators |
| Actual mouse drag over the standalone vector w, then Ctrl+C | Passed |
| Copy whole equation as MathML, followed by Ctrl+V into a textarea | 8/8 exact XML matches |
| Ordinary whole-expression Ctrl+C | Copies characters but introduces line breaks and loses fraction/script structure; radical structure is absent from the browser's plain-text copy |
| Desktop layout | Eight native math elements, zero SVG elements, no horizontal overflow |
| 390px viewport | No page-level overflow; three wide expressions scroll within their own containers |
| Printed PDF | Four pages; all visually inspected, no clipping or overlapping expressions |
| PDF text extraction | 137 math characters with individual bounding boxes; all expected visible token characters accounted for after diagnostic Unicode normalization |

The PDF is a substantial improvement over outlined SVG: mathematical letters,
Greek symbols, operators, and digits exist as extractable text. But PDF text
extraction is not the same as interactive copying in a particular PDF viewer.
Acrobat, Edge, and other viewer clipboard behavior has not yet been tested.
The PDF uses mathematical Unicode forms such as italic mathematical v rather
than always the ordinary ASCII v. Those characters may paste differently into
search fields or equation editors. Unicode normalization was used only to
compare test evidence; neither the PDF nor historical source was rewritten.

Whole-expression PDF extraction still rearranges numerator/denominator and
script text according to layout. No claim is made that copying the PDF equation
will produce an editable equation. Likewise, the website's button copies XML
as plain clipboard text: it preserves structure but does not establish native
equation import into Word, LibreOffice, or any other destination application.

## Rendering adaptations

The test reuses the prototype's existing Content-to-Presentation MathML adapter.
In the derived output only, it expands legacy mfenced elements into explicit
operator brackets/separators, maps bold-vector styling to CSS, and removes
formatting-only whitespace between MathML elements. Original XML is retained in
the sample manifest alongside the presentation XML. Bracket and vector changes
are recorded in the generated adaptation log.

Visual inspection confirms the sample fractions, scripts, radicals, aligned
rows, and brace render. Typography differs from the SVG preview. The test uses
an installed system font, so it is not a portable, pinned publishing environment.
The PDF parser emitted a FontBBox warning for a font descriptor while still
extracting characters and their positions; investigate font embedding before
treating this as production output.

## Reproduce and inspect

From the repository root, after building the CNX prototype:

```powershell
python prototype/native_math_test.py
$env:NODE_PATH='C:/Users/a/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules'
node prototype/tools/test_native.cjs
& C:/Users/a/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe prototype/tools/check_native_pdf.py
```

The Python PDF checker requires pdfplumber. Build and browser dependencies are
otherwise the same as the original prototype. Results are recorded under
`prototype/qa/native-browser.json` and `native-pdf.json`. The generated site is
`prototype/dist/native-test/`, and the PDF is
`prototype/output/native-math-selection-test.pdf`.

On the local preview server, open `/native-test/`. Try dragging over a Greek
letter, a superscript, or an entire expression, then paste into the provided
text box. Compare that with the MathML copy button. Open the PDF in your usual
viewer to evaluate selection and copying there.

Next, test the receiving applications actually used for course preparation,
Firefox/Safari where available, and the full six-module sample. Before replacing
the current renderer, assess all legacy constructs and choose a redistributable,
pinned math font. A structured equation-copy control remains necessary even if
native MathML becomes the chosen display renderer.
