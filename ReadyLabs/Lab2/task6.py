from utils.handleInput import check_type_of_input, BadInputException, parse_graph_input
from utils.graph import Graph, GraphRepresentationType
from utils.Stack import Stack

class HamiltonChecker:
    def __init__(self, graph):
        self.hamiltonian_flag = False
        self.graph = graph 
        self.visited = [False]*(len(graph.graph_representation)+1)
        self.stack = Stack()
        self.hamiltonianPath = []

    def check_hamilton(self, vertex):
        if not self.hamiltonian_flag:
            self.stack.push(vertex)
            self.visited[vertex] = True
            if self.stack.size() < len(self.graph.graph_representation):
                for neighbour in self.graph.graph_representation[vertex]:
                    if self.visited[neighbour] == False:
                        self.check_hamilton(neighbour)
                if self.stack.size() < len(self.graph.graph_representation):
                    self.visited[self.stack.pop()] = False
            else:
                if self.stack.bottom() in self.graph.graph_representation[vertex]:
                    self.hamiltonian_flag = True
                    self.stack.push(self.stack.bottom())
                    self.hamiltonianPath = self.stack.getListFromStack()
                else:
                    self.visited[self.stack.pop()] = False

    def is_hamiltionian(self):
        return (self.hamiltonian_flag , self.hamiltonianPath)
    
    def reset(self):
        self.hamiltonian_flag = False
        self.visited = [False]*len(graph.graph_representation)
        self.stack = Stack()
        self.hamiltonianPath = []

if __name__ == "__main__":
    with open ('input/input6.txt', 'r') as graph_input:
        try:
            graph_input = graph_input.readlines()
            representation_type = check_type_of_input(graph_input)
            parsed_graph_input = parse_graph_input(representation_type, graph_input)

            graph = Graph(representation_type, parsed_graph_input)

            checker = HamiltonChecker(graph)
            checker.check_hamilton(0)
            result = checker.is_hamiltionian()
            
            print(result[0])
            print(result[1])

        except BadInputException:
            print(BadInputException)