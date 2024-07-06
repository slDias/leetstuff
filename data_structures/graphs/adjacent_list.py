from typing import List


class Vertex:
    def __init__(self, value):
        self.value = value


class GraphManager:
    def __init__(self):
        self._map = {}

    def add_new_vertex(self, value):
        new_vertex = Vertex(value)
        self._map[new_vertex] = []

        return new_vertex

    def has_vertex_value(self, value) -> bool:
        # todo turn this into a find_vertex_by_value.
        for vertex in self._map.keys():
            if vertex.value == value:
                return True
        return False

    def add_vertex(self, vertex: Vertex) -> List:
        if self.has_vertex(vertex):
            raise ValueError("Vertex already in graph")

        vertex_edges = []
        self._map[vertex] = vertex_edges

        return vertex_edges

    def has_vertex(self, vertex: Vertex) -> bool:
        return vertex in self._map

    def add_edge(self, vertex_a: Vertex, vertex_b: Vertex):
        self._map[vertex_a].append(vertex_b)
        self._map[vertex_b].append(vertex_a)
        # considering an undirected graph, is it useful to have it like?:
        # a -> [b]
        # b -> [a]
        # at a first glance, it seems only one is necessary

    def get_degree(self, vertex: Vertex) -> int:
        return len(self._map[vertex])
        

