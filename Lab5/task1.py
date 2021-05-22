from utils.flow_network import generate_network, generate_network_with_weights
from utils.plot_by_layers import plot_digraph_by_layers

if __name__ == '__main__':

    print("Podaj liczbe warstw sieci.")
    N = int(input())
    network = generate_network_with_weights(N, 1, 10)
    network.print_weights()
    network.print_graph_representation()
    plot_digraph_by_layers(network)