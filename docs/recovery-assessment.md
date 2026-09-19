# Recovery assessment: Introduction to Physics

Assessment date: 2026-09-19 UTC. Scope: recovery, inventory, evidence, and reversible
setup only. No conversion of textbook prose or equations, no publication, and no
remote GitHub changes have been performed.

## 1. Identity and preservation

The repository contains three book branches. Its default `main` is **Concepts of
Physics**, not this textbook. The correct branch is `introduction-to-physics`.
Its collection is `collections/introduction-to-physics.collection.xml`, with title
**Introduction to Physics**, content ID `col25183`, and UUID
`58fbacb7-693d-4d0a-80dc-21e7c33abd8f`. `META-INF/books.xml` and `canonical.json`
select that collection. The UUID's first six bytes encode to `WPust2k9` in base64url,
which corroborates the supplied short identifier; it does not establish the version.

The preface (`m67030`) identifies Andrew Park, College of Alameda, June 2018; describes
the adaptation through Bobby Bailey's Concepts of Physics; and acknowledges James
Rittenbach's linear-momentum contribution and OpenStax College Physics. These are
strong, independent content-level identity checks.

**The book identity is verified; the exact CNX version 12.1 is not independently
verified.** Neither the recovered collection nor module metadata records the CNX
version. The original-import Git date is not a CNX revision number. Archive requests
for both supplied short ID and full UUID at `@12.1.json` timed out. The user-provided
LibreTexts PDF corroborates the book/organization but does not attest CNX 12.1.
Recover an original CNX export manifest, version history, or archived 12.1 artifact
before asserting an exact version match. This qualification is machine-readable in
`metadata/recovery-lock.json`.

Two distinct snapshots are pinned:

| Snapshot | Commit | Meaning |
|---|---|---|
| `recovered/cnx-import-2022-06-23` | `e2b8ec04bd22d78da0e97826b9705a3f0cc6eba5` | Earliest available import of this book; selected conservative baseline |
| `recovered/introduction-branch-2022-09-29` | `4a8661442d4612738ff388f7f1be7c5deabd1b68` | Latest recovered branch tip, also targeted by release tag `20230109.213414` |

The branch tip is not byte-identical to the import. Commit `018a9858aaeb02d46329c5a7fc903ab8b3107d95`
changes MathML in 21 modules (94 added / 100 removed lines). Changes include spacing,
table structure, script operands, and removal of empty expressions. Math element count
drops from 7,394 to 7,390. These edits are preserved for review, not silently adopted.
Other later changes add licensing/build files and reformat the collection while adding
`authors="Bobby Bailey"`; that attribute alone omits the adaptation authorship in the preface.

Preservation consists of a full original-ref mirror, verified self-contained Git bundle,
two `git archive` tar files, two local tags, and SHA-256 hashes for all 959 baseline
files and the portable archives. `git fsck --full` and `git bundle verify` passed.
The working source is byte-identical to the import. Tags are an immutability convention,
not an indestructible backup: retain the bundle off-device and, once remote settings
are approved, publish/protect the recovery tags and archive checksums. Never force-move
them. No claim is made that the GitHub import is an untouched original CNX service
export: media paths and metadata may have been transformed before that initial commit.

## 2. Inventory and content representation

All counts below refer to the original-import snapshot. Machine-readable evidence is
in `reports/`; `tools/inventory.py` reproduces it with standard-library Python.

| Item | Finding |
|---|---|
| Book membership | 141 module occurrences, 141 distinct module files; none missing or unused |
| Structure | Preface, Introduction group, four units containing 14 topic groups, then four ungrouped reference modules |
| XML | All 141 modules and the collection parse successfully; no full CNXML/MathML schema validation yet |
| Text | CNXML mixed-content XML, not Markdown; 4,748 paragraphs, nested sections, lists, emphasis, glossary terms |
| Math | 7,394 MathML expressions; 384 contain Content MathML elements across 36 modules |
| Numbered-object candidates | 564 figures, 125 examples, 1,011 equations, 993 exercises, 185 notes, 42 tables |
| Media | 813 files, 185,245,224 bytes; 563 local image references resolve with exact filename case |
| IDs | No duplicate IDs within a module; every audited figure/example/equation/exercise/note/table has an ID |
| Titles and slugs | All 141 module titles and all 141 proposed normalized slugs are unique |

