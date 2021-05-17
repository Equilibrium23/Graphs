import sys
sys.path.append('../')
from Lab1.utils.plot import plot_graph
from utils.graph_randomizer import randomize_edges
from utils.degree_sequence import generate_graph_from_degree_sequence
            

if __name__ == "__main__":
    A = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
    
    graph = generate_graph_from_degree_sequence(A)
    plot_graph(graph)
    randomize_edges(graph, 5)
    plot_graph(graph)