import pq
import unittest

class TestMaxPQ(unittest.TestCase):
    
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
        self.assertEqual(self.mpq.delMax(), 5)
        self.assertEqual(self.mpq.size(), 3)
    def test_pq_with_initializer(self):
        self.mpq = pq.MaxPQ([3,4,5,6,7,2,3,1])
        self.assertEqual(self.mpq.delMax(), 7)
        self.assertEqual(self.mpq.delMax(), 6)
        self.assertEqual(self.mpq.size(), 6)

class TestMinPQ(unittest.TestCase):
    def setUp(self):
        self.mpq = pq.MinPQ()

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
        self.assertEqual(self.mpq.delMin(), 1)
        self.assertEqual(self.mpq.size(), 4)

    def test_pq_with_initializer(self):
        self.mpq = pq.MinPQ([3,4,5,6,7,2,3,1])
        self.assertEqual(self.mpq.delMin(), 1)
        self.assertEqual(self.mpq.delMin(), 2)
        self.assertEqual(self.mpq.size(), 6)


if __name__ == '__main__':
    unittest.main()
        

