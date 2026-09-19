"""Safety checks: trivial rows must not hide changed mathematical structure."""
import unittest,xml.etree.ElementTree as ET
from triage_upstream_math import signature
def sig(s):return signature(ET.fromstring(s))
class RepresentationChecks(unittest.TestCase):
    def test_redundant_rows(self):
        self.assertEqual(sig('<math><mrow><mrow><mi>x</mi></mrow><mrow/></mrow></math>'),sig('<math><mi>x</mi></math>'))
    def test_fraction_order_matters(self):
        self.assertNotEqual(sig('<mfrac><mi>x</mi><mi>y</mi></mfrac>'),sig('<mfrac><mi>y</mi><mi>x</mi></mfrac>'))
    def test_scripts_and_grouping_matter(self):
        self.assertNotEqual(sig('<msub><mi>x</mi><mn>2</mn></msub>'),sig('<msup><mi>x</mi><mn>2</mn></msup>'))
        self.assertNotEqual(sig('<msup><mrow><mi>x</mi><mo>+</mo><mi>y</mi></mrow><mn>2</mn></msup>'),sig('<mrow><mi>x</mi><mo>+</mo><msup><mi>y</mi><mn>2</mn></msup></mrow>'))
    def test_empty_script_base_is_preserved(self):
        self.assertNotEqual(sig('<msub><mrow/><mi>x</mi></msub>'),sig('<msub><mi>x</mi></msub>'))
    def test_attributes_and_text_matter(self):
        self.assertNotEqual(sig('<mi mathvariant="bold">x</mi>'),sig('<mi>x</mi>'))
        self.assertNotEqual(sig('<mtext>a b</mtext>'),sig('<mtext>ab</mtext>'))
    def test_equal_spacing_spellings(self):
        self.assertEqual(sig('<mspace width=".25em"/>'),sig('<mspace width="0.25em"/>'))
        self.assertNotEqual(sig('<mspace width=".25em"/>'),sig('<mspace width="0.5em"/>'))
if __name__=='__main__':unittest.main()
