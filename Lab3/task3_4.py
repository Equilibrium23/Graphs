import sys
sys.path.append('../')
from Lab1.graph import Graph
from task3_2 import _dijkstra
from task3_3 import calculate_distance_matrix, print_distance_matrix
from Lab1.plot import plot_graph
from connected_graph import _generate_connected_graph, add_connection_weights
from copy import copy, deepcopy

def find_center_of_graph(G: Graph):
    m = calculate_distance_matrix(G)
    center_data = (0, float('inf'))

    for i in range(len(m)):
        sum_of_distances = sum(m[i])
        if sum_of_distances < center_data[1]:
            center_data = (i, sum_of_distances)

    print(f"Center of graph: {center_data[0]} (sum of distances: {center_data[1]}")
    return center_data

def find_minimax_center_of_graph(G: Graph):
    m = calculate_distance_matrix(G)
    center_data = (0, float('inf'))

    for i in range(len(m)):
        biggest_distance = max(m[i])
        if biggest_distance < center_data[1]:
            center_data = (i, biggest_distance)

    print(f"Minimax center of graph: {center_data[0]} (biggest distance: {center_data[1]})")
    return center_data

if __name__ == "__main__":
    graph = _generate_connected_graph(10)

    gr_cpy = deepcopy(graph.graph_representation)

    add_connection_weights(graph, 1, 10)
    print_distance_matrix(graph)
    find_center_of_graph(graph)
    find_minimax_center_of_graph(graph)

    graph_to_draw = Graph("adjacency_matrix", gr_cpy)
    plot_graph(graph_to_draw)