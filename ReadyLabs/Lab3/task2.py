import sys
sys.path.append('../')
import numpy as np
from Lab1.utils.graph import Graph
from Lab1.utils.plot import plot_graph
from Lab1.utils.handleInput import *
from utils.connected_graph import *
from utils.dijkstra import dijkstra
from copy import copy, deepcopy



def print_dijkstra(G: Graph, s):
    p_s, d_s = dijkstra(G, s)
    w = G.graph_weights

    G.print_graph_representation()
    G.print_weights()

    print("\nSTART: s =", s)

    for v in range(len(p_s)):
        path = []
        print('d({}) = {} ===> '.format(v, d_s[v]), end='')

        currNode = v
        path.append(currNode)

        while p_s[currNode] != None:
            currNode = p_s[currNode]
            path.append(currNode)

        path = path[::-1] # reversing
        print(path)

    plot_graph(graph)



if __name__ == "__main__":
    #examples
    graph = generate_connected_graph(7)
    graph.add_connection_weights(1, 10)

    print_dijkstra(graph, 0)



    
