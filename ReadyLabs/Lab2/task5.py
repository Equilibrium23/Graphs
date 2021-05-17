import sys
sys.path.append('../')

from Lab1.utils.plot import plot_graph
from utils.k_regular import generate_k_regular_graph
from random import randrange


if __name__ == "__main__":
	k = randrange(0, 6)
	graph = generate_k_regular_graph(k)
	print(f"generated {k}_regular graph")
	plot_graph(graph)
