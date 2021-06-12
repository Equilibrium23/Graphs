from .graph import Graph, GraphRepresentationType
from .sum_wages_in_cycle import sum_wages_in_cycle
from .graph_randomizer import two_opt
from random import uniform
from math import exp
from copy import deepcopy

def generate_hamilton_cycle_graph(graph: Graph):
    matrix = graph.graph_representation
    cycle = range(len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] = 0

    for i in range(len(cycle) - 1):
        matrix[cycle[i]][cycle[i+1]] = 1
        matrix[cycle[i+1]][cycle[i]] = 1
    matrix[cycle[len(cycle) - 1]][0] = 1
    matrix[cycle[0]][len(cycle) - 1] = 1

    graph.graph_representation = matrix
    return graph

def komiwojazer(full_graph : Graph):
    cycle = generate_hamilton_cycle_graph(full_graph)
    path = annealing(cycle)

    return path


def annealing(cycle : Graph, IT_MAX : int):
    path_length = sum_wages_in_cycle(cycle)
    for i in range(100):
        T = 0.001 * i**2
        for it in range(IT_MAX):
            new_matrix = deepcopy(cycle.graph_representation)
            new_cycle = Graph(GraphRepresentationType.ADJACENCY_MATRIX, new_matrix)
            new_cycle.add_connection_weights(new_matrix)
            two_opt(new_cycle, 2)
            new_path_length = sum_wages_in_cycle(new_cycle)
            if(new_path_length < path_length):
                path_length = new_path_length
                cycle = new_cycle
            else:
                if(uniform(0, 1) < exp(-(new_path_length - path_length) / T)):
                    path_length = new_path_length
                    cycle = new_cycle
    return cycle