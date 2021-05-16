import random
from .graph import Graph, GraphRepresentationType


def generate_Gnp_digraph(number_of_vertexes : int, probability : float):
    matrix = [[0 for i in range(number_of_vertexes)] for j in range(number_of_vertexes)]
    for i in range(number_of_vertexes):
        for j in range(number_of_vertexes):
            if j != i and random.randint(0, 100) < probability*100:
                matrix[i][j] = 1
    
    graph = Graph(GraphRepresentationType.DIGRAF_ADJACENCY_MATRIX, matrix)
    return graph
