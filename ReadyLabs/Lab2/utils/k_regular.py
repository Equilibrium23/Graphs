import sys
sys.path.append('../')
from Lab1.utils.graph import Graph
from Lab1.utils.plot import plot_graph
from utils.graphic_string import is_graphic_string, generate_graph_from_graphic_string

from random import randrange

def generate_vertex_count(k):
	max_degree = 10
	vertex_count = randrange(k + 1, max_degree)

	while (vertex_count * k) % 2:
		vertex_count = randrange(k + 1, max_degree)

	return vertex_count 

def generate_graph_properties(k):
	vertex_count = generate_vertex_count(k)
	string = [k for i in range(vertex_count)]
	return vertex_count, string


def generate_k_regular_graph(k, vertex_count = 0):
	if(vertex_count):
		graphic_string = [k for i in range(vertex_count)]
	else:
		vertex_count, graphic_string = generate_graph_properties(k)

		while is_graphic_string(graphic_string) is False:
			vertex_count, graphic_string = generate_graph_properties(k)

	print(f"generated {k}_regular graph")
	
	return generate_graph_from_graphic_string(graphic_string)