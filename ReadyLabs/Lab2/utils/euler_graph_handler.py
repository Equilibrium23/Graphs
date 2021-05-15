import sys
sys.path.append('../')
from Lab1.utils.graph import Graph
from Lab1.utils.plot import plot_graph
from Lab1.utils.graphRandomizer import *
from utils.graphic_string import is_graphic_string, generate_graph_from_graphic_string
from utils.if_eulerian_graph import check_if_eulerian

from random import randrange

def generate_vertex_degrees(vertex_count, step = 2):
	vertex_degrees = []

	for i in range(vertex_count):
		vertex_degrees.append(randrange(step, vertex_count, step))

	return vertex_degrees

def generate_graphic_string(vertex_count):
	vertex_degrees = generate_vertex_degrees(vertex_count)

	while is_graphic_string(vertex_degrees) is False:
		vertex_degrees = generate_vertex_degrees(vertex_count)

	return vertex_degrees

def generate_random_eulerian_graph(min, max):
	vertex_count = randrange(min, max)
	vertex_degrees = generate_graphic_string(vertex_count)

	return generate_graph_from_graphic_string(vertex_degrees)