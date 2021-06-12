import matplotlib.pyplot as plt
from math import sin, cos, radians
from .graph import Graph, GraphRepresentationType
from random import random

def plot_graph(graph, labels = []):     # aby kolory dla etykiet zadzialaly trzeba podac tablice z etykietami (1,2,3...), ktora ma taki sam rozmiar jak ilosc wierzcholkow
    graph.change_graph_representation_to(GraphRepresentationType.ADJACENCY_LIST)
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
            ax.plot([x, x2], [y, y2], color='gray')

        if(len(labels) == number_of_nodes):
            color_index = labels[count] - 1
        else:
            color_index = 0
    
        node_circle = plt.Circle((x, y), 0.5, color=node_color[color_index])
        ax.text(x - 0.2, y - 0.2, f'{count}')
        ax.add_patch(node_circle)
    
    plt.show()

from math import sqrt

def plot_minimum_spanning_tree_road(graph, minimum_spanning_tree_road):
	other_color_vertices = set()
	for edge in minimum_spanning_tree_road:
		other_color_vertices.add(edge[0])
		other_color_vertices.add(edge[1])

	radius = 6

	fig, ax = plt.subplots()
	ax.set_xlim((-10, 10))
	ax.set_ylim((-10, 10))
	plt.axis('off')

	number_of_nodes = len(graph.graph_representation)

	node_color = ['lightgreen', 'yellow']
	color_index = 0

	for count in range(len(graph.graph_representation)):
		x = radius*cos(radians((count/number_of_nodes*360)))
		y = radius*sin(radians((count/number_of_nodes*360)))

		if(count in other_color_vertices):
			color_index = 1
		else:
			color_index = 0
	
		node_circle = plt.Circle((x, y), 0.5, color=node_color[color_index])
		ax.text(x + x*0.2, y + y*0.2, f'{count+1}')
		ax.add_patch(node_circle)

	#plot arrows
	for count, adj in enumerate(graph.graph_representation):
		x = radius*cos(radians((count/float(number_of_nodes)*360)))
		y = radius*sin(radians((count/float(number_of_nodes)*360)))
		for count2, neighbor in enumerate(adj):
			if neighbor == 1:
				x2 = radius*cos(radians(((count2)/float(number_of_nodes)*360)))
				y2 = radius*sin(radians(((count2)/float(number_of_nodes)*360)))
				if [count,count2] in minimum_spanning_tree_road or [count2, count] in minimum_spanning_tree_road:
					plt.arrow(x, y, x2 - x, y2 - y, width = 0.05, length_includes_head = True, head_width = 0.3, edgecolor='yellow')
				else:
					plt.arrow(x, y, x2 - x, y2 - y, width = 0.05, length_includes_head = True, head_width = 0.3)

				# wagi krawedzi
				direction = [x2-x, y2-y]
				length = sqrt(direction[0]**2 + direction[1]**2)
				direction[0] = direction[0]/length
				direction[1] = direction[1]/length

				distance = 1.5
				strToDraw = str(graph.graph_weights[count][count2])
				ax.text(x + direction[0]*distance,  y +  direction[1]*distance + 0.2, strToDraw, color = 'red')

	plt.show()