from utils.flow_network import generate_network
from utils.plot import plot_digraph

if __name__ == '__main__':

    print("Podaj liczbe warstw sieci.")
    N = int(input())
    network = generate_network(N)
    network.print_graph_representation()
    plot_digraph(network)
    network.print_graph_representation()