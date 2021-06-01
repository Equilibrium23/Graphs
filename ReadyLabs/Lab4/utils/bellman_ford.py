from .graph import Graph,GraphRepresentationType
import numpy as np

def _relax(u, v, w, d_s, p_s):
    if d_s[v] > d_s[u] + w[u][v]:
        d_s[v] = d_s[u]  + w[u][v]
        p_s[v] = u

def bellman_ford(graph: Graph, s: int):
    if(len(graph.graph_weights) == 0):
        raise Exception('Graf nie ma wag lub wierzcholkow!!!')

    w = graph.graph_weights
    nodeAmount = len(w)

    # Init
    p_s = np.full(nodeAmount, None)
    d_s = np.full(nodeAmount, float('Inf'))
    d_s[s] = 0
    
    for _ in range(nodeAmount-1):
        for u in range(len(w)):
            for v in range(len(w)):
                if graph.graph_representation[u][v]:
                    _relax(u, v, w, d_s, p_s)

    for u in range(len(w)):
        for v in range(len(w)):
            if graph.graph_representation[u][v]:
                if d_s[v] > d_s[u] + w[u][v]:
                    print("W grafie jest cykl o ujemnej wadze osiągalny ze źródła s={s}")
                    return False, _, _

    return True, d_s, p_s

def print_bellman_ford(G: Graph, s):
    result, d_s, p_s = bellman_ford(G, s)
    if result == False:
        raise Exception(f"W grafie jest cykl o ujemnej wadze osiągalny ze źródła s={s}")

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

    #plot_graph(graph)
