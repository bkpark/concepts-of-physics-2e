"""Render the version 1.1 publication-and-credits review page."""
from pathlib import Path
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf/v1.1-publication-and-credits.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
for name, filename in [('Serif', 'georgia.ttf'), ('SerifItalic', 'georgiai.ttf'),
                       ('Sans', 'arial.ttf'), ('SansBold', 'arialbd.ttf')]:
    pdfmetrics.registerFont(TTFont(name, 'C:/Windows/Fonts/' + filename))
pdfmetrics.registerFontFamily('Serif', normal='Serif', italic='SerifItalic', bold='Serif')
pdfmetrics.registerFontFamily('Sans', normal='Sans', bold='SansBold')
body = ParagraphStyle('body', fontName='Serif', fontSize=10, leading=14, spaceAfter=8)
heading = ParagraphStyle('heading', fontName='SansBold', fontSize=10, leading=14,
                         spaceBefore=9, spaceAfter=5)
title = ParagraphStyle('title', fontName='Serif', fontSize=23, leading=29, spaceAfter=9)
small = ParagraphStyle('small', fontName='Sans', fontSize=9, leading=12, spaceAfter=8)

def link(url, label=None):
    return f'<link href="{url}">{label or url}</link>'

story = [Paragraph('Publication and credits', title),
         Paragraph('Introduction to Physics · Version 1.1', small), Spacer(1, 9)]

sections = [
('License and reuse', [
 'Except where otherwise noted, <i>Introduction to Physics</i> is licensed under the '
 'Creative Commons Attribution 4.0 International License (CC BY 4.0).',
 link('https://creativecommons.org/licenses/by/4.0/'),
 'You may copy, share, and adapt the licensed material for any purpose, including commercial use. '
 'When sharing it, credit the creators, retain supplied copyright, license, and warranty notices '
 'and source links, link to the license, and indicate changes, including earlier adaptations. '
 'Do not imply endorsement or impose legal or technological restrictions on the licensed freedoms. '
 'This summary does not replace the license.']),
('Sources and adaptation history', [
 'This book was adapted by Andrew Park from Bobby Bailey’s <i>Concepts of Physics</i> (2015), '
 'itself adapted from OpenStax <i>College Physics</i>. Linear-momentum material also draws on '
 'James Rittenbach’s derived version of <i>Concepts of Physics</i>. The original OpenStax book’s '
 'senior contributing authors are Paul Peter Urone and Roger Hinrichs; OpenStax is an initiative '
 'of Rice University.',
 'Source-module copyright holders include Rice University and Bobby Bailey. Their individual '
 'notices and source histories are retained in the attribution records linked below. '
 'Selected updates draw on the CC BY 4.0 source snapshot of OpenStax <i>College Physics 2e</i> '
 'dated February 4, 2026. OpenStax illustrations without separate credits are attributed to '
 'Rice University, OpenStax, under CC BY 4.0.',
 'The Carnot’s principle passage also credits Samuel J. Ling, Jeff Sanny, and William Moebs, '
 'OpenStax / Rice University, <i>University Physics Volume 2</i> (2016), under CC BY 4.0; '
 'its source and modifications are identified with the passage.',
 'Adaptations include selection and reorganization for conceptual physics, revised explanations '
 'and figures, updated information, curated exercises, and new web and print layouts. '
 'The Preface describes the adaptation history and version 1.1 revisions.']),
('Individual credits and notices', [
 'Section source notes and figure captions provide additional attribution and any separate '
 'license terms. Those notices remain part of this book. Material identified as public domain '
 'or separately licensed retains that status. The CC license does not license trademarks. '
 'Source credits do not imply endorsement of this adaptation.',
 'The licensed material is provided as-is, without warranties, to the extent permitted by law. '
 'The license’s disclaimer of warranties and limitation of liability apply.']),
('Publication, sources, and citation', [
 'Maintained by Andrew Park. Website: ' + link('https://intro.coaphys.xyz/', 'intro.coaphys.xyz') + '.<br/>'
 'Source files, detailed attribution records, and revision history:<br/>'
 + link('https://github.com/bkpark/concepts-of-physics-2e', 'github.com/bkpark/concepts-of-physics-2e') + '.',
 'Suggested citation: Park, Andrew (adapter). <i>Introduction to Physics.</i> Version 1.1. '
 'intro.coaphys.xyz. CC BY 4.0.'])]

for name, paragraphs in sections:
    story.append(Paragraph(name, heading))
    story.extend(Paragraph(p, body) for p in paragraphs)

doc = SimpleDocTemplate(str(OUT), pagesize=(612,792), leftMargin=62, rightMargin=62,
                        topMargin=47, bottomMargin=44,
                        title='Introduction to Physics - Publication and credits', author='Andrew Park')
doc.build(story)
print(OUT)
