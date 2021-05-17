import sys
sys.path.append('../')
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
            if self.stack.size() < len(self.graph.graph_representation):
                self.visited[vertex] = True
                for neighbour in self.graph.graph_representation[vertex]:
                    if self.visited[neighbour] == False:
                        self.check_hamilton(neighbour)
                self.visited[vertex] = False
            else:
                self.hamiltonian_flag = True
                if self.stack.bottom() in self.graph.graph_representation[vertex]:
                    self.stack.push(self.stack.bottom())
                self.hamiltonianPath = self.stack.getListFromStack()
            self.stack.pop()

    def is_hamiltionian(self):
        return {self.hamiltonian_flag : self.hamiltonianPath}
    

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
            
            for is_hamiltonian,hamiltonian_path in result.items():
                print(is_hamiltonian)
                print([x for x in hamiltonian_path])

        except BadInputException:
            print(BadInputException)