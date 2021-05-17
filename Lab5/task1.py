from utils.flow_network import generate_network
from utils.plot import plot_graph

if __name__ == '__main__':

    print("Podaj liczbe warstw sieci.")
    N = int(input())
    network = generate_network(N)
    plot_graph(network)
    network.print_graph_representation()