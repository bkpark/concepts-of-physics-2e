# Historical CNX PDF reference received

The user supplied `introduction-to-physics-12.1.pdf`, identifying it as version 12.1
downloaded before the CNX shutdown. An unchanged copy is preserved at
`../references/introduction-to-physics-12.1.pdf`, outside generated publication output
and outside the Git repository's ordinary tracked files (110,861,820 bytes).
Its SHA-256 is recorded in `metadata/recovery-lock.json`:

`9f1fd756b7892eca543f1b57c4fae433fa9509361e3beb51d3c306eb3deb6120`

The original Downloads file is unchanged. Back up the sibling reference directory
alongside the Git recovery bundle; cloning this repository alone does not retrieve PDFs.

## Evidence observed

- 671 PDF pages; title **Introduction to Physics**.
- Title page: collection edited by Andrew Park; content authors Bobby Bailey,
  Andrew Park, OpenStax, and James Rittenbach; CC BY 4.0.
- Printed collection URL: `https://legacy.cnx.org/content/col25183/1.12`.
- Printed structure revision: 2019/10/14; PDF generated: 2019/11/01 14:46:23.
- PDF metadata identifies Prince 11 and DocBook XSL Stylesheets V1.79.1. This identifies
  a historical rendering path, not a decision to adopt that tooling now.
- TOC starts with Chapter 1 Introduction and Chapter 2 Kinematics; appendices A-D
  are distinct from the LibreTexts PDF's Chapters 15-18. Section titles in this TOC
  are printed without section-number prefixes; do not infer section counters from
  chapter offsets alone.

The filename/user-provided designation `12.1` and the printed legacy notation `1.12`
are retained as separate literal fields. This inspection does not establish the service's
conversion rule between version formats. The PDF is accepted as the user's historical
12.1 reference; it does not by itself prove that the 2022 Git import has identical
prose, math, or module revisions.

## Attribution and source membership

The extracted attribution section contains **141 unique module IDs**, exactly matching
the recovered collection's 141 modules: none missing on either side. It supplies module
revision URLs, authors, copyright holders, and licenses absent from the CNXML export.
**114 records include direct “Based on” module/version links.** These include both
OpenStax originals and intermediate adaptations by Bailey and Rittenbach. Do not treat
every direct ancestor as a College Physics 2e module.

Machine-readable files:

- `references/cnx-12.1-pdf-evidence.json`: PDF hash, metadata, scope, membership checks,
  and raw text for the inspected front/back matter pages.
- `references/cnx-12.1-module-attributions.json`: per-module revision, attribution,
  direct ancestors, and PDF page locations. Extraction results are explicitly marked
  as pending full visual review; text extraction may affect punctuation/line breaks.

The title page and attribution page 655 were visually inspected. Front matter and the
final 25 pages were extracted. This was **not** a complete 671-page visual review or
a full content comparison. `tools/inspect_cnx_pdf.py` reproduces the extraction using
`pypdf` without editing the PDF or textbook.

## Impact on next steps

Use this PDF as the historical CNX rendering, numbering, and attribution reference.
Continue using the separate 2026-07-07 LibreTexts PDF for course-numbering alignment.
Neither replaces the editable XML source. Preserve both unchanged.

Next, review extracted attribution records and incorporate their direct ancestry into
the mapping manifest, tracing intermediate adaptations where necessary. Compare module
text and representative equations against this PDF before upgrading the recovered Git
snapshot's status to a verified source match. Derive CNX section/object-numbering rules
from actual body pages, not just TOC positions. The initial assessment's claim that
no historical PDF/attribution evidence was available is now superseded.
