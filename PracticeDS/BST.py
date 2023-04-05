class Node: 
    def __init__(self,value): 
        self.value = value
        self.right = None
        self.left  = None
        

class BinarySerchTree: 
    def __init__(self): 
        self.root = None
        
    def add_val_tree(self,value): 
        new_node = Node(value)
        
        if self.root is None: 
            self.root = new_node
            return True
        
        temp = self.root 
        
        while(True): 
            if new_node.value == temp.value: 
                return False 
            
            if new_node.value < temp.value: 
                if temp.left is  None: 
                    temp.left = new_node
                    return True 
                temp = temp.left 
                
            if new_node.value > temp.value: 
                if temp.right is  None: 
                    temp.right = new_node 
                    return True 
                temp = temp.right
                
    def contains_value(self,value): 
        if self.root is None: 
            return False
        temp = self.root 
        
        while(temp is not None): 
            if value < temp.value: 
                temp = temp.left
            if value > temp.value: 
                temp = temp.right 
            else: 
                return True
        return False
    
            
bst = BinarySerchTree()
bst.add_val_tree(2)
bst.add_val_tree(3)
bst.add_val_tree(1)

print(bst.root.right.value)