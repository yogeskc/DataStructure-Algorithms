class Hashmap: 
    def __init__(self,size = 7): 
        self.datamap = [None] * size
        
    
    def __hash__(self, key): 
        hashCode = 0 
        for letters in key: 
            hashCode = ((hashCode + ord(letters)) * 23 ) % (len(self.datamap))
        return hashCode; 
    

    def print_map(self): 
        if self.datamap == None: 
            return False
        for index, value in enumerate(self.datamap): 
            print("{}: {}".format(index, value))
    
    
    def add_val_map(self, key,value): 
        index = self.__hash__(key)
        if self.datamap[index] is None: 
            self.datamap[index]= []
            self.datamap[index].append([key,value])
            
    
    def get_value_with_key(self,key): 
        index = self.__hash__(key)
        if self.datamap[index] is  not None: 
            for i in range(len(self.datamap[index])): 
                if self.datamap[index][i][0] == key: 
                    return  self.datamap[index][i][1] 
                
        return False
                    
                    
hashm = Hashmap()
hashm.add_val_map("banana", 9)

print(hashm.get_value_with_key("banana"))