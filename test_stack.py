import stack
import unittest

class TestStackFunction(unittest.TestCase):

    def setUp(self):
        self.test_stack = stack.Stack()

    def tearDown(self):
        self.test_stack = None
        
    def testMethods(self):
        self.assertEqual(self.test_stack.size(), 0)
        self.assertTrue(self.test_stack.is_empty())
        self.test_stack.push('a')
        self.assertEqual(self.test_stack.size(), 1)
        self.assertFalse(self.test_stack.is_empty())
        self.assertEqual(self.test_stack.pop(), 'a')
        self.test_stack.push('a')
        self.test_stack.push('b')
        self.test_stack.push('c')
        self.assertEqual(self.test_stack.pop(), 'c')
        self.assertEqual(self.test_stack.pop(), 'b')
        self.assertEqual(self.test_stack.pop(), 'a')

    def testIndexError(self):
        with self.assertRaises(IndexError):
            self.test_stack.push('a')
            self.test_stack.pop()
            self.test_stack.pop()

if __name__ == '__main__':
    unittest.main()
            
