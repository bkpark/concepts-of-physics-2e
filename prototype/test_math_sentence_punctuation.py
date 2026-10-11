import unittest
import xml.etree.ElementTree as ET
from math_sentence_punctuation import separate, M
from math_copy import copy_formats


class SentencePunctuationTests(unittest.TestCase):
    def split(self, body):
        return separate('<math xmlns="'+M[1:-1]+'">'+body+'</math>')

    def test_terminal_punctuation_and_copy(self):
        xml, p, _ = self.split('<mrow><mi>L</mi><mo>=</mo><mi>n</mi><mi>ℏ</mi><mo>,</mo><mrow/></mrow>')
        self.assertEqual(p, ',')
        self.assertNotIn(',', copy_formats(xml)['latex'])
        self.assertEqual(''.join(ET.fromstring(xml).itertext()), 'L=nℏ')

    def test_units_and_decimal_not_truncated(self):
        xml, p, _ = self.split('<mrow><mi>x</mi><mo>=</mo><mn>3.20</mn><mtext> cm.</mtext></mrow>')
        self.assertEqual(p, '.')
        self.assertIn('3.20', xml)
        self.assertIn(' cm</', xml)

    def test_mathematical_punctuation_unchanged(self):
        for body in ['<mn>3.20</mn>', '<mrow><mn>1</mn><mo>,</mo><mn>2</mn><mo>,</mo><mo>…</mo></mrow>',
                     '<mrow><mi>n</mi><mo>=</mo><mtext>1, 2, 3, ...</mtext></mrow>',
                     '<mrow><mi>x</mi><mo>=</mo><mo>?</mo></mrow>',
                     '<mrow><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>)</mo></mrow>',
                     '<mfrac><mi>x</mi><mrow><mi>y</mi><mo>,</mo></mrow></mfrac>',
                     '<msup><mi>x</mi><mrow><mi>n</mi><mo>.</mo></mrow></msup>']:
            with self.subTest(body=body):
                xml='<math xmlns="'+M[1:-1]+'">'+body+'</math>'
                self.assertEqual(separate(xml)[:2], (xml, ''))

    def test_final_table_cell_only_and_baseline(self):
        for columns in (1, 2, 3):
            prefix='<mtd/>'*(columns-1)
            body='<mtable><mtr>'+prefix+'<mtd><mi>a</mi><mo>,</mo></mtd></mtr><mtr>'+prefix+'<mtd><mi>b</mi><mo>.</mo></mtd></mtr></mtable>'
            xml,p,_=self.split(body)
            self.assertEqual(p,'.')
            root=ET.fromstring(xml)
            self.assertEqual(root.find(M+'mtable').get('align'),'baseline -1')
            self.assertEqual(''.join(root.itertext()),'a,b')

    def test_ellipsis_followed_by_sentence_period(self):
        xml,p,_=self.split('<mrow><mi>r</mi><mo>=</mo><mtext>0.123....</mtext></mrow>')
        self.assertEqual(p,'.')
        self.assertTrue(''.join(ET.fromstring(xml).itertext()).endswith('...'))

    def test_idempotent(self):
        xml,p,_=self.split('<mrow><mi>a</mi><mo>,</mo></mrow>')
        self.assertEqual(separate(xml)[:2], (xml,''))

    def test_block_keeps_display_style_without_forcing_punctuation_newline(self):
        xml,p,_=separate('<math xmlns="'+M[1:-1]+'" display="block"><mi>x</mi><mo>.</mo></math>')
        root=ET.fromstring(xml)
        self.assertEqual(p,'.')
        self.assertEqual(root.get('display'),'inline')
        self.assertEqual(root.get('displaystyle'),'true')

    def test_question_mark_in_prose(self):
        xml,p,_=self.split('<mrow><mi>B</mi><mo>?</mo></mrow>')
        self.assertEqual(p,'?')
        self.assertEqual(''.join(ET.fromstring(xml).itertext()),'B')


if __name__ == '__main__':
    unittest.main()
