from utils.graph import Graph
from utils.plot import plot_graph
from utils.graph_randomizer import randomize_edges
from utils.degree_sequence import is_degree_sequence, generate_graph_from_degree_sequence

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
		degree_sequence = [k for i in range(vertex_count)]
	else:
		vertex_count, degree_sequence = generate_graph_properties(k)

		while is_degree_sequence(degree_sequence) is False:
			vertex_count, degree_sequence = generate_graph_properties(k)
	
	graph = generate_graph_from_degree_sequence(degree_sequence)

	try:
		randomize_edges(graph, 7)
	except:
		pass

	print(f"generated {k}_regular graph")
	return graph