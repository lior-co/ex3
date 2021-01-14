import unittest
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo


def graph_algo():
    ga_ = GraphAlgo()
    for n in range():
        ga_.g.add_node(n)
    ga_.g.add_edge(0, 1, 10.10)
    ga_.g.add_edge(1, 2, 12.12)
    ga_.g.add_edge(2, 1, 21.21)
    return ga_  # graph [v=3, out_e=3, mc=6]


def graph3():
    g_ = GraphAlgo()

    g_.g.add_node(0, (10, 0))
    g_.g.add_node(1, (15, 0))
    g_.g.add_node(5, (5, 0))
    g_.g.add_node(7, (0, 0))
    g_.g.add_node(3, (0, 5))
    g_.g.add_node(4, (5, 5))
    g_.g.add_node(6, (10, 5))
    g_.g.add_node(2, (15, 5))

    g_.g.add_edge(1, 2, 12)
    g_.g.add_edge(2, 0, 20)
    g_.g.add_edge(0, 1, 10)
    g_.g.add_edge(6, 0, 60)
    g_.g.add_edge(6, 4, 64)
    g_.g.add_edge(4, 5, 45)
    g_.g.add_edge(5, 0, 50)
    g_.g.add_edge(6, 2, 62)
    g_.g.add_edge(3, 4, 34)
    g_.g.add_edge(7, 5, 75)
    g_.g.add_edge(3, 7, 37)
    g_.g.add_edge(7, 3, 73)
    g_.g.add_edge(5, 6, 56)
    return g_


def graph2():
    g_ = GraphAlgo()
    for n in range(5):
        g_.g.add_node(n)

    g_.g.add_edge(0, 1, 9)
    g_.g.add_edge(1, 0, 9)

    g_.g.add_edge(0, 2, 1)
    g_.g.add_edge(2, 0, 1)

    g_.g.add_edge(1, 2, 4)
    g_.g.add_edge(2, 1, 4)

    g_.g.add_edge(1, 3, 2)
    g_.g.add_edge(3, 1, 2)

    g_.g.add_edge(2, 3, 7)
    g_.g.add_edge(3, 2, 7)

    g_.g.add_edge(1, 4, 12)
    g_.g.add_edge(4, 1, 12)

    g_.g.add_edge(3, 4, 3)
    g_.g.add_edge(4, 3, 3)
    return g_  # graph [v=5, out_e=14, mc=19]


def digraph():
    g_ = DiGraph()
    for n in range(3):
        g_.add_node(n)
    g_.add_edge(0, 1, 10.10)
    g_.add_edge(1, 2, 12.12)
    g_.add_edge(2, 1, 21.21)
    return g_  # graph [v=3, out_e=3, mc=6]


class TestDiGraph(unittest.TestCase):

    def test_add_node(self):
        g_ = digraph()
        g_.add_node(0)
        self.assertEqual(g_.v_size(), 3)
        self.assertEqual(g_.mc, 7)
        g_.add_node(3)
        self.assertEqual(g_.v_size(), 4)
        self.assertEqual(g_.mc, 8)

    def test_add_edge(self):
        g_ = digraph()
        g_.add_edge(0, 2, 2.02)
        self.assertEqual(g_.e_size(), 4)
        self.assertEqual(g_.mc, 7)
        g_.add_edge(1, 1, 11.11)
        self.assertEqual(g_.e_size(), 4)
        self.assertEqual(g_.mc, 7)

    def test_remove_edge(self):
        g_ = digraph()
        g_.remove_edge(2, 1)
        self.assertEqual(g_.e_size(), 2)
        self.assertEqual(g_.mc, 7)
        g_.remove_edge(2, 1)
        self.assertEqual(g_.e_size(), 2)
        self.assertEqual(g_.mc, 7)
        g_.remove_edge(1, 1)
        self.assertEqual(g_.e_size(), 2)
        self.assertEqual(g_.mc, 7)

    def test_remove_node(self):
        g_ = digraph()
        g_.remove_node(4)
        self.assertEqual(g_.v_size(), 3)
        self.assertEqual(g_.e_size(), 3)
        self.assertEqual(g_.mc, 6)
        g_.remove_node(2)
        self.assertEqual(g_.v_size(), 2)
        self.assertEqual(g_.e_size(), 2)
        self.assertEqual(g_.mc, 7)


class TestGraphAlgo(unittest.TestCase):

    def test_save_and_load_from_json(self):
        g1 = GraphAlgo(digraph())
        g1.save_to_json("t1")
        g2 = GraphAlgo()
        g2.load_from_json("t1")
        self.assertEqual(g1.g.v_size(), g2.g.v_size())
        self.assertEqual(g1.g.e_size(), g2.g.e_size())

    def test_shortest_path(self):
        g = graph2()
        self.assertEqual((g.shortest_path(0, 4)), (10, [0, 2, 1, 3, 4]))

    def test_connected_components(self):
        g = graph3()
        a = g.connected_components()    # [[0, 1, 2], [5, 6, 4], [7, 3]]
        self.assertEqual(a, [[0, 1, 2], [5, 6, 4], [7, 3]])

    def test_connected_componentO(self):
        g = graph3()
        a = g.connected_component(0)  # [0, 1, 2]
        self.assertEqual(a, [0, 1, 2])


if __name__ == '__main__':
    unittest.main()
