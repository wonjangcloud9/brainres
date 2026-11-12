import unittest
from age import parse_age

class T(unittest.TestCase):
    def test_ok(self):
        self.assertEqual(parse_age(" 42 "), 42)
    def test_negative(self):
        with self.assertRaises(ValueError):
            parse_age("-1")
    def test_too_old(self):
        with self.assertRaises(ValueError):
            parse_age("151")
    def test_not_number(self):
        with self.assertRaises(ValueError):
            parse_age("forty")
    def test_float_string(self):
        with self.assertRaises(ValueError):
            parse_age("4.5")

if __name__ == "__main__":
    unittest.main()
