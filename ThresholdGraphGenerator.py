from graph import *
import random


class ThresholdGraphGenerator:

    @staticmethod
    def generate_random_graph(num_vertices: int):
        g = Graph(cl="threshold")

        if num_vertices == 0:
            return g
        else:
            g.add_vertex(Vertex(index=0))

        for i in range(num_vertices - 1):
            k = random.randint(0, 1)
            if k == 0:  # gamma vertex
                g.add_new_vertex(index=g.vsize)
            else:  # phi vertex
                v = Vertex(index=g.vsize)
                g.add_vertex(v)

                for vert in g.vertices:
                    if vert != v:
                        g.add_edge(vert, v)
        return g

    @staticmethod
    def check_threshold(g: Graph):
        if g is None:
            print("ThresholdGraphGenerator.check_threshold: no graph given")
            return None

        # We can do this simply by sorting the vertices by degree first
        s_degrees = sorted([v.degree for v in g.vertices])

        for i in range(len(s_degrees)):
            if s_degrees[i] - i < 0:
                return False
        return True



