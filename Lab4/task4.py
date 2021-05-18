from utils.handleInput import parse_graph_input
from utils.graph import Graph,GraphRepresentationType
from utils.graphRandomizer import generate_strongly_connected_digraph
from utils.johnson import johnson

def print_distance_matrix(D: list):
    print("\nMacierz odleglosci:")

    for i in range(len(D)):
        for j in range(len(D[i])):
            print('{:>6}'.format(D[i][j]), end='')
        print()

if __name__ == "__main__":
    digraph = generate_strongly_connected_digraph(4, 0.2)
    digraph.add_connection_weights(-5, 10)
    digraph.print_graph_representation()
    digraph.print_weights()
    D = johnson(digraph)
    print_distance_matrix(D)