class Node: 
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
        
class BinarySerachTree:
    def __init__(self):
        self.root = None
        
        
    def insert_node(self,value):
        new_node = Node(value)
        if self.root is None: 
            self.root = new_node
            return True
        temp = self.root
        
        while(True):
            if new_node.value == temp.value :
              return False
          
            if new_node.value < temp.value: 
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if new_node.value > temp.value:
                      if temp.right is None:
                        temp.right = new_node
                        return True
                      temp = temp.right  
                    
                    
    def containsVal(self, value):
        if self.root is None:
            return False
        
        temp = self.root
        
        while(temp is not None):
            if value < temp.value:
                temp = temp.left 
            elif value > temp.value:
                temp = temp.right
            else: 
                return True 
        return False   
        

bst = BinarySerachTree()
bst.insert_node(2)
bst.insert_node(3)
bst.insert_node(1)

print(bst.root.left.value)

