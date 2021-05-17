import sys
sys.path.append('../')

from Lab1.utils.plot import plot_graph
from utils.k_regular import generate_k_regular_graph
from utils.graph_randomizer import randomize_edges
from random import randrange


if __name__ == "__main__":
	k = randrange(0, 6)
	graph = generate_k_regular_graph(2, 3)
	plot_graph(graph)
	randomize_edges(graph, 5)
	plot_graph(graph)
	graph = generate_k_regular_graph(k)
	plot_graph(graph)
	randomize_edges(graph, k)
	plot_graph(graph)