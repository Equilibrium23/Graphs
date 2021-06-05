from utils.graph import Graph
from utils.dijkstra import calculate_distance_matrix

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