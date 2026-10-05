# Sites preview hosting

Published 2026-09-27: https://introduction-to-physics-1-1-preview.bkpark.chatgpt.site

This is the full HTML 1.1 work-in-progress preview, not a final release or new PDF. The existing 1.0 website remains unchanged. Search indexing is discouraged through robots.txt and page metadata; the site is public.

## Deployment identity

- Project: appgprj_6ab9a2afbb1c8191bf74ed20b035ce33
- Version: appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_a689121ad7488191bc7b55a8b7751021
- Deployment: appgdep_6ab9a3fbc2d0819183d20a64c49d3884 (succeeded)
- Generated source commit: 8fac83d83c8aa38203247b6abe85d40bb3d5ade9
- Generated checkout: ../sites-preview-1.1
- Archive: output/sites-preview-1.1.tar.gz
- Validation: prototype/qa/course-full-validation.json and course-full-browser-audit.json
- Application evidence: reports/1.1/priority34-application/manifest.json

## Custom domain

Status at registration: pending DNS and certificate validation. In the coaphys.xyz zone, add:

| Type | Name relative to coaphys.xyz | Value |
|---|---|---|
| CNAME | intro-1-1 | custom-domains.chatgpt.site. |
| TXT | _openai-site-verification.intro-1-1 | openai-site-verification=LVY9ENGnljCJ8OrFVjIQGYrktaBZs0K_kDBLleapoo4 |
| TXT | _cf-custom-hostname.intro-1-1 | f6f1ef08-3185-4953-b13a-90c9ee24af30 |

The provider may expect fully qualified names instead. Do not add apex A records: this is a subdomain. Keep the validation TXT records. Recheck the Sites custom-domain status after DNS propagation; registration alone does not confirm activation.

## Updating

Edit only the maintained source in the canonical textbook repository. Rebuild with `python prototype/build.py course --all`, run the appropriate source and browser validation, then run `python tools/prepare_sites_preview.py`. The latter refreshes the separate generated checkout and preserves its Sites project identity.

Use the Sites workflow helper with a fresh short-lived repository credential to commit and push the exact generated checkout, package static output, save a version and deploy it to the same project. Never create a replacement site for routine updates. Never store Git credentials. On this Windows host the generated Git checkout uses `http.sslBackend=openssl` with TLS verification enabled. The provided packaging shell script works with Git Bash and its /usr/bin plus the bundled Node directory on PATH; use relative archive paths to avoid Windows path translation issues.

The generated dist directory is also a portable static webroot for backup hosting. The canonical GitHub repository remains the maintained source of truth. Future updates can be published here without manually uploading individual website files; updates are not automatic until the build/publish workflow is invoked.


## Domain activation confirmed — 2026-09-27

After the maintainer added DNS, Sites refresh completed validation and routing activation. Domain, provider, and SSL statuses are active. An HTTPS request to https://intro-1-1.coaphys.xyz/ returned HTTP 200 with the textbook title and version 1.1 preview label. No DNS changes beyond the supplied records were needed.

## Chapter 0 update — 2026-09-27

Deployment succeeded to the same public site and existing custom domain.
- Saved version: appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_7f5ba183b26481918f5ab7420a5a0fe8 (version 2)
- Deployment: appgdep_6ab9b87509d4819198b85494ca5a8c38
- Pushed generated commit: 6af6d64ecfdd69f90c567204e41f2ce5b6a37cf1
- Archive SHA-256: 91772c3536969edabf48ed6e8d15a99f4e5252021f152fbae66f4351db0eb5f7
- Review: https://intro-1-1.coaphys.xyz/exercises/introduction-exercises/index.html
- Checks: full browser audit (156 pages, no findings), full source validation, targeted chapter0-review-validation.json, desktop/mobile visual inspection.

Windows workflow helper successfully committed/pushed; its packaging subprocess selected unavailable WSL Bash. Packaging completed using explicit Git Bash with the provided package-site.sh and relative paths, from the unchanged pushed source.

## Sequential reading navigation — 2026-09-27

Published successfully to the existing public preview/custom domain. Previous/Next controls appear at both ends of section and chapter exercise/review pages, with destination titles and current numbering.
- Version: appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_f8eb92a7fb988191b653091be4ad4ede (3)
- Deployment: appgdep_6ab9ba12e39c8191b5d27ee934ff7ca6 (succeeded)
- Pushed source: b131fbba857fc0d71a5680845377f7e03fb69044
- Archive SHA-256: 1ec4143a6fc37192426034de97ab8d1df3788843f4c7d103874a3bd5c5d11d23
- Validation: full browser audit (156 pages, no findings) and reading-navigation-validation.json.
- Packaging used the same explicit Git Bash fallback documented above after the workflow helper pushed source successfully.

## Section 0.2 attribution footer trial — 2026-09-27

Deployment succeeded; only Section 0.2 HTML and generated provenance changed.
- Version: appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_bd12c36c99648191b04bd12a59167bd2 (4)
- Deployment: appgdep_6ab9bba80d648191a8be43864bb8cd9a
- Pushed source: e8208d4cd3d61b2bec78028f4066658d9a02b0ae
- Archive SHA-256: 2b4e84886c31d84d15c327cc2308d6bce8b41a24e18ce65ae2158212ce3e00a4
- Packaging: same explicit Git Bash fallback after successful workflow-helper push.

