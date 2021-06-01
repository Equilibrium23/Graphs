import sys
sys.path.append('../')
import numpy as np
from .graph import Graph, GraphRepresentationType
from .plot_by_layers import plot_digraph_by_layers
import copy

def BFS(G: Graph, s):
    if(G.representation_type != GraphRepresentationType.DIGRAF_ADJACENCY_MATRIX):
        raise Exception('representation_type must be: DIGRAF_ADJACENCY_MATRIX')
    if(len(G.graph_weights) == 0):
        raise Exception('Graf nie ma wag lub wierzcholkow!!!')

    number_of_vertices = len(G.graph_representation)
    gw = G.graph_weights    #c_f
    p_s = np.full(number_of_vertices, None)
    d_s = np.full(number_of_vertices, float('Inf'))
    d_s[s] = 0

    queue = []
    queue.append(s)

    while len(queue):
        
        v = queue.pop(0)
        for u in range(number_of_vertices):
            if gw[v][u]:

                if(d_s[u] == float('Inf')):
                    d_s[u] = d_s[v] + 1
                    p_s[u] = v
                    queue.append(u)
    
    return p_s, d_s
    

def Ford_Fulkerson(G: Graph, s, t):
    if(G.representation_type != GraphRepresentationType.DIGRAF_ADJACENCY_MATRIX):
        raise Exception('representation_type must be: DIGRAF_ADJACENCY_MATRIX')
    if(len(G.graph_weights) == 0):
        raise Exception('Graf nie ma wag lub wierzcholkow!!!')
    gr = G.graph_representation

    G_f = copy.deepcopy(G)
    c_f = G_f.graph_weights
    
    number_of_vertices = len(gr)
    f = np.full([number_of_vertices,number_of_vertices], 0)


    p_s, d_s = BFS(G_f, s)
    while(p_s[t] != None):

        path = []
        currNode = t
        path.append([p_s[currNode], currNode])
        p_s[s] = s
        while p_s[currNode] != s:
            currNode = p_s[currNode]
            path.append([p_s[currNode], currNode])


        c_f_p = float('Inf')
        for i in range(len(path)):
            c_f_i = c_f[path[i][0]][path[i][1]]
            if(c_f_i < c_f_p):
                c_f_p = c_f_i


        for i in range(len(path)):
            c_f[path[i][0]][path[i][1]] = c_f[path[i][0]][path[i][1]] - c_f_p
            c_f[path[i][1]][path[i][0]] = c_f_p

            if gr[path[i][0]][path[i][1]]:
                f[path[i][0]][path[i][1]] = f[path[i][0]][path[i][1]] + c_f_p
            else:
                f[path[i][0]][path[i][1]] = f[path[i][0]][path[i][1]] - c_f_p
        p_s, d_s = BFS(G_f, s)

    return f
    
        
