import unittest
from src.graph import Graph
from src.algorithms import dijkstra, pagerank

class TestGraphLibrary(unittest.TestCase):
    def test_add_node_and_edge(self):
        g = Graph()
        g.add_edge('A', 'B', 2)
        self.assertIn('A', g.graph)
        self.assertIn(('B', 2), g.graph['A'])

    def test_dijkstra(self):
        g = Graph()
        g.add_edge('A', 'B', 1)
        g.add_edge('B', 'C', 2)
        distances = dijkstra(g, 'A')
        self.assertEqual(distances['C'], 3)

    def test_pagerank(self):
        g = Graph(directed=True)
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        g.add_edge('C', 'A')
        ranks = pagerank(g)
        self.assertAlmostEqual(sum(ranks.values()), 1, places=5)

if __name__ == "__main__":
    unittest.main()
