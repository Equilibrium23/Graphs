import matplotlib.pyplot as plt
from math import sin, cos, radians
from random import random

from .graph import Graph, GraphRepresentationType


def plot_graph(digraph, labels = []):
	graph = digraph
	graph.change_to_adjacency_list()
	radius = 6

	fig, ax = plt.subplots()
	ax.set_xlim((-10, 10))
	ax.set_ylim((-10, 10))
	plt.axis('off')

	number_of_nodes = len(graph.graph_representation)

	node_color = ['lightgreen']
	color_index = 0
	if(len(labels) == number_of_nodes):
		number_of_labels = max(labels)
		node_color = []
		for i in range(number_of_labels):
			node_color.append([random(), random(), random()])

	for count, node in graph.graph_representation.items():
		x = radius*cos(radians((count/number_of_nodes*360)))
		y = radius*sin(radians((count/number_of_nodes*360)))
		
		for neighbor in graph.graph_representation[count]:
			x2 = radius*cos(radians(((neighbor)/number_of_nodes*360)))
			y2 = radius*sin(radians(((neighbor)/number_of_nodes*360)))
			plt.arrow(x, y, x2 - x, y2 - y, width = 0.05, length_includes_head = True)

		if(len(labels) == number_of_nodes):
			color_index = labels[count] - 1
		else:
			color_index = 0
	
		node_circle = plt.Circle((x, y), 0.5, color=node_color[color_index])
		ax.text(x - 0.2, y - 0.2, f'{count}')
		ax.add_patch(node_circle)
	
	plt.show()