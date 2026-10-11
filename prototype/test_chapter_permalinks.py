import unittest
from chapter_permalinks import preferred_url


class ChapterPermalinksTest(unittest.TestCase):
    def setUp(self):
        self.routes = {'sections/introduction-to-light': 'chapters/light/'}

    def test_section_reference_preserves_query_and_anchor(self):
        self.assertEqual(preferred_url('../introduction-to-light/index.html?q=x#figure',
                                      'sections/reflection/index.html', self.routes),
                         '../../chapters/light/?q=x#figure')

    def test_home_contents_and_search(self):
        for page, url, expected in [
            ('index.html', 'sections/introduction-to-light/index.html', 'chapters/light/'),
            ('contents/index.html', '../sections/introduction-to-light/', '../chapters/light/'),
            ('index.html', 'sections/introduction-to-light/index.html#id', 'chapters/light/#id'),
            ('sections/reflection/index.html', '/sections/introduction-to-light/', '../../chapters/light/'),
        ]:
            self.assertEqual(preferred_url(url, page, self.routes), expected)

    def test_external_nonintro_and_local_anchors_unchanged(self):
        for url in ['https://example.org/sections/introduction-to-light/',
                    '../reflection/index.html#id', '#id', '?q=light',
                    '//example.org/sections/introduction-to-light/']:
            self.assertEqual(preferred_url(url, 'sections/refraction/index.html', self.routes), url)

    def test_repeated_application_is_stable(self):
        self.assertEqual(preferred_url('../../chapters/light/#id',
                                      'sections/refraction/index.html', self.routes),
                         '../../chapters/light/#id')


if __name__ == '__main__':
    unittest.main()