Hierarchy lives in nested `col:subcollection` / `col:content` elements; leaf
`col:module document="m..."` entries establish order. A module has a top-level title,
metadata, content, and often a glossary. Metadata supplies module ID, UUID, title,
and an abstract containing learning objectives. These abstracts must not be dropped.

Math is embedded XML in the standard MathML namespace, frequently under `semantics`,
with 5,587 annotation elements (often StarMath 5.0), as well as `mfenced`, tables,
superscripts, subscripts, multiscripts, and mixed Content/Presentation MathML.
The Content MathML is active expression content, not merely hidden annotations.
Preserve original bytes and annotations; do not assume annotations are authoritative
or round-trip through LaTeX to replace the source.

Figures use `figure/media/image` with captions and alt attributes; image paths such
as `../../media/Figure_02_05_00.jpg` refer to the shared media directory. Filenames
contain spaces and mixed case. There are 775 JPG, 8 PNG, 1 SVG, 9 WMF, 16 JAR files,
and 4 files with numeric suffixes. 251 media files are not referenced by audited `src`
attributes; retain them. Three remote iframes reference two YouTube videos and an
archive.cnx.org simulation. Local-image availability does not make these interactive
resources available offline. Assets have been checked for presence, not comprehensively
decoded or visually inspected.

Objects use persistent `id` attributes (including `eip-*`, `fs-id*`, and
`import-auto-id*`). Examples contain ordinary paragraphs/lists/equations; exercises
contain `problem` and sometimes `solution` (264 solution elements). Notes may have
titles or empty labels. Classes/types distinguish chapter introductions, splash figures,
summaries, conceptual questions, problems, appendices, and 12 explicitly unnumbered
equations. The `problem-exercises` / `problems-exercises` variation must be handled
explicitly, not normalized in the historical source. Object counts are not a license
to number every object indiscriminately.

Links use `document`, `target-id`, or `url`. A target without `document` is local to
its module; empty link text often requires a generated object label. An assembled PDF
must namespace IDs by module because local IDs are not globally unique by contract.
Footnotes, tables with CALS-style `tgroup`/`row`/`entry`, learning objectives, glossaries,
and solutions all need dedicated rendering rules.

The collection declares CC BY 4.0. The import lacks a root LICENSE file; one was added
later. Individual module exports retain no author lists, revision numbers, licenses,
or explicit `derived-from` chains. Attribution survives partly in the preface and
figure captions. Preserve those credits and reconstruct missing provenance from
historical evidence; do not equate Git commit authors with textbook authors.

## 3. Missing and suspicious material

- **26 unresolved internal links:** 24 references name absent modules, and two name
  absent local anchors (`m52427` → `import-auto-id1169737992146`; `m67122` → `fs-id1444855`).
  These may be adaptation leftovers, renamed/derived modules, or genuine omissions.
  None is a missing collection member. Do not import omitted chapters automatically.
  All attributes and labels are in `reports/references.json`; 806 links resolve.
- **Seven fixed-operand MathML findings** occur in `m42531`, `m42674`, `m42709`, and
  `m67807`. This small structural audit is not a complete equation validator. The later
  migration contains additional potential repairs beyond this audit; review each.
- **Modern-renderer gap:** Content MathML, vector typing, units, unusual operators,
  and mixed markup require a tested adapter. Current MathJax documentation explicitly
  states the v2 Content MathML extension is unavailable in v3 and above. Passing raw
  source directly to a modern renderer is not a fidelity strategy.
