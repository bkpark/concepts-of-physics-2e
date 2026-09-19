"""Regression checks for mathematical meaning and failure visibility."""
import unittest, xml.etree.ElementTree as ET
from mathml import math_node, UnsupportedMath
class MathTests(unittest.TestCase):
    def render(self,s):return math_node(ET.fromstring(s))
    def test_vector_is_bold_like_historical_pdf(self):
        r=ET.fromstring(self.render('<ci type="vector">a</ci>'))
        self.assertEqual((r.tag,r.get('mathvariant'),r.text),('mi','bold','a'))
    def test_missing_exponent_is_never_guessed(self):
        with self.assertRaises(UnsupportedMath):self.render('<apply><power/><ci>n</ci></apply>')
    def test_scientific_notation_not_silently_flattened(self):
        with self.assertRaises(UnsupportedMath):self.render('<cn type="e-notation">1.2<sep/>3</cn>')
    def test_additive_factor_keeps_grouping(self):
        out=self.render('<apply><times/><ci>a</ci><apply><plus/><ci>b</ci><ci>c</ci></apply></apply>')
        r=ET.fromstring(out);self.assertIn('(b+c)',''.join(r.itertext()))
    def test_mixed_content_fraction_retains_subscript(self):
        out=self.render('<apply><divide/><cn>1</cn><msub><ci>n</ci><ci>f</ci></msub></apply>')
        r=ET.fromstring(out);self.assertEqual(r.tag,'mfrac');self.assertEqual(r[1].tag,'msub')
    def test_invalid_presentation_arity_is_visible(self):
        with self.assertRaises(UnsupportedMath):self.render('<msup><mi>x</mi></msup>')
    def test_unknown_operator_is_visible(self):
        with self.assertRaises(UnsupportedMath):self.render('<apply><mystery/><ci>x</ci></apply>')
    def test_input_tree_is_not_modified(self):
        r=ET.fromstring('<math><mspace width=".25 em"/><semantics><ci>x</ci><annotation>original</annotation></semantics></math>');before=ET.tostring(r);math_node(r);self.assertEqual(before,ET.tostring(r))
if __name__=='__main__':unittest.main()
