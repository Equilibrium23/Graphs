from .graph import Graph, GraphRepresentationType

from random import randrange


def generate_layers(N):
	layers_sizes = [randrange(2, N + 1) for i in range(N)]
	return layers_sizes


def connect_first_layer(graph, layer_size):
	for i in range(1, layer_size + 1):
		graph.graph_representation[0][i] = 1

	return layer_size, layer_size


def connect_last_layer(graph, layer_size):
	vertex_count = len(graph.graph_representation)
	for i in range(1, layer_size + 1):
		graph.graph_representation[vertex_count - i - 1][vertex_count - 1] = 1


def connect_layers(graph, layer_size, last_connected, prior_layer_size):
	for i in range(last_connected + 1, layer_size + last_connected + 1):
		j = randrange(last_connected - prior_layer_size + 1, last_connected + 1)
		graph.graph_representation[j][i] = 1
	for j in range(last_connected - prior_layer_size + 1, last_connected + 1):
		i = randrange(last_connected + 1, layer_size + last_connected + 1)
		graph.graph_representation[j][i] = 1


def make_base_connections(graph, layers_sizes):
	last_connected, prior_layer_size = connect_first_layer(graph, layers_sizes[0])

	for i in range(1, len(layers_sizes)):
		connect_layers(graph, layers_sizes[i], last_connected, prior_layer_size)
		prior_layer_size = layers_sizes[i]
		last_connected += layers_sizes[i]

	connect_last_layer(graph, layers_sizes[len(layers_sizes) - 1])

	return graph


def generate_base_network(layers_sizes):
	vertex_count = sum(layers_sizes) + 2
	graph = Graph(GraphRepresentationType.DIGRAF_ADJACENCY_MATRIX, [])
	graph.graph_representation = [[0 for i in range(vertex_count)] for j in range(vertex_count)]

	return make_base_connections(graph, layers_sizes)


def is_connection_legal(graph, i, j):
	return graph.graph_representation[i][j] == 0 and graph.graph_representation[j][i] == 0


def black_box():
	return randrange(1, 15) % 2


def add_one_connection(graph, N):
	vertex_count = len(graph.graph_representation) - 2
	i = randrange(1, vertex_count + 1)
	j = randrange(1, vertex_count + 1)
	if(i != j and is_connection_legal(graph, i, j)):
		if(black_box()):
			graph.graph_representation[i][j] = 1
		else:
			graph.graph_representation[j][i] = 1
		return True
	return False


def make_additional_connections(network, N):
	needed_connections = N
	while(needed_connections > 0):
		if(add_one_connection(network, N)):
			needed_connections -= 1
	
	return network


def add_layers(graph, layers_sizes):
	layer_numbers = []
	layer_numbers.append(0)
	for i in range(len(layers_sizes)):
		for j in range(layers_sizes[i]):
			layer_numbers.append(i + 1)
	layer_numbers.append(max(layer_numbers) + 1)
	graph.layer_numbers = layer_numbers


def generate_network(N : int):
	layers_sizes = generate_layers(N)
	graph = generate_base_network(layers_sizes)
	graph = make_additional_connections(graph, N)
	add_layers(graph, layers_sizes)

	return graph


def generate_network_with_weights(N, min, max):
	network = generate_network(N)
	network.add_connection_weights(1, 10)

	return network