class Node: 
    def __init__(self,value):
        self.value = value
        self.next = None
        
        
class LinkList: 
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while (temp is not None): 
            print(temp.value)
            temp = temp.next

    def append_list(self,value):
        new_node = Node(value)
        if self.length == 0: 
            self.head = new_node
            self.tail = new_node
        else: 
           self.tail.next = new_node
           self.tail = new_node
        self.length += 1
        
                    
    def prepend_list(self,value): 
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node           
        self.length +=1
        
        
    def pop_tail(self):
        if self.length == 0: 
            return None
        
        pre = self.head 
        temp = self.head
        
        while temp.next is not None: 
            pre = temp 
            temp = temp.next
        
        self.tail = pre 
        self.tail.next = None
        self.length -= 1
            
            
    def pop_first(self):
        if self.length == 0:
            return None
        else: 
            temp = self.head 
            self.head = temp.next
            temp.next = None           
        self.length -= 1
        
        
    def get_index(self,index):
        if (index < 0 or index >= self.length): 
            return False
        temp = self.head
        for _ in range(index):
            temp = temp.next      
        return temp
                       
                       
    def insert_node(self, index, value):
        new_node = Node(value)   
        if index < 0 or index >= self.length:
            return False
        
        if (index == 0): 
            return self.prepend_list(value)
        
        if (index == self.length): 
            return self.append_list(value)
    
        temp = self.get_index(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length+=1
        
        
    def remove_node(self, index):
         if (index < 0 or index >= self.length): 
             return False
         
         if (index == 0): 
             return self.pop_first(index)
         
         if (index == self.length): 
             return self.pop_tail()
         
         prev = self.get_index(index-1)
         temp = prev.next
         
         prev.next = temp.next
         temp.next = None 
         
         self.length-=1
        
        
    def reverse_list(self): 
        temp = self.head
        self.head = self.tail 
        self.tail = temp
                
        after = temp.next 
        before = None
        
        for _ in range(self.length): 
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
            

myLink = LinkList(5)
myLink.append_list(6)
myLink.prepend_list(2)
myLink.pop_first()
myLink.insert_node(1,20)
myLink.reverse_list()
myLink.print_list()
      
           
           
           
        
            