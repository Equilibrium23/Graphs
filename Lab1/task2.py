from graph import Graph
from plot import plot_graph

def is_graphic_string(A):
    list.sort(A)
    while True:
        if sum(A) == 0:
            return True

        for node in A:
            if node < 0 or node >= len(A):
                return False

        i = 1
        while i <= A[0]:
            A[i] = A[i] - 1
            i = i + 1

        A[0] = 0
        list.sort(A, reverse=True)

def generate_graph_from_graphic_string(A):
    if not is_graphic_string(A.copy()):
        raise Exception("To nie jest ciag graficzny")

    list.sort(A, reverse=True)
    n = len(A)
    matrix = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        j = 0
        while A[i] > 0:
            if i < j and A[j] > 0:
                matrix[i][j] = 1
                matrix[j][i] = 1
                A[i] = A[i] - 1
                A[j] = A[j] - 1
            j = j + 1

    graph = Graph.create_graph_representation("adjacency_matrix", matrix)
    return graph
            

if __name__ == "__main__":

    A = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
    B = [4, 4, 3, 1, 2]
    
    graph = generate_graph_from_graphic_string(A)
    plot_graph(graph)