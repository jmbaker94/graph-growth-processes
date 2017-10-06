from collections import defaultdict


class Vertex:
    def __init__(self, index=None, value=None, parent=None):
        self.index = index
        self.value = value
        self.parent = parent

    @property
    def degree(self):
        if self.parent is not None:
            return len(self.parent[self])

    def __str__(self):
        return "Vertex Object: " + str(self.index) + ', ' + str(self.value)

    def __lt__(self, other):
        if self.degree < other.degree:
            return True
        else:
            return False


class Graph:
    def __init__(self, cl=None):
        self.__vertices = []
        self.__adj_list = defaultdict(set)
        self.__index_to_vertex = defaultdict(Vertex)
        self.__edge_set = set()
        self.__graph_class = cl

    def add_edge(self, u: Vertex, v: Vertex):
        if u not in self.__vertices or v not in self.__vertices:
            print("graph.add_edge: invalid vertices given.")
            return None

        self.__adj_list[u].add(v)
        self.__adj_list[v].add(u)

    def set_edge_list(self):
        self.__edge_set = set()
        for v in self.__vertices:
            for u in self.__adj_list[v]:
                self.__edge_set.add(frozenset([u, v]))

    def add_vertex(self, v: Vertex):
        v.parent = self
        self.__vertices.append(v)
        self.__adj_list[v] = set()
        self.__index_to_vertex[v.index] = v

    def add_new_vertex(self, index=None, value=None):
        self.add_vertex(Vertex(index, value, self))

    def get_vertex(self, index):
        if type(index) != int:
            raise TypeError

        return self._get_vertex_from_index(index)

    def _get_vertex_from_index(self, index):
        return self.__index_to_vertex[index]

    def set_adjacency_set(self, v, a_set):
        for s in a_set:
            if type(s) is not Vertex:
                raise TypeError

        if type(v) is not Vertex:
            raise TypeError

        self.__adj_list[v] = set(a_set)

    def get_subgraph(self, vertices):
        g = Graph()
        for v in vertices:
            g.add_vertex(v)
            for adj in self.__adj_list[v]:
                if adj in vertices:
                    g.add_edge(v, adj)

    @property
    def degree_sequence(self):
        output = []
        for v in self.vertices:
            output.append(v.degree)
        return sorted(output)[::-1]

    @property
    def id_degree_sequence(self):
        class DegPair:
            def __init__(self, t):
                self.data = t

            def __lt__(self, other):
                if self.data[1] < other.data[1]:
                    return True
                return False

        output = []
        for v in self.vertices:
            output.append(DegPair((v, v.degree)))
        return [(x.data[0], x.data[1]) for x in sorted(output)[::-1]]

    def __getitem__(self, item):
        if type(item) is int:
            return self.__adj_list[self._get_vertex_from_index(item)]
        elif type(item) is Vertex:
            return self.__adj_list[item]
        else:
            raise TypeError

    @property
    def edge_set(self):
        self.set_edge_list()
        return self.__edge_set

    @property
    def vertices(self):
        return self.__vertices

    @property
    def vsize(self):
        return len(self.__vertices)

    @property
    def esize(self):
        return len(self.__edge_set)

    def __contains__(self, thing):
        if type(thing) is set:
            if thing in self.__edge_set:
                return True
            else:
                return False
        elif type(thing) is tuple:
            if thing[0] in self.__adj_list[thing[1]] and thing[1] in self.__adj_list[thing[0]]:
                return True
            else:
                return False
        elif type(thing) is Vertex:
            if thing in self.vertices:
                return True
            else:
                return False
        else:
            raise TypeError

    def __str__(self):
        v_string = ""
        for v in self.vertices:
            v_string += "\t\t" + str(v) + "\n"

        e_string = ""
        for e in self.edge_set:
            e_string += "\t\t"
            for v in e:
                e_string += str(v.index) + ' '
            e_string += "\n"

        return "Graph Object: \n\t vertices: \n" + v_string + "\t edges: \n " + e_string

