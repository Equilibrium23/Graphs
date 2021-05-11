from utils.graph import Graph
from utils.plot import plot_graph
from utils.graphRandomizer import generate_Gnl_graph, generate_Gnp_graph

if __name__ == "__main__":
    G_nl = generate_Gnl_graph(6, 10)
    plot_graph(G_nl)

    G_np = generate_Gnp_graph(8, 0.3)
    plot_graph(G_np)