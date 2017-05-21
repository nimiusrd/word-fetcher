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
