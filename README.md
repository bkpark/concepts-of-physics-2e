# Introduction to Physics

Recovery and publishing project. Intended maintained GitHub repository name:
`concepts-of-physics-2e`. The book title remains **Introduction to Physics**.

Start with [the recovery assessment](docs/recovery-assessment.md).

This is phase one, not a completed publishing system. The 959 recovered files are
unchanged from the earliest available Introduction to Physics import. Metadata files
ending in `.proposed.json` are reviewable drafts, not deployed URLs or verified
numbering rules. No remote repository has been created or modified.

## Preservation

- `recovered/cnx-import-2022-06-23` pins original import `e2b8ec04bd22d78da0e97826b9705a3f0cc6eba5`.
- `recovered/introduction-branch-2022-09-29` pins branch tip `4a8661442d4612738ff388f7f1be7c5deabd1b68`.
- `metadata/recovery-lock.json` records identity evidence, file hashes, and archive hashes.
- A full Git bundle and two exact Git-export tar archives are stored one directory
  above this project. The sibling `recovered.git` mirror preserves original remote refs.
- The original remote is named `recovered`; its local push URL is disabled.

The default historical `main` branch contains a different book. Work here is on
`recovery-assessment`, based on the correct import. Do not use the historical `main`
as the maintained book's starting point. A future maintained `main` must be created
deliberately from this work, preserving the historical refs.

The user has now supplied the historical **12.1 PDF**, preserved unchanged alongside
the repository. It prints collection `col25183/1.12` and a generation date of
2019-11-01. Its attribution section identifies all 141 recovered module IDs and
provides 114 direct ancestry records. See [the PDF evidence update](docs/cnx-pdf-reference.md).
The PDF is the historical rendering reference; exact source-text and MathML agreement
between it and the Git import still requires comparison.

## Reproduce the audit

With Python 3.12+ and Git, from this directory:

```sh
git config core.autocrlf false
python tools/verify_baseline.py
python tools/inventory.py
```

Disable automatic line-ending conversion before checking out historical files on
Windows. The verifier compares raw working bytes to the original Git blob IDs as well
as SHA-256 checksums; a normalized checkout must not be mistaken for an exact copy.
The maintained branch adds `.gitattributes` to disable automatic line-ending conversion.
When exporting a historical tag that predates that file, use
`git -c core.autocrlf=false archive` to keep archive members byte-identical too.
The verifier checks original bytes and preservation tags. The inventory command regenerates
`reports/*.json` from the working source without changing it. Reports diagnose known
issues; a successful run does not certify publication readiness or validate all MathML.

`tools/seed_metadata.py` created the initial draft manifests and deliberately refuses
to overwrite them. Edit reviewed metadata through Git; do not regenerate published
identities when a title changes. The PDF TOC evidence is already checked in, so no PDF
package or network is needed to reproduce the inventory.

## Attribution

The recovered collection declares CC BY 4.0. Preserve all recovered attribution and
figure credits. Its preface identifies Andrew Park's adaptation, Bobby Bailey's prior
adaptation, James Rittenbach's momentum contribution, and OpenStax College Physics.
The later branch's single `authors` attribute is incomplete evidence of authorship.
The upstream reference collection has its own CC BY-NC-SA 4.0 declaration; it is a
comparison reference, not incorporated textbook content. See the assessment for the
attribution and licensing work still required before publication.
