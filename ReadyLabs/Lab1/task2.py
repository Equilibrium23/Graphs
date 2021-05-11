from utils.handleInput import check_type_of_input, BadInputException, parse_graph_input
from utils.graph import Graph
from utils.plot import plot_graph

if __name__ == "__main__":
    with open ('input/input.txt', 'r') as graph_input:
        try:
            graph_input = graph_input.readlines()
            input_type = check_type_of_input(graph_input)
            parsed_graph_input = parse_graph_input(input_type, graph_input)

            graph = Graph(input_type, parsed_graph_input)
            plot_graph(graph)

        except BadInputException:
            print(BadInputException)