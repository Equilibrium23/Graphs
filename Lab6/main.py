from utils.input import travelling_salesman_graph
from utils.plot import plot_graph
from utils.simulated_annealing import komiwojazer

if __name__ == "__main__":
    path1 = 'input/59.dat'
    path2 = 'input/200.dat'
    graph = travelling_salesman_graph(path1)

    new_cycle, length = komiwojazer(graph)
    plot_graph(new_cycle)
    print(f"Długość cyklu: {length}")