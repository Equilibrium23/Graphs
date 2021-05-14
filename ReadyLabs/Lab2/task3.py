import sys

from matplotlib.pyplot import viridis
sys.path.append('../')
from Lab1.utils.graph import Graph
from Lab1.utils.plot import plot_graph
from Lab1.utils.handleInput import *
from Lab1.utils.graphRandomizer import *

def find_connected_components(G: Graph):
    old_representation = G.representation_type
    graph.change_graph_representation_to(GraphRepresentationType.ADJACENCY_LIST)

    comp = components(graph)
    number_of_connected_components = max(comp)
    connected_components_list = []
    for i in range(number_of_connected_components):
        connected_components_list.append([])
        for j in range(len(G.graph_representation)):
            if(i + 1 == comp[j]):
                connected_components_list[i].append(j)

    for i in range(len(connected_components_list)):
        temp_str = f"{i + 1}: "
        for c in connected_components_list[i]:
            temp_str = temp_str + f"{c} "
        print(temp_str)

    plot_graph(graph, comp)

    G.change_graph_representation_to(old_representation)


def get_number_of_connected_components(G: Graph):
    return max(components(G))


def _components_R(nr, v, G, comp):
    for u in range(len(G.graph_representation[v])):
        node = G.graph_representation[v][u]
        if(comp[node] == -1):
            comp[node] = nr
            _components_R(nr, node, G, comp)
        

def components(G: Graph):
    if(G.representation_type != GraphRepresentationType.ADJACENCY_LIST):
        raise Exception('representation_type must be: ADJACENCY_LIST')
    nr = 0
    comp = []
    for node in range(len(G.graph_representation)):
        comp.append(-1)
    for v in range(len(G.graph_representation)):
        if(comp[v] == -1):
            nr = nr + 1
            comp[v] = nr
            _components_R(nr, v, G, comp)

    return comp


if __name__ == "__main__":


    #graph = generate_Gnl_graph(5, 6)
    graph = generate_Gnp_graph(10, 0.2)

    graph.change_graph_representation_to(GraphRepresentationType.ADJACENCY_LIST)
    graph.print_graph_representation()
    
    find_connected_components(graph)