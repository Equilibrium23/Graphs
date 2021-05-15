import sys
sys.path.append('../')

from utils.connected_graph import generate_connected_graph
from Lab1.utils.plot import plot_graph

if __name__ == "__main__":
	graph = generate_connected_graph(5)
	
	graph.add_connection_weights(1, 10)

	plot_graph(graph)
	graph.print_weights();