- **Seven media wrappers have missing/empty alt text.** Existing alt-text quality,
  long descriptions, reading order, and PDF accessibility remain unassessed.
- **Offline gaps:** the three remote iframes and three ordinary URL links are inventoried,
  not availability-tested. Plan descriptive print/offline fallbacks and retain credits.
- **Exact historical numbering/version and full attribution remain unverified.** A
  well-formed, structurally complete export does not prove visual/textual equivalence
  to the final CNX publication.

Conclusion: the repository is sufficiently complete to begin a controlled rendering
prototype, but not to certify a faithful complete textbook without the checks above.

## 4. Recommended source and build architecture

Keep CNXML + MathML as the maintained canonical content for the first implementation.
This is driven by the source's rich structures and bespoke equations, not a framework
preference. Retain the existing `modules/`, `media/`, and `collections/` layout initially.
A later move under `source/` is optional and should be a separate, byte-preserving change.

| Layer | Proposed location / responsibility |
|---|---|
| Immutable recovery | Pinned tags and portable archives; never regenerated from maintained content |
| Maintained textbook | `modules/`, `media/`, `collections/`; initially exact import, then reviewed edits |
| Publication metadata | `metadata/sections.json`, stable group IDs, numbering profiles, object policies, credits, aliases |
| Upstream references | Pinned commit/artifact manifests and separate snapshots/cache, never mixed into canonical modules |
| Transformation code | `tools/`, `render/`, templates, CSS; allowlisted XML transformations |
| Generated intermediate | `build/` semantic HTML, resolved links, numbering tables, adapted math; disposable |
| Publication outputs | `dist/site/`, `dist/pdf/`; generated, not independently edited |

Proposed pipeline:

1. Parse and validate collection, modules, metadata, assets, identities, and profile.
2. Build a document/object graph keyed by persistent IDs. Resolve references and compute
   all labels from the selected hierarchy and explicit counter rules.
3. Render semantic HTML from CNXML. Pass preserved MathML through a versioned, tested
   Content-to-Presentation adapter when needed, with unsupported forms failing loudly.
4. Emit one static `index.html` per frozen slug, plus TOC, glossary, navigation,
   attribution, exercise views, and local assets. No PHP or server-side runtime is needed.
5. Assemble the same rendered content into a print document with namespaced anchors,
   print CSS, running heads, TOC/bookmarks, footnotes, solutions, and page references.
   Prototype Paged.js/headless Chromium with locally pinned math rendering. Compare
   another paged-media engine if long equations, tables, or accessibility fail.

Keep original MathML in canonical XML; build-time transformations are derived outputs
and need regression evidence. MathJax SVG/CHTML are candidates after Content MathML is
handled. Ship fonts/scripts locally, not via an unpinned CDN. PDF SVG math needs separate
text/accessibility checks. A PDF existing successfully does not establish readable
equations, selectable text, useful bookmarks, or tagged accessibility.

Pin renderer versions, fonts, dependencies, container digest/browser version, locale,
and build inputs. Record source commit, profile, asset hashes, and tool versions in
release manifests. Control timestamps; test reproducibility in clean environments.
Promise content/layout reproducibility first; verify byte-identical PDF output before
claiming it, because metadata timestamps and PDF IDs can vary.

Alternatives: the recovered Enki workflow is useful historical evidence and published
an EPUB, but uses a mutable `sk-epub-fixes` checkout, a 2022 container, dummy styling,
and write-enabled release actions. Do not reactivate it as the maintained pipeline.
Generic Markdown/Pandoc/LaTeX migration would require translating custom MathML and
semantic objects and risks losing edits. A custom XML-to-HTML layer keeps the source
model intact while allowing the final print engine to be selected experimentally.
No production framework or renderer has been installed or committed as a final choice.

## 5. Stable URLs and two numbering profiles

