import unittest
from DSALinkedList import DSALinkedList

class DSALinkedListTests(unittest.TestCase):
    def setUp(self):
        self.list = DSALinkedList()

    def test_is_empty(self):
        print("Running test_is_empty")
        self.assertTrue(self.list.is_empty())
        self.list.insert_first(10)
        self.assertFalse(self.list.is_empty())

    def test_insert_first(self):
        print("Running test_insert_first")
        self.list.insert_first(10)
        self.assertEqual(self.list.peek_first(), 10)
        self.list.insert_first(20)
        self.assertEqual(self.list.peek_first(), 20)

    def test_insert_last(self):
        print("Running test_insert_last")
        self.list.insert_last(10)
        self.assertEqual(self.list.peek_last(), 10)
        self.list.insert_last(20)
        self.assertEqual(self.list.peek_last(), 20)

    def test_peek_first(self):
        print("Running test_peek_first")
        self.assertRaises(ValueError, self.list.peek_first)
        self.list.insert_first(10)
        self.assertEqual(self.list.peek_first(), 10)

    def test_peek_last(self):
        print("Running test_peek_last")
        self.assertRaises(ValueError, self.list.peek_last)
        self.list.insert_last(10)
        self.assertEqual(self.list.peek_last(), 10)

    def test_remove_first(self):
        print("Running test_remove_first")
        self.assertRaises(ValueError, self.list.remove_first)
        self.list.insert_last(10)
        self.assertEqual(self.list.remove_first(), 10)
        self.assertTrue(self.list.is_empty())

    def test_remove_last(self):
        print("Running test_remove_last")
        self.assertRaises(ValueError, self.list.remove_last)
        self.list.insert_last(10)
        self.assertEqual(self.list.remove_last(), 10)
        self.assertTrue(self.list.is_empty())

    def test_iteration(self):
        print("Running test_iteration")
        self.list.insert_last(10)
        self.list.insert_last(20)
        self.list.insert_last(30)
        result = []
        for item in self.list:
            result.append(item)
        self.assertListEqual(result, [10, 20, 30])

if __name__ == '__main__':
    unittest.main()

