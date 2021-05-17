import sys
sys.path.append('../')
from Lab1.utils.graph import Graph
from Lab1.utils.plot import plot_graph
from Lab1.utils.handleInput import *
from utils.connected_graph import *
from utils.dijkstra import calculate_distance_matrix


def print_distance_matrix(G: Graph):
    old_representation = G.representation_type
    graph.change_graph_representation_to(GraphRepresentationType.ADJACENCY_MATRIX)

    m = calculate_distance_matrix(G)

    print("\nMacierz odleglosci:")

    for i in range(len(m)):
        for j in range(len(m[i])):
            print('{:>6}'.format(m[i][j]), end='')
        print()

    G.change_graph_representation_to(old_representation)


    


if __name__ == "__main__":
    #examples
    graph = generate_connected_graph(7)

    graph.add_connection_weights(1, 10)

    graph.print_weights()

    print_distance_matrix(graph)

    plot_graph(graph)