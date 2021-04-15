import sys
sys.path.append('../')
from Lab1.graph import Graph
from Lab1.plot import plot_graph
from Lab1.graphRandomizer import *
from Lab1.handleInput import *
from task2 import is_graphic_string, generate_graph_from_graphic_string

from random import randrange

def compute_max_connections(vertex_count):
	if vertex_count % 2:
		return vertex_count
	else:
		return vertex_count + 1 

def generate_vertex_degrees(vertex_count):
	vertex_degrees = []

	for i in range(vertex_count):
		vertex_degrees.append(randrange(2, compute_max_connections(vertex_count), 2))

	return vertex_degrees

def generate_graphic_string(vertex_count):
	vertex_degrees = generate_vertex_degrees(vertex_count)

	while is_graphic_string(vertex_degrees.copy()) is False:
		vertex_degrees = generate_vertex_degrees(vertex_count)

	return vertex_degrees

def generate_random_eulerian_graph():
	vertex_count = randrange(3, 10)
	vertex_degrees = generate_graphic_string(vertex_count)

	return generate_graph_from_graphic_string(vertex_degrees)

def main():
	plot_graph(generate_random_eulerian_graph())

if __name__ == "__main__":
	main()