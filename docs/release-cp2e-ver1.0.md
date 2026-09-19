# Introduction to Physics — cp2e-ver1.0

The initial maintained edition is published at https://intro.coaphys.xyz.
The textbook remains CC BY 4.0 and uses Lecture-aligned numbering (July 2026),
matching recorded lectures for Physics 10 at College of Alameda. Section URLs and
object identities are independent of displayed numbering.

## Download and preservation

- `cp2e-ver1.0.pdf`: the exact published 1,149-page PDF.
- `cp2e-ver1.0-static-html.zip`: the exact webroot package, including the PDF and robots.txt.
- `artifact-manifest.json`: original per-file and textbook-source hashes.
- `release-record.json`: final publication status, provenance and limitations.
- `cp2e-ver1.0-source.bundle`: Git history, maintained source and historical preservation tags.
- `SHA256SUMS.txt`: SHA-256 checksums for release assets.
- `UPLOAD-INSTRUCTIONS.txt`: static Apache deployment instructions.

The original PDF and ZIP were promoted unchanged. Their embedded release-candidate
labels and false readiness fields record build-time status; this final release and
`release-record.json` supersede those labels. This avoids altering already-published
files. The release tag captures the same textbook module bytes with subsequent
provenance documentation and archival safeguards. The record identifies the earlier
PDF, website and package build commits. No new website upload is required.

## Scope and limitations

Includes 141 sections, 7,391 mathematical expressions and 563 image references.
All 25 reviewed unresolved references were resolved, M01/M02 corrections applied,
and the malformed M03 question part removed. PDF ordinary exercises are at chapter
ends, with Check Your Understanding inline. Website chapter navigation is grouped
by four units and includes a full contents page.

Exercise revision remains deferred. Among 803 uniquely matched reference exercises,
102 have label differences; other exercises do not have a unique automatic match.
CNX numbering remains a compatibility preview. PDF visual inspection sampled 21
pages, with automated link and margin checks; full accessibility certification is
not claimed. Three external interactive/video links need internet access.

Rebuilding requires the recorded Windows font/Chrome/Node/Playwright environment.
Fonts are not redistributed; byte-identical PDF regeneration is not promised.
Exact published artifacts and checksums are provided instead. See
`docs/release-candidate-cp2e-ver1.0.md` and `metadata/render-environment.lock.json`.

## Restore or develop

Verify asset hashes against SHA256SUMS.txt. To recover from the bundle:

    git clone --branch maintained cp2e-ver1.0-source.bundle textbook
    git -C textbook checkout cp2e-ver1.0

The bundle includes both historical recovery tags. External historical/course PDF
references and the large upstream comparison archive are not in Git; their source
locations and hashes are recorded in metadata. They are not required to serve the
published textbook. The source tag's release-build commands intentionally refuse
to overwrite frozen 1.0 output; development builds remain available. For an exact
pre-finalization build workflow, use the recorded build commits in a separate
checkout and the locked environment, never overwrite the archival assets.

## Next release

Target cp2e-ver1.1: reviewed CC BY upstream corrections starting with Special
Relativity, a systematic remainder-of-book comparison, and conceptual exercise
revision informed by the author's MyOpenMath exports. No 1.1 content changes are
included here. Preserve existing section URLs and object anchors.
