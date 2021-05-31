from utils.handleInput import parse_graph_input
from utils.graph import Graph,GraphRepresentationType
from utils.graphRandomizer import generate_strongly_connected_digraph
from utils.bellman_ford import print_bellman_ford
from utils.plot import plot_digraph

if __name__ == "__main__":
    digraph = generate_strongly_connected_digraph(8, 0.2)
    digraph.add_connection_weights(-5, 10)
    digraph.print_graph_representation()
    digraph.print_weights()
    print_bellman_ford(digraph, 0)
    plot_digraph(digraph)