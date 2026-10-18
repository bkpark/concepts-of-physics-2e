# Maintained Introduction to Physics source

Edit textbook content here. This is the single maintained source layer for both
PDF and static HTML. The repository-root `modules/`, `media/`, and `collections/`
directories remain the immutable historical baseline.

- `modules/{CNX-ID}/index.cnxml`: editable prose and MathML, retaining source IDs.
- `media/`: editable media; inherited references remain valid.
- `collections/introduction-to-physics.collection.xml`: inherited book hierarchy.
- `sections.json`: authoritative stable section IDs and frozen slugs used by the build.
- `exercise-views.json`: frozen identities for generated chapter exercise views.
- `numbering.json`: profile-specific object numbering rules, independent of identity.
- `initialization.json`: baseline commit, author-approved R1–R4 repairs, and the
  author-submitted OpenStax erratum 30172. This is an initialization record,
  not a file to regenerate after later edits.

All 141 modules are present and form the source of the published version 1.1.
The renderer supports the full corpus with `--all`. See the
[release documentation](../docs/release-cp2e-ver1.1.md) for validation results and
known limitations. CNXML remains the canonical authoring format.

The initial source differs from the historical corpus only in three XML files,
containing the four approved repairs. All media and hierarchy files initially
match their historical bytes. Later edits should be ordinary, reviewable Git
changes to this directory, with source IDs preserved. Never run the bootstrap
script over an existing maintained directory; it deliberately refuses to do so.

Regenerate the current previews from the repository root:

```powershell
python prototype/build.py cnx --all
python prototype/build.py course --all
python prototype/check_numbering.py
# With Playwright available in NODE_PATH and Chrome installed:
node prototype/tools/render.cjs
python prototype/validate.py
```

Use `tools/verify_baseline.py` for permanent historical protection.
`tools/verify_maintained_initialization.py` checks this initial approved state;
it is a recovery-stage audit and must be revised or retired when additional
intentional editorial changes are introduced. Git remains the change history.

URLs never derive from display numbering. Freeze published slugs, retain old
slugs as aliases if a change becomes necessary, and do not regenerate identifiers
from newly edited titles. Cross-reference targets remain XML IDs; labels are
computed at build time.

Retain applicable licensing and author/figure credits when editing. Reviewed
CC BY-compatible upstream corrections are incorporated with provenance records.
See the [license-source audit](../docs/license-source-audit.md) before importing
additional material.

Approved post-initialization corrections are recorded in `editorial-changes.json`.
The historical ledger-replay utility does not support all later maintainer and
multi-file entry formats. Complete ledger replay is not claimed; version 1.1
checks compare current source bytes directly with the builds and release package.
