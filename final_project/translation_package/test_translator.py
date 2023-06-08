import unittest
from translation_package.translator import english_to_french, french_to_english

class TranslationTests(unittest.TestCase):
    def test_english_to_french(self):
        translation = english_to_french("hello")
        self.assertEqual(translation, "bonjour")

    def test_french_to_english(self):
        translation = french_to_english("bonjour")
        self.assertEqual(translation, "hello")

if __name__ == "__main__":
    unittest.main()
