# College Physics 2e: pinned CC BY 4.0 update reference

Use commit **f98d7a792138a6133fe7267d17e70aa04e9ccbed**, dated **2026-02-04 03:33:26 UTC**,
from [OpenStax's source repository](https://github.com/openstax/osbooks-college-physics-bundle/tree/f98d7a792138a6133fe7267d17e70aa04e9ccbed).
This is the latest unambiguous CC BY 4.0 snapshot identified in the public repository
history, not a separately verified downloadable PDF edition or semantic release number.

## License boundary

The snapshot is the immediate parent of
[5182c46ee4854d84e3e35ea34e5ed0bef461b19b](https://github.com/openstax/osbooks-college-physics-bundle/commit/5182c46ee4854d84e3e35ea34e5ed0bef461b19b),
which changed LICENSE, README, and both book prefaces to NC-SA on March 19, 2026.
At the selected snapshot, LICENSE, README, the College Physics 2e collection XML,
and its preface all declare CC BY 4.0. Exact copies and SHA-256 checksums are retained
under `references/college-physics-2e-cc-by/` and in
`metadata/upstream-cc-by-reference.json`.

The collection declaration was changed only on April 23, 2026, in
[9065107cf140924c253aae15e82f8f75cba401df](https://github.com/openstax/osbooks-college-physics-bundle/commit/9065107cf140924c253aae15e82f8f75cba401df).
Its parent is therefore NOT the recommended cutoff: it has inconsistent declarations.
No claim is made that later NC-SA versions can be imported under the earlier license.
The [CC BY 4.0 deed](https://creativecommons.org/licenses/by/4.0/) explains that its
granted freedoms cannot be revoked while the license terms are followed.

## Special relativity

The snapshot contains all seven chapter modules, including these identifiable updates:

- `m42531`, Simultaneity and Time Dilation: September 17, 2023, erratum 22075,
  commit [949cdcd94269aaee6a5bb042cd7fc56addda3591](https://github.com/openstax/osbooks-college-physics-bundle/commit/949cdcd94269aaee6a5bb042cd7fc56addda3591).
  The train/flash-lamp explanation specifies B's reference frame, distinguishes
  nonsimultaneous emission from nonsimultaneous arrival in A's frame, and clarifies
  agreement on the order of arrivals at A. This is a substantive review candidate,
  not a conclusion that all problems with the explanation are resolved.
- `m42540`, Relativistic Addition of Velocities: erratum 19462, April 14, 2022,
  followed by MathML/layout changes in May 2022.
- `m42542` and `m42546`, Relativistic Momentum and Relativistic Energy: introductory
  link revisions in July 2022; the energy module also has December 2022 formatting changes.

The manifest records each module's exact hash and recent commit history. These
findings establish that pre-license-change relativity updates are available; they
do not yet constitute a section-by-section comparison with Introduction to Physics.
No textbook content or generated release has been changed.

## Preservation and import policy

The complete source archive is stored locally at
`output/upstream/college-physics-2e-cc-by/f98d7a792138a6133fe7267d17e70aa04e9ccbed.tar.gz`
(422,332,670 bytes), with SHA-256
`62a1b3545388115220058b88edfd3a0b84fb5a2f651cb0a1c47052cb9dd80f2d`.
It is not committed to Git or included in the website package. Its immutable
commit-based download URL is in the manifest. The archive contains all 283 modules
referenced by the College Physics 2e collection. Automated module-text screening
found no explicit NC/SA/ND license strings; this is not a substitute for reviewing
individual figure credits, external resources, and third-party exceptions before reuse.

The structured local-to-upstream mapping now pins this CC BY snapshot; every existing
candidate target ID was checked for membership in its collection. Unresolved mappings
and intentional adaptations remain unchanged. Never use floating upstream main for
updates. Review proposed differences before merging; imported content must preserve
Introduction to Physics's CC BY 4.0 reuse rights, without NC or SA restrictions.

At the author's explicit direction, prior NC-SA comparison copies may remain in Git
history. No history rewrite is planned. They remain excluded from publishing inputs.
