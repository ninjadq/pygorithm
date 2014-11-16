import queue
import unittest

class TestStackFunction(unittest.TestCase):

    def setUp(self):
        self.test_q = queue.Queue()

    def tearDown(self):
        self.test_q = None
        
    def testMethods(self):
        self.assertEqual(self.test_q.size(), 0)
        self.assertTrue(self.test_q.is_empty())
        self.test_q.enqueue('a')
        self.assertEqual(self.test_q.size(), 1)
        self.assertFalse(self.test_q.is_empty())
        self.assertEqual(self.test_q.dequeue(), 'a')
        self.test_q.enqueue('a')
        self.test_q.enqueue('b')
        self.test_q.enqueue('c')
        self.assertEqual(self.test_q.dequeue(), 'a')
        self.assertEqual(self.test_q.dequeue(), 'b')
        self.assertEqual(self.test_q.dequeue(), 'c')

    def testIndexError(self):
        with self.assertRaises(IndexError):
            self.test_q.enqueue('a')
            self.test_q.dequeue()
            self.test_q.dequeue()

if __name__ == '__main__':
    unittest.main()
            
