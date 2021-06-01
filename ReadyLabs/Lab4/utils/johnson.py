from .graph import Graph,GraphRepresentationType
import numpy as np
from .bellman_ford import bellman_ford, print_bellman_ford
from .dijkstra import dijkstra
import copy

def create_graph_with_new_node(graph: Graph):
    matrix = graph.graph_representation.copy()
    w = graph.graph_weights.copy()
    for i in matrix:
        i.append(0)
    for i in w:
        i.append(0)

    matrix.append([1 for i in range(len(matrix))])
    matrix[len(matrix)-1].append(0)
    w.append([0 for i in range(len(matrix))])
    new_G = Graph(GraphRepresentationType.DIGRAF_ADJACENCY_MATRIX, matrix)
    new_G.graph_weights = w
    return new_G


def johnson(graph: Graph):
    saved_weights = copy.deepcopy(graph.graph_weights)
    n_of_nodes = len(graph.graph_representation)
    s = n_of_nodes
    new_G = create_graph_with_new_node(graph)
    result, d_s, _ = bellman_ford(new_G, s)

    if result == False:
        raise Exception(f"W grafie jest cykl o ujemnej wadze osiągalny ze źródła s={s}")

    h = d_s
    for v in range(n_of_nodes+1):
        for u in range(n_of_nodes+1):
            if new_G.graph_representation[u][v] == 1:
                new_G.graph_weights[u][v] += int(h[u] - h[v])

    new_G.graph_weights.pop()
    new_G.graph_representation.pop()
    for i in range(n_of_nodes):
        new_G.graph_weights[i].pop()
        new_G.graph_representation[i].pop()

    graph.graph_weights = new_G.graph_weights
    D = [[0 for i in range(n_of_nodes)] for j in range(n_of_nodes)]
    for u in range(n_of_nodes):
        _, d_s = dijkstra(graph, u)
        for v in range(n_of_nodes):
            D[u][v] = d_s[v] - h[u] + h[v]

    graph.graph_weights = saved_weights
    return D