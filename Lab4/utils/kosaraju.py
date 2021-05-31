from .graph import Graph,GraphRepresentationType
import numpy

def DFSUtil(graph : Graph, vertex : int, visitedVertcies : set, dfs_path : list, vertex_process_time : list):
    visitedVertcies.add(vertex)
    dfs_path.append(vertex)
    for neighbour in range(len(graph.graph_representation[vertex])):
        if graph.graph_representation[vertex][neighbour] != 0 and neighbour not in visitedVertcies:
            DFSUtil(graph, neighbour, visitedVertcies, dfs_path, vertex_process_time)
    vertex_process_time.append(vertex)

def DFS(graph : Graph, startVertex : int, visited_vertices : set):
    dfs_path = list()
    vertex_process_time = []
    if startVertex not in visited_vertices:
        DFSUtil(graph, startVertex, visited_vertices, dfs_path, vertex_process_time)
    return (dfs_path, vertex_process_time)

def merge_list(list_to_merge):
    return [y for x in list_to_merge for y in x]

def kosaraju(graph : Graph, startVertex : int):
    # 1. DFS 
    dfs_paths = [ ] 
    visited = set()
    vertex_process_time = []
    for vertex in range(len(graph.graph_representation)):
        result = DFS(graph, vertex, visited)
        dfs_path = result[0]
        if len(dfs_path) > 0:
            dfs_paths.append(dfs_path)
            vertex_process_time.append(result[1])
        visited = set(merge_list(dfs_paths))

    # 2. prepare process time for re-walk
    vertex_process_time = merge_list(vertex_process_time)
    vertex_process_time.reverse()

    # 3. transpose_graph  
    graph.graph_representation = numpy.transpose(graph.graph_representation).tolist()

    # 4. second DFS
    stronglyConnectedComponents = [ ] 

    visited = set()
    for vertex in vertex_process_time:
        result = DFS(graph, vertex, visited)
        stronglyConnectedComponent = result[0]
        if len(stronglyConnectedComponent) > 0:
            stronglyConnectedComponents.append(stronglyConnectedComponent)
        visited = set(merge_list(stronglyConnectedComponents))
    
    return stronglyConnectedComponents