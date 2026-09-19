# Six-module fidelity prototype

This is an experiment, not a student edition or the final publishing system.
It reads the preserved CNXML without modifying it. Both profiles use the same
frozen slug manifest, source modules, and object anchors. The sample contains
constant acceleration, Newton's second law, gravitation, the ideal gas law,
the Bohr model, and the glossary of symbols.

From the repository root, with Python 3.10+:

```powershell
python prototype/build.py cnx
python prototype/build.py course
python -m unittest discover -s prototype -p test_mathml.py
```

The builder uses only the Python standard library. MathJax 3.2.2 is vendored
with its license and SHA-256 manifest; the website does not need a CDN.
Serve the result with any ordinary static web server, for example:

```powershell
python -m http.server 8765 --bind 127.0.0.1 --directory prototype/dist
```

Open `http://127.0.0.1:8765/cnx/` or `/course/`. The profile prefix is a local
comparison device; production would deploy the selected profile at the same
domain root. Canonical paths are `/sections/{frozen-slug}/` under either build.

For PDF output and browser checks, use Node.js, Playwright **1.62.1**, and Chrome.
Install Playwright in a separate tooling environment and expose its node_modules
through NODE_PATH, or use the bundled runtime already available on this machine:

```powershell
$env:NODE_PATH='C:/Users/a/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules'
# Optional on other machines: set PROTOTYPE_CHROME to the Chrome executable.
node prototype/tools/render.cjs
python prototype/validate.py
python tools/verify_baseline.py
python prototype/tools/package.py
```

The renderer starts and closes its own local server, blocks external browser
requests, audits all twelve section/profile combinations, and prints two PDFs
to `prototype/output/`. Chrome 153.0.8010.50 was used for the recorded run.
The generated site, PDFs, and screenshots are ignored by Git. QA JSON is retained.
The packaging command creates a profile chooser and a ZIP containing the static
site, both PDFs, artifact checksums, and assessment in `prototype/output/`.

This is repeatable generation, not yet a byte-reproducible production build:
Chrome and operating-system fonts are not packaged or pinned, and PDF metadata
can vary. Production needs a locked renderer/font environment and broader
pagination, accessibility, and fidelity tests.

See `docs/fidelity-prototype-report.md` for findings, limitations, and next steps.
