from utils.graph import Graph
from utils.plot import plot_graph
from utils.handleInput import *
from utils.graph_randomizer import *
from utils.connected_components import get_number_of_connected_components

import copy
import random


def check_if_eulerian(G: Graph):
    old_representation_type = G.representation_type
    G.change_graph_representation_to(GraphRepresentationType.ADJACENCY_LIST)

    old_graph_representation = copy.deepcopy(G.graph_representation)

    starting_vertex = 0

    path = []

    if(len(G.graph_representation) == 1):               # graf składa się z jednego wierzchołka
        return True, path
    else:
        for key, l in G.graph_representation.items():    # jezeli jakis wierzcholek jest odosobniony
            if(len(l) == 0):
                return False, path

    
    last_vertex = choose_edge_and_delete(G, starting_vertex, path)

    is_eulerian_graph = last_vertex == starting_vertex and check_if_graph_has_no_edges(G)

    G.graph_representation = old_graph_representation
    G.change_graph_representation_to(old_representation_type)

    return is_eulerian_graph, path


def check_if_edge_is_bridge(G: Graph, vertex1: int, vertex2: int):
    assert G.representation_type.value == GraphRepresentationType.ADJACENCY_LIST.value
    prev_number_of_connected_components = get_number_of_connected_components(G)

    delete_edge(G, vertex1, vertex2)
    curr_number_of_connected_components = get_number_of_connected_components(G)
    add_edge(G, vertex1, vertex2)

    if(curr_number_of_connected_components>prev_number_of_connected_components):
        return True
    else:
        return False


def check_if_graph_has_no_edges(G: Graph):
    assert G.representation_type.value == GraphRepresentationType.ADJACENCY_LIST.value
    for key, n in G.graph_representation.items():
        if(len(n)>0):
            return False
    return True


def choose_edge_and_delete(G: Graph, curr_vertex: int, path):
    gr = G.graph_representation

    if(len(gr[curr_vertex]) == 0):
        return curr_vertex
    else:
        for i in range(len(gr[curr_vertex])):
            vert = gr[curr_vertex][i]
            if(not(check_if_edge_is_bridge(G, curr_vertex, vert) and i!=len(gr[curr_vertex])-1)):
                #print(f"Usuwam: {curr_vertex}, {vert}")
                #path.append(vert)
                path.append([curr_vertex, vert])
                delete_edge(G, curr_vertex, vert)
                return choose_edge_and_delete(G, vert, path)


def delete_edge(G: Graph, vertex1: int, vertex2: int):
    assert G.representation_type.value == GraphRepresentationType.ADJACENCY_LIST.value
    assert vertex2 in G.graph_representation[vertex1]
    assert vertex1 in G.graph_representation[vertex2]
    G.graph_representation[vertex1].remove(vertex2)
    G.graph_representation[vertex2].remove(vertex1)

    
def add_edge(G: Graph, vertex1: int, vertex2: int):
    assert G.representation_type.value == GraphRepresentationType.ADJACENCY_LIST.value
    G.graph_representation[vertex1].append(vertex2)
    G.graph_representation[vertex1].sort()
    G.graph_representation[vertex2].append(vertex1)
    G.graph_representation[vertex2].sort()



if __name__ == "__main__":

    #examples
    
    graph_input = [ "0 1 1 1 1",
                    "1 0 1 0 0",
                    "1 1 0 0 0",
                    "1 0 0 0 1",
                    "1 0 0 1 0"]

    graph_input2 = ["0. 2 4",
                    "1. ",
                    "2. 0 4",
                    "3. ",
                    "4. 0 2"]

    graph_input = graph_input2

    representation_type = check_type_of_input(graph_input)
    parsed_graph_input = parse_graph_input(representation_type, graph_input)

    graph = Graph(representation_type, parsed_graph_input)
    delete_edge(graph, 1, 3)

    graph = generate_Gnp_graph(5, 0.5)
    
    graph.change_graph_representation_to(GraphRepresentationType.ADJACENCY_LIST)
    
    graph.print_graph_representation()



    
    if_eulerian = check_if_eulerian(graph)
    print(f"Czy graf jest eulerowski: {if_eulerian}")

    if(if_eulerian):
        plot_graph(graph)

    findEulerianGraph = False

    if(findEulerianGraph):
        while not check_if_eulerian(graph):
            graph = generate_Gnp_graph(7, 0.4)

        graph.change_graph_representation_to(GraphRepresentationType.ADJACENCY_LIST)
        graph.print_graph_representation()
        if_eulerian = check_if_eulerian(graph)
        print(f"Czy graf jest eulerowski: {if_eulerian}")
        plot_graph(graph)

    
    





