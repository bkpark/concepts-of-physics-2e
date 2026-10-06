"""Structural copy-format audit; does not claim round-trip conversion validation."""
from pathlib import Path
import collections
import html
import hashlib
import json
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'prototype'))
from native_math import native_math

BUILD = ROOT/'prototype/dist/course-full'
OUT = ROOT/'reports/1.1/math-copy-inventory'
OUT.mkdir(parents=True, exist_ok=True)
sources = json.loads((BUILD/'math-source.json').read_text(encoding='utf-8'))
registry = json.loads((BUILD/'identity-registry.json').read_text(encoding='utf-8'))
labels = json.loads((BUILD/'object-labels.json').read_text(encoding='utf-8'))
sections = json.loads((BUILD/'build-manifest.json').read_text(encoding='utf-8'))['section_labels']
tag = lambda e: e.tag.rsplit('}', 1)[-1]
txt = lambda e: ''.join(e.itertext()).strip()
categories = {
 'hbar-portability': ('ASCIIMath renderer compatibility', "The standalone ASCIIMathML.js source defines hbar, but the author verified that asciimath.org's MathJax 4 demo does not render it correctly. Do not enable hbar export on source-table evidence alone. LaTeX uses \\hbar; retain a compatibility flag until the target renderer is tested. An explicit h/(2 pi) substitution is possible only with author approval."),
 'detached-nonnuclear-subscript': ('Repair source before conversion', 'An empty-base prescript is visually attached to a neighboring symbol. Normalize to v_0, y_1, or W_net; do not export an unrelated empty-base subscript.'),
 'script-over-slash-token': ('Normalize unit powers', 'A script is attached to text containing a slash. Preserve the displayed meaning: m/s^2, not (m/s)^2. Inspect the full base before applying a generic braced conversion.'),
 'script-over-quantity-text': ('Normalize quantity tokens', 'The scripted base includes a number and unit text. Tokenize the quantity so the exponent remains on the intended final unit, unless explicit parentheses square the entire quantity.'),
 'multiline-layout': ('Conversion handling: multiline layout', 'LaTeX aligned/array can preserve the layout. ASCIIMath supports invisible-delimiter matrix layouts, but column alignment is less portable. Prefer whole-expression LaTeX plus an explicitly chosen ASCIIMath row layout or line-by-line copy.'),
 'empty-script-base': ('Handle nuclear and detached scripts', 'Most are nuclear mass/atomic numbers placed on an empty base before the element. LaTeX {}^{A}_{Z}X_{N} is straightforward; ASCIIMath needs an invisible empty group before X. Do not mistake these for missing data. A few are detached primes or degree signs.'),
 'nuclear-prescripts': ('Normalize nuclear scripts', 'Combine adjacent empty-base left scripts and the element into a nuclear-notation unit before exporting. Preserve the right neutron-count subscript and any excited-state superscript.'),
 'script-ell': ('ASCIIMath symbol choice', 'LaTeX has \\ell. Standard ASCIIMath has no documented ell token. Options: ordinary l (explicit stylistic substitution), quoted "ell" (changes appearance), or omit ASCIIMath for this expression. Do not silently flatten the symbol.'),
 'greek-alphabet-display': ('Alphabet-table fidelity', 'Greek letters visually identical to Latin letters, and omicron, have no distinct standard token in some ASCII/TeX vocabularies. In an alphabet reference table, replacing them with Latin letters loses character identity; keep these cells out of strict ASCII-only copying or approve explicit transliterations.'),
 'angstrom-name': ('ASCII-only unit spelling', 'LaTeX can use \\text{\\AA}. For ASCIIMath, quoted "angstrom" is a readable unit-name substitution but is not an exact copy of the symbol.'),
 'cancellation': ('Supported with package caveat', 'ASCIIMath cancel(...) is supported. LaTeX \\cancel{...} usually needs the cancel package; advertise that requirement instead of dropping cancellation marks.'),
 'padding': ('Cosmetic spacing', 'Convert positive padding to ordinary math spacing; do not carry browser-specific box widths into the copied expression.'),
}
categories['hbar-portability'] = ('ASCIIMath renderer compatibility', 'Approved conversion handling: retain Unicode ℏ for ASCIIMath and use \\hbar in LaTeX. The author verified that the MathJax 4 demo does not handle the ASCII hbar token correctly. No further author decision is needed.')
categories['script-ell'] = ('Conversion handling: Unicode fallback approved', 'Use Unicode ℓ in ASCIIMath when no clear supported named equivalent exists; preserve the source symbol. LaTeX uses \\ell. No author decision remains.')
categories['greek-alphabet-display'] = ('Conversion handling: Greek symbol names and fallback', 'Use the supported ASCIIMath spelling where it preserves the actual Greek letter or variant. Otherwise retain the Unicode character; do not substitute a visually similar Latin letter. This fallback policy is author-approved.')
categories['angstrom-name'] = ('Conversion handling: Unicode fallback approved', 'Preserve Å in ASCIIMath if no clear supported named equivalent exists. Do not substitute the word angstrom for the symbol. LaTeX can use \\text{\\AA}. No author decision remains.')
categories['empty-script-base'] = ('Source review: unattached scripts', 'The intended attachment is not established. Inspect the surrounding prose before changing or converting this expression. Reviewed nuclear prescripts are listed separately as conversion handling.')
categories['nuclear-notation-compatibility'] = ('Conversion handling: valid nuclear notation', 'No source correction is required for the empty-base nuclear scripts. Preserve the mass/atomic numbers as left scripts on the following element. LaTeX supports an empty base, for example {}^{258}\\mathrm{Ha}; ASCIIMath can use an empty group for prescripts. Test the target renderer when implementing copying. Other independent flags, if any, remain applicable.')
reviewed_nuclear = json.loads((ROOT/'tools/math_copy_reviewed_nuclear_notation.json').read_text(encoding='utf-8'))
nuclear_hashes = {r['source_xml_sha256'] for r in reviewed_nuclear['expressions']}
reviewed_expressions = json.loads((ROOT/'tools/math_copy_reviewed_expressions.json').read_text(encoding='utf-8'))
resolved_flags = {r['source_xml_sha256']: set(r['resolved_flags']) for r in reviewed_expressions['expressions']}
counts = collections.Counter()
tokens = collections.Counter()
records = []
for source in sources:
    rendered, adaptations = native_math(ET.fromstring(source['xml']))
    tree = ET.fromstring(rendered)
    flags = set()
    for node in tree.iter():
        t = tag(node)
        tokens[t] += 1
        if t == 'mtable': flags.add('multiline-layout')
        if t == 'menclose': flags.add('cancellation')
        if t == 'mpadded': flags.add('padding')
        if t == 'mmultiscripts' and not txt(node[0]): flags.add('nuclear-prescripts' if source['module']=='m76603' else 'detached-nonnuclear-subscript')
        if t in ('msup','msub','msubsup'):
            base = txt(node[0])
            if not base: flags.add('empty-script-base')
            if '/' in base: flags.add('script-over-slash-token')
            if len(base.split()) > 1 and any(c.isdigit() for c in base): flags.add('script-over-quantity-text')
        if t in ('mi','mn','mo','mtext'):
            value = node.text or ''
            if 'ℓ' in value: flags.add('script-ell')
            if '\u210f' in value: flags.add('hbar-portability')
            if 'Å' in value: flags.add('angstrom-name')
            if any(c in value for c in 'ΑΒΕΖΗΙΚΜΝΟΡΤΧΥο'): flags.add('greek-alphabet-display')
    if 'empty-script-base' in flags and hashlib.sha256(source['xml'].encode()).hexdigest() in nuclear_hashes:
        flags.remove('empty-script-base')
        flags.add('nuclear-notation-compatibility')
    flags.difference_update(resolved_flags.get(hashlib.sha256(source['xml'].encode()).hexdigest(), set()))
    counts.update(flags)
    mid, ident = source['module'], source['source_object']
    obj = labels.get(mid+'#'+ident, {})
    anchor = mid+'--'+ident.encode().hex()
    location = (obj.get('kind','object')+' '+str(obj['label'])) if obj.get('label') else ('Section '+str(sections.get(mid,''))+' · '+ident)
    records.append(dict(key=source['key'], module=mid, source_object=ident, location=location,
                        url='https://introduction-to-physics-1-1-preview.bkpark.chatgpt.site/sections/'+registry[mid]['slug']+'/#'+anchor,
                        flags=sorted(flags), mathml=rendered, source_xml=source['xml']))

