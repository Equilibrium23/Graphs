import random
from .graph import Graph, GraphRepresentationType
from .kosaraju import kosaraju


def generate_Gnp_digraph(number_of_vertexes : int, probability : float):
    matrix = [[0 for i in range(number_of_vertexes)] for j in range(number_of_vertexes)]
    for i in range(number_of_vertexes):
        for j in range(number_of_vertexes):
            if j != i and random.randint(0, 100) < probability*100:
                matrix[i][j] = 1
    
    graph = Graph(GraphRepresentationType.DIGRAF_ADJACENCY_MATRIX, matrix)
    return graph

def generate_strongly_connected_digraph(number_of_vertexes : int, probability : float):
    while True:
        graph = generate_Gnp_digraph(number_of_vertexes, probability)
        components = kosaraju(graph, 0)
        if len(components) == 1:
            return graph
        
