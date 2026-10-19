# Introduction to Physics - version 1.1

## Final release

The maintainer has approved the complete 654-page book and its screen-optimized edition. The approved release is published on the existing Sites project at https://intro.coaphys.xyz. Publication receipts record the completed deployment and GitHub release.

The default website download is `cp2e-ver1.1.pdf`, the approved 68.7 MB screen-optimized PDF. The approved 123.7 MB original is `cp2e-ver1.1-print-quality.pdf`, a GitHub-release-only asset. It is excluded from the website folder and ZIP, and the website contains no print-quality download link. Both PDFs preserve the same pagination, links, and bookmarks.

## Changes from version 1.0

- Reviewed CC BY-compatible upstream corrections, factual updates, and maintainer-directed revisions across the textbook; retained source attribution and revision records.
- Revised chapter exercises: 648 ordinary questions and exercises, collected at chapter ends with sequential numbering. Inline checks remain in the sections. Exercise answers remain outside the textbook release.
- Revised mathematical typography, figures, learning objectives, summaries, and appendix reference material.
- Complete two-column PDF with cover, title and copyright pages, contents, preface, chapters 0-14, appendices A-D, index, and book-wide licensing and attribution. Roman front matter and Arabic pages 1-642; 202 bookmarks and 2,615 internal link areas.
- Website search, sequential navigation, stable chapter/section links, numbering selector, theme selector, equation copying as LaTeX or ASCIIMath, and favicon.

## Release checks

The package contains 174 HTML pages. Automated checks cover 9,662 local links, 141 exact source-module copies, 10,580 source anchors, 6,442 mathematical expressions, and sequential numbering for all 648 ordinary exercises. Both numbering-profile builds report no issues.

All public pages were checked in Chrome at 1280px and 390px widths with external rendering requests blocked. Checks found no broken images, missing image descriptions, unnamed links, duplicate IDs, root horizontal overflow, or script errors. Search, theme selection, numbering selection, LaTeX copying and ASCIIMath copying passed. Home-page desktop and mobile renders were visually reviewed. This is not a full accessibility certification or independent numerical audit of every exercise.

The immutable historical baseline check and 36 rendering tests pass. The old version 1.0 ledger-replay utility does not support the later maintainer and multi-file ledger formats; complete replay of that historical ledger is not claimed. Current source bytes are verified directly against both builds and the package. The release manifest records the exact module and public-file hashes.

PDF approval and existing PDF verification are retained through byte-for-byte hash checks. Website packaging does not regenerate the PDFs. The smaller PDF was also compared visually at 200% screen scale on 12 selected pages; all page content streams, labels, link annotations and bookmarks match the original.

## Assets and upload

Prepared files are in `output/releases/cp2e-ver1.1/`:

- `cp2e-ver1.1-static-html.zip`: website package, including only the screen PDF.
- `cp2e-ver1.1.pdf`: default screen PDF; website and GitHub release.
- `cp2e-ver1.1-print-quality.pdf`: GitHub release only.
- `artifact-manifest.json`, `release-record.json`, `release-checks.json`, `browser-audit.json`, and `SHA256SUMS.txt`: provenance and verification.
- `UPLOAD-INSTRUCTIONS.txt`: static-host deployment and live checks.

Publish only `public/` or the website ZIP contents. The sibling `site/` directory contains development/build data and must not be uploaded. The public source directory contains the maintained CNXML. The crawler policy excludes PDF download paths from compliant crawlers and leaves HTML crawlable.

The Git tag is cp2e-ver1.1. Release assets include a Git source-history bundle and an exact source ZIP. Version 1.0 artifacts and tags are preserved. Consult the publication receipt for deployment and live download verification.

## Rebuild the website package

Use the documented bundled Python/Node/Playwright/Chrome environment, with `NODE_PATH` pointing to the runtime's Node packages. From the repository root:

```powershell
python prototype/build.py course --all --release
python prototype/build.py cnx --all
python -m unittest discover -s prototype -p 'test*.py'
python prototype/tools/package_release.py
node prototype/tools/audit-release.cjs --public
python prototype/tools/check-release-package.py
```

Before packaging, copy the approved screen PDF to the release directory as `cp2e-ver1.1.pdf` and the approved original as `cp2e-ver1.1-print-quality.pdf`. Retain their approval hashes from `reports/1.1/screen-pdf/optimization.json`. The PDF-production tools and print content are in `prototype/tools/` and `prototype/print-content/`; chapter and assembly reports record pagination and link data. Byte-identical regeneration of Chrome PDFs is not promised; preserve the approved binaries and checksums.

## Sites download delivery

Sites rejected the 68.7 MB PDF at its Git source-upload limit. The live Sites variant links Download PDF directly to the approved screen PDF in the GitHub release. The self-hosting ZIP still embeds that same PDF and uses local download links. The print-quality original is never linked by the website. Both variants are hashed in the publication receipt. The failed unpublished Sites commit is retained in the earlier local checkout for recovery.

## Publication verification correction

Live visual review found incorrectly encoded middle dots and dashes in the HTML renderer templates. These are corrected in the live site and static HTML ZIP. The approved PDFs and maintained textbook CNXML are unchanged. The source ZIP and bundle preserve the original `cp2e-ver1.1` tag; apply `cp2e-ver1.1-publication-fixes.patch` at that tag for the corrected renderer and live audit. The maintained branch also records this correction without moving the release tag.

## Main-domain canonical URLs

Sites version 186 sets all 174 canonical URLs to `https://intro.coaphys.xyz`. The self-hosting ZIP includes the same update. Both domains returned all 174 pages successfully, with the expected canonical URLs; navigation, search and the screen-PDF link passed on each domain. `intro-1-1.coaphys.xyz` remains a working alias. The PDFs are unchanged.

## Theme asset cache update

Sites version 187 adds content hashes to stylesheet and theme-script URLs, including in the self-hosting ZIP. This bypasses stale assets cached before the hosting migration. A simulated stale stylesheet reproduced the reported light-only appearance and the versioned URLs corrected it. Mobile Chrome emulation passed Light/Dark switching, reload persistence and navigation on both domains. The maintainer subsequently confirmed that the phone issue was a stale stylesheet and that the update resolved it. The PDFs are unchanged.

## Closeout and version 1.2 starting point

The final closeout audit confirmed that the maintained branch is pushed, all 19 assets listed in the version 1.1 checksum manifest match the published GitHub digests, and the version 1.0 release notes include the archived PDF link while its original assets remain unchanged. The maintainer reports that the printed book through Unit 3 looks good; detailed reading and markup will inform version 1.2. This does not constitute a full print review of the remaining units.

Start version 1.2 from the current `maintained` branch, which includes the post-tag HTML punctuation correction, main-domain metadata, canonical URLs, versioned theme assets, and updated READMEs. The latest implementation/documentation commit before this closeout is `a00c9a6373c806aa7ef1aafffb4d4f303c13f0a1`. Preserve the `cp2e-ver1.1` tag, approved PDFs, source archives, and published release assets. Use a separate development branch or worktree for 1.2, keep outputs separate, and retain the live 1.1 site until a new publication is authorized.

The local untracked `reports-objectives-overview.txt` is an objectives/headings inventory. It has been retained without modification and is not part of the release.
