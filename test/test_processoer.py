import unittest
from processer import processer


class Processer(unittest.TestCase):

    def test_remove_url(self):
        text = [
            'https://example.com',
            'http://example.com',
            'example.com',
        ]
        for x in text:
            with self.subTest(x=x):
                self.assertEqual(processer.remove_url(x), '')

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
