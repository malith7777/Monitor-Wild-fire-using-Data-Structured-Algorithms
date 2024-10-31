import unittest
from Heap import DSAHeap
from Heap import DSAHeapEntry

class DSAHeapTestCase(unittest.TestCase):
    def setUp(self):
        self.heap = DSAHeap()
        self.heap.push(DSAHeapEntry(5, "value5"))
        self.heap.push(DSAHeapEntry(3, "value3"))
        self.heap.push(DSAHeapEntry(8, "value8"))
        self.heap.push(DSAHeapEntry(1, "value1"))

    def testPushAndPop(self):
        print("Running testPushAndPop")
        self.assertEqual(len(self.heap.data), 4)
        self.assertEqual(self.heap.pop().getPriority(), 1)
        self.assertEqual(self.heap.pop().getPriority(), 3)
        self.assertEqual(self.heap.pop().getPriority(), 5)
        self.assertEqual(self.heap.pop().getPriority(), 8)
        self.assertTrue(self.heap.is_empty())

    def testIsEmpty(self):
        print("Running testIsEmpty")
        empty_heap = DSAHeap()
        self.assertTrue(empty_heap.is_empty())
        self.assertFalse(self.heap.is_empty())

    def testPopOnEmptyHeap(self):
        print("Running testPopOnEmptyHeap")
        empty_heap = DSAHeap()
        self.assertIsNone(empty_heap.pop())

    def testHeapOrder(self):
        print("Running testHeapOrder")
        self.assertEqual(self.heap.pop().getPriority(), 1)
        self.assertEqual(self.heap.pop().getPriority(), 3)
        self.assertEqual(self.heap.pop().getPriority(), 5)
        self.assertEqual(self.heap.pop().getPriority(), 8)

if __name__ == '__main__':
    unittest.main()
