import unittest
from DSALinkedList import DSALinkedList
from DSAStack import DSAStack

class DSAStackTestCase(unittest.TestCase):
    def setUp(self):
        self.stack = DSAStack()

    def test_push(self):
        self.stack.push(1)
        self.assertFalse(self.stack.isEmpty())
        self.assertEqual(self.stack.peek(), 1)
        print("Test Case: test_push")

    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.peek(), 1)
        print("Test Case: test_pop")

    def test_peek(self):
        self.assertRaises(ValueError, self.stack.peek)
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)
        print("Test Case: test_peek")

    def test_is_empty(self):
        self.assertTrue(self.stack.isEmpty())
        self.stack.push(1)
        self.assertFalse(self.stack.isEmpty())
        print("Test Case: test_is_empty")

    def test_iterator(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        result = [item for item in self.stack]
        self.assertEqual(result, [3, 2, 1])
        print("Test Case: test_iterator")

if __name__ == '__main__':
    unittest.main()