Propose `/sections/{slug}/`, materialized as `sections/{slug}/index.html`, with a host
that serves directory indexes. Example: `/sections/newtons-universal-law-of-gravitation/`.
The namespace avoids conflicts with assets, the TOC, and future supporting pages.
Trailing-slash redirects and HTTPS/canonical host behavior belong in static hosting
configuration; test them before distributing links.

Internally use `cnx:m71410`-style section keys and retain each original UUID. New local
sections receive permanent UUIDs. Human-readable slugs are stored separately and frozen
at publication, even if the title changes. Current titles and proposed slugs have no
collisions. Future collisions get a short semantic qualifier; if ambiguous, append a
stable ID fragment, never a chapter/section number. Explicitly register aliases for
any unavoidable later move. Static redirect pages can work without server code, though
host-level redirects are preferable when supported. We cannot redirect a LibreTexts
domain we do not control; course materials need one final switch to the owned domain.

Object identity is `(section-id, original-object-id)`, e.g. an equation in `m67034`.
Use a deterministic, injective encoding for HTML/PDF anchors; preserve aliases if an
object moves. Never encode the displayed figure/example/equation number in its identity.
An object registry links source selectors to web/PDF anchors and each profile's labels.

Numbering profiles contain hierarchy/order, stable group keys, labels, counter reset
rules, unnumbered exceptions, and any verified legacy overrides. The build resolves
both cross-reference text and captions from the same table. Audit literal prose such
as “Equation 4.2” separately; do not silently rewrite it. One active profile publishes
at canonical URLs; show alternate labels parenthetically or provide a generated
concordance during transition. Both profile PDFs may be built from the same content.
Switching the active profile must leave the URL/anchor registry byte-for-byte unchanged.

The user-designated 744-page PDF, compiled 2026-07-07, is the course numbering authority.
Its hash is recorded. TOC pages 4–8 were extracted; page 4 was visually checked. Chapters
0–14 contain 136 numbered module entries; Chapters 15–18 cover four reference modules.
139 of these 140 titles match recovered titles after punctuation/case normalization;
one is a candidate: PDF 13.1 “Prelude to Special Relativity” versus source “Introduction
to Special Relativity.” The preface placement remains separate. No PDF prose replaces
the source. The current LibreTexts site is not used as an authority for these labels.

The PDF also lists 15 chapter exercise pages (`0.E` through `14.E`), while CNXML stores
exercises within modules. Propose generated exercise views selecting the same canonical
objects, not duplicated editable exercises. Verify actual exercise membership, solutions,
and numbering against the PDF before implementing this rearrangement. CNX labels and
all historical object numbering remain unverified: the draft CNX profile records only
the recovered hierarchy and intentionally leaves labels null.

## 6. Upstream mapping and review workflow

The identified upstream is OpenStax's `osbooks-college-physics-bundle`. Its College
Physics 2e collection is pinned at `fd1b25dfd5d8c6580c6e2b2b34a19e29cc69ada9`, separately
stored with checksum and license declaration. Only the collection has been snapshotted,
not the entire upstream textbook. The pinned collection declares **CC BY-NC-SA 4.0**,
unlike the recovered **CC BY 4.0** declaration. Track source-version-specific permissions
and credits before incorporating later upstream wording or figures; do not assume the
older license covers a newer source snapshot.

`metadata/upstream-map.proposed.json` contains a record for every local section:
22 are same-module-ID candidates; 119 are unresolved. Same ID proves a usable comparison
candidate, not unchanged content or confirmed derivation. Local CNX UUIDs remain in the
section registry. An unresolved record is distinct from a reviewed “no counterpart.”
No exported derivation chain exists to fill the rest automatically.

Mapping records use arrays of local and upstream sections, plus optional object/range
selectors, evidence, review status, reviewer/date, and intentional-difference notes.
Thus they can represent split, merged, partial, and many-to-many relationships. Match
remaining modules using archived derivation records first, then title similarity,
shared object IDs, figure hashes, and distinctive prose. All heuristic matches need
review. Preserve intermediate Concepts of Physics and momentum adaptations as useful
ancestry references rather than assuming a direct edit of College Physics 2e.

