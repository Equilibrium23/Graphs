from utils.plot import plot_graph
from utils.euler_graph_handler import generate_random_eulerian_graph, check_if_eulerian

if __name__ == "__main__":
	graph = generate_random_eulerian_graph(3, 10)
	is_eulerian_graph, path = check_if_eulerian(graph)
	print(f"Czy graf jest eulerowski: {is_eulerian_graph}")
	if is_eulerian_graph:
		print("Path:")
		print(path)
	plot_graph(graph)