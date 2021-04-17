import sys
sys.path.append('../')
from Lab1.graph import Graph
from Lab1.plot import plot_graph
from Lab1.graphRandomizer import *
from Lab1.handleInput import *
from task2 import is_graphic_string, generate_graph_from_graphic_string

from random import randrange

def generate_vertex_count(k):
	vertex_count = randrange(k + 1, 10)

	while (vertex_count * k) % 2:
		vertex_count = randrange(k + 1, 10)

	return vertex_count 

def generate_graph_properties(k):
	vertex_count = generate_vertex_count(k)
	string = [k for i in range(vertex_count)]
	return vertex_count, string


def generate_k_regular_graph(k):
	vertex_count, graphic_string = generate_graph_properties(k)

	while is_graphic_string(graphic_string) is False:
		vertex_count, graphic_string = generate_graph_properties(k)
	
	return generate_graph_from_graphic_string(graphic_string)


def main():
	k = randrange(0, 6)
	graph = generate_k_regular_graph(k)
	print(f"generated {k}_regular graph")
	plot_graph(graph)

if __name__ == "__main__":
	main()