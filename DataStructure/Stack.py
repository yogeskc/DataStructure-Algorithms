class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack: 
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        
    def print_stack(self): 
        temp = self.top
        while temp is not None: 
            print(temp.value)
            temp = temp.next
            
    def add_to_stack(self,value):
        new_node = Node(value)
        if self.top is None: 
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        
        
    def remove_from_stack(self):
        temp = self.top 
        self.top = temp.next
        temp.next = None 
        self.height -= 1
        
myStack = Stack(2)
myStack.add_to_stack(20)
myStack.add_to_stack(200)
myStack.remove_from_stack()
myStack.print_stack()
            