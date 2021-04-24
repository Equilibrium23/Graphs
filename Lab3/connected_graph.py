import sys
sys.path.append('../')
from Lab1.graph import Graph
from Lab1.plot import plot_graph
from Lab2.task2 import is_graphic_string, generate_graph_from_graphic_string
from Lab2.euler_graph_handler import generate_vertex_degrees

from random import randrange

def generate_graphic_string(vertex_count):
	vertex_degrees = generate_vertex_degrees(vertex_count, 1)

	while is_graphic_string(vertex_degrees) is False:
		vertex_degrees = generate_vertex_degrees(vertex_count, 1)

	return vertex_degrees

def generate_connected_graph(max_vertex_count):
	vertex_count = randrange(2, max_vertex_count)
	graphic_string = generate_graphic_string(vertex_count)

	return generate_graph_from_graphic_string(graphic_string)

def add_connection_weights(graph, min, max):
	graph.change_graph_representation_to("adjacency_matrix")
	nodes_count = len(graph.graph_representation)
	
	for row in range(nodes_count):
		for column in range(row + 1, nodes_count):
			if(graph.graph_representation[row][column]):
				weight = randrange(min, max)
				graph.graph_representation[row][column] = weight
				graph.graph_representation[column][row] = weight

def main():
	graph = generate_connected_graph(15)
	plot_graph(graph)
	add_connection_weights(graph, 1, 10)
	graph.print_graph_representation()

if __name__ == "__main__":
	main()