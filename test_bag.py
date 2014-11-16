import bag
import unittest

class TestBagFunction(unittest.TestCase):
    
    def setUp(self):
        self.bag = bag.Bag()

    def tearDown(self):
        self.bag = None

    def testMethods(self):
        self.assertEqual(self.bag.size(), 0)
        self.bag.add('a')
        self.assertEqual(self.bag.size(), 1)

    def testIteration(self):
        self.bag.add(0)
        self.bag.add(1)
        self.bag.add(2)
        for i, item in enumerate(self.bag):
            self.assertEqual(i, item)

if __name__ == '__main__':
    unittest.main()
