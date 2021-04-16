import sys
sys.path.append('../')
from Lab1.graph import Graph
from Lab1.plot import plot_graph
from Lab1.handleInput import *

def find_connected_components(G: Graph):
    old_representation = G.representation_type
    G.change_graph_representation_to("adjacency_list")

    comp = components(graph)
    number_of_connected_components = max(comp)
    connected_components_list = []
    for i in range(number_of_connected_components):
        connected_components_list.append([])
        for j in range(len(G.graph_representation)):
            if(i + 1 == comp[j]):
                connected_components_list[i].append(j + 1)

    for i in range(len(connected_components_list)):
        temp_str = f"{i + 1}: "
        for c in connected_components_list[i]:
            temp_str = temp_str + f"{c} "
        print(temp_str)

    plot_graph(graph, comp)

    G.change_graph_representation_to(old_representation)


def get_number_of_connected_components(G: Graph):
    return max(components(G))


def components_R(nr, v, G, comp):
    for u in range(len(G.graph_representation[v])):
        node = G.graph_representation[v][u]
        if(comp[node - 1] == -1):
            comp[node - 1] = nr
            components_R(nr, node - 1, G, comp)
        

def components(G: Graph):
    nr = 0
    comp = []
    for node in range(len(G.graph_representation)):
        comp.append(-1)
    for v in range(len(G.graph_representation)):
        if(comp[v] == -1):
            nr = nr + 1
            comp[v] = nr
            components_R(nr, v, G, comp)

    return comp


if __name__ == "__main__":

    #examples
    graph_input1 = [ "0 1 0 0 1 1 0 0 0 0 0 0",
                    "1 0 1 0 0 1 0 0 0 0 0 0",
                    "0 1 0 1 1 0 0 0 0 0 0 1",
                    "0 0 1 0 0 0 0 1 1 0 1 0",
                    "1 0 1 0 0 0 1 0 1 0 0 0",
                    "1 1 0 0 0 0 1 0 0 0 0 0",
                    "0 0 0 0 1 1 0 1 0 0 0 0",
                    "0 0 0 1 0 0 1 0 1 0 0 1",
                    "0 0 0 1 1 0 0 1 0 1 0 0",
                    "0 0 0 0 0 0 0 0 1 0 0 0",
                    "0 0 0 1 0 0 0 0 0 0 0 0",
                    "0 0 1 0 0 0 0 1 0 0 0 0"]

    graph_input2 = [ "1. 2 5 6",
                    "2. 1 3 6",
                    "3. 2 4 5 12",
                    "4. 3 8 9",
                    "5. 1 3 7 9",
                    "6. 1 2 7",
                    "7. 5 6 8",
                    "8. 4 7 9 12",
                    "9. 4 5 8",
                    "10. 11",
                    "11. 10",
                    "12. 3 8",
                    "13. 16 17",
                    "14. 15 17",
                    "15. 14 16 17",
                    "16. 13 15",
                    "17. 13 14 15"]

    graph_input3 = [ "0 0 0 0 0 0 0 0 0 0 0 0",
                    "0 0 0 0 0 0 0 0 0 0 0 0",
                    "0 0 0 0 0 0 0 0 0 0 0 0",
                    "0 0 0 0 0 0 0 0 0 0 0 0",
                    "0 0 0 0 0 0 0 0 0 0 0 0",
                    "0 0 0 0 0 0 0 0 0 0 0 0",
                    "0 0 0 0 0 0 0 0 0 0 0 0",
                    "0 0 0 0 0 0 0 0 0 0 0 0",
                    "0 0 0 0 0 0 0 0 0 0 0 0",
                    "0 0 0 0 0 0 0 0 0 0 0 0",
                    "0 0 0 0 0 0 0 0 0 0 0 0",
                    "0 0 0 0 0 0 0 0 0 0 0 0"]

 
    graph_input = graph_input2


    input_type = check_type_of_input(graph_input)
    graph = Graph.create_graph_representation(input_type, graph_input)

    find_connected_components(graph)





