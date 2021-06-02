from utils.plot import plot_graph
from utils.euler_graph_handler import generate_random_eulerian_graph, check_if_eulerian


if __name__ == "__main__":
	graph = generate_random_eulerian_graph(3, 10)
	is_euler = check_if_eulerian(graph)
	print(f"Czy graf jest eulerowski: {is_euler}")
	plot_graph(graph)