from copy import deepcopy
class Stack:
    def __init__ (self):
        self.Stack = []
    
    def getListFromStack (self):
        return deepcopy(self.Stack)

    def push(self, item):
        self.Stack.append(item)  
        return self 
    
    def pop(self):
        if not self.isEmpty():
            return self.Stack.pop( len(self.Stack)-1 )
        else:
            raise Exception("Cannot pop from empty stack")
    
    def size(self):
        return len(self.Stack)
    
    def top(self):
        if not self.isEmpty():
            return self.Stack[ len(self.Stack)-1 ]
            return self 
        else:
            raise Exception("Cannot get top element from empty stack")
    
    def bottom(self):
        if not self.isEmpty():
            return self.Stack[ 0 ]
            return self 
        else:
            raise Exception("Cannot get bottom element from empty stack")
    
    def isEmpty(self):
        return len(self.Stack) == 0
    
    def printStack(self):
        for item in self.Stack:
            print(item)

    def __str__(self):
        representation = ""
        for item in self.Stack:
            representation = "{}\n".format(item)
        return representation
