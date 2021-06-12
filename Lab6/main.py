from utils.input import travelling_salesman_graph, create_graph_as_cycle
from utils.plot import plot_graph

if __name__ == "__main__":
    path1 = 'input/59.dat'
    path2 = 'input/200.dat'
    graph = travelling_salesman_graph(path1)

    random_cycle = range(59)
    cycle_graph = create_graph_as_cycle(graph, random_cycle)
    plot_graph(cycle_graph)
