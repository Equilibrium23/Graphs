from utils.flow_network import generate_network, generate_network_with_weights
from utils.plot_by_layers import plot_digraph_by_layers
from utils.Ford_Fulkerson import *

if __name__ == '__main__':

    N = 3
    network = generate_network_with_weights(N, 1, 10)
    network.print_graph_representation()
    print()
    network.print_weights()
    


    last = len(network.graph_representation)-1
    f = Ford_Fulkerson(network, 0, last)

    print("\nPrzeplyw krawedzi (f):")
    for i in range(len(f)):
        for j in range(len(f[i])):
            print('{:>3}'.format(f[i][j]), end='')
        print()

    maximumFlow = 0
    for i in range(len(f)):
        maximumFlow = maximumFlow + f[i][last]

    print(f"Maksymalny przeplyw = {maximumFlow}" )
    plot_digraph_by_layers(network, f)
