import sys
sys.path.append('../')
from Lab1.utils.plot import plot_graph
from utils.graph_randomizer import randomize_edges
from utils.graphic_string import generate_graph_from_graphic_string
            

if __name__ == "__main__":
    A = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
    
    graph = generate_graph_from_graphic_string(A)
    plot_graph(graph)
    randomize_edges(graph, 5)
    plot_graph(graph)