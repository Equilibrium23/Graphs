import sys
sys.path.append('../')
from Lab1.utils.graph import Graph
from Lab1.utils.plot import plot_graph
from Lab1.utils.handleInput import *
from utils.connected_graph import *
from utils.dijkstra import calculate_distance_matrix
from copy import copy, deepcopy


def print_distance_matrix(G: Graph):
    m = calculate_distance_matrix(G)

    for i in range(len(m)):
        print(m[i])


    


if __name__ == "__main__":
    #examples
    graph = generate_connected_graph(7)

    graph.add_connection_weights(1, 10)

    graph.print_weights()

    print_distance_matrix(graph)

    plot_graph(graph)