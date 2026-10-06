"""Check exponent scope, isotope attachment, and preservation of approved edits."""
import copy,json,re,unittest
import xml.etree.ElementTree as E
from normalize_math_copy_sources import normalize, ROOT, M, tag, text

def parse(s):return E.fromstring('<math xmlns="'+M[1:-1]+'">'+s+'</math>')

class NormalizationTests(unittest.TestCase):
    def test_unit_power_does_not_square_numerator(self):
        root=parse('<msup><mtext>20 m/s</mtext><mn>2</mn></msup>')
        normalize(root,'test',0)
        power=next(root.iter(M+'msup'))
        self.assertEqual(text(power[0]),'s')
        self.assertEqual(text(power[1]),'2')
        self.assertEqual([text(x) for x in root.iter(M+'mn')],['20','2'])

    def test_explicit_parentheses_keep_whole_quantity_squared(self):
        root=parse('<msup><mfenced><mtext>20 m/s</mtext></mfenced><mn>2</mn></msup>')
        normalize(root,'test',0)
        self.assertEqual(tag(root[0]),'msup')
        self.assertEqual(tag(root[0][0]),'mfenced')

    def test_nuclear_left_and_right_scripts(self):
        root=parse('<mrow><msubsup><mrow/><mn>6</mn><mn>14</mn></msubsup><msub><mtext>C</mtext><mn>8</mn></msub></mrow>')
        normalize(root,'test',0)
        n=next(root.iter(M+'mmultiscripts'))
        self.assertEqual([tag(x) for x in n],['mtext','mn','none','mprescripts','mn','mn'])
        self.assertEqual([text(n[i]) for i in [0,1,4,5]],['C','8','6','14'])

    def test_unknown_quantity_and_separate_integers_untouched(self):
        root=parse('<mrow><mn>1</mn><mn>2</mn><msup><mtext>x/y</mtext><mn>2</mn></msup></mrow>')
        before=E.tostring(root)
        self.assertFalse(normalize(root,'test',0))
        self.assertEqual(E.tostring(root),before)

    def test_all_applied_expressions_idempotent(self):
        report=json.loads((ROOT/'reports/1.1/math-source-normalization/changes.json').read_text(encoding='utf-8'))
        for item in report['items']:
            root=E.fromstring(item['after'])
            self.assertFalse(normalize(root,item['module'],int(item['key'].rsplit('-',1)[1])),item['key'])

    def test_nonmath_source_and_annotations_unchanged(self):
        for path in (ROOT/'proposals/author-corrections').glob('MATH-COPY-NORMALIZE-*.json'):
            p=json.loads(path.read_text(encoding='utf-8'))
            strip=lambda s:re.sub(r'<m:math\b.*?</m:math>','MATH',s,flags=re.S)
            self.assertEqual(strip(p['before']),strip(p['after']),path.name)
            for old,new in zip(E.fromstring(p['before']).iter(M+'math'),E.fromstring(p['after']).iter(M+'math')):
                self.assertEqual([x.text for x in old.iter(M+'annotation')],[x.text for x in new.iter(M+'annotation')])

if __name__=='__main__':unittest.main()
