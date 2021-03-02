from handleInput import check_type_of_input, BadInputException
from graph import Graph

if __name__ == "__main__":
    with open ('input/input.txt', 'r') as graph_input:
        try:
            graph_input = graph_input.readlines()
            input_type = check_type_of_input(graph_input)
            graph = Graph.create_graph_representation(input_type, graph_input)
            graph.print_graph_representation()
            graph.change_graph_representation_to("adjacency_matrix")
            graph.print_graph_representation()
            graph.change_graph_representation_to("adjacency_list")
            graph.print_graph_representation()
        except BadInputException:
            print(BadInputException)