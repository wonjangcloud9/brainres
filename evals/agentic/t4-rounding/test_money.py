import unittest
from money import round_price

class T(unittest.TestCase):
    def test_half_up(self):
        self.assertEqual(round_price(2.675), 2.68)
    def test_half_up_2(self):
        self.assertEqual(round_price(0.125), 0.13)
    def test_negative(self):
        self.assertEqual(round_price(-1.005), -1.01)
    def test_plain(self):
        self.assertEqual(round_price(3.14159), 3.14)

if __name__ == "__main__":
    unittest.main()
