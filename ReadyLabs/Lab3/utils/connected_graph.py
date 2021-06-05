from utils.graph import Graph, GraphRepresentationType
from utils.degree_sequence import is_degree_sequence, generate_graph_from_degree_sequence

from random import randrange


def create_tree(vertexes):
	vertex_count = len(vertexes.graph_representation)

	for row in range(1, vertex_count):
		column = randrange(0, row)
		vertexes.graph_representation[row][column] = 1
		vertexes.graph_representation[column][row] = 1

	return vertexes


def make_additional_connections(graph):
	connections = sum([sum(row) for row in graph.graph_representation]) / 2
	vertex_count = len(graph.graph_representation)
	max_connections = vertex_count * (vertex_count - 1) / 2

	all_connections = randrange(connections, max_connections)
	needed_connections = all_connections - connections

	while needed_connections:
		row = randrange(0, vertex_count)
		column = randrange(0, vertex_count)
		if row != column and graph.graph_representation[row][column] == 0:
			graph.graph_representation[row][column] = 1
			graph.graph_representation[column][row] = 1
		needed_connections -= 1

	return graph


def generate_connected_graph(max_vertex_count):
	vertex_count = randrange(2, max_vertex_count)
	vertex_degrees = [0 for i in range(max_vertex_count)]

	return make_additional_connections(create_tree(generate_graph_from_degree_sequence(vertex_degrees)))
