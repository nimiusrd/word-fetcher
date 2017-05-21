import unittest
from processer import processer


class Processer(unittest.TestCase):

    def test_remove_url(self):
        text = [
            'https://example.com',
            'http://example.com',
        ]
        unremoved_text = [
            'example.com'
        ]
        for x in text:
            with self.subTest(x=x):
                self.assertEqual(processer.remove_url(x), '')

        for x in unremoved_text:
            with self.subTest(x=x):
                self.assertEqual(processer.remove_url(x), x)

    def test_extract_word(self):
        case = [
            {
                'text': 'これでSafari, Chrome  FirefoxでESMが使えるようになったのか',
                'words': ['Safari', 'Chrome', 'Firefox', 'ESM']
            },
            {
                'text': 'flake8, autoflake, autopepで運用しようか',
                'words': ['flake8', 'autoflake', 'autopep']
            },
        ]
        for x in case:
            with self.subTest(x=x):
                self.assertEqual(processer.extract_word(x['text']), x['words'])

    @unittest.skip("TODO")
    def test_is_stopwords(self):
        pass

    def test_is_twitter_username(self):
        expectTrue = [
            '@username',
            '@000',
            '@0o0'
        ]
        expectFalse = [
            'm@aster',
            '@',
            '',
            'hoge@'
        ]
        for x in expectTrue:
            with self.subTest(x=x):
                self.assertTrue(processer.is_twitter_username(x))

        for x in expectFalse:
            with self.subTest(x=x):
                self.assertFalse(processer.is_twitter_username(x))

    def test_is_number(self):
        expectTrue = [
            '42'
            '2.1'
        ]
        expectFalse = [
            '@a11y',
            '1a1'
            ''
        ]
        for x in expectTrue:
            with self.subTest(x=x):
                self.assertTrue(processer.is_number(x))

        for x in expectFalse:
            with self.subTest(x=x):
                self.assertFalse(processer.is_number(x))
