from .graph import Graph,GraphRepresentationType
import numpy

def DFSUtil(graph : Graph, vertex : int, visitedVertcies : set, dfs_path : list ):
    visitedVertcies.add(vertex)
    dfs_path.append(vertex)
    for neighbour in range(len(graph.graph_representation[vertex])):
        if graph.graph_representation[vertex][neighbour] != 0 and neighbour not in visitedVertcies:
            DFSUtil(graph, neighbour, visitedVertcies, dfs_path)

def DFS(graph : Graph, startVertex : int, visited_vertices : set):
    dfs_path = list()
    if startVertex not in visited_vertices:
        DFSUtil(graph, startVertex, visited_vertices, dfs_path)
    return dfs_path

def merge_list(list_to_merge):
    return [y for x in list_to_merge for y in x]

def kosaraju(graph : Graph, startVertex : int):
    # 1. DFS 
    dfs_paths = [ ] 
    visited = set()
    for vertex in range(len(graph.graph_representation)):
        dfs_path = DFS(graph, vertex, visited)
        if len(dfs_path) > 0:
            dfs_paths.append(dfs_path)
        visited = set(merge_list(dfs_paths))

    # 2. prepare DFS paths for re-walk
    dfs_paths.reverse()
    dfs_paths = merge_list(dfs_paths)

    # 3. transpose_graph  
    graph.graph_representation = numpy.transpose(graph.graph_representation).tolist()

    # 4. second DFS
    stronglyConnectedComponents = [ ] 

    visited = set()
    for vertex in dfs_paths:
        stronglyConnectedComponent = DFS(graph, vertex, visited)
        if len(stronglyConnectedComponent) > 0:
            stronglyConnectedComponents.append(stronglyConnectedComponent)
        visited = set(merge_list(stronglyConnectedComponents))
    
    return stronglyConnectedComponents