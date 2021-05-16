import sys

from matplotlib.pyplot import viridis
sys.path.append('../')
from Lab1.utils.graph import Graph
from Lab1.utils.handleInput import *

def get_number_of_connected_components(G: Graph):
    return max(components(G))

def _components_R(nr, v, G, comp):
    for u in range(len(G.graph_representation[v])):
        node = G.graph_representation[v][u]
        if(comp[node] == -1):
            comp[node] = nr
            _components_R(nr, node, G, comp)
        
def components(G: Graph):
    if(G.representation_type != GraphRepresentationType.ADJACENCY_LIST):
        raise Exception('representation_type must be: ADJACENCY_LIST')
    nr = 0
    comp = []
    for node in range(len(G.graph_representation)):
        comp.append(-1)
    for v in range(len(G.graph_representation)):
        if(comp[v] == -1):
            nr = nr + 1
            comp[v] = nr
            _components_R(nr, v, G, comp)

    return comp