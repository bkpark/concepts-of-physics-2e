# Version 1.1 new-word proportions by section

Compared on October 17, 2026, after the approved electron-mass correction. Current maintained source includes pending changes after public preview 152.

## Method

- Baseline: archived cp2e-ver1.0-source.bundle, tag cp2e-ver1.0. Every compared module SHA-256 matches the published release metadata.
- Scope: all 136 numbered teaching sections; ranked by new-word percentage, rather than absolute added-word count. Appendices and chapter introductions are excluded.
- Count section body prose, subsection headings, worked examples, captions and textual table entries. Exclude chapter-end exercises, summaries, glossaries, metadata/learning objectives, media alternative text, and mathematical markup. This avoids counting relocated review material and formatting changes as new prose.
- Normalize Unicode, case and apostrophes; tokenize words and numeric text, ignoring punctuation. Compare the ordered word sequences with Python difflib.SequenceMatcher(autojunk=False). Count current words in insertion or replacement spans as new. Repeated ordinary vocabulary in a new passage counts as new wording; this is not a count of previously unused vocabulary.
- Formula: new words / current section words × 100. Unchanged matched words do not count as new; deletions do not enter the numerator. As with any text diff, the precise percentage depends on alignment and tokenization; use rounded figures in the preface.
- Script: tools/compare_release_words.py. Full results and source hashes: results.json.

## Highest proportions

| Section | Title | New words | Current words | New wording |
|---|---|---:|---:|---:|
| 13.2 | Einstein’s Postulates | 692 | 1,154 | 60.0% |
| 14.8 | Biological Effects of Ionizing Radiation | 1,377 | 3,350 | 41.1% |
| 12.5 | Uncertainty Principle | 435 | 1,355 | 32.1% |
| 8.14 | Statistical Interpretation of Entropy and the Second Law of Thermodynamics: The Underlying Explanation | 465 | 1,661 | 28.0% |
| 14.14 | GUTs: The Unification of Forces | 458 | 1,684 | 27.2% |
