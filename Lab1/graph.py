class Graph:
    @staticmethod
    def create_graph_representation(representation_type, graph_input):
        if representation_type == "adjacency_list":
            neighborhood_of_vertexes  = [list(map(int,line.split(". ")[1].split(" "))) for line in graph_input]
            return Graph(representation_type, {vertex+1:neighborhood_of_vertexes[vertex] for vertex in range(len(neighborhood_of_vertexes))})
        else:
            # incidence_matrix or adjacency_matrix so graph rep is matrix
            return Graph(representation_type, [list(map(int,line.split(" "))) for line in graph_input])

    def __init__(self,representation_type, graph_representation):
        self.representation_type = representation_type
        self.graph_representation = graph_representation
    

    def change_graph_representation(self,new_representation_type):
        if self.representation_type != new_representation_type:
            if new_representation_type == "adjacency_list":
                self.change_to_adjacency_list()
                
            if new_representation_type == "incidence_matrix":
                self.change_to_incidence_matrix()

            if new_representation_type == "adjacency_matrix":
                self.change_to_adjacency_matrix()

    def change_to_adjacency_matrix(self):
        if self.representation_type == "adjacency_list":
            pass
            # to do 
        if self.representation_type == "incidence_matrix":
            pass
            # to do 


    def change_to_adjacency_list(self):
        if self.representation_type == "adjacency_matrix":
            pass
            # to do 
        if self.representation_type == "incidence_matrix":
            pass
            # to do 
            
    def change_to_incidence_matrix(self):
        if self.representation_type == "adjacency_list":
            pass
            # to do 
        if self.representation_type == "adjacency_matrix":
            pass
            # to do 

    