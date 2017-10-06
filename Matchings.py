from graph import *
from itertools import chain, combinations
from ThresholdGraphGenerator import ThresholdGraphGenerator as TGG


def _check_if_matching(m):
    x = True
    for e1 in m:
        for e2 in m:
            if e1 != e2:
                for i in e1:
                    for j in e2:
                        if i == j:
                            x = False
    return x


def find_maximum_matching(g):
    """Very very inefficient search algorithm, just looks at all the combinations"""
    maximum_matchings = []
    max_length = 0
    for s in chain.from_iterable(combinations(g.edge_set, n) for n in range(g.esize + 1))[::-1]:
        if _check_if_matching(s):
            if len(s) > max_length:
                maximum_matchings = [s]
            elif len(s) == max_length:
                maximum_matchings.append(s)

    if len(maximum_matchings) > 0:
        return maximum_matchings[0]


def matching_jmb(g):
    """Attempts to find a maximum matching using the degree sequence of g"""
    d_bar = g.id_degree_sequence
    


g = TGG.generate_random_graph(6)
print(g.id_degree_sequence)