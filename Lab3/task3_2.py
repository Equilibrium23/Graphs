import sys
sys.path.append('../')
import numpy as np
from Lab1.graph import Graph
from Lab1.plot import plot_graph
from Lab1.handleInput import *
from connected_graph import _generate_connected_graph, add_connection_weights
from copy import copy, deepcopy

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


def _dijkstra(G: Graph, s):
    if(G.representation_type != 'adjacency_matrix'):
        raise Exception('representation_type must be: adjacency_matrix')
    s = s-1

    w = G.graph_representation
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
            if(w[u][v] != 0 and v not in S):
                _relax(u, v, w, d_s, p_s)

    return p_s, d_s


def Dijkstra(G: Graph, s):
    p_s, d_s = _dijkstra(G, s)
    w = G.graph_representation

    G.print_graph_representation()

    print("\nSTART: s =", s)

    for v in range(len(p_s)):
        path = []
        print('d({}) = {} ===> '.format(v + 1, d_s[v]), end='')

        currNode = v
        path.append(currNode + 1)

        while p_s[currNode] != None:
            currNode = p_s[currNode]
            path.append(currNode + 1)

        path = path[::-1] # reversing
        print(path)



if __name__ == "__main__":

    #examples
    graph = _generate_connected_graph(10)

    gr_cpy = deepcopy(graph.graph_representation)

    add_connection_weights(graph, 1, 10)


    Dijkstra(graph, 1)


    graph_to_draw = Graph("adjacency_matrix", gr_cpy)
    plot_graph(graph_to_draw)

    
