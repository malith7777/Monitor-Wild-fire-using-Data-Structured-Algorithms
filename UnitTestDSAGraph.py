import unittest
from Graph import DSAGraph 
from Graph import DSAGraphNode

class DSAGraphTestCase(unittest.TestCase):
    def setUp(self):
        self.graph = DSAGraph()
        self.graph.addVertex("A")
        self.graph.addVertex("B")
        self.graph.addVertex("C")
        self.graph.addVertex("D")
        self.graph.addEdge("A", "B")
        self.graph.addEdge("B", "C")
        self.graph.addEdge("C", "D")

    def testAddVertex(self):
        print("Running testAddVertex")
        self.assertEqual(self.graph.getVertexCount(), 4)

    def testAddEdge(self):
        print("Running testAddEdge")
        self.assertTrue(self.graph.isAdjacent("A", "B"))
        self.assertTrue(self.graph.isAdjacent("B", "C"))
        self.assertTrue(self.graph.isAdjacent("C", "D"))
        self.assertFalse(self.graph.isAdjacent("A", "C"))

    def testHasVertex(self):
        print("Running testHasVertex")
        self.assertTrue(self.graph.hasVertex("A"))
        self.assertFalse(self.graph.hasVertex("E"))

    def testGetVertexCount(self):
        print("Running testGetVertexCount")
        self.assertEqual(self.graph.getVertexCount(), 4)

    def testGetEdgeCount(self):
        print("Running testGetEdgeCount")
        self.assertEqual(self.graph.getEdgeCount(), 3)

    def testIsAdjacent(self):
        print("Running testIsAdjacent")
        self.assertTrue(self.graph.isAdjacent("A", "B"))
        self.assertTrue(self.graph.isAdjacent("B", "C"))
        self.assertTrue(self.graph.isAdjacent("C", "D"))
        self.assertFalse(self.graph.isAdjacent("A", "C"))

    def testGetAdjacent(self):
        print("Running testGetAdjacent")
        self.assertEqual(self.graph.getAdjacent("A"), ["B"])
        self.assertEqual(self.graph.getAdjacent("B"), ["A", "C"])
        self.assertEqual(self.graph.getAdjacent("C"), ["B", "D"])
        self.assertEqual(self.graph.getAdjacent("D"), ["C"])

    def testDisplayAsList(self):
        print("Running testDisplayAsList")
        # Redirect stdout to a string buffer for testing output
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        output = StringIO()
        sys.stdout = output

        self.graph.displayAsList()
        expected_output = 'D: C \nC: B D \nB: A C \nA: B \n'
        self.assertEqual(output.getvalue(), expected_output)

        # Restore stdout
        sys.stdout = saved_stdout

    def testDisplayAsMatrix(self):
        print("Running testDisplayAsMatrix")
        # Redirect stdout to a string buffer for testing output
        import sys
        from io import StringIO
        saved_stdout = sys.stdout
        output = StringIO()
        sys.stdout = output

        self.graph.displayAsMatrix()
        expected_output = "D: 0 1 0 0\nC: 1 0 1 0\nB: 0 1 0 1\nA: 0 0 1 0\n"
        self.assertEqual(output.getvalue(), expected_output)

        # Restore stdout
        sys.stdout = saved_stdout

if __name__ == "__main__":
    unittest.main()

