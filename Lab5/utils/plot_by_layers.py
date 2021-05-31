import matplotlib.pyplot as plt
from math import sin, cos, radians
from random import random
import math

from .graph import Graph, GraphRepresentationType

def _get_offsets(index, layer_numbers, number_of_nodes_in_layer):
    layer = layer_numbers[index]
    x = layer - 1
    y = 0
    for i in range(layer):
        y = y+number_of_nodes_in_layer[i]
    y = index - y

    return x, y

def plot_digraph_by_layers(digraph, f_FF = []):
    if len(digraph.layer_numbers) == 0:
        raise Exception('W grafie nie ma numerow warstw!!!')

    layer_numbers = digraph.layer_numbers 

    graph = Graph(GraphRepresentationType.DIGRAF_ADJACENCY_MATRIX, digraph.graph_representation.copy())
    graph.layer_numbers = digraph.layer_numbers.copy()
    graph.change_to_adjacency_list()
    graph.graph_weights = digraph.graph_weights.copy()
    radius = 9.5
    #graph.print_graph_representation()

    fig, ax = plt.subplots()
    ax.set_xlim((-10, 10))
    ax.set_ylim((-10, 10))
    plt.axis('off')

    number_of_nodes = len(graph.graph_representation)

    number_of_layers = max(layer_numbers) + 1
    X_layer_offset = []
    positon_of_first_layer = -9.5
    for i in range(number_of_layers):
        X_layer_offset.append((2*9.5)/(number_of_layers - 1))


    number_of_nodes_in_layer = []
    for i in range(number_of_layers):
        number_of_nodes_in_layer.append(layer_numbers.count(i))
    #print(number_of_nodes_in_layer)

    layer_offset = []
    positon_of_first_node_in_layer = []
    for i in range(number_of_layers):
        if(number_of_nodes_in_layer[i] == 1):
            layer_offset.append(9.5)
            positon_of_first_node_in_layer.append(0)
        if(number_of_nodes_in_layer[i] == 2):
            layer_offset.append((2*9.5)/2)
            positon_of_first_node_in_layer.append(-(2*9.5)/4)
        if(number_of_nodes_in_layer[i] >= 3):
            layer_offset.append((2*9.5)/(number_of_nodes_in_layer[i]-1))
            positon_of_first_node_in_layer.append(-9.5)
    #print(layer_offset)

    for count, node in graph.graph_representation.items():

        layer_0 = layer_numbers[count] 
        x, y = _get_offsets(count, layer_numbers, number_of_nodes_in_layer)

        x_Pos = positon_of_first_layer + layer_0 * X_layer_offset[layer_0]
        y_Pos = positon_of_first_node_in_layer[layer_0] + y * layer_offset[layer_0]

        node_circle = plt.Circle((x_Pos, y_Pos), 0.5, color='lightgreen')
        ax.text(x_Pos + x_Pos*0.2,  y_Pos +  y_Pos*0.2, f'{count}')
        ax.add_patch(node_circle)

	#plot arrows
    for count, node in graph.graph_representation.items():

        layer_0 = layer_numbers[count] 
        x, y = _get_offsets(count, layer_numbers, number_of_nodes_in_layer)

        x_Pos = positon_of_first_layer + layer_0 * X_layer_offset[layer_0]
        y_Pos = positon_of_first_node_in_layer[layer_0] + y * layer_offset[layer_0]

        for neighbor in graph.graph_representation[count]:
            second_layer_0 = layer_numbers[neighbor] 
            x2, y2 = _get_offsets(neighbor, layer_numbers, number_of_nodes_in_layer)

            x_Pos2 = positon_of_first_layer + second_layer_0 * X_layer_offset[second_layer_0]
            y_Pos2 = positon_of_first_node_in_layer[second_layer_0] + y2 * layer_offset[second_layer_0]

            # strzlki z kolorami gdy podano f_FF ( dla zad 2 zestaw 5 )
            if(len(f_FF) and f_FF[count][neighbor] == 0):
                plt.arrow(x_Pos, y_Pos, x_Pos2 - x_Pos, y_Pos2 - y_Pos, width = 0.05, length_includes_head = True, head_width = 0.3, color = 'grey')
            else:
                plt.arrow(x_Pos, y_Pos, x_Pos2 - x_Pos, y_Pos2 - y_Pos, width = 0.05, length_includes_head = True, head_width = 0.3)

            # wagi krawedzi
            direction = [x_Pos2 - x_Pos, y_Pos2 - y_Pos]
            length = math.sqrt(direction[0]**2 + direction[1]**2)
            direction[0] = direction[0]/length
            direction[1] = direction[1]/length

            distance = 1.5
            strToDraw = str(graph.graph_weights[count][neighbor])
            if(len(f_FF)):  #
                strToDraw = str(f_FF[count][neighbor]) + '/' + strToDraw
            ax.text(x_Pos + direction[0]*distance,  y_Pos +  direction[1]*distance + 0.2, strToDraw, color = 'red')

    plt.show()