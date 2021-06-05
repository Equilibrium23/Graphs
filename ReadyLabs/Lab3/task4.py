from copy import deepcopy
from utils.graph import Graph, GraphRepresentationType
from utils.plot import plot_graph
from task3 import print_distance_matrix
from utils.connected_graph import generate_connected_graph
from utils.graph_center import find_center_of_graph, find_minimax_center_of_graph

if __name__ == "__main__":
    graph = generate_connected_graph(5)
    graph.add_connection_weights(1, 10)
    print_distance_matrix(graph)

    find_center_of_graph(graph)
    find_minimax_center_of_graph(graph)

    plot_graph(graph)