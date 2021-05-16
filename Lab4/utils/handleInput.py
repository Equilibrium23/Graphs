from .graph import GraphRepresentationType

class BadInputException(Exception):
    def __init__(self, message="Given input does not meet the requirements!"):
        self.message = message
        super().__init__(self.message)

def is_adjacency_list(graph_input):
    return "." in graph_input[0]

def is_incidence_matrix(graph_matrix):
    sum_of_each_column_equals_2 = True
    for i in range(len(graph_matrix[0])):
        if sum(row[i] for row in graph_matrix) != 2:
            sum_of_each_column_equals_2 = False

    return len(graph_matrix) != len(graph_matrix[0]) and sum_of_each_column_equals_2
    

def is_adjacency_matrix(graph_matrix):
    zeros_on_main_diagonal = True
    for i in range(len(graph_matrix)):
        for _ in range(len(graph_matrix[i])):
            if graph_matrix[i][i] != 0:
                zeros_on_main_diagonal = False

    return len(graph_matrix) == len(graph_matrix[0]) and zeros_on_main_diagonal


def check_type_of_input(graph_input):
    if len(graph_input) > 1:
        try:
            if is_adjacency_list(graph_input):
                return GraphRepresentationType.ADJACENCY_LIST
            else:
                graph_matrix = [list(map(int,line.split(" "))) for line in graph_input]
                if is_incidence_matrix(graph_matrix):
                    return GraphRepresentationType.INCIDENCE_MATRIX
                elif is_adjacency_matrix(graph_matrix):
                    return GraphRepresentationType.ADJACENCY_MATRIX
                else:
                    raise  BadInputException
        except:
            raise BadInputException
    else:
        raise BadInputException

def parse_graph_input(representation_type : GraphRepresentationType, graph_input):
    
    if representation_type == GraphRepresentationType.ADJACENCY_LIST:
        neighborhood_of_vertices  = [list(map(int, line.split(". ")[1].split(" "))) if line.split(". ")[1] != "\n" else [] for line in graph_input]
        parsed_graph_input = {vertex:neighborhood_of_vertices[vertex] for vertex in range(len(neighborhood_of_vertices))}

    elif representation_type == GraphRepresentationType.ADJACENCY_MATRIX or representation_type == GraphRepresentationType.INCIDENCE_MATRIX or representation_type == GraphRepresentationType.DIGRAF_ADJACENCY_MATRIX:
        parsed_graph_input = [list(map(int, line.split(" "))) for line in graph_input]

    else:
        raise ValueError("{} - Not know representation type".format(representation_type))
        
    return parsed_graph_input
