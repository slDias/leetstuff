from unittest import TestCase
from data_structures.graphs.adjacent_list import GraphManager, Vertex


class TestGraphManager(TestCase):
    def test_add_new_vertex(self):
        gm = GraphManager()

        added_vertex = gm.add_new_vertex(2)

        assert added_vertex.value == 2
        assert isinstance(added_vertex, Vertex)
        assert gm.has_vertex_value(2)

    
    def test_not_has_vertex_with_value(self):
        gm = GraphManager()

        assert not gm.has_vertex_value(2)

    def test_add_vertex(self):
        v = Vertex(5)
        gm = GraphManager()

        edges = gm.add_vertex(v)

        assert gm.has_vertex(v)
        assert edges == []
    
    def test_add_vertex_does_not_replace(self):
        v = Vertex(5)
        gm = GraphManager()
        gm.add_vertex(v)
        
        with self.assertRaises(Exception):
            gm.add_vertex(v)

        assert gm.has_vertex(v)

    def test_has_vertex_when_true(self):
        v = Vertex(5)
        gm = GraphManager()
        gm.add_vertex(v)
        
        result = gm.has_vertex(v)

        assert result is True
    
    def test_has_vertex_when_false(self):
        v = Vertex(5)
        gm = GraphManager()
        
        result = gm.has_vertex(v)

        assert result is False

    def test_add_edge(self):
        v_a = Vertex(5)
        v_b = Vertex(3)
        gm = GraphManager()
        a_edges = gm.add_vertex(v_a)
        b_edges = gm.add_vertex(v_b)
        
        gm.add_edge(v_a, v_b)

        assert a_edges[0] == v_b
        assert len(a_edges) == 1
        assert b_edges[0] == v_a
        assert len(b_edges) == 1
    
    def test_get_degree(self):
        v_a = Vertex(3)
        v_b = Vertex(3)
        gm = GraphManager()
        a_edges = gm.add_vertex(v_a)
        b_edges = gm.add_vertex(v_b)
        gm.add_edge(v_a, v_b)

        result = gm.get_degree(v_a)

        assert result == 1
    

class TestUndirectAcyclicGraph:
    pass

class TestDirectAcyclicGraph:
    pass

class TestUndirectCyclicGraph:
    pass

class TestDirectCyclicGraph:
    pass
