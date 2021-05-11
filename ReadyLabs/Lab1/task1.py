from utils.handleInput import check_type_of_input, parse_graph_input
from utils.graph import Graph,GraphRepresentationType
from utils.graphRandomizer import generate_Gnl_graph

if __name__ == "__main__":
    with open ('input/input.txt', 'r') as graph_input:
        graph_input = graph_input.readlines()
        representation_type = check_type_of_input(graph_input)
        parsed_graph_input = parse_graph_input(representation_type, graph_input)

        graph = Graph(representation_type, parsed_graph_input)
        graph.print_graph_representation()

        menu = '''
1. Change to ADJACENCY_LIST
2. Change to ADJACENCY_MATRIX
3. Change to INCIDENCE_MATRIX
4. EXIT
Your choice : '''
        while True:
            print(menu)
            choice = int(input())
            if 1 <= choice <= 3 :
                graph.change_graph_representation_to(GraphRepresentationType(choice))
            elif choice == 4:
                break
            else:
                print("Bad input, try again !")
                continue
            graph.print_graph_representation()

