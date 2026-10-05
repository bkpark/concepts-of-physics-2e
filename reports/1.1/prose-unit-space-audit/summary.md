# Prose number–unit spacing correction

Applied 1,346 nonbreaking-space replacements in 1,338 number–unit occurrences across 113 maintained modules. The extra eight gaps are inside multiword units, such as light years and metric tons. Includes prose, captions, tables, summaries, glossary text, and exercises; includes numerical and common spelled-out quantities. Twenty-four corrected occurrences straddle prose/MathML boundaries. All MathML is byte-for-byte unchanged.

Expanded the initial dictionary using a supplemental inventory of words following numbers. Included spelled-out units, atomic mass units, customary units, time intervals, nuclear yield units, and percentages. Excluded six ordinary-word “as” matches and two A.M. clock-time matches. Reviewed day/year abbreviations in context and applied them as clear unit cases.

Three occurrences remain for author review, grouped into two decisions in review.md. The post-change scan reports zero remaining automatic-fix candidates. Full original and updated source snapshots are recorded in per-module STYLE-PROSE-NUMBER-UNIT-NBSP patches and the editorial ledger.

Validation: course and CNX builds passed; full validation checked 156 browser pages, 10,642 prose fragments and 6,821 math expressions. The previously known external-media issue remains. Whitespace-normalized source equality was checked for each changed module; all MathML strings are identical. Browser checks on three representative pages at 390, 712 and 1,100 px verified 51 prose gaps without a number/unit line split.

Scope limits: editable XML text, including inline markup and recognized numeric MathML boundaries. Does not change image lettering, alternative-text attributes, metadata, missing-space typos, or unfamiliar quantity notation not recognized by the scanner. Re-run tools/prose_unit_spaces.py to audit future changes; ambiguous cases remain review-only.

Changes are saved locally for the next preview refresh.

Author follow-up: all three previously flagged occurrences are now resolved. 1 TeV has the corrected capitalization and NBSP; both 45g references are single math expressions. Seven forced-italic attributes in Section 2.4 were also removed in separate follow-up patches.
