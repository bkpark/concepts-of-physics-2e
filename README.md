# Introduction to Physics

An openly licensed physics textbook adapted and revised by Andrew Park at College of Alameda.

[Read online](https://intro.coaphys.xyz/) · [Download the PDF](https://github.com/bkpark/concepts-of-physics-2e/releases/download/cp2e-ver1.1/cp2e-ver1.1.pdf) · [Full contents](https://intro.coaphys.xyz/contents/) · [Version 1.1 release](https://github.com/bkpark/concepts-of-physics-2e/releases/tag/cp2e-ver1.1)

## Version 1.1

Published October 18, 2026, version 1.1 includes chapters 0–14, appendices A–D, a preface, an index, and licensing and attribution information. The 654-page PDF includes linked contents, index entries, and bookmarks. The book contains 648 chapter-end questions and exercises, along with inline checks.

The online edition supports search, light and dark themes, and equation copying as LaTeX or ASCIIMath. Its default **Lecture-aligned numbering (July 2026)** matches the recorded Physics 10 lectures at College of Alameda; readers can also select CNX-aligned numbering. Section URLs remain stable when the numbering preference changes.

### Downloads

All files are available in the [version 1.1 release](https://github.com/bkpark/concepts-of-physics-2e/releases/tag/cp2e-ver1.1):

| File | Use |
| --- | --- |
| [Screen PDF](https://github.com/bkpark/concepts-of-physics-2e/releases/download/cp2e-ver1.1/cp2e-ver1.1.pdf) — 68.7 MB | Recommended for reading on screen; the default website download. |
| [Print-quality PDF](https://github.com/bkpark/concepts-of-physics-2e/releases/download/cp2e-ver1.1/cp2e-ver1.1-print-quality.pdf) — 123.7 MB | Full-resolution original with the same pagination, links, and bookmarks. |
| `cp2e-ver1.1-static-html.zip` | Self-hosting website package, including the screen PDF. |
| `cp2e-ver1.1-source.zip` and `cp2e-ver1.1-source.bundle` | Tagged source and recoverable Git history. |
| `cp2e-ver1.1-publication-fixes.patch` | Post-tag renderer corrections; apply to the tagged source. These changes are already included on `maintained`. |
| `SHA256SUMS.txt` and release records | File checksums, publication details, and validation results. |

See the [release documentation](docs/release-cp2e-ver1.1.md) for changes, build details, and verification scope. [Version 1.0](https://github.com/bkpark/concepts-of-physics-2e/releases/tag/cp2e-ver1.0) remains available as an archived release.

## Working with the source

The default branch, **`maintained`**, contains the current publishing project. The inherited historical `main` branch contains a different book and is preserved for provenance.

- [`maintained/`](maintained/README.md): editable textbook prose, MathML, figures, section identities, and numbering metadata.
- [`prototype/`](prototype/): HTML rendering, website assets, and PDF-production tools. The directory retains its original development name.
- [`metadata/release.json`](metadata/release.json): current release metadata and public website address.
- [`docs/`](docs/): publishing instructions, editorial history, and provenance records.
- Repository-root `modules/`, `media/`, and `collections/`: the preserved historical source baseline.

To generate development HTML from the repository root, with Python and the required build dependencies installed:

```sh
python prototype/build.py course --all
python prototype/build.py cnx --all
python -m unittest discover -s prototype -p 'test*.py'
```

The output is written to `prototype/dist/course-full/` and `prototype/dist/cnx-full/`. Published artifacts are frozen; use development builds for changes and prepare a new release before replacing approved PDFs. Consult the [maintained-source guide](maintained/README.md) and [release documentation](docs/release-cp2e-ver1.1.md) before preparing a publication.

## License and attribution

Copyright © 2018–2026 Andrew Park for the collection and its original adaptations and revisions. Copyright in incorporated material remains with its respective copyright holders. Except where otherwise indicated, the textbook is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

The book is adapted from OpenStax *College Physics*, through Bobby Bailey’s *Concepts of Physics*, with momentum material from James Rittenbach’s adaptation. Retain the source and figure credits supplied with the material. Detailed notices appear in the textbook’s **Licensing and Attribution** pages and the chapter and appendix **Sources and adaptations** sections.

Future source imports must have compatible licensing. See the [license-source audit](docs/license-source-audit.md) and [upstream source review](docs/upstream-cc-by-reference.md) for the provenance and licensing boundaries used in this project.

## Source history and preservation

This repository is a fork of [cnx-user-books/cnxbook-concepts-of-physics](https://github.com/cnx-user-books/cnxbook-concepts-of-physics). *Introduction to Physics* was recovered from CNX collection **col25183**, legacy identifier **WPust2k9@12.1**; the repository name reflects its ancestry.

Original module identifiers, source snapshots, historical branches, and preservation tags are retained. The [recovery assessment](docs/recovery-assessment.md), [historical PDF evidence](docs/cnx-pdf-reference.md), and [recovery lock](metadata/recovery-lock.json) document that history. Earlier planning and audit documents describe their respective stages; the version 1.1 release documentation records the current published edition.

To check the preserved historical baseline:

```sh
python tools/verify_baseline.py
```

Preserve exact file bytes when checking historical sources. In particular, disable automatic line-ending conversion before checking out historical files on Windows. Baseline verification protects the archived source; it does not validate every mathematical or factual statement in the textbook.
