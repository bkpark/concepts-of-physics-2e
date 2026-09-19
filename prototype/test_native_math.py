import unittest,xml.etree.ElementTree as ET
from native_math import native_math,NS

class NativeMathTests(unittest.TestCase):
    def convert(self,body):return native_math(ET.fromstring(f'<math xmlns="{NS}">{body}</math>'))[0]
    def test_fenced_separators_and_empty_open(self):
        out=self.convert('<mfenced open="" close="}" separators=";"><mi>a</mi><mi>b</mi><mi>c</mi></mfenced>')
        r=ET.fromstring(out);self.assertEqual(''.join(r.itertext()),'a;b;c}')
        self.assertNotIn('mfenced',out)
    def test_inherited_bold_style(self):
        out=self.convert('<mstyle mathvariant="bold"><mi>v</mi></mstyle>')
        self.assertIn('font-weight:700',out);self.assertIn('mathvariant="normal"',out)
    def test_input_is_unchanged(self):
        e=ET.fromstring(f'<math xmlns="{NS}"><mfenced><mi>x</mi></mfenced></math>');before=ET.tostring(e)
        native_math(e);self.assertEqual(ET.tostring(e),before)
    def test_namespace_is_native(self):
        out=self.convert('<mi>x</mi>');self.assertTrue(out.startswith('<math '));self.assertIn(f'xmlns="{NS}"',out)

if __name__=='__main__':unittest.main()
