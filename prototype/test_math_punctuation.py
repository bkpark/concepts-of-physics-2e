import unittest
import xml.etree.ElementTree as ET
from math_punctuation import render_child


class PunctuationTests(unittest.TestCase):
    def render(self, content):
        root = ET.fromstring('<p xmlns:m="http://www.w3.org/1998/Math/MathML">'+content+'</p>')
        return render_child(root[0], lambda e: '<math>unchanged</math>')

    def test_closing_sequence_and_following_space(self):
        result = self.render('<m:math/> \n), next')
        self.assertEqual(result, '<span class="math-with-punctuation"><math>unchanged</math>),</span> next')

    def test_prose_and_opening_bracket_not_consumed(self):
        for tail in (' next', ' (next)', ' — next'):
            self.assertEqual(self.render('<m:math/>'+tail), '<math>unchanged</math>'+tail)

    def test_display_not_grouped(self):
        self.assertNotIn('math-with-punctuation', self.render('<m:math display="block"/>.'))

    def test_quotes_and_other_closing_punctuation(self):
        for punctuation in ['.', ',', ';', ':', '!', '?', '…', '”', '’', '"', "'", '].']:
            self.assertIn('math-with-punctuation', self.render('<m:math/>'+punctuation))

    def test_math_only_emphasis(self):
        self.assertIn('math-with-punctuation', self.render('<emphasis><m:math/></emphasis>.'))

    def test_long_emphasis_not_made_unbreakable(self):
        root = ET.fromstring('<p xmlns:m="http://www.w3.org/1998/Math/MathML"><emphasis>Long prose <m:math/></emphasis>.</p>')
        result = render_child(root[0], lambda e: '<em>Long prose <span data-math-key="test"><math/></span></em>')
        self.assertEqual(result, '<em>Long prose <span class="math-with-punctuation"><span data-math-key="test"><math/></span>.</span></em>')


if __name__ == '__main__':
    unittest.main()
