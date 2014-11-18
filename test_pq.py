import pq
import unittest

class TestPQ(unittest.TestCase):
    
    def setUp(self):
        self.mpq = pq.MaxPQ()
    def tearDown(self):
        self.mpq = None

    def test_pq_function(self):
        self.assertTrue(self.mpq.isEmpty())
        self.assertEqual(self.mpq.size(), 0)
        self.mpq.insert(3)
        self.assertFalse(self.mpq.isEmpty())
        self.assertEqual(self.mpq.size(), 1)
        self.mpq.insert(5)
        self.mpq.insert(2)
        self.mpq.insert(6)
        self.mpq.insert(1)
        self.assertEqual(self.mpq.size(), 5)
        self.assertEqual(self.mpq.delMax(), 6)
        self.assertEqual(self.mpq.size(), 4)

if __name__ == '__main__':
    unittest.main()
        

