import sys
sys.path.append('../')
from Lab1.graph import Graph
from Lab1.plot import plot_graph
from Lab1.graphRandomizer import *
from Lab1.handleInput import *
from task2_2 import get_number_of_connected_components

import copy
import random


def check_if_euler(G: Graph):
    old_representation_type = G.representation_type
    G.change_graph_representation_to("adjacency_list")

    old_graph_representation = copy.deepcopy(G.graph_representation)

    starting_vertex = 1

    if(len(G.graph_representation[starting_vertex - 1]) == 0):

        for l in G.graph_representation:    # jezeli jakis wierzcholek jest odosobniony
            if(len(l) == 0):
                return False

        if(len(G.graph_representation) == 1):
            return True
        else:
            return False

    last_vertex = choose_edge_and_delete(G, starting_vertex)

    is_euler_graph = last_vertex == starting_vertex and check_if_graph_has_no_edges(G)

    G.graph_representation = old_graph_representation
    G.change_graph_representation_to(old_representation_type)

    return is_euler_graph


def check_if_edge_is_bridge(G: Graph, vertex1: int, vertex2: int):
    assert G.representation_type == "adjacency_list"
    prev_number_of_connected_components = get_number_of_connected_components(G)

    delete_edge(G, vertex1, vertex2)
    curr_number_of_connected_components = get_number_of_connected_components(G)
    add_edge(G, vertex1, vertex2)

    if(curr_number_of_connected_components>prev_number_of_connected_components):
        return True
    else:
        return False


def check_if_graph_has_no_edges(G: Graph):
    assert G.representation_type == "adjacency_list"
    for n in G.graph_representation:
        if(len(n)>0):
            return False
    return True


def choose_edge_and_delete(G: Graph, curr_vertex: int):
    gr = G.graph_representation

    if(len(gr[curr_vertex - 1]) == 0):
        return curr_vertex
    else:
        for i in range(len(gr[curr_vertex - 1])):
            vert = gr[curr_vertex - 1][i]
            if(not(check_if_edge_is_bridge(G, curr_vertex, vert) and i!=len(gr[curr_vertex - 1])-1)):
                delete_edge(G, curr_vertex, vert)
                #print(f"Usuwam: {curr_vertex}, {vert}")
                return choose_edge_and_delete(G, vert)


def delete_edge(G: Graph, vertex1: int, vertex2: int):
    assert G.representation_type == "adjacency_list"
    assert vertex2 in G.graph_representation[vertex1-1]
    assert vertex1 in G.graph_representation[vertex2-1]
    G.graph_representation[vertex1-1].remove(vertex2)
    G.graph_representation[vertex2-1].remove(vertex1)

    
def add_edge(G: Graph, vertex1: int, vertex2: int):
    assert G.representation_type == "adjacency_list"
    G.graph_representation[vertex1-1].append(vertex2)
    G.graph_representation[vertex1-1].sort()
    G.graph_representation[vertex2-1].append(vertex1)
    G.graph_representation[vertex2-1].sort()



if __name__ == "__main__":

    #examples
    
    graph_input = [ "0 1 1 1 1",
                    "1 0 1 0 0",
                    "1 1 0 0 0",
                    "1 0 0 0 1",
                    "1 0 0 1 0"]

    input_type = check_type_of_input(graph_input)
    graph = Graph.create_graph_representation(input_type, graph_input)


    graph = generate_Gnl_graph(6, 10)
    
    graph.change_graph_representation_to("adjacency_list")
    
    graph.print_graph_representation()

    
    if_euler = check_if_euler(graph)
    print(f"Czy graf jest eulerowski: {if_euler}")


    if(if_euler):
        plot_graph(graph)

    
    





