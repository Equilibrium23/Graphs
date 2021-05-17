import sys
sys.path.append('../')
import numpy as np
from Lab1.utils.graph import Graph
from Lab1.utils.handleInput import *

def calculate_distance_matrix(G: Graph):
    if(G.representation_type != GraphRepresentationType.ADJACENCY_MATRIX):
        raise Exception('representation_type must be: ADJACENCY_MATRIX')
    if(len(G.graph_weights) == 0):
        raise Exception('Graf nie ma wag lub wierzcholkow!!!')

    gr = G.graph_representation

    distance_matrix = []

    for i in range(len(gr)):
        p_s, d_s = dijkstra(G, i)
        distance_matrix.append(d_s)

    return distance_matrix


def dijkstra(G: Graph, s):
    if(G.representation_type != GraphRepresentationType.ADJACENCY_MATRIX):
        raise Exception('representation_type must be: ADJACENCY_MATRIX')
    if(len(G.graph_weights) == 0):
        raise Exception('Graf nie ma wag lub wierzcholkow!!!')

    gr = G.graph_representation
    w = G.graph_weights
    nodeAmount = len(w)

    # Init
    p_s = np.full(nodeAmount, None)
    d_s = np.full(nodeAmount, float('Inf'))
    d_s[s] = 0
    S = []

    u = _find_min_u(S, d_s)

    while len(S) != nodeAmount:
        u = _find_min_u(S, d_s)
        S.append(u)
        for v in range(len(w[u])):
            if(gr[u][v] != 0 and v not in S):
                _relax(u, v, w, d_s, p_s)

    return p_s, d_s


def _find_min_u(S, d_s):
    min_node = -1
    for i in range(len(d_s)):
        if(i not in S):
            if min_node == -1:
                min_node = i
            else:
                if(d_s[i] < d_s[min_node]):
                    min_node = i

    return min_node

def _relax(u, v, w, d_s, p_s):
    if d_s[v] > d_s[u] + w[u][v]:
        d_s[v] = d_s[u]  + w[u][v]
        p_s[v] = u