summary = {'expressions':len(records), 'flagged_expressions':sum(bool(r['flags']) for r in records),
           'category_counts':dict(counts), 'element_counts':dict(tokens),
           'scope':'Structural audit of all source-sidecar expressions through the current native-MathML renderer; repeated appearances count separately. Categories overlap. Not a tested converter or proof that unflagged expressions round-trip.',
           'references':['https://asciimath.org/','https://github.com/asciimath/asciimathml/blob/master/ASCIIMathML.js']}
(OUT/'inventory.json').write_text(json.dumps({'summary':summary,'categories':categories,'expressions':records},ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
esc = html.escape
body = '<h1>Math copying: conversion inventory</h1><p>'+esc(summary['scope'])+'</p>'
body += '<p><strong>'+str(len(records))+' expressions examined; '+str(summary['flagged_expressions'])+' have at least one special-handling flag.</strong> These are not all errors or unconvertible expressions.</p>'
body += '<p>No textbook source, copy controls, or preview deployment changed. This report identifies implementation rules and a short author-review queue.</p>'
body += '<h2>Priority review</h2><p>The verified detached subscripts and common unit/nuclear structures have been normalized; see the math-source-normalization report for changes. Remaining structural flags are conservative review candidates, not confirmed errors. Unit powers need converter normalization, not mathematical changes. Reviewed nuclear prescripts need conversion handling, not source correction or an author decision. Multiline layout is converter implementation work. Symbol copying follows the approved rule: supported ASCIIMath names first, Unicode fallback when a clear supported equivalent is absent; preserve Greek variants and character identity.</p>'
body += '<p>LaTeX: no mathematical construct in this structural inventory appears inherently unrepresentable, with amsmath and cancel where needed. This is not yet a verified conversion guarantee. ASCIIMath: multiline layouts, bars, vector arrows, cancellation and minus-or-plus exist in the reference implementation. The standalone source also defines hbar, but the author demonstrated that the MathJax 4 demo does not render it correctly; treat it as renderer-dependent. Preserve upright unit names and distinguish variables from reserved words.</p>'
body += '<label>Filter examples <input id="filter" type="search" placeholder="e.g., 1.6.40 or nuclear"></label>'
for category,(heading,note) in categories.items():
    subset=[r for r in records if category in r['flags']]
    body += '<section><h2>'+esc(heading)+' ('+str(len(subset))+')</h2><p>'+esc(note)+'</p>'
    for r in subset:
        body += '<details data-search="'+esc(category+' '+r['location']+' '+r['key'],quote=True)+'"><summary>'+esc(r['location']+' · '+r['key'])+'</summary><p><a href="'+esc(r['url'],quote=True)+'">Open textbook passage</a></p><div class="math">'+r['mathml']+'</div><pre>'+esc(r['source_xml'])+'</pre></details>'
    body += '</section>'
body += '<script>document.querySelector("#filter").addEventListener("input",e=>{const q=e.target.value.toLowerCase();document.querySelectorAll("details").forEach(d=>d.hidden=!d.dataset.search.toLowerCase().includes(q));});</script>'
page='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Math copy inventory</title><style>body{max-width:1100px;margin:2rem auto;padding:0 1rem;font:17px/1.55 system-ui;color:#172b35}h1,h2{color:#176b80}details{border-top:1px solid #ccd;padding:.5rem}summary{cursor:pointer}pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:12px}.math{overflow:auto;margin:1rem 0;font-size:22px}input{font:inherit;padding:.4rem}a{color:#176b80}section{margin:2rem 0}</style>'+body+'</html>'
(OUT/'index.html').write_text(page,encoding='utf-8',newline='\n')
print(json.dumps(summary,ensure_ascii=False,indent=2))

# Keep the concise review report synchronized with the inventory on every run.
flagged = [r for r in records if r['flags']]
(OUT/'flagged-only.json').write_text(json.dumps(flagged, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='\n')
order = ['empty-script-base', 'detached-nonnuclear-subscript', 'script-over-slash-token', 'script-over-quantity-text', 'multiline-layout', 'script-ell', 'greek-alphabet-display', 'angstrom-name', 'hbar-portability', 'cancellation', 'padding', 'nuclear-prescripts', 'nuclear-notation-compatibility']
groups = {c: [] for c in order}
for r in flagged:
    groups[next(c for c in order if c in r['flags'])].append(r)
body = '<h1>Remaining math-copy flags</h1><p><strong>'+str(len(flagged))+' expressions; each appears once.</strong> Source-review candidates and conversion handling are distinguished below. Flags are not necessarily textbook errors.</p>'
body += '<p>'+str(counts['nuclear-notation-compatibility'])+' reviewed nuclear-notation expressions need converter support, not correction of their empty-base scripts. Any other flags on these expressions remain listed. Textbook links open the published preview; expressions below use current local source.</p>'
body += '<label>Filter by section, equation, or issue <input id="q" type="search"></label><p id="count" role="status"></p><nav>'
for c, rows in groups.items():
    if rows: body += '<a href="#'+c+'">'+esc(categories[c][0])+' ('+str(len(rows))+')</a> · '
body += '</nav>'
for c, rows in groups.items():
    if not rows: continue
    heading, note = categories[c]
    body += '<section class="group" id="'+c+'"><h2>'+esc(heading)+'</h2><p>'+esc(note)+'</p>'
    for r in rows:
        title = r['location']+' · '+r['key']
        reasons = '; '.join(categories[f][0] for f in r['flags'])
        body += '<article data-search="'+esc(title+' '+reasons,quote=True)+'"><h3>'+esc(title)+'</h3><p class="reason">'+esc(reasons)+'</p>'
        if 'nuclear-notation-compatibility' in r['flags']:
            body += '<p><strong>Nuclear scripts: conversion handling only; no source correction required.</strong></p>'
        body += '<p><a href="'+esc(r['url'],quote=True)+'">Open textbook passage</a></p><div class="math">'+r['mathml']+'</div><details><summary>Source MathML</summary><pre>'+esc(r['source_xml'])+'</pre></details></article>'
    body += '</section>'
body += '<script>document.querySelector("#q").addEventListener("input",e=>{const q=e.target.value.toLowerCase();let n=0;document.querySelectorAll("article").forEach(a=>{a.hidden=!a.dataset.search.toLowerCase().includes(q);if(!a.hidden)n++;});document.querySelector("#count").textContent=n+" expressions shown";});</script>'
head = page.split('<h1>',1)[0]
(OUT/'flagged-only.html').write_text(head+body+'</html>',encoding='utf-8',newline='\n')
