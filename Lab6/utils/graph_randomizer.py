import random
from utils.graph import Graph
from utils.plot import plot_graph

def get_random_two_connected_nodes(graph: Graph):
    number_of_nodes = len(graph.graph_representation)
    matrix = graph.graph_representation
    max_iter = 1000*number_of_nodes
    while True:
        first = random.randint(0, number_of_nodes-1)
        second = random.randint(0, number_of_nodes-1)

        if(first != second and matrix[first][second] == matrix[second][first] and matrix[first][second] == 1):
            return (first, second)

        max_iter -= 1
        if max_iter == 0:
            raise Exception("Graph cannot be randomized")

def swap_two_pairs_of_nodes(graph: Graph):
    max_iter = 10000
    while True:
        a, b = get_random_two_connected_nodes(graph)
        c, d = get_random_two_connected_nodes(graph)
        matrix = graph.graph_representation

        if(a != d and b != c and a != c and b != d):# and matrix[a][d] == 0 and matrix[b][c] == 0):
            matrix[a][b] = matrix[b][a] = matrix[c][d] = matrix[d][c] = 0
            matrix[a][d] = matrix[d][a] = matrix[c][b] = matrix[b][c] = 1
            return
        
        max_iter -= 1
        if max_iter == 0:
            raise Exception("Graph cannot be randomized")

def two_opt(graph: Graph, number_of_randomisations: int):
    if len(graph.graph_representation) < 4:
        raise Exception("Minimal size of graph == 4")
    graph.change_to_adjacency_matrix()
    for i in range(number_of_randomisations):
        swap_two_pairs_of_nodes(graph)