## All-module attribution convention — 2026-09-27

Published Sources and adaptations footers across all 141 modules; source credit/link checks and target mobile rendering passed.
- Version: appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_4ef9bdd45e2c81919662495cfeb35ff4 (5)
- Deployment: appgdep_6ab9bd2a77748191a0847486b33ec1cf (succeeded)
- Pushed source: 8d4036cb75ee87ed427d8e72768e2a906b9f9791
- Archive SHA-256: b2d118ecf0dcf41736a621fc50f91d39270b62730de761ccf3c3b5fea96a786d
- Same explicit Git Bash packaging fallback used after successful workflow-helper push.

## Chapter 0 exercise additions — 2026-09-27

Published successfully. Chapter 0 contains 17 Questions and Exercises, with five approved additions.
- Version: appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_bda9f21979888191aeb3f3ea1c610835 (6)
- Deployment: appgdep_6ab9bfdf3be88191aa8ecce0e8ba1371
- Pushed source: 5b383668a84b7cb33ac13d885809c05ae7a7bbc5
- Archive SHA-256: dd5043d98842ce2e7142ea31fea5ea0d183b453499337a93b6a8f2b3af2c103d
- Full browser/source validation passed. Existing Git Bash packaging fallback used.

## Chapter 0 exercise order — 2026-09-27

Published successfully to the existing preview. All 17 exercises reordered by topic/progression with unchanged wording and IDs.
- Version: appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_a698986a05c08191b11207ff3bcb9d5d (7)
- Deployment: appgdep_6ab9c1d757c08191932b2c26a3bdb447
- Pushed source: f411e12ddbb7d2a2f3a3d27ef63ac9514a0c3549
- Archive SHA-256: ececcbe3308a5aff23b2de6cd2cd57d937fb8067a53414a0f9a4003f8089a1d8
- Validation: full source/link validation, both profiles rebuilt, targeted 17-ID/label chain and mobile fit check. Git Bash packaging fallback as documented above.

## Chapter 1 organization — 2026-09-27

Published successfully to the existing public preview/custom domain.
- Version: appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_7de1c3c11c448191823682f3ef1f9f95 (8)
- Deployment: appgdep_6ab9c461b8488191b278b8cdb60c0924
- Pushed source: 7446ec4b648e63d22bf6e6324bd6f06a42d960b2
- Archive SHA-256: 2917d825a252c43c74043a5ef42baad1b38b62170da391c1429bb79176cd4444
- Validation: 156-page browser audit, source/link/math checks, 38 continuous exercise labels, 28 alphabetized glossary terms and loaded displacement figure. Git Bash packaging fallback used.

## Duplicate review-link fix — 2026-09-27

Published successfully. Generated source 46280c3d1af8d2406b3869274a43f4b5b92bb38a; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_e9d18a2a795881918092e4d83e24aebc (9); deployment appgdep_6ab9c569e2388191878cbd40720d1af6. Archive SHA-256 6d6b5d7b38cfc5d9e51ae786c581bfdb88a2b5250f3e1298310329791f89a807. Full source/link checks passed; all section review-link destinations deduplicated. Same Git Bash packaging fallback used.

### Chapter 1 MyOpenMath-guided additions — 2026-09-27

Published six approved questions in topic order; Chapter 1 now has 44 consecutively numbered questions. New questions are 17, 18, 27, 29, 30, and 38. Existing question wording and stable IDs are preserved.

- Sites version: 10 (`appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_6d7c433aba8081919ccd3ddd082a799c`).
- Deployment: `appgdep_6ab9c8a507048191bb784e3a0514610d`; native status `succeeded`.
- Sites source commit: `96bbec2076074e590f1bbcaa041f762f6a35e596`.
- Archive SHA256: `3f427f314df7b6ecfed428a42aed19ce3a1b3eedd9f6c4d247d040c37526916f`.
- Review: https://intro-1-1.coaphys.xyz/exercises/kinematics-exercises/index.html#questions
- Validation: course and CNX builds, full source validation, 44 sequential exercise labels, retained existing exercise XML, and targeted mobile layout passed. No new PDF binary generated.

### Exercise review refresh — 2026-09-27

Published Sites version 11: Exercise 2 wording, shared path figure within Exercise 4 with dynamically numbered references from Exercises 5–7, and removal of 223 ordinary exercise solutions. Retained all 40 Check Your Understanding solutions and worked examples. Course/CNX builds and source/link validation passed; existing three external-media issues remain.

