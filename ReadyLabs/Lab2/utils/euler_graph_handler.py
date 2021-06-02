from utils.graph import Graph
from utils.plot import plot_graph
from utils.graph_randomizer import *
from utils.degree_sequence import is_degree_sequence, generate_graph_from_degree_sequence
from utils.if_eulerian_graph import check_if_eulerian

from random import randrange

def generate_vertex_degrees(vertex_count, step = 2):
	vertex_degrees = []

	for i in range(vertex_count):
		vertex_degrees.append(randrange(step, vertex_count, step))

	return vertex_degrees

def generate_degree_sequence(vertex_count):
	vertex_degrees = generate_vertex_degrees(vertex_count)

	while is_degree_sequence(vertex_degrees) is False:
		vertex_degrees = generate_vertex_degrees(vertex_count)

	return vertex_degrees

def generate_random_eulerian_graph(min, max):
	vertex_count = randrange(min, max)
	vertex_degrees = generate_degree_sequence(vertex_count)

	return generate_graph_from_degree_sequence(vertex_degrees)