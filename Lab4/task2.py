from utils.handleInput import parse_graph_input
from utils.graph import Graph,GraphRepresentationType
from utils.kosaraju import kosaraju
from utils.graphRandomizer import generate_Gnp_digraph
from utils.plot import plot_digraph

if __name__ == "__main__":
    digraph = generate_Gnp_digraph(10,0.2)
    stronglyConnectedComponents = kosaraju(digraph, 0)
    print(stronglyConnectedComponents)
    plot_digraph(di)
