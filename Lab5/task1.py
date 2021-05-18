from utils.flow_network import generate_network, generate_network_with_weights
from utils.plot import plot_digraph

if __name__ == '__main__':

    print("Podaj liczbe warstw sieci.")
    N = int(input())
    network = generate_network_with_weights(N, 1, 10)
    plot_digraph(network)
    network.print_weights()