from .graph import Graph
from .sum_wages_in_cycle import sum_wages_in_cycle

from random import uniform



def komiwojazer(full_graph : Graph):
    cycle = generate_hamilton_cycle(full_graph)
    path = annealing(cycle)

    return path


def annealing(cycle : Graph, IT_MAX : int):
    path_length = sum_wages_in_cycle(cycle)
    for i in range(100):
        T = 0.001 * i**2
        for it in range(IT_MAX):
            new_cycle = two_opt(cycle)
            new_path_length = sum_wages_in_cycle(new_cycle)
            if(new_path_length < path_length):
                path_length = new_path_length
                cycle = new_cycle
            else:
                if(uniform(0, 1) < exp(-(new_path_length - path_length) / T)):
                    path_length = new_path_length
                    cycle = new_cycle
    return cycle