import numpy as np

class Graph:
    @staticmethod
    def create_graph_representation(representation_type, graph_input):
        if representation_type == "adjacency_list":
            neighborhood_of_vertices  = [list(map(int, line.split(". ")[1].split(" "))) for line in graph_input]
            vertices = [ int(line.split(". ")[0]) for line in graph_input ]
            return Graph(representation_type, {vertices[vertex]:neighborhood_of_vertices[vertex] for vertex in range(len(neighborhood_of_vertices))})
        elif type(graph_input[0]) is str:
            return Graph(representation_type, [list(map(int, line.split(" "))) for line in graph_input])
        else:
            return Graph(representation_type, graph_input)


    def __init__(self, representation_type, graph_representation):
        self.representation_type = representation_type
        self.graph_representation = graph_representation
    

    def change_graph_representation_to(self, new_representation_type):
        if self.representation_type != new_representation_type:
            if new_representation_type == "adjacency_list":
                self.change_to_adjacency_list()
                
            elif new_representation_type == "incidence_matrix":
                self.change_to_incidence_matrix()

            else:
                self.change_to_adjacency_matrix()


    def change_to_adjacency_matrix(self):
        if self.representation_type == "incidence_matrix":
            self.change_to_adjacency_list()
        if self.representation_type == "adjacency_list":
            self.set_graph_representation_type("adjacency_matrix")
            self.graph_representation = self.create_adjacency_matrix_from_list() 


    def change_to_adjacency_list(self):
        if self.representation_type == "adjacency_matrix":
            self.set_graph_representation_type("adjacency_list")
            self.graph_representation = self.create_list_from_adjacency_matrix()
        if self.representation_type == "incidence_matrix":
            self.set_graph_representation_type("adjacency_list")
            self.create_list_from_incidence_matrix()
            

    def change_to_incidence_matrix(self):
        if self.representation_type == "adjacency_list":
            self.change_to_adjacency_matrix()
        if self.representation_type == "adjacency_matrix":
            self.set_graph_representation_type("incidence_matrix")
            self.create_incidence_matrix_from_adjacency_matrix() 


    def create_list_from_incidence_matrix(self):
        nodes_count = len(self.graph_representation)
        new_representation = []
        for i in range(nodes_count):
            new_representation.append([])

        edges_count = len(self.graph_representation[0])

        for i in range(nodes_count):
            for j in range(edges_count):
                if(self.graph_representation[i][j]):
                    for k in range(nodes_count):
                        if(self.graph_representation[k][j] and k != i):
                            new_representation[i].append(k+1)
                            break
            new_representation[i].sort()

        self.graph_representation = [list(map(int, line)) for line in new_representation]


    def create_incidence_matrix_from_adjacency_matrix(self):
        number_of_edges = 0
        nodes_count = len(self.graph_representation)

        for i in range(nodes_count):
            for j in range(i + 1, nodes_count):
                if(self.graph_representation[i][j]):
                    number_of_edges += 1

        new_representation = np.zeros((nodes_count, number_of_edges))
        edge_counter = 0

        for i in range(nodes_count):
            for j in range(i + 1, nodes_count):
                if(self.graph_representation[i][j]):
                    new_representation[i][edge_counter] = 1
                    new_representation[j][edge_counter] = 1
                    edge_counter += 1

        self.graph_representation = [list(map(int,line)) for line in new_representation]


    def create_adjacency_matrix_from_list(self):
        matrix = np.zeros((len(self.graph_representation), len(self.graph_representation)))
        matrix = matrix.astype(int)
        for node in range(len(self.graph_representation)):
            for neighbor in self.graph_representation[node]:
                matrix[node][neighbor - 1] = 1
                matrix[neighbor - 1][node] = 1
        return matrix


    def create_list_from_adjacency_matrix(self):
        neighbors = list()
        row_number = 0
        for row in self.graph_representation:
            neighbors.append(list())
            neighbor = 0
            for node in row:
                neighbor = neighbor + 1
                if node == 1:
                    neighbors[row_number].append(neighbor)
            row_number = row_number + 1

        return neighbors


    def print_graph_representation(self):
        print(self.representation_type)
        if self.representation_type == "adjacency_list":
            for node in range(len(self.graph_representation)):
                print(node, end = '. ')
                for neighbor in self.graph_representation[node]:
                    print(neighbor, end = ' ')
                print()
        else:
            for row in self.graph_representation:
                for node in row:
                    print(node, end = ' ')
                print()
        print()


    def set_graph_representation_type(self, new_type):
        self.representation_type = new_type