A future comparison job should accept two pinned upstream snapshots and the reviewed
mapping, producing a report only. Show (a) changes between old/new upstream, (b) local
differences from the mapped baseline, and (c) candidate applicable corrections. Separate
prose, math structure/rendering, media hashes/previews, alt text, attribution, and
hierarchy changes. Normalization may aid comparison in disposable representations but
must not modify source or hide notation changes. If a historical upstream ancestor is
unavailable, label the report a two-way comparison; do not imply a reliable three-way
merge. Preserve accepted/rejected decisions and intentional local simplifications.
Human-reviewed patches and normal Git review are the only path to textbook changes.

## 7. Next implementation steps and acceptance gates

1. Corroborate CNX 12.1 and historical CNX labels using an original export/PDF/archive;
   retain current uncertainty if none can be obtained. Review the 2022 MathML patch
   independently. Confirm the single course-title mismatch and preface placement.
2. Make a small representative rendering corpus: `m67034` (kinematics), `m67530`
   (vector Content MathML), `m67122` (tables), `m67807` and `m42709` (structural math
   problems/reference tables), a figure-rich page, and exercises with solutions.
   Compare original import, later migration, and course PDF visually without equating
   PDF text extraction to equation fidelity.
3. Prototype the XML/MathML renderers on those samples. Require no dropped or
   unsupported math nodes; verify vector styling, operator precedence, units, scripts,
   table structure, captions, and alt text. Approve any source repair as a focused patch.
4. Review the 26 link failures; create explicit mappings/repairs with evidence. Finalize
   stable URLs/object anchors and both numbering profiles, including exercise relocation
   and derived counters. Test that profile switching cannot change URLs or anchors.
5. Build the full static tree and PDF. Check complete module/object coverage, references,
   offline assets/fallbacks, page breaks, equations, navigation, attribution, and accessible
   reading. Run Linux case-sensitive link checks and clean rebuild comparisons.
6. Only then configure CI and releases with pinned tooling. Keep deployment separately
   gated. Ask the user for GitHub owner/visibility and consequential repository settings
   before creating `concepts-of-physics-2e`; ask about hosting/DNS before publishing.

Phase-one setup is reversible: only audit tools, documentation, derived reports, and
draft metadata have been added. No recovered file has been changed.

## Evidence and technical references

- [Recovered branch](https://github.com/cnx-user-books/cnxbook-concepts-of-physics/tree/introduction-to-physics)
- [Original import](https://github.com/cnx-user-books/cnxbook-concepts-of-physics/tree/e2b8ec04bd22d78da0e97826b9705a3f0cc6eba5)
- [Later MathML migration](https://github.com/cnx-user-books/cnxbook-concepts-of-physics/commit/018a9858aaeb02d46329c5a7fc903ab8b3107d95)
- [Historical EPUB release](https://github.com/cnx-user-books/cnxbook-concepts-of-physics/releases/tag/20230109.213414): API lists `introduction-to-physics.epub` (101,806,191 bytes); not downloaded or fidelity-validated.
- [Course-numbering PDF](https://coaphys.xyz/wordpress/wp-content/uploads/2026/07/Introduction-to-Physics-Park-PHYS-10-2026-07-07.pdf)
- [Pinned upstream collection and license metadata](https://github.com/openstax/osbooks-college-physics-bundle/blob/fd1b25dfd5d8c6580c6e2b2b34a19e29cc69ada9/collections/college-physics-2e.collection.xml)
- [MathJax MathML support and Content MathML limitation](https://docs.mathjax.org/en/latest/input/mathml.html)
- [Paged.js HTML/CSS and headless PDF workflow](https://pagedjs.org/en/documentation/2-getting-started-with-paged.js/)
