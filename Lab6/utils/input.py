from math import sqrt
from typing import List
from .graph import Graph, GraphRepresentationType

class Point:
    @staticmethod
    def distance(point1, point2):
        return sqrt ( pow(point1.x - point2.x, 2) + pow (point1.y - point2.y, 2) )

    def __init__(self, x, y):
        self.x = x
        self.y = y

    
def read_input(path: str):
    with open (path, 'r') as points:
        graph_points = []
        for line in points:
            coordinates = [ float(item) for item in line.split(" ") if item != "" ]
            graph_points.append( Point( coordinates[0], coordinates[1]) )
        return graph_points

def travelling_salesman_graph(path):
    points = read_input(path)
    adjacency_matrix = []
    weights_matrix = []
    for i in range(len(points)):
        adjacency_matrix.append([])
        for j in range(len(points)):
            adjacency_matrix[i].append(1 if i != j else 0)
    
    for i in range(len(points)):
        weights_matrix.append([])
        for j in range(len(points)):
            weights_matrix[i].append( Point.distance(points[i], points[j]) )
    
    graph = Graph(GraphRepresentationType.ADJACENCY_MATRIX, adjacency_matrix)
    graph.add_connection_weights(weights_matrix)
    return graph
    
def create_graph_as_cycle(graph: Graph, cycle: List):
    matrix = graph.graph_representation
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
