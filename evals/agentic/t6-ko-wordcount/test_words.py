import unittest
from words import top_words

class T(unittest.TestCase):
    def test_case_and_punct(self):
        self.assertEqual(top_words("The cat. the CAT! a dog", 2), [("cat", 2), ("the", 2)])
    def test_tie_alphabetical(self):
        self.assertEqual(top_words("b a c b a c", 3), [("a", 2), ("b", 2), ("c", 2)])
    def test_korean(self):
        self.assertEqual(top_words("사과 배 사과, 배 사과", 1), [("사과", 3)])

if __name__ == "__main__":
    unittest.main()
