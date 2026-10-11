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
    def test_equation_style_without_block_layout(self):
        e=ET.fromstring(f'<math xmlns="{NS}"><mfrac><mi>R</mi><mn>2</mn></mfrac></math>')
        before=ET.tostring(e)
        inline=ET.fromstring(native_math(e)[0])
        display=ET.fromstring(native_math(e,equation_context=True)[0])
        self.assertIsNone(inline.get('displaystyle'))
        self.assertEqual(display.get('displaystyle'),'true')
        self.assertEqual(display.get('display'),'inline')
        self.assertEqual(ET.tostring(e),before)
    def test_explicit_compact_style_is_preserved(self):
        e=ET.fromstring(f'<math xmlns="{NS}" displaystyle="false"><mstyle displaystyle="false"><mi>x</mi></mstyle></math>')
        out=ET.fromstring(native_math(e,equation_context=True)[0])
        self.assertEqual(out.get('displaystyle'),'false')
        self.assertEqual(out[0].get('displaystyle'),'false')

if __name__=='__main__':unittest.main()
