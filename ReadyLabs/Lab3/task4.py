import sys
sys.path.append('../')
from copy import deepcopy
from Lab1.utils.graph import Graph, GraphRepresentationType
from Lab1.utils.plot import plot_graph
from utils.tu_wstaw_nowy_plik import print_distance_matrix
from utils.tu_wstaw_nowy_plik import _generate_connected_graph, add_connection_weights
from utils.graph_center import find_center_of_graph, find_minimax_center_of_graph

if __name__ == "__main__":
    graph = _generate_connected_graph(10)
    gr_cpy = deepcopy(graph.graph_representation)

    add_connection_weights(graph, 1, 10)
    print_distance_matrix(graph)
    find_center_of_graph(graph)
    find_minimax_center_of_graph(graph)

    graph_to_draw = Graph(GraphRepresentationType.ADJACENCY_MATRIX, gr_cpy)
    plot_graph(graph_to_draw)