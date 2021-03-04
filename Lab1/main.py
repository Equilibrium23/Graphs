from handleInput import check_type_of_input, BadInputException
from graph import Graph
from plot import plot_graph
from graphRandomizer import generate_Gnl_graph, generate_Gnp_graph

if __name__ == "__main__":
    with open ('input/input.txt', 'r') as graph_input:
        try:
            graph_input = graph_input.readlines()
            input_type = check_type_of_input(graph_input)
            graph = Graph.create_graph_representation(input_type, graph_input)
            
            print("INPUT:")
            graph.print_graph_representation()

            graph.change_graph_representation_to("incidence_matrix")

            print("AM <-> IM:")   
            graph.print_graph_representation()         
            graph.change_graph_representation_to("adjacency_matrix")
            graph.print_graph_representation()
            graph.change_graph_representation_to("incidence_matrix")
            graph.print_graph_representation()  


            print("IM <-> AL:")   
            graph.print_graph_representation()     
            graph.change_graph_representation_to("adjacency_list")
            graph.print_graph_representation()
            graph.change_graph_representation_to("incidence_matrix")
            graph.print_graph_representation() 

            graph.change_graph_representation_to("adjacency_matrix")

            print("AM <-> AL:")   
            graph.print_graph_representation()
            graph.change_graph_representation_to("adjacency_list")
            graph.print_graph_representation()
            graph.change_graph_representation_to("adjacency_matrix")
            graph.print_graph_representation()

            plot_graph(graph)

        except BadInputException:
            print(BadInputException)

    print("Generate G(n, l):")
    G_nl = generate_Gnl_graph(6, 10)
    plot_graph(G_nl)

    print("Generate G(n, p):")
    G_np = generate_Gnp_graph(8, 30)
    plot_graph(G_np)