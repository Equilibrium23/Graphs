from utils.handleInput import parse_graph_input
from utils.graph import Graph,GraphRepresentationType
from utils.kosaraju import kosaraju
from utils.graphRandomizer import generate_Gnp_digraph

if __name__ == "__main__":
    with open ('input/input2.txt', 'r') as graph_input:
        digraph_input = graph_input.readlines()
        parsed_digraph_input = parse_graph_input(GraphRepresentationType.DIGRAF_ADJACENCY_MATRIX, digraph_input)
        graph = Graph(GraphRepresentationType.DIGRAF_ADJACENCY_MATRIX, parsed_digraph_input)
        # graph = generate_Gnp_digraph(10,0.2)
        stronglyConnectedComponents = kosaraju(graph, 0)
        print(stronglyConnectedComponents)