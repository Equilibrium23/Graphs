from handleInput import check_type_of_input, BadInputException
from graph import Graph

if __name__ == "__main__":
    with open ('input/input.txt', 'r') as graph_input:
        try:
            graph_input = graph_input.readlines()
            input_type = check_type_of_input(graph_input)
            graph = Graph.create_graph_representation(input_type, graph_input)
            
            print("INPUT:")
            graph.print_graph_representation()

            graph.change_graph_representation_to("incidence_matrix")
            input()

            print("AM <-> IM:")   
            graph.print_graph_representation()         
            graph.change_graph_representation_to("adjacency_matrix")
            graph.print_graph_representation()
            graph.change_graph_representation_to("incidence_matrix")
            graph.print_graph_representation()  
            input()

            print("IM <-> AL:")   
            graph.print_graph_representation()     
            graph.change_graph_representation_to("adjacency_list")
            graph.print_graph_representation()
            graph.change_graph_representation_to("incidence_matrix")
            graph.print_graph_representation() 

            graph.change_graph_representation_to("adjacency_matrix")
            input()

            print("AM <-> AL:")   
            graph.print_graph_representation()
            graph.change_graph_representation_to("adjacency_list")
            graph.print_graph_representation()
            graph.change_graph_representation_to("adjacency_matrix")
            graph.print_graph_representation()

        except BadInputException:
            print(BadInputException)