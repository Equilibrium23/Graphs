from handleInput import check_type_of_input, BadInputException
from graph import Graph

if __name__ == "__main__":
    with open ('input/input.txt','r') as graph_input:
        try:
            graph_input = graph_input.readlines()
            input_type = check_type_of_input(graph_input)
            graph = Graph.create_graph_representation(input_type,graph_input)
            graph.change_graph_representation("adjacency_matrix")
        except BadInputException:
            print(BadInputException)