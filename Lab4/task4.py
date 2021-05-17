from utils.handleInput import parse_graph_input
from utils.graph import Graph,GraphRepresentationType
from utils.graphRandomizer import generate_strongly_connected_digraph
from utils.johnson import johnson

if __name__ == "__main__":
    # digraph = generate_strongly_connected_digraph(4, 0.2)
    # digraph.add_connection_weights(-5, 10)
    mx1 = [[0, 1, 1], [1, 0, 0], [0, 1, 0]]
    w1 = [[0, -1, -4], [4, 0, 0], [0, 2, 0]]
    digraph = Graph(GraphRepresentationType.DIGRAF_ADJACENCY_MATRIX, mx1)
    digraph.graph_weights = w1
    digraph.print_graph_representation()
    digraph.print_weights()
    D = johnson(digraph)
    print(D)