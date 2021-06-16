from utils.input import travelling_salesman_graph
from utils.plot import plot_tsp
from utils.simulated_annealing import komiwojazer, FUNCTION_TYPES

if __name__ == "__main__":
    path1 = 'input/59.dat'
    path2 = 'input/200.dat'
    graph = travelling_salesman_graph(path1)

    new_cycle, length = komiwojazer(graph, 100, FUNCTION_TYPES.QUADRATIC )
    print(f"Długość cyklu: {length}")

    new_cycle, length = komiwojazer(graph, 100, FUNCTION_TYPES.LINEAR )
    print(f"Długość cyklu: {length}")

    new_cycle, length = komiwojazer(graph, 100, FUNCTION_TYPES.EXPONENTIAL )
    print(f"Długość cyklu: {length}")
