import sys
sys.path.append('../')
from Lab1.graph import Graph
from Lab1.plot import plot_graph
from graph_randomizer import randomize_edges

def is_graphic_string(string):
    A = string.copy()
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

def generate_graph_from_graphic_string(A):
    if not is_graphic_string(A):
        raise Exception("To nie jest ciag graficzny")

    list.sort(A, reverse=True)
    n = len(A)
    matrix = [[0 for i in range(n)] for j in range(n)]
    mod_A = [[i, A[i]] for i in range(n)]

    while sum([n[1] for n in mod_A]):
        list.sort(mod_A, key=lambda x: x[1], reverse=True)
        for i in range(1, n):
            if matrix[mod_A[0][0]][mod_A[i][0]] == 0:
                matrix[mod_A[0][0]][mod_A[i][0]] = 1
                matrix[mod_A[i][0]][mod_A[0][0]] = 1
                mod_A[i][1] = mod_A[i][1] - 1
                mod_A[0][1] = mod_A[0][1] - 1
                break

    graph = Graph.create_graph_representation("adjacency_matrix", matrix)
    return graph
            

if __name__ == "__main__":

    A = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
    B = [4, 4, 3, 1, 2]
    
    graph = generate_graph_from_graphic_string(A)
    plot_graph(graph)
    randomize_edges(graph, 5)
    plot_graph(graph)