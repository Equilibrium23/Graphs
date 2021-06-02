from matplotlib.pyplot import viridis
from utils.graph import Graph
from utils.plot import plot_graph
from utils.handleInput import *
from utils.graph_randomizer import *
from utils.connected_components import *

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



if __name__ == "__main__":

    graph = generate_Gnp_graph(10, 0.1)

    graph.change_graph_representation_to(GraphRepresentationType.ADJACENCY_LIST)
    graph.print_graph_representation()
    
    find_connected_components(graph)