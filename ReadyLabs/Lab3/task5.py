def minimum_not_visited_edge(edges, visited):
    print
    for edge in edges:
        # sprawdzenie czy krawedz z drzewa T laczy sie drzewem W
        if edge[0] not in visited: 
            return edge
    return [-1] 

def filter_list(edges):
    return [ x for x in edges if x[0] != -1 ]

def prime_minimum_spanning_tree(graph, start):
    road_weight = 0
    visited = [start]
    minimum_spanning_tree = []
    while len(visited) < len(graph):
        # wybieram (startujac z wierzcholkow odwiedzonych) 
        # najlzejsze krawedzie nieodwiedzone dla danych wierzcholkow
        # [ [nast_wierz, waga, wierzch_startowy], ... ]
        min_not_visited_edges = [  minimum_not_visited_edge(graph[vertex], visited) + [vertex]  for vertex in visited ]
        min_not_visited_edges = filter_list(min_not_visited_edges)

        # Krawedz ktora bedzie dodawana do drzewa to najmniejsza ze znalezionych
        next_edge = min(min_not_visited_edges, key = lambda x : x[1])

        # dodawanie
        visited.append(next_edge[0])
        minimum_spanning_tree.append([next_edge[2],next_edge[0]])
        road_weight += next_edge[1]
    return (minimum_spanning_tree,road_weight)

def find_min_and_max_vertex(graph):
    min_vertex = graph[0][0]
    max_vertex = graph[0][0]
    for edge in graph:
        temp_min = min(edge[:-1])
        temp_max = max(edge[:-1])
        if min_vertex > temp_min:
            min_vertex = temp_min
        if max_vertex < temp_max:
            max_vertex = temp_max
    return [min_vertex,max_vertex]
    
def reduce_graph(graph, value):
    for edge in graph:
        edge[0] -= value
        edge[1] -= value

def parse_wage_graph(graph_input):
    graph = [ [ int(x) for x in line.split(",")]  for line in graph_input ]
    min_max_vertex = find_min_and_max_vertex(graph)
    reduce_graph(graph, min_max_vertex[0])
    parsed_graph = { vertex:[] for vertex in range( min_max_vertex[1] - min_max_vertex[0] + 1 ) }
    for edge in graph:
        parsed_graph[edge[0]].append( [edge[1],edge[2]] )
        parsed_graph[edge[1]].append( [edge[0],edge[2]] )
    for key,value in parsed_graph.items():
        value.sort(key = lambda x : x[1])
    return [parsed_graph,min_max_vertex[0],min_max_vertex[1]]

def get_graph_object(graph_input):
    adjacency_matrix = [[0] * len(graph_input) for i in range(len(graph_input))]
    weights_matrix = [[0] * len(graph_input) for i in range(len(graph_input))]

    for vertex,neighborhood in graph_input.items():
        for neighbour_vertex in neighborhood:
            adjacency_matrix[vertex][neighbour_vertex[0]] = 1
            weights_matrix[vertex][neighbour_vertex[0]] = neighbour_vertex[1]

    graph = Graph( GraphRepresentationType.ADJACENCY_MATRIX, adjacency_matrix )
    graph.add_connection_weights(weights_matrix)
    return graph

from utils.plot import plot_graph, plot_minimum_spanning_tree_road
from utils.graph import Graph, GraphRepresentationType

if __name__ == "__main__":
    with open ('input/input5.txt', 'r') as graph_input:
        graph_data = parse_wage_graph(graph_input)
        graph = graph_data[0]
        min_vertex = graph_data[1]
        max_vertex = graph_data[2]
        start_vertex = 1
        minimum_spanning_tree_road = prime_minimum_spanning_tree(graph, start_vertex - min_vertex)

        graph = get_graph_object(graph)
        plot_minimum_spanning_tree_road(graph, minimum_spanning_tree_road[0], start_vertex)
        for edge in minimum_spanning_tree_road[0]:
            print("[{},{}]".format(edge[0]+min_vertex,edge[1]+min_vertex))
        print("Waga drogi -> {}".format(minimum_spanning_tree_road[1]))