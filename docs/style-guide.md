# Introduction to Physics — style guide

Maintained by Andrew Park. This is a living record of agreed editorial conventions, not a mandate to rewrite existing prose. Add decisions as they are made. Preserve the immutable CNX baseline; apply edits to the maintained source with reversible editorial records.

## Quotation marks and apostrophes

Use typographic double quotation marks (“…”) for ordinary quotations and quoted terms. Use single quotation marks (‘…’) for a quotation within a quotation. Retain an established nickname convention in attribution credits. Use the right single quotation mark (’) for apostrophes in contractions and possessives. Straight keyboard input is acceptable in drafts; normalize it for publication.

Use **logical punctuation**: punctuation belongs inside quotation marks only when it belongs to the quoted material. Otherwise it belongs to the surrounding sentence and goes outside.

- Terms in a list: The terms “action”, “reaction”, and “force” have specific meanings.
- A quoted term at sentence end: The force is called “normal force”.
- A complete quoted question: She asks, “Is the acceleration zero?”
- A question about a term: What does “weightlessness” mean?
- A complete quoted sentence: The student writes, “The acceleration is zero.”

Commas separating the surrounding sentence's clauses or list items normally go outside. A comma internal to a quotation remains inside. Apply the same ownership rule to periods, question marks, exclamation marks, colons and semicolons. Preserve substantive direct quotations; typography normalization is not authorization to change their wording or authenticate their attribution. Check context rather than mechanically moving every punctuation mark next to a closing quote.

Distinguish apostrophes from mathematical prime symbols (′, ″) and angle/length notation. Never apply blanket smart-quote replacements to MathML, StarMath annotations, code, XML attributes, URLs, or historical source. Text drawn into artwork needs separate review.

## Scope and maintenance

The textbook title remains **Introduction to Physics**; the project role is **Maintainer**. Repository/release identifiers are not alternate book titles. Keep content corrections minimal unless a substantive revision has been agreed. Stable source IDs and public URLs are independent of displayed numbering. Other recorded project decisions remain in the release work log and architecture documents; this guide will grow as further house-style choices are agreed.

## Slashes in units

Use compact solidus notation in units, such as m/s and kg/m³. When the solidus is a MathML `mo` operator, give it `lspace="0em" rspace="0em"`. Preserve the space between a number and its unit. Apply this only to identified unit expressions (including conventional MeV/c² mass units), not algebraic ratios or division of measured quantities. Slashes already inside a text token need no operator-spacing attributes.

## Minus signs

Use the mathematical minus sign (−, U+2212) for subtraction, negative values and exponents, and negative-charge superscripts. Do not substitute a hyphen or en dash. Preserve hyphens in compounds and value-unit modifiers, en dashes in ranges, and existing overbars for averages or antiparticles. Check the mathematical context; a dash-shaped mark is not necessarily a minus. Preserve legacy equation annotations unless separately revising their representation.


## Equations in summaries

Section and chapter summaries repeat relationships introduced in the instructional text. Do not display equation numbers in summaries. Preserve stable equation IDs, links and internal numbering assignments so this presentation choice does not renumber other equations. Check summary-only formulas against the body; introduce needed formulas in the instructional text or revise the summary, rather than teaching new material there.

## Descriptive subscripts

Use upright (roman), normal-weight type for subscripts abbreviated from descriptive names, including single letters: i for initial or image, f for final or fusion, and o for object. The base quantity retains its appropriate mathematical styling; for example, d is italic in image distance, but its subscript i is upright. In MathML, use `mi mathvariant="normal"` or upright `mtext` for these labels. A subscript that represents a variable, quantity, or running index remains italic. Classify by meaning, not by the letter alone; do not globally de-italicize every subscript.

## Van de Graaff

Use “Van de Graaff” consistently for the name, generator, and accelerator, including captions, headings, glossary entries, and alternative text. Capitalize Van and Graaff; keep de lowercase.

## IR drop

Write the phrase IR drop (and plural IR drops) as ordinary upright prose, not as a math expression. Quote its first introduction as “IR drop”. Later uses normally need neither italics nor quotation marks; use quotation marks again only when a distant reintroduction warrants reminding readers of the term. Mathematical products such as V = IR retain normal mathematical styling.

## Number–unit spaces in prose

Outside mathematical expressions, use a nonbreaking space (U+00A0) between a numerical value and its unit symbol or spelled-out unit name so they stay together across line breaks. This applies to prose, captions, tables, and exercises. Preserve existing MathML spacing; inspect ambiguous letters and markup boundaries in automated audits rather than treating every letter following a number as a unit.

## Punctuation following inline math

The web renderer keeps trailing prose punctuation with its inline equation in one nonbreaking group. This covers periods, commas, colons, semicolons, question/exclamation marks, ellipses, closing brackets, and closing quotes, including sequences such as `).`. Source whitespace before closing punctuation is suppressed in the rendered output. Punctuation remains outside MathML, preserving structured equation copying. Oversized groups scroll horizontally. Do not manually move prose punctuation into MathML merely to prevent a line break.