- Source commit: `34f6533ba7ed50f4b866e003ceb9b4127a419da4`.
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_5031a7b8955481919b40fb3e0df80f28`.
- Deployment: `appgdep_6ab9cc7575e481918499ef11e5d76e0c`; succeeded.
- Archive content hash: `sha256:06ef49fb6e9613e21774d135e3f89e9b088715e0e137e5c31173f5d12ddc0c95`.
- Supersedes pending-publication notes for these exercise-review changes. No new PDF binary generated.

### Degree symbols and units — 2026-09-27

Replaced 233 mistaken masculine ordinal indicators with degree symbols across 22 maintained modules (temperature/angle contexts). Corrected m52316 Exercise 8 numeric/unit markup and Exercise 9 compact upright m/s. Reversible TYPE-DEGREES records preserve before/after source; historical source untouched. Course/CNX builds and fidelity/link validation passed.

Published Sites version 12; source b2dca6c9cfc5064bfdcad9259e1709720e71c8b0; saved version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_8110b9097560819197ca9e25b6f6d522; deployment appgdep_6ab9ce3c8bf48191a065565afda4d4d0 succeeded. Archive content hash sha256:fbe874e3ced0442de0bc4e23b84374fa4ca3fc425730f0468df52cb6da26668f. No new PDF binary generated.

### Exercise 30 part labels — 2026-09-27

Added (a), (b), (c) for rising, highest point, descending; EX-C1-REVIEW-30-m68876 records approval and before/after source. Course/CNX builds and validation passed. Published Sites version 13: source f2c101d102e8b92270059c02169bcd122513f815; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_0983a22d76b48191a27a88b527700cf9; deployment appgdep_6ab9d055110481919fd24b481c4fe162 succeeded. Archive content hash sha256:77dd60ddb1344d497f19ab122ee82b5602e62713112d67d4c88dc6a39875ffb6.

### Exercise 31 part labels — 2026-09-27

Replaced three fragmented questions with one sentence labeled (a), (b), (c); EX-C1-REVIEW-31-m68876. Course/CNX builds and validation passed. Published Sites version 14: source e93ae72045b3270194f55bbd4cb02fa514739659; saved version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_94f910ae720c81918a4e4c949275aec5; deployment appgdep_6ab9d16fa4c08191ad813666e4768004 succeeded. Archive content hash sha256:f0019db1f0c7eabe4908bc205c996bd5a71aaa36f373c9d3df87cc42403cb60e.

### Exercise 40 shared setup and speed — 2026-09-27

Applied EX-C1-REVIEW-40-m67038: reference Exercise 39 for setup and ask about minimum/maximum speed in (b). Course/CNX builds and validation passed. Sites version 15 published: source 9b339cf9a3c98816daf2f1cf65e64aa917e3d7e8; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_e3fbfc7025cc819188c7f8f9ac43b5b6; deployment appgdep_6ab9d34fd02c81919a4c5be05594b11c succeeded. Archive content hash sha256:932fafbdc607ac7d9a4cbd587ace3966cdbe96add83a27a29787f342baadb75b.

### Chapter 2 organization — 2026-09-27

Published glossary (34 terms), summaries, and 40 existing questions in chapter-end review; retained one inline check. Maintainer approved collecting the two CNX inline Normal Force/Tension questions. Source wording/IDs preserved; relocation links corrected; full builds/source/link validation and targeted desktop/mobile check passed. See reports/1.1/chapter2-structure/review.md.

Sites version 16: source 8d4e430205649c7ef9d5c6cc763a48232ad2aeb5; saved version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_c07b34db653481918a12b2e07d2cbab7; deployment appgdep_6ab9d57d8a548191a0244ccbc7677727 succeeded. Archive content hash sha256:913ee8828d6539d99c12a7b16607c20f937e1bb2b39d73d9f49b00349fd2a2c5. No new PDF binary generated.

### Quotation typography and style guide — 2026-09-27

Created docs/style-guide.md; approved curly prose quotation marks/apostrophes and logical punctuation applied in 65 modules. MathML and XML attributes preserved; source/build/link validation passed. Published Sites version 17: source 28af0a7a115fb55be2dce34ff6bb25df4aca0671; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_16422e8b49188191bb01f7705adc0830; deployment appgdep_6ab9da4f153c8191bc6111cbbf18368e succeeded. Archive content hash sha256:68e06dea198a82d056715ded9a857b1f2368982040be178d9cbdebfb6344c1e7.

### Codex disclosure in preview banner — 2026-09-27

Requested banner: “Version 1.1 preview — work (using Codex) in progress.” Applied through tools/prepare_sites_preview.py to all preview pages, pending the maintainer-written preface.

Published Sites version 18; source 689c6e7395ff6582dc1c119a6cde7c249deaf091; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_a9f24c2b1034819194e8ee0aa9b137e7; deployment appgdep_6ab9dc68ac1c81919ace83503b61ab59 succeeded. Archive content hash sha256:2b87fb051bd31421c013d4572e3e8be136d5997ba3cec8d0d8261625418d4f78.

### Chapter 2 exercise placement and Exercise 5 — 2026-09-27

Published approved Exercise 5 wording and former Exercise 6 placement after the third-law system-choice question. Former 6 is now 20; former 7 is now 6; cancellation/system-choice question is 19. All 40 questions retained; old anchors preserved. Builds, source/link checks and sequential numbering/mobile validation passed. Shared PDF placement code updated; no PDF binary generated.

Sites version 19; source ba9438d233f19415b240c50f3d62ffdd9be96f11; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_6a5cf6228ba8819190fdb94e7ccfc569; deployment appgdep_6ab9f202c65c81919929ed7a9e17abd5 succeeded. Archive content hash sha256:656d6cd51f0386dc43a9d9fadb9ef8b0ca1800af60ce0851754f65b7133048e0.

### Preview version 20 — Chapter 2 Exercises 10, 14, and 15

Applied the approved force/mass comparison, aircraft-seat sensation, and ballistocardiograph recoil revisions. Exercise 14 relocation remains deferred until the overall chapter exercise reorder. Course and CNX builds and full validation passed with the same three known external-media findings.

- Source commit: `5f5a924897f160de0fcec996cfca7163da472e81`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_0292d47d4b548191a2f14ee33f713328`
- Deployment: `appgdep_6ab9f55b6fcc81918d4056124e059043` — succeeded
- Archive SHA-256: `d973e72e8d5214ac060e2c9eb96793a371e47d947e07f2ebb2384a9df832038d`

