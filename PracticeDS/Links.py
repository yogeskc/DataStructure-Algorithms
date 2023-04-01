class Node: 
    def __init__(self,value): 
        self.value = value 
        self.next = None
        
class LinkList: 
    def __init__(self, value): 
        new_node = Node(value)
        self.length = 1
        self.head = new_node
        self.tail = new_node
            
    def print_list(self):
        temp = self.head
        while(temp is not None): 
            print(temp.value)
            temp = temp.next
            
    def append_list(self,value):
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node 
        self.tail.next = new_node 
        self.tail = new_node
        self.length += 1
        
        
    def reverse_list(self): 
        temp = self.head 
        self.head = self.tail 
        after = temp.next 
        before = None
        while temp is not None: 
            after = temp.next 
            temp.next = before
            before = temp 
            temp = after 


myList = LinkList(1)
myList.append_list(2)
myList.append_list(3)
myList.reverse_list()
myList.print_list()