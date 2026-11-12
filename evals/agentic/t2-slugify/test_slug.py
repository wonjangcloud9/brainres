import unittest
from slug import slugify

class T(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello World"), "hello-world")
    def test_punctuation(self):
        self.assertEqual(slugify("  What's new, in 2026?! "), "whats-new-in-2026")
    def test_collapse(self):
        self.assertEqual(slugify("a  --  b"), "a-b")
    def test_empty(self):
        self.assertEqual(slugify("!!!"), "")

if __name__ == "__main__":
    unittest.main()