### Preview version 21 — Exercise 16

Published the maintainer-approved book-on-table question comparing Newton’s second and third laws. Numbering and stable exercise identity unchanged. Both builds and full validation passed (three pre-existing external-media findings).

- Source commit: `681cfacf83ed5e791580196c8a6fe721d4e155d8`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_c7035a697dd4819186ccf3a675804643`
- Deployment: `appgdep_6ab9f81d08b48191bc6a320d0b9b573f` — succeeded
- Archive SHA-256: `2e42727d7c7de3236dcb75f50b6a3d5cc063dcada6b268c54d99baa1c4455aed`

### Preview version 22 — Exercises 17, 21, and 22

Published approved garden-hose recoil and shorter normal-force/tension questions. Both profiles rebuilt and validation passed with the three known external-media findings. Numbering unchanged.

- Source commit: `28e8c8862b05de8f56bac94acc11b592cf819c0b`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_eb955834dfb0819184519731099e05c0`
- Deployment: `appgdep_6ab9fa042780819186b433fcbb265a2b` — succeeded
- Archive SHA-256: `9dadd423195fe19051006fd24b448cd4ecfaa66a5ff1f54b9e64b8705a1a9df4`

### Preview version 23 — Chapter 2 tape-question removal and pending edits

Published all approved pending question wording, including Exercise 25 eraser prompt. Removed former Exercise 26; chapter now has 39 consecutively numbered exercises. Course/CNX builds and validation passed; adjusted expected global projected count to 962 for this approved removal. Three known external-media findings unchanged. Exercise 14 relocation remains deferred.

- Source commit: `be669632433b01bc8bf2d552a0754f16361e976d`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_cfcb837001cc8191af7dc5d242e45411`
- Deployment: `appgdep_6ab9fbd9022481918f60127019328f7c` — succeeded
- Archive SHA-256: `7ad1838d9a1a8c8431987dc62aae53c04e3349babc569de12b2133f1bd10154e`

### Preview version 24 — Chapter 2 additions and final review order

Published all queued approved revisions/removals, six MyOpenMath-guided additions, topic ordering, and aircraft question relocation into Section 2.4. Chapter 2 now has 41 consecutive exercises. New questions: 1, 24, 25, 28, 29 (Tommy), 35; aircraft now 13. Existing exercise IDs preserved. Course/CNX builds and full validation passed; targeted Chapter 2 desktop/mobile browser checks found no math errors, broken images, or overflow. Known three external-media findings unchanged. No new PDF generated.

- Source commit: `5ed30adc7b8194abe67dd8d029cfafed922fe658`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_61624d02a51c8191a8b867377e8cb71f`
- Deployment: `appgdep_6aba035aa79c8191977fbfd050449562` — succeeded
- Archive SHA-256: `5a75c7669f3f9cac8c70df967f58c05d3a563dca3b71812abf280ba6b4f409c6`

### Preview version 25 — Chapter 3 organization

Collected 23 glossary definitions (alphabetized), section summaries, and 20 existing questions at chapter end. Two Check Your Understanding prompts/answers remain inline. Original question wording/order and identities preserved; no historical placement exception found in CNX PDF pages 107–132. All seven section pages checked, course/CNX builds and full validation passed, targeted review-page desktop/mobile checks passed including local links/anchors. No new PDF binary.

- Source commit: `d1d7cd61ff7c01fabc01175074d1774e426931af`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_6bf08050f32c8191a9bfdc6d8f40c107`
- Deployment: `appgdep_6aba064b49f08191b1ae83b5389d8ebf` — succeeded
- Archive SHA-256: `ec5d8d00855d8a322e7c3437354a905267a4f80ca5628803fc558e98f0d0621b`

### Preview version 26 — Equation 3.4.19 layout

Removed the symbolic radical repeated from 3.4.18; numerical substitution and result now appear on two aligned lines. Equation identity/number and values unchanged. Course/CNX builds and full validation passed. Visual check at 600px fits; at 390px the numerical line still uses the existing horizontal math scroller. No new PDF binary.

- Source commit: `7129224c369ef02b21b287a3e70c13ac47efdd93`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_0545ec6ce7e0819188d8d1cdedf0bd9e`
- Deployment: `appgdep_6aba087b27f481919961ee7f5b13454a` — succeeded
- Archive SHA-256: `278e7f578fcd97a01c06daa876fd71b99d7a38cdc8775c6b2ee89646ec4fc62c`

### Preview version 27 — Equation 3.4.19 unit slash spacing

Set explicit zero left/right MathML operator spacing on the three unit slashes in Eq. 3.4.19. Upright units and number-unit spaces preserved. Validated both builds and inspected 600px/390px layouts; intrinsic equation width reduced from 421 to 405px, phone math still horizontally scrollable. No new PDF binary.

