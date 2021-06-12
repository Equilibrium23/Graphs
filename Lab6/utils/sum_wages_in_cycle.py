from utils.graph import Graph, GraphRepresentationType

def sum_wages_in_cycle(graph: Graph):
    if(graph.representation_type != GraphRepresentationType.ADJACENCY_MATRIX):
        raise Exception('representation_type must be: adjacency_matrix')

    gr = graph.graph_representation
    gw = graph.graph_weights

    sum = 0

    for i in range(len(gr)):
        for j in range(len(gr[i])):
            if(gr[i][j] == 1):
                sum = sum + gw[i][j]

    return sum // 2


