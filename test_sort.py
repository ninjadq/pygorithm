import sorting
import unittest

class TestMergeSort(unittest.TestCase):
    
    def setUp(self):
        self.merge = sorting.MergeSort.merge
        self.sort  = sorting.MergeSort.sort

    def tearDown(self):
        self.merge = None
        self.sort  = None

    def testMerge(self):
        self.lst = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
        self.merge(self.lst, 0, len(self.lst) )
        self.assertListEqual(self.lst, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def testMergesort(self):
        self.unordered_list = [3, 5, 7, 4, 1]
        self.r = self.sort(self.unordered_list)
        self.assertListEqual(self.r, [1, 3, 4, 5, 7])

class TestQuickSort(unittest.TestCase):
    
    def setUp(self):
        self.partition = sorting.QuickSort.partition
        self.sort  = sorting.QuickSort.sort

    def tearDown(self):
        self.partition = None
        self.sort  = None

    def testPartition(self):
        self.lst = [3, 8, 9, 4, 5, 7, 2, 1]
        index = self.partition(self.lst)
        self.assertEqual(index, 2)
        for i in self.lst[:index+1]:
            self.assertLessEqual(i, self.lst[index])
        for i in self.lst[index+1:]:
            self.assertGreaterEqual(i, self.lst[index])

    def testQuickSort(self):
        self.unordered_list = [3, 5, 7, 4, 1]
        self.result_list = self.sort(self.unordered_list)
        self.assertListEqual(self.result_list, [1, 3, 4, 5, 7])

if __name__=='__main__':
    unittest.main()