- Source commit: `458e6f2efe54afd9afff12776d6d88f224de6c6b`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_b6fc4fb975ec8191ba02146e2cfe4238`
- Deployment: `appgdep_6aba09b5d5d88191940c816272db23d7` — succeeded
- Archive SHA-256: `f63455f584faf7895d50825ad0447c6610a55100420c42ac7d721c77e389455d`

### Preview version 28 — Book-wide unit-slash spacing

63 spacing-only fixes in 20 maintained modules; all 292 explicit slash operators classified. Both numbering builds validated; representative native MathML renders inspected. No new PDF binary.

- Source commit: `1fb445474e0f6f40fdb2bc27bbcdd8857ebeda2a`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_d425eedd88588191b0995ed20b06fe19`
- Deployment: `appgdep_6aba0c235b648191864782283c485cea` — succeeded
- Archive SHA-256: `d467f07862898fcddcc6676a6de89482ebdc1949b6833b2f3d2fcbe4af8752f8`

### Preview version 29 — Section 3.5 equation typography

Display punctuation and unnecessary parentheses repaired; Delta-energy spacing repaired in 3.5.2; standalone or row removed from 3.5.3. Example radicals inspected and left unchanged. Builds and validation passed.

- Source commit: `27e7d2d1f99a1f9259e86fdb21d75d6732a07637`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_5723ebb339248191aa152eb7e78320bd`
- Deployment: `appgdep_6aba0e930f7c8191893651f9d2412b37` — succeeded
- Archive SHA-256: `8058596f63628c0c76a6b74246b08602e3eebfddd2f148958b479de7b79fbc19`

### Preview version 30 — Section 3.5 display spacing

Added local margins around the unnumbered equation preceding 3.5.2 and half-em row separation in 3.5.3 (including a native-MathML CSS fallback). No global line-height or radical changes. Both builds completed; representative renders inspected.

- Source commit: `5382823e0c6b083f8a65b65c87419d7e23233e23`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_d692dda20d488191ad9c14fdf75992bd`
- Deployment: `appgdep_6aba10a5998c8191aafdc0be1163dd10` — succeeded
- Archive SHA-256: `b7e52eea71eeeb86acb777c81b9029dffe326e1608dcfcf3cc4b2f026492919c`

### Preview version 31 — Conceptual energy strategy box

Replaced six-step quantitative strategy with approved three-question “Using Energy to Understand Motion” box. Box anchor retained; no incoming references to removed child paragraphs. Both builds and full validation passed (6,915 math expressions); inspected rendered box.

- Source commit: `cf275ef083801f7ba4ae5c366d38dd886cbc1127`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_e1a1bdf7fc008191b92fb412380417da`
- Deployment: `appgdep_6aba12c7c4c08191a3c880fdad9282f0` — succeeded
- Archive SHA-256: `80bb5288da43040a751f6c91160a9ee0e1b050370452e75af01018d94e7f5ace`

### Preview version 32 — Energy box placement

Moved the unchanged conceptual energy box immediately after the path-simplification paragraph, inside the mechanical-energy subsection and before Conservation of Total Energy. Both builds and full validation passed.

- Source commit: `817f728c95420666782610a8a2ddc089f8cc7f1f`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_1b94e9d05774819189b900fe0c8b9b0d`
- Deployment: `appgdep_6aba14315300819186400b3a289effa2` — succeeded
- Archive SHA-256: `00d7b5931cd6a5d147a22e6843e10074e1c4b90fdee79beb986852a3cb4f5c66`

### Preview version 33 — Section 3.6 math displays

Repaired 15 math expressions including summary formulas. Separated k/x and m/v exponent bases, repaired split decimal and unit tokens, regularized fractions, kept introductory Hooke law inline, and split long worked-example equations into spaced rows. Preserved numerical values, prose, equation IDs and fractional powers. Both builds and full validation passed; inspected section and checked 600/390px rendering. No PDF binary rebuilt.

- Source commit: `71010d6ad7d7326c2a7210175434477fffac6154`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_1f8b1d5659b08191bc5990b016d13493`
- Deployment: `appgdep_6aba15b149288191bb7ead96510fc98e` — succeeded
- Archive SHA-256: `f43ce2f7786fa3e6f1f3568eb1abd9c80185c5283656f7b064079fdb0598faa3`

### Preview version 34 — Average-force bar

Section 3.6 unnumbered work equation: bar over F alone, app outside the accent; non-accent placement provides visible clearance in native MathML. Both builds completed and enlarged rendering inspected.

- Source commit: `9a4a08a1bb711e27ceb7b09dc3926166e23271dd`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_50eff2c8cb408191a7ff32bd66522b99`
- Deployment: `appgdep_6aba17c93b788191b8cb5d49f8581c30` — succeeded
- Archive SHA-256: `3796d2a6134de8b73a62c95feb7e739fcc9252c28ed164ba8574a13ef4a9937b`

### Preview version 35 — Watt glossary heading

Moved (W) into watt glossary term, with definition beginning SI unit of power. Both builds completed; stable IDs retained.

