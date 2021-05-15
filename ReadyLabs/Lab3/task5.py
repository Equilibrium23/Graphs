def minimum_not_visited_edge(edges, visited):
    for edge in edges:
        if edge[0] not in visited:
            return edge
    return [-1,999] 


def prime_minimum_spanning_tree(graph, start):
    visited = [start]
    minimum_spanning_tree = []
    while len(visited) < len(graph):
        min_not_visited_edges = [  minimum_not_visited_edge(graph[vertex], visited) + [vertex]  for vertex in visited ]
        next_edge = min(min_not_visited_edges, key = lambda x : x[1])
        visited.append(next_edge[0])
        minimum_spanning_tree.append([next_edge[2],next_edge[0]])
    return minimum_spanning_tree

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

if __name__ == "__main__":
    with open ('input/zad5.txt', 'r') as graph_input:
        graph_data = parse_wage_graph(graph_input)
        graph = graph_data[0]
        min_vertex = graph_data[1]
        max_vertex = graph_data[2]
        start_vertex = 1 - min_vertex
        minimum_spanning_tree_road = prime_minimum_spanning_tree(graph, start_vertex)
        for edge in minimum_spanning_tree_road:
            print("[{},{}]".format(edge[0]+min_vertex,edge[1]+min_vertex))