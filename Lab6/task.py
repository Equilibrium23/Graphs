import sys
from utils.input import travelling_salesman_graph
from utils.plot import plot_tsp
from utils.simulated_annealing import komiwojazer, FUNCTION_TYPES
from utils.graph_randomizer import HamiltonChecker
from utils.graph import GraphRepresentationType
import time

#przyklad: python task.py "input/59.dat"
if __name__ == "__main__":
    start = time.time()
    filepath = sys.argv[1]
    graph = travelling_salesman_graph(filepath)

    new_cycle, length = komiwojazer(graph, 50, FUNCTION_TYPES.QUADRATIC )
    new_cycle.change_graph_representation_to(GraphRepresentationType.ADJACENCY_LIST)
    checker = HamiltonChecker(new_cycle)
    checker.check_hamilton(0)
    print(checker.is_hamiltionian()[1])
    new_cycle.change_graph_representation_to(GraphRepresentationType.ADJACENCY_MATRIX)
    print(f"Długość cyklu: {length}")
    plot_tsp(filepath, checker.is_hamiltionian()[1], save=True)
    end = time.time()
    print(end - start, 's')
