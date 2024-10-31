import unittest
from Hash import DSAHashTable
from Hash import DSAHashEntry

class DSAHashTableTestCase(unittest.TestCase):
    def setUp(self):
        self.table = DSAHashTable(5)
        self.table.put("key1", "value1")
        self.table.put("key2", "value2")
        self.table.put("key3", "value3")

    def testPutAndGet(self):
        print("Running testPutAndGet")
        self.assertEqual(self.table.get("key1"), "value1")
        self.assertEqual(self.table.get("key2"), "value2")
        self.assertEqual(self.table.get("key3"), "value3")

    def testHasKey(self):
        print("Running testHasKey")
        self.assertTrue(self.table.hasKey("key1"))
        self.assertTrue(self.table.hasKey("key2"))
        self.assertTrue(self.table.hasKey("key3"))
        self.assertFalse(self.table.hasKey("key4"))

    def testRemove(self):
        print("Running testRemove")
        self.table.remove("key2")
        self.assertFalse(self.table.hasKey("key2"))
        self.assertEqual(self.table.get("key2"), None)
        self.assertEqual(self.table.export(), ["key1", "key3"])

    def testResize(self):
        print("Running testResize")
        self.table.put("key4", "value4")
        self.table.put("key5", "value5")
        self.table.put("key6", "value6")
        self.assertEqual(self.table.maxSize, 10)
        self.assertEqual(len(self.table.hashArray), 10)

    def testExport(self):
        print("Running testExport")
        export_list = self.table.export()
        self.assertEqual(export_list, ["key1", "key2", "key3"])

if __name__ == '__main__':
    unittest.main()

