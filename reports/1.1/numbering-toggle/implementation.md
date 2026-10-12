# Numbering selector — 2026-10-11

The complete older chapter/section map is maintained/numbering-legacy.json, verified against the outline of the locally preserved 2019 CNX 1.12 PDF (SHA-256 recorded in the map). It covers 121 numbered sections, 15 unnumbered chapter introductions, and appendices A–D; the preface stays unnumbered. All six previously checked sample labels agree.

Both modes use section-based figure, equation, example, and table counters, as requested by the maintainer. Only the prefix changes. Historical chapter introductions use chapter.0 object prefixes; collected review objects use chapter.E. Exercise numbers remain those of the reviewed current edition. This is a numbering scheme for the edited textbook, not a restoration of every historical object number.

The default is lecture-aligned. Numbering is a localStorage preference shared across tabs. Switching retains the page URL, anchors, scroll position, source content, and MathML. Navigation, headings, object labels, cross-references, summary equation aliases, titles, and search results are translated from canonical course labels. JavaScript-disabled browsers retain the complete lecture-aligned text. No service or account is required.

Implementation: prototype/numbering_toggle.py emits a label map and includes the selector on the existing pages. prototype/numbering-toggle.js updates presentation text only. The search index stays canonical and is translated before matching and rendering. Complete browser checks cover all 141 section pages and every generated object-label translation, plus same-page round trips, persistent preference, cross-tab synchronization, search, chapter review, and the no-JavaScript fallback.
