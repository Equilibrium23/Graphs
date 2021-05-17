import numpy as np

from random import randrange
from enum import Enum

class GraphRepresentationType(Enum):
	ADJACENCY_LIST = 1
	ADJACENCY_MATRIX = 2
	INCIDENCE_MATRIX = 3
	DIGRAF_ADJACENCY_MATRIX = 4

class Graph:
	def __init__(self, representation_type : GraphRepresentationType, graph_representation):
		self.representation_type = representation_type
		self.graph_representation = graph_representation
		self.graph_weights = []
	
	def change_graph_representation_to(self, new_representation_type : GraphRepresentationType):
		if self.representation_type != new_representation_type and self.representation_type != GraphRepresentationType.DIGRAF_ADJACENCY_MATRIX:
			if new_representation_type == GraphRepresentationType.ADJACENCY_LIST:
				self.change_to_adjacency_list()

			elif new_representation_type == GraphRepresentationType.INCIDENCE_MATRIX:
				self.change_to_incidence_matrix()
				
			else:
				self.change_to_adjacency_matrix()

	def change_to_adjacency_list(self):
		if self.representation_type == GraphRepresentationType.ADJACENCY_MATRIX:
			self.change_to_list_from_adjacency_matrix()

		if self.representation_type == GraphRepresentationType.INCIDENCE_MATRIX:
			self.change_to_list_from_incidence_matrix()

		self.representation_type = GraphRepresentationType.ADJACENCY_LIST

	def change_to_list_from_adjacency_matrix(self):
		neighbors = list()
		row_number = 0
		for row in self.graph_representation:
			neighbors.append(list())
			neighbor = 0
			for node in row:
				if node == 1:
					neighbors[row_number].append(neighbor)
				neighbor = neighbor + 1
			row_number = row_number + 1
		adjacency_list = {vertex:neighbors[vertex] for vertex in range(len(neighbors)) }
		self.graph_representation = adjacency_list

	def change_to_list_from_incidence_matrix(self):
		nodes_count = len(self.graph_representation)
		new_representation = []
		for i in range(nodes_count):
			new_representation.append([])
		edges_count = len(self.graph_representation[0])
		for i in range(nodes_count):
			for j in range(edges_count):
				if(self.graph_representation[i][j]):
					for k in range(nodes_count):
						if(self.graph_representation[k][j] and k != i):
							new_representation[i].append(k)
							break
			new_representation[i].sort()
		neighbors = [list(map(int, line)) for line in new_representation]
		adjacency_list = {vertex:neighbors[vertex] for vertex in range(len(neighbors)) }
		self.graph_representation = adjacency_list 
	
	def change_to_adjacency_matrix(self):
		if self.representation_type == GraphRepresentationType.INCIDENCE_MATRIX:
			self.change_to_adjacency_list()

		if self.representation_type == GraphRepresentationType.ADJACENCY_LIST:
			self.change_to_adjacency_matrix_from_list()

		self.representation_type = GraphRepresentationType.ADJACENCY_MATRIX
		
	def change_to_adjacency_matrix_from_list(self):
		matrix = np.zeros((len(self.graph_representation), len(self.graph_representation)))
		matrix = matrix.astype(int)
		for vertex, neighbors  in self.graph_representation.items():
			for neighbour_vertex in neighbors:
				matrix[vertex][neighbour_vertex] = 1
				matrix[neighbour_vertex][vertex] = 1
		self.graph_representation = matrix


	def change_to_incidence_matrix(self):
		if self.representation_type == GraphRepresentationType.ADJACENCY_LIST:
			self.change_to_adjacency_matrix()

		if self.representation_type == GraphRepresentationType.ADJACENCY_MATRIX:
			self.change_to_incidence_matrix_from_adjacency_matrix()

		self.representation_type = GraphRepresentationType.INCIDENCE_MATRIX
		
	def change_to_incidence_matrix_from_adjacency_matrix(self):
		number_of_edges = 0
		nodes_count = len(self.graph_representation)

		for i in range(nodes_count):
			for j in range(i + 1, nodes_count):
				if(self.graph_representation[i][j]):
					number_of_edges += 1

		new_representation = np.zeros((nodes_count, number_of_edges))
		edge_counter = 0

		for i in range(nodes_count):
			for j in range(i + 1, nodes_count):
				if(self.graph_representation[i][j]):
					new_representation[i][edge_counter] = 1
					new_representation[j][edge_counter] = 1
					edge_counter += 1

		self.graph_representation = [list(map(int,line)) for line in new_representation]

	def print_graph_representation(self):
		print(self.representation_type)
		if self.representation_type == GraphRepresentationType.ADJACENCY_LIST:
			for key,value in self.graph_representation.items():
				print("{}:{}".format(key,value))
		else:
			for row in self.graph_representation:
				for node in row:
					print(node, end = ' ')
				print()
		print()


	def print_weights(self):
		if self.graph_weights:
			print("Weights matrix: ")
			for row in self.graph_weights:
				for weight in row:
					print(weight, end = ' ')
				print()
		else:
			print("Graph has no weights.")


	def add_connection_weights(self, min, max):
		self.change_graph_representation_to(GraphRepresentationType.ADJACENCY_MATRIX)
		nodes_count = len(self.graph_representation)

		self.graph_weights = [[0 for i in range(nodes_count)] for j in range(nodes_count)]
	
		if self.representation_type == GraphRepresentationType.DIGRAF_ADJACENCY_MATRIX:
			for row in range(nodes_count):
				for column in range(nodes_count):
					if(self.graph_representation[row][column]):
						weight = randrange(min, max)
						self.graph_weights[row][column] = weight
		else:
			for row in range(nodes_count):
				for column in range(row + 1, nodes_count):
					if(self.graph_representation[row][column]):
						weight = randrange(min, max)
						self.graph_weights[row][column] = weight
						self.graph_weights[column][row] = weight