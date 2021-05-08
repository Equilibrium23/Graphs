import sys
sys.path.append('../')
from Lab1.graph import Graph
from task3_2 import _dijkstra
from Lab1.plot import plot_graph
from connected_graph import _generate_connected_graph, add_connection_weights
from copy import copy, deepcopy

def calculate_distance_matrix(G: Graph):

    if(G.representation_type != 'adjacency_matrix'):
        raise Exception('representation_type must be: adjacency_matrix')

    gr = G.graph_representation

    distance_matrix = []

    for i in range(len(gr)):
        p_s, d_s = _dijkstra(G, i+1)
        distance_matrix.append(d_s)

    return distance_matrix

def print_distance_matrix(G: Graph):
    G.print_graph_representation()

    m = calculate_distance_matrix(G)

    for i in range(len(m)):
        print(m[i])


    


if __name__ == "__main__":
    #examples
    graph = _generate_connected_graph(10)

    gr_cpy = deepcopy(graph.graph_representation)

    add_connection_weights(graph, 1, 10)


    print_distance_matrix(graph)


    graph_to_draw = Graph("adjacency_matrix", gr_cpy)
    plot_graph(graph_to_draw)