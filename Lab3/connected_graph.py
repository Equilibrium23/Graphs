import sys
sys.path.append('../')
from Lab1.graph import Graph
from Lab1.plot import plot_graph
from Lab2.task2 import is_graphic_string, generate_graph_from_graphic_string

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


def _generate_connected_graph(max_vertex_count):
	vertex_count = randrange(2, max_vertex_count)
	vertex_degrees = [0 for i in range(max_vertex_count)]

	return make_additional_connections(create_tree(generate_graph_from_graphic_string(vertex_degrees)))


def add_connection_weights(graph, min, max):
	graph.change_graph_representation_to("adjacency_matrix")
	nodes_count = len(graph.graph_representation)
	
	for row in range(nodes_count):
		for column in range(row + 1, nodes_count):
			if(graph.graph_representation[row][column]):
				weight = randrange(min, max)
				graph.graph_representation[row][column] = weight
				graph.graph_representation[column][row] = weight


def generate_connected_graph(max_vertex_count, min_weight, max_weight):
	graph = _generate_connected_graph(max_vertex_count)
	plot_graph(graph)
	add_connection_weights(graph, min_weight, max_weight)
	graph.print_graph_representation()


if __name__ == "__main__":
	generate_connected_graph(5, 1, 10)