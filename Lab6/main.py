from utils.input import travelling_salesman_graph
from utils.plot import plot_graph
from utils.simulated_annealing import komiwojazer, FUNCTION_TYPES

if __name__ == "__main__":
    path1 = 'input/59.dat'
    path2 = 'input/200.dat'
    graph = travelling_salesman_graph(path1)

    new_cycle, length = komiwojazer(graph, 50, FUNCTION_TYPES.QUADRATIC )
    # plot_graph(new_cycle)
    print(f"Długość cyklu: {length}")

    new_cycle, length = komiwojazer(graph, 50, FUNCTION_TYPES.LINEAR )
    # plot_graph(new_cycle)
    print(f"Długość cyklu: {length}")

    new_cycle, length = komiwojazer(graph, 50, FUNCTION_TYPES.EXPONENTIAL )
    # plot_graph(new_cycle)
    print(f"Długość cyklu: {length}")
