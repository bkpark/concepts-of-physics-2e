# License-source audit

The restrictive declaration belongs to OpenStax College Physics 2e in
`openstax/osbooks-college-physics-bundle` at commit
`fd1b25dfd5d8c6580c6e2b2b34a19e29cc69ada9`. The pinned collection declared
CC BY-NC-SA 4.0. The current official 2e preface corroborates that declaration:
https://openstax.org/books/college-physics-2e/pages/preface
The original College Physics preface declares CC BY 4.0:
https://openstax.org/books/college-physics/pages/preface

## Removal from current source tree

Removed the copied `references/college-physics-2e.collection.xml` and three
comparison modules: `references/repair-evidence/m42216.cnxml`, `m42596.cnxml`,
and `m42709.cnxml`. Provenance URLs and checksums remain; the mapping tools now
use a sorted set of module identifiers rather than copied collection XML.
No prose, equations, illustrations, titles, or hierarchy from those files is
retained in the replacement identifier manifest.

## Textbook impact

The release package allowlist excludes the references directory. Its manifest
contains no reference snapshots. Source verification accounts for all 955
maintained content files as the recovered baseline plus four initialization
repairs and 27 approved editorial changes. No additional imported upstream
modules or media appear in that maintained layer.

The four initialization repair implementations operate on recovered content:
R1 adds two missing exponent values; R2 deletes empty malformed markup;
R3 reconstructs notation using the original annotation and subtree; R4 retargets
an existing internal link. The later upstream sources were corroborating evidence,
not imported replacement passages or figures. This audit makes no change to those
repairs. The X12–X14 references are outbound links to an OpenStax table, not a copy
of that table. User-approved editorial wording and equations remain unchanged.

The historical baseline verifier passed for all 959 files and both preservation
tags. The PDF checksum is unchanged. There is no identified textbook content to
remove as a result of the four reference-copy removals, and no site upload is
needed for this cleanup. This is an audit of migration inputs and changes, not a
new legal determination of every historical image's rights.

## History and future work

The removed reference copies remain in earlier migration commits already pushed
to GitHub. This cleanup does not erase Git history. Purging those historical
copies is a separate history-rewrite operation, with care required to preserve
the untouched CNX baseline and its tags. No history was rewritten here.

Do not import CC BY-NC-SA content. Future comparison work may record provenance,
identify factual corrections, and propose independently authored repairs; imported
wording, MathML, or media requires verified CC BY-compatible source-version
provenance. The 2e identifier mappings are review aids, not permission to reuse.

The author subsequently confirmed that the removed NC/SA reference copies may remain
in historical commits. Do not purge history. The update source is now the separately
verified CC BY 4.0 snapshot documented in [the reference report](upstream-cc-by-reference.md).
