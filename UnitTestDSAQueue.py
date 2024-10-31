import unittest
from DSALinkedList import DSALinkedList
from DSAQueue import DSAQueue

class DSAQueueTestCase(unittest.TestCase):
    def setUp(self):
        self.queue = DSAQueue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())
        self.assertEqual(self.queue.peek(), 1)
        print("Test Case: test_enqueue")

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.peek(), 2)
        print("Test Case: test_dequeue")

    def test_peek(self):
        self.assertRaises(ValueError, self.queue.peek)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.peek(), 1)
        print("Test Case: test_peek")

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())
        print("Test Case: test_is_empty")

    def test_iterator(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        result = [item for item in self.queue]
        self.assertEqual(result, [1, 2, 3])
        print("Test Case: test_iterator")

if __name__ == '__main__':
    unittest.main()

