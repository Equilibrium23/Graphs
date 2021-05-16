from .graph import Graph, GraphRepresentationType

from random import randrange


def generate_layers(N):
	layers_sizes = [randrange(2, N + 1) for i in range(N)]
	return layers_sizes


def make_base_connections(graph, layers_sizes):
	all_vertexes = 0;
	old_layer = 0
	for vertexes in layers_sizes:
		for i in range(vertexes):
			for j in range(old_layer):
				if(i != j):
					graph.graph_representation[i + all_vertexes][j + all_vertexes] = 1
		old_layer = vertexes
		all_vertexes += vertexes
	return graph

def generate_base_network(layers_sizes):
	vertex_count = sum(layers_sizes) + 2
	graph = Graph(GraphRepresentationType.DIGRAF_ADJACENCY_MATRIX, [])
	graph.graph_representation = [[0 for i in range(vertex_count)] for j in range(vertex_count)]

	return make_base_connections(graph, layers_sizes)


def generate_network(N : int):
	layers_sizes = generate_layers(N)
	graph = generate_base_network(layers_sizes)
	
	return graph