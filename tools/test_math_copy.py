"""Run with python tools/test_math_copy.py."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'prototype'))
from math_copy import copy_formats

def formats(body):
    return copy_formats('<math xmlns="http://www.w3.org/1998/Math/MathML">'+body+'</math>')

class MathCopyTests(unittest.TestCase):
    def test_fraction_groups(self):
        x=formats('<mfrac><mrow><mi>Δ</mi><mi>Q</mi></mrow><mrow><mi>Δ</mi><mi>t</mi></mrow></mfrac>')
        self.assertEqual(x['asciimath'],'(Delta Q)/(Delta t)')
        self.assertEqual(x['latex'],r'\frac{\Delta Q}{\Delta t}')
    def test_inline_division_preserves_denominator_group(self):
        x=formats('<mrow><mi>E</mi><mo>/</mo><mrow><mi>h</mi><mi>c</mi></mrow></mrow>')
        self.assertEqual(x['asciimath'],'(E)/(h c)')
    def test_unit_square(self):
        x=formats('<mtext>m</mtext><mo>/</mo><msup><mtext>s</mtext><mn>2</mn></msup>')
        self.assertEqual(x['asciimath'],'("m")/("s"^(2))')
    def test_nuclear_prescripts_and_neutron_count(self):
        x=formats('<mmultiscripts><mtext>X</mtext><mi>N</mi><none/><mprescripts/><mi>Z</mi><mi>A</mi></mmultiscripts>')
        self.assertEqual(x['asciimath'],'""_(Z)^(A) "X"_(N)')
        self.assertIn('{}_{Z}^{A}',x['latex'])
    def test_unicode_and_greek_variants(self):
        for symbol,expected in [('Δ','Delta'),('ϕ','phi'),('φ','varphi'),('ℏ','ℏ'),('ℓ','ℓ'),('Å','Å'),('Α','Α'),('ϵ','ϵ')]:
            self.assertEqual(formats('<mi>'+symbol+'</mi>')['asciimath'],expected)
    def test_excited_state_star_is_not_multiplication_dot(self):
        self.assertEqual(formats('<mo>*</mo>')['asciimath'],'**')
    def test_multiline_commas_and_fences(self):
        x=formats('<mtable><mtr><mtd><mo>(</mo><mn>20,930</mn><mo>)</mo></mtd></mtr><mtr><mtd><mn>2</mn></mtd></mtr></mtable>')
        self.assertIn('"20,930"',x['asciimath']);self.assertIn('"("',x['asciimath'])
        self.assertIn('multiline',x['notes']);self.assertIn(r'\begin{array}',x['latex'])
    def test_annotations_ignored_and_decimals_joined(self):
        x=formats('<semantics><mrow><mtext>12</mtext><mtext>.</mtext><mrow><mn>4</mn><mtext>m</mtext></mrow></mrow><annotation>WRONG</annotation></semantics>')
        self.assertEqual(x['asciimath'],'12.4 "m"');self.assertNotIn('WRONG',str(x))
    def test_cancellation_and_vector(self):
        x=formats('<menclose notation="updiagonalstrike"><mover><mi>v</mi><mo>→</mo></mover></menclose>')
        self.assertEqual(x['latex'],r'\cancel{\vec{v}}');self.assertEqual(x['asciimath'],'cancel(vec(v))')
        self.assertIn('cancel',x['notes'])
    def test_unsupported_construct_does_not_silently_drop(self):
        with self.assertRaises(ValueError):formats('<made-up><mi>x</mi></made-up>')

if __name__=='__main__':unittest.main()
