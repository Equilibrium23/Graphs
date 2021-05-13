import sys
sys.path.append('../')
from Lab1.utils.plot import plot_graph
from utils.graphic_string import generate_graph_from_graphic_string, is_graphic_string
            

if __name__ == "__main__":
    A = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
    B = [4, 4, 3, 1, 2]

    print(f"Czy ciag {A} jest ciagiem graficznym: {is_graphic_string(A)}")
    print(f"Czy ciag {B} jest ciagiem graficznym: {is_graphic_string(B)}")
    
    graph = generate_graph_from_graphic_string(A)
    plot_graph(graph)