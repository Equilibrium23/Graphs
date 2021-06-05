import random
import itertools
from utils.graph import Graph
from utils.plot import plot_graph
from utils.graph import Graph, GraphRepresentationType
from utils.plot import plot_graph
from random import randint

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

        if(a != d and b != c and a != c and b != d and matrix[a][d] == 0 and matrix[b][c] == 0):
            matrix[a][b] = matrix[b][a] = matrix[c][d] = matrix[d][c] = 0
            matrix[a][d] = matrix[d][a] = matrix[c][b] = matrix[b][c] = 1
            return
        
        max_iter -= 1
        if max_iter == 0:
            raise Exception("Graph cannot be randomized")

def randomize_edges(graph: Graph, number_of_randomisations: int):
    if len(graph.graph_representation) < 4:
        raise Exception("Minimal size of graph == 4")
    graph.change_to_adjacency_matrix()
    for i in range(number_of_randomisations):
        swap_two_pairs_of_nodes(graph)


def create_adjacency_matrix_from_edges_list(edges_list, number_of_vertexes, number_of_edges):
    random_indexes = random.sample(range(len(edges_list)), number_of_edges)
    matrix = [[0 for i in range(number_of_vertexes)] for j in range(number_of_vertexes)]
    for random_index in random_indexes:
        matrix[edges_list[random_index][0]][edges_list[random_index][1]] = 1
        matrix[edges_list[random_index][1]][edges_list[random_index][0]] = 1
    return matrix

def generate_Gnl_graph(number_of_vertexes : int, number_of_edges : int):
    possible_edges = list(itertools.combinations(range(number_of_vertexes),2))
    count_of_possible_edges = len(possible_edges)
    if count_of_possible_edges > number_of_edges:
        return Graph(GraphRepresentationType.ADJACENCY_MATRIX,create_adjacency_matrix_from_edges_list(possible_edges, number_of_vertexes, number_of_edges))
    else:
        raise Exception("{} of edges is too large with this number of vertexes - max = {}".format(number_of_edges,count_of_possible_edges))


def generate_Gnp_graph(number_of_vertexes : int, probability : float):
    matrix = [[0 for i in range(number_of_vertexes)] for j in range(number_of_vertexes)]
    for i in range(number_of_vertexes):
        for j in range(number_of_vertexes):
            if j < i and randint(0, 100) < probability*100:
                matrix[i][j] = 1
            matrix[j][i] = matrix[i][j]
    
    graph = Graph(GraphRepresentationType.ADJACENCY_MATRIX, matrix)
    return graph