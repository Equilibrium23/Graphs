import matplotlib.pyplot as plt
from math import sin, cos, radians
from .graph import Graph, GraphRepresentationType
from random import random
from .input import Point, read_input

def plot_graph(graph, labels = [], save = False):     # aby kolory dla etykiet zadzialaly trzeba podac tablice z etykietami (1,2,3...), ktora ma taki sam rozmiar jak ilosc wierzcholkow
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
    
    graph.change_graph_representation_to(GraphRepresentationType.ADJACENCY_MATRIX)
    if(save):
        plt.savefig("input.png")
    else:
        plt.show()

def plot_tsp(filename, cycle, save=False):
    points = read_input(filename)

    list_x = [point.x for point in points]
    list_y = [point.y for point in points]
    list.sort(list_x)
    list.sort(list_y)
    fig, ax = plt.subplots()
    ax.set_xlim((list_x[0] - 5, list_x[len(points)-1] + 5))
    ax.set_ylim((list_y[0] - 5, list_y[len(points)-1] + 5))
    plt.axis('off')
    for point in points:
        node_circle = plt.Circle((point.x, point.y), 1.5)
        ax.add_patch(node_circle)

    for i in range(len(cycle)-1):
        ax.plot([points[cycle[i]].x, points[cycle[i+1]].x],
                [points[cycle[i]].y, points[cycle[i+1]].y],
                color='red')

    if(save):
        plt.savefig(filename.split('.')[0] + ".png")
    else:
        plt.show()
