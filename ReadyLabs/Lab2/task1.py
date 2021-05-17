import sys
sys.path.append('../')
from Lab1.utils.plot import plot_graph
from utils.degree_sequence import generate_graph_from_degree_sequence, is_degree_sequence
            

if __name__ == "__main__":
    A = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
    B = [4, 4, 3, 1, 2]

    print(f"Czy ciag {A} jest ciagiem graficznym: {is_degree_sequence(A)}")
    print(f"Czy ciag {B} jest ciagiem graficznym: {is_degree_sequence(B)}")
    
    graph = generate_graph_from_degree_sequence(A)
    plot_graph(graph)