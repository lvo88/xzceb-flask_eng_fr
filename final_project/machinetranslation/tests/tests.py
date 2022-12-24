"""Import modules"""
import unittest

from translator import english_to_french, french_to_english


class test_english_to_french(unittest.TestCase):
    def test1(self):
        # Test My name is DJ
        self.assertEqual(english_to_french("I am DJ"), "Je suis DJ")
        # Test Hello
        self.assertEqual(english_to_french("Hello"), "Bonjour")


class test_french_to_english(unittest.TestCase):
    def test1(self):
        # Test Je m'appelle DJ
        self.assertEqual(french_to_english("Je m'appelle DJ"), "My name is DJ")
        # Test Bonjour
        self.assertEqual(french_to_english("Bonjour"), "Hello")


if __name__ == "__main__":
    unittest.main()
