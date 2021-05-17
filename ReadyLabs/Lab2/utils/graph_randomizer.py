import sys
sys.path.append('../')
from random import randint
from Lab1.utils.graph import Graph
from Lab1.utils.plot import plot_graph

def get_random_two_connected_nodes(graph: Graph):
    number_of_nodes = len(graph.graph_representation)
    matrix = graph.graph_representation
    while True:
        first = randint(0, number_of_nodes-1)
        second = randint(0, number_of_nodes-1)

        if(first != second and matrix[first][second] == matrix[second][first] and matrix[first][second] == 1):
            return (first, second)

def swap_two_pairs_of_nodes(graph: Graph):
    while True:
        a, b = get_random_two_connected_nodes(graph)
        c, d = get_random_two_connected_nodes(graph)
        matrix = graph.graph_representation

        if(a != d and b != c and matrix[a][d] == 0 and matrix[b][c] == 0 and
           a != c and b != d and matrix[a][c] == 0 and matrix[b][d] == 0 ):
            matrix[a][b] = matrix[b][a] = matrix[c][d] = matrix[d][c] = 0
            matrix[a][d] = matrix[d][a] = matrix[c][b] = matrix[b][c] = 1
            return

def randomize_edges(graph: Graph, n: int):
    graph.change_to_adjacency_matrix()
    for i in range(n):
        swap_two_pairs_of_nodes(graph)
    