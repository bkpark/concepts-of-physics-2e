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

All 141 modules are present. The renderer supports the full corpus with `--all`; full
course HTML is audited, with explicit unresolved findings. It is not yet a
publication-ready edition. The original CNXML remains the canonical authoring
format until a separately justified migration is selected.

The initial source differs from the historical corpus only in three XML files,
containing the four approved repairs. All media and hierarchy files initially
match their historical bytes. Later edits should be ordinary, reviewable Git
changes to this directory, with source IDs preserved. Never run the bootstrap
script over an existing maintained directory; it deliberately refuses to do so.

Regenerate the current previews from the repository root:

```powershell
python prototype/build.py cnx
python prototype/build.py course
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

Licensing and author/figure credits are inherited unchanged. Upstream 2e files
under `references/` remain comparison evidence, not incorporated content.

Approved post-initialization corrections are recorded in `editorial-changes.json`.
The existing verification command now replays that ordered ledger after the four
initial repairs. X01 updates a module destination while retaining the figure ID.
