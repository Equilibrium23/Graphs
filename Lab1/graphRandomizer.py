import random
from graph import Graph
from plot import plot_graph
import itertools

def two_vertices(vertices):
    list_of_generated_veritces = []
    while True:
        two_vertices = random.sample(vertices, k=2)
        if two_vertices not in list_of_generated_veritces and two_vertices[::-1] not in list_of_generated_veritces:
            list_of_generated_veritces.append(two_vertices)
            yield two_vertices


def create_incidence_matrix_from_edges_list(graph,count_of_vertices,count_of_edges):
    matrix = [[0]*count_of_edges for _ in range(count_of_vertices)]
    for edge_nr, vertices in graph.items():
        for vertex in vertices:
            matrix[vertex][edge_nr] = 1
    return matrix


def generate_Gnl_graph(number_of_vertexes, number_of_edges):
    
    vertices = [ vertex_nr for vertex_nr in range(number_of_vertexes) ]
    max_possibilities = sum(1 for _ in itertools.combinations(vertices,2))
    if number_of_edges > max_possibilities:
        raise Exception("number of edges is too large with this number of vertexes")
    else:
        vertices_generator = two_vertices(vertices)
        graph = { i:next(vertices_generator) for i in range(number_of_edges)} #edge_nr:list of vertices which edge is connecting
        matrix = create_incidence_matrix_from_edges_list(graph, number_of_vertexes, number_of_edges)
        graph = Graph.create_graph_representation("incidence_matrix", matrix)
        return graph


def generate_Gnp_graph(number_of_vertexes, probability):
    matrix = [[0 for i in range(number_of_vertexes)] for j in range(number_of_vertexes)]
    for i in range(number_of_vertexes):
        for j in range(number_of_vertexes):
            if j < i and random.randint(0, 100) < probability:
                matrix[i][j] = 1
            matrix[j][i] = matrix[i][j]
    
    graph = Graph.create_graph_representation("adjacency_matrix", matrix)
    return graph
