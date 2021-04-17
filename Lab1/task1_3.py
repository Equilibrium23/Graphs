from graph import Graph
from plot import plot_graph
from graphRandomizer import generate_Gnl_graph, generate_Gnp_graph

if __name__ == "__main__":
    print("Generate G(n, l):")
    G_nl = generate_Gnl_graph(6, 10)
    plot_graph(G_nl)

    print("Generate G(n, p):")
    G_np = generate_Gnp_graph(8, 0.3)
    plot_graph(G_np)