- Source commit: `e47c99d0ae703db77458d665c08c087b2b3fafd5`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_eee75dd9faac81919f16d6fa12f647ac`
- Deployment: `appgdep_6aba196a62408191881cca4bf49e9c73` — succeeded
- Archive SHA-256: `4ca4197e281a9c20e8e8001fe8996a4c0a57915ea9237e3da50b50e02c677fea`

### Preview version 36 — Exercise 4 figure reference

Exercise 4 now references existing Figure 3.2.1(a) via stable cross-module link. Removed duplicate unnumbered lawn-mower figure from the exercise; retained media asset and historical baseline. Both builds and full validation passed; checked generated target link.

- Source commit: `3d54ff1618cc3f4d426f687ed16053d7f1d48f01`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_12672643f34c81919a5812a80e769d1b`
- Deployment: `appgdep_6abab5813d9881919097a50d123eb58b` — succeeded
- Archive SHA-256: `23f20fa20989b7e91e51f7760023e295a7c1ce0bc12ecbcefa60096475df421a`

### Preview version 37 — Chapter 3 question additions and ordering

Published five approved MyOpenMath-guided questions and reordered all 25 questions by section topic. Included the previously held roller-coaster and book-lifting edits. New questions: 6, 7, 9, 16, 22; revised older questions: 10 and 11. Both numbering builds and full validation passed. Browser check confirmed sequential numbering and no page overflow at 390px. No PDF binary rebuilt.

- Source commit: `39f2142e43df423cd24cfa99fc3c2c611051ce91`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_b3f995d77eb0819185dca5d978c6f103`
- Deployment: `appgdep_6abab9297f748191ae06b9f7f7f0a4d6` — succeeded
- Archive SHA-256: `ec36e89df569befcddda438dce989a718c9152c2af31d7e4f3a1b56a5e0c6bcf`

### Preview version 38 — Chapter 4 organization

Collected eight glossary terms, five section summaries and 19 unchanged questions at chapter end, following CNX PDF pages 145–147. No historical placement exceptions. Preserved source IDs and links; updated PDF grouping without generating a PDF. Both builds, full validation and browser layout/link checks passed.

- Source commit: `576221b4aeb0818654a5d99b1e073f7590d28192`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_897fd7520ea88191ac871acd3adb285e`
- Deployment: `appgdep_6ababc329bd881919f9f1439d8293e51` — succeeded
- Archive SHA-256: `d3a88941a5df59a7bdcebaed323c79518e8d981397a50be9183d1e19087dc744`

### Preview version 39 — Remove optional Chapter 4 intro video

Removed unreferenced concept-trailer video from m42155; surrounding prose unchanged. Both builds and full validation passed (two remaining external-media findings).

- Source commit: `2d393d45578ce3d53758655577e0dcdbfbed2e25`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_21116741974481918a62c25693a95f76`
- Deployment: `appgdep_6abadaf6b9808191b8819e3a970895e7` — succeeded
- Archive SHA-256: `e39633f716f1d11e5a604014b2b2ce047d45dcf60cc59cfcba7f844bb9b680f5`

### Preview version 40 — Optional algebra in Section 4.5

Replaced the algebra exercise invitation with approved optional-algebra wording emphasizing interpretation of numerical collision results. Both builds and full validation passed.

- Source commit: `1ba5dafdaa70bd2504b49c3005346224d5377c3d`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_004cdbc4079081919d3175b8aefa8071`
- Deployment: `appgdep_6abadc898cb48191b497c76fa6493b31` — succeeded
- Archive SHA-256: `cc6605dddce7749c54c29b553078b225badd2cec2f4eba77109c67d74fee67a6`

### Preview version 41 — No-collision solution in Section 4.5

Applied approved hypothetical missed-collision explanation; unchanged velocities satisfy both conservation laws. Both builds and full validation passed.

- Source commit: `0a957a315f3186ce627c904e3c1e41d34b7729b4`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_a7eef802b1e481919165bc5644b622c1`
- Deployment: `appgdep_6abae89a6a3881918a9a4bdc695f39da` — succeeded
- Archive SHA-256: `6abd34ca89a13fd164ffa7324d8f0c813ff1c29bb272f89abf26a9900b909743`

### Preview version 42 — Example 4.6.2 typography

Corrected minus signs and displayed calculation values to hundredths; original problem givens retain three significant figures. Final answers unchanged. Both builds/full validation passed; equation screenshot inspected.

- Source commit: `96c37086dd6d37d73681b011a4fff38785522bd0`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_f2a8572ed25c8191b12adecb7af6d36a`
- Deployment: `appgdep_6abae99f3bcc81918be52968b1c85920` — succeeded
- Archive SHA-256: `9af9aaa4786c923886f7db3a586a3ca9639cf3e5abee4697344123405f735d5e`

### Preview version 43 — Book-wide minus typography

Audited 284 candidate MathML tokens: corrected 174 in 40 modules and eight nearby text passages; preserved 110 non-minus tokens (overbars, compounds/unit modifiers, label separators). Added style-guide convention. Both builds/full validation passed; representative negative exponent, subtraction and inline-value rendering inspected. Separate negative scientific-notation base in Chapter 13 exercise logged for review. Historical source unchanged.

- Source commit: `d330cc091737b088b0d6d7adc0ab5922082ca654`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_c72783ef92708191bb9f4dd84ad43c85`
- Deployment: `appgdep_6abaeb89b3a4819194914cb75f7aa0ee` — succeeded
- Archive SHA-256: `1114b06ab319b516b830b65b5b4509f209d441372d25c512d903efb29622b51b`

### Preview version 44 — Remove Professional Application labels

Removed all five remaining labels, in Chapter 4. Question content, IDs and numbering retained; no references to removed paragraph IDs. Both builds/full validation passed.

- Source commit: `593c85f90cc9fdcb859c7c755e2b42683716a78c`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_721a79183e08819190372ae4ce8f7d34`
- Deployment: `appgdep_6abaec8b1a408191a82b3a797ede557c` — succeeded
- Archive SHA-256: `1b3a2208fe7e5aea42d87e5e18693d728748f36b5cfb36f406af7cfe38aade69`

