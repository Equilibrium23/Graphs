from typing import List
from utils.graph import Graph, GraphRepresentationType
from utils.plot import plot_graph

def is_degree_sequence(degree_sequence: List):
    A = degree_sequence.copy()
    list.sort(A)
    while True:
        for node in A:
            if node < 0 or node >= len(A):
                return False

        if sum(A) == 0:
            return True

        i = 1
        while i <= A[0]:
            A[i] = A[i] - 1
            i = i + 1

        A[0] = 0
        list.sort(A, reverse=True)

def generate_graph_from_degree_sequence(A: List):
    if not is_degree_sequence(A):
        raise Exception("To nie jest ciag graficzny")

    list.sort(A, reverse=True)
    n = len(A)
    matrix = [[0 for i in range(n)] for j in range(n)]
    mod_A = [[i, A[i]] for i in range(n)]

    while sum([n[1] for n in mod_A]):
        list.sort(mod_A, key=lambda x: x[1], reverse=True)
        for i in range(1, mod_A[0][1]+1):
            mod_A[i][1] = mod_A[i][1] - 1
            mod_A[0][1] = mod_A[0][1] - 1
            matrix[mod_A[i][0]][mod_A[0][0]] = 1
            matrix[mod_A[0][0]][mod_A[i][0]] = 1

    graph = Graph(GraphRepresentationType.ADJACENCY_MATRIX, matrix)
    return graph