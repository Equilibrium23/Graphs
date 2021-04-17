import matplotlib.pyplot as plt
from math import sin, cos, radians
from graph import Graph
from random import random

def plot_graph(graph, labels = []):     # aby kolory dla etykiet zadzialaly trzeba podac tablice z etykietami (1,2,3...), ktora ma taki sam rozmiar jak ilosc wierzcholkow
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

    for count, node in enumerate(graph.graph_representation):
        x = radius*cos(radians((count/number_of_nodes*360)))
        y = radius*sin(radians((count/number_of_nodes*360)))
        
        for neighbor in graph.graph_representation[count]:
            x2 = radius*cos(radians(((neighbor-1)/number_of_nodes*360)))
            y2 = radius*sin(radians(((neighbor-1)/number_of_nodes*360)))
            ax.plot([x, x2], [y, y2], color='gray')

        if(len(labels) == number_of_nodes):
            color_index = labels[count] - 1
        else:
            color_index = 0
    
        node_circle = plt.Circle((x, y), 0.5, color=node_color[color_index])
        ax.text(x - 0.2, y - 0.2, f'{count+1}')
        ax.add_patch(node_circle)
    
    plt.show()