### Preview version 45 — Chapter 4 exercise additions and ordering

Published 23 questions, including six approved MyOpenMath-inspired additions and the garden-hose cross-reference. Included the three approved removals and reordered all questions by section/topic. Both numbering builds, full validation, link checks and narrow-screen layout checks passed. Await final maintainer review.

- Source commit: `3152078180af6cfb9f6796efe2fbdbb9910e5d4b`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_40ec5fb53f608191a931ee794d3311f9`
- Deployment: `appgdep_6abb48452f2c8191973055c0679cf8ed` — succeeded
- Archive SHA-256: `e5790082c7ca4856bd4025e3b13c7e700f845c8d3cf6174e6b9ae810c56092fb`

### Preview version 46 — Chapter 4 second review and force questions

Published all pending Chapter 4 exercise edits and three approved force/momentum questions. 24 questions reordered by topic; Exercise 1 unchanged. Full builds, validation, links and narrow-screen checks passed.

- Source commit: `170f61cb80599a09204d1f3f03a8de74f03fd92b`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_e0b6f4075a9c8191b458d1f21c5e8ceb`
- Deployment: `appgdep_6abb4d98ff0c8191be0528f03eb4d515` — succeeded
- Archive SHA-256: `8ae00cff4cf4ff83fd51da274562a6b103010f43da8981f50cbb461f6783615a`

### Preview version 47 — Chapter 5 organization

Chapter 4 marked approved. Chapter 5 now collects 33 glossary entries, eight summaries and 23 ordinary questions at chapter end. Includes maintainer-approved repair of unclassified period/frequency questions. Twelve Check Your Understanding prompts remain inline. Both builds, full validation and browser checks passed; ready for maintainer read-through.

- Source commit: `94fed760b3bc3fbca9ca2f05116d7844d038b5bb`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_7866d16de87c81918a5520038967db97`
- Deployment: `appgdep_6abb501136848191962aab72c8568ec6` — succeeded
- Archive SHA-256: `d689623345ddea766ba0aadf5a93884f481c25863f5df4b672dd6fd710295d42`

### Preview version 48 — Chapter 5 prose and equation review

Published nine approved Chapter 5 corrections: introductory dash; Eq. 5.2.2 spacing; aligned two-line Eq. 5.2.7; Eq. 5.3.4 cleanup; inline function spacing; walking example replacing breathing resonance; frequency/wavelength parentheticals; superposition paragraph; three summary bullets in Section 5.8. Both builds, full validation and browser checks passed. Equations and summary visually inspected. Exercises unchanged at 23.

- Source commit: `e5fbcf9f77de6631ed024386cc2fa9de1ce515b0`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_c94e990190a08191853e5110a8625eda`
- Deployment: `appgdep_6abb5ea644e081919a56047aa34a6900` — succeeded
- Archive SHA-256: `e79d9f5af236d3cd0339b738060ef9fa22d992f8623a399b29a639854cb5bec9`

### Preview version 49 — Hide summary equation labels

Published summary-number suppression for all 108 displayed summary equations, retaining stable IDs and internal labels. No non-summary equation numbers changed. Included Eq. 5.2.7 RHS alignment correction. Both builds/full validation and Chapter 5 browser checks passed. Content audit and pending decisions in reports/1.1/summary-equation-audit/review.md.

- Source commit: `85b7418d5f83cfd98de70279d7d75b975ff7734a`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_e04a43ad473c8191b3e4af71e990224c`
- Deployment: `appgdep_6abc3c4d9bcc81918fd520440de844ad` — succeeded
- Archive SHA-256: `e03c4ee873dc80326b9d2371801a31d23447310b71b8e96f09341b74e52d4366`


### Preview version 50 — Chapter 5 question additions

Published twenty MyOpenMath-guided additions and topic ordering of all 43 Chapter 5 questions for maintainer review. Existing 23 question texts and inline Check Your Understanding retained. Both builds/full validation and chapter browser checks passed (consecutive numbering, links, images, narrow-screen layout).

- Source commit: `e6363bd76e5f3af80236ac6358e1813efa3f8797`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_1df9dd05da788191bc7693d972598858`
- Deployment: `appgdep_6abc510cb0dc81918261f1fad1e2b52c` — succeeded
- Archive SHA-256: `371ac574a0e0c729157c0ea325502f2675e1e49c849615c0047c9626e8d6c843`


### Preview version 51 — Chapter 5 review complete

Published final approved exercise edits: swapped 10/11, new spring question in 11, figure references in 21 and 30, antinodes in 31(b). All 43 questions reviewed. Full validation and chapter browser checks passed, including Section 5.7 exercise navigation.

