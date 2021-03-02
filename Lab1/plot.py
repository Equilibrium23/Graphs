import matplotlib.pyplot as plt
from math import sin, cos, radians
from graph import Graph

def plot_graph(graph):
    graph.change_to_adjacency_list()
    radius = 6
    circle = plt.Circle((0, 0), radius, color='red', linestyle='--', fill=False)

    fig, ax = plt.subplots()
    ax.set_xlim((-10, 10))
    ax.set_ylim((-10, 10))
    ax.add_patch(circle)

    number_of_nodes = len(graph.graph_representation)
    for count, node in enumerate(graph.graph_representation):
        x = radius*cos(radians((count/number_of_nodes*360)))
        y = radius*sin(radians((count/number_of_nodes*360)))
        
        for neighbor in graph.graph_representation[count]:
            x2 = radius*cos(radians(((neighbor-1)/number_of_nodes*360)))
            y2 = radius*sin(radians(((neighbor-1)/number_of_nodes*360)))
            ax.plot([x, x2], [y, y2])

        node_circle = plt.Circle((x, y), 0.5, color='orange')
        ax.text(x - 0.2, y - 0.2, f'{count+1}')
        ax.add_patch(node_circle)
    
    plt.show()
