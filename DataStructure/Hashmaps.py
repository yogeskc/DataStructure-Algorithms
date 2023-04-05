class HashMap:
    def __init__(self, size=7): 
        self.datamap = [None] * size
        
    def _hash(self, key): 
        hashindex = 0 
        for letter in key: 
            hashindex = ((hashindex + ord(letter))* 23) * len(self.datamap)
        return hashindex
        
        
    def print_hashmap(self):
        for index,value in enumerate(self.datamap):
            print("{}:{}".format(index,value))
            
    def set_value_inmap(self, key, value):
        index = self._hash(key)
        if self.datamap[index] ==  None:
            self.datamap[index] = []
        self.datamap[index].append([key, value])
        
        
    def get_item(self, key):
        index = self._hash(key)
        if self.datamap[index] is not None: 
            for i in range(len(self.datamap[index])):
                if self.datamap[index][i][0] == key:
                    return self.datamap[index][i][1]
        return None
                
    def removeValuefromHash(self,key): 
        index = self.__hash__(key)
        if self.datamap[index] != None: 
            for  i in range(len(self.datamap)): 
              if self.datamap[index][i][0] == key: 
                  val =  self.datamap[index][i][1]
                  self.datamap[index].remove([key,val])
                  if self.datamap[index] == []: 
                      self.datamap[index] = None 
                  return True
        return False
                
            
    
    
    
hashmap = HashMap()
hashmap.set_value_inmap('bolts',1400)
hashmap.set_value_inmap('washers',50)
hashmap.set_value_inmap('lumber',70)
print(hashmap.get_item('washers'))