- Source commit: `1230616dbfab742248f131f5a01654715cd3b738`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_b6ae80936bfc81919f9f1eec07b21722`
- Deployment: `appgdep_6abc5744ae088191aeb733a8d2d590bf` — succeeded
- Archive SHA-256: `23a6a043e9137246f5381c0f5ccee460a3bf55b004141cb9f1730cb4b5e1b601`


### Preview version 52 — Chapter 6 organization

Collected Chapter 6 glossary, five summaries and 28 unchanged questions at chapter end, matching CNX PDF pages 196–200. Five inline Check Your Understanding prompts retained. Removed unreferenced optional introduction video. Both builds, full validation and browser checks passed.

- Source commit: `9f792a791dbe048243488ae8f08049c3ad226182`
- Version: `appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_60cdc3b249988191bf54f4caebc247af`
- Deployment: `appgdep_6abc58f44ba88191b99792cb5a2672a1` — succeeded
- Archive SHA-256: `8ce8c9dc3063f1baf9221914bd6fbbf117072e9d4f9d2e8b90ca23ab361bcebc`

Chapter 6 additions/review batch published as Sites version 53 (2026-09-29 local): 35 questions, all eight additions, topic ordering, prior approved exercise edits. Course/CNX builds and full validation passed (pre-existing external-media finding elsewhere); chapter browser check passed 35 consecutive questions, links, images, MathML, and 390px overflow. Four edited equation layouts rechecked at 920/798px. Non-exercise changes in this batch: Eqs. 6.4.6, 6.4.7, 6.5.23, 6.5.25. Ready for final Chapter 6 exercise review.
Source commit: 88c31d6ab2cdd4ebe4155c76681f3e6bdb86ff0b. Version: appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_41a0444086d08191be8a94b881e7b35f. Deployment: appgdep_6abca2a6d9508191859245bfb6d49208 (succeeded). Archive SHA256: e2d0fe87c9b71bd8a2ff5aa188070c932450572e0c051f01ea30dad891bf364c. Published URL: https://introduction-to-physics-1-1-preview.bkpark.chatgpt.site ; custom domain https://intro-1-1.coaphys.xyz . Workflow source push succeeded; local WSL packaging issue recovered using Git Bash packaging of the exact pushed HEAD.

Chapter 6 final review complete: Exercise 28 work/rotational-kinetic-energy addition published in Sites version 54. No further maintainer notes; chapter ready for progression to Chapter 7. Course/CNX builds and full validation passed with existing external-media finding elsewhere.
Source d7dbbe67d56d61790e2a1a2051129d000aeee467; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_d7cae24870e481918b3020a09f2a21c7; deployment appgdep_6abca79b7d1c8191b8b1abcf66ae425e succeeded. Archive SHA256 c6dc33017b91ecccd4bf06382295d642db87f34ed7dd6b09184fe6224b68780c. URL https://introduction-to-physics-1-1-preview.bkpark.chatgpt.site (custom domain intro-1-1.coaphys.xyz). Exact pushed source packaged using Git Bash after the known WSL packaging failure.

Chapter 7 organization published: Sites version 55, source b786e16db103686c5a62e86958c3cd2a751b16bb. Version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_5945650852208191975e972b139189dc; deployment appgdep_6abca9388b9c8191afbcef86df36ada8 succeeded. Archive SHA256 2aa1e07dd52ff61b09aa036c82f5f3e9c53adfd6a6fb7e3ad4c920e9e0c83a78. URL https://introduction-to-physics-1-1-preview.bkpark.chatgpt.site (intro-1-1.coaphys.xyz custom domain). Used Git Bash packaging after known WSL failure; exact pushed HEAD preserved.

Chapter 7 review/additions published as version 56: source ad68741436d1c1bdc358088c65bcf3e54d2be7b9; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_22d5af129cc88191957d77f4c72a28ad; deployment appgdep_6abcc2fc30808191839ae29270d37b1d succeeded. Archive SHA256 f4242ffad2a5976088d3b930cee1d9c3c422b76d6652a3e89d4389d3338364cb. URL https://introduction-to-physics-1-1-preview.bkpark.chatgpt.site (custom domain intro-1-1.coaphys.xyz). Known WSL packaging failure recovered using Git Bash, preserving exact pushed source. 50 chapter questions ready for final review.

Chapter 7 final review batch published as version 57: source 5de7fb29ff7a287784945450e9c77ddd86e51eaa; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_7ea11026d2948191b7f12515d96ca478; deployment appgdep_6abccde461c881918a0e4dd214d2fd72 succeeded. Archive SHA256 69d22095ed6a029313eb7d17d1baa656ee750008143d48f089b5b0898a38fb18. URL https://introduction-to-physics-1-1-preview.bkpark.chatgpt.site (custom domain intro-1-1.coaphys.xyz). Exact pushed source packaged with Git Bash after known WSL issue. 49 questions; all approved pending edits included.

Chapter 8 organization published as version 58: source cb6b1827bc5b22e00a07c36e52874c7138a8055f; version appgprj_6ab9a2afbb1c8191bf74ed20b035ce33~appgver_a39ec4f06e5081918c49720fb42b840c; deployment appgdep_6abcd1764a008191b16a22dfd7f81100 succeeded. Archive SHA256 453a2e7d0f2c80cc616a3f4827fb35ae979ad9c4cda47ec0d313af5be09d9639. URL https://introduction-to-physics-1-1-preview.bkpark.chatgpt.site (intro-1-1.coaphys.xyz). Known WSL packaging failure recovered with Git Bash at exact pushed HEAD. 105 ordinary questions, 47 glossary entries, 13 summaries; no content pruning.
