import unittest
from lru import LRUCache

class T(unittest.TestCase):
    def test_evicts_least_recent(self):
        c = LRUCache(2); c.put("a", 1); c.put("b", 2); c.get("a"); c.put("c", 3)
        self.assertIsNone(c.get("b")); self.assertEqual(c.get("a"), 1); self.assertEqual(c.get("c"), 3)
    def test_update_moves_to_front(self):
        c = LRUCache(2); c.put("a", 1); c.put("b", 2); c.put("a", 10); c.put("c", 3)
        self.assertEqual(c.get("a"), 10); self.assertIsNone(c.get("b"))
    def test_missing(self):
        self.assertIsNone(LRUCache(1).get("x"))

if __name__ == "__main__":
    unittest.main()
