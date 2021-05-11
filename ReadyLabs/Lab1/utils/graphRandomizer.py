import random
from .graph import Graph, GraphRepresentationType
from .plot import plot_graph
import itertools

def create_adjacency_matrix_from_edges_list(edges_list, number_of_vertexes, number_of_edges):
    random_indexes = random.sample(range(len(edges_list)), number_of_edges)
    matrix = [[0 for i in range(number_of_vertexes)] for j in range(number_of_vertexes)]
    for random_index in random_indexes:
        matrix[edges_list[random_index][0]][edges_list[random_index][1]] = 1
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
            if j < i and random.randint(0, 100) < probability*100:
                matrix[i][j] = 1
            matrix[j][i] = matrix[i][j]
    
    graph = Graph(GraphRepresentationType.ADJACENCY_MATRIX, matrix)
    return graph
