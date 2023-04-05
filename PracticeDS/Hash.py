class Hashmap: 
    def __init__(self, size=7): 
        self.datamap = [None] * size
        
    def __hash__(self,key): 
        hashCode = 0 
        for letters in key: 
            hashCode = ((hashCode + ord(letters)) * 23) % (len(self.datamap))
        return hashCode
    
    def print_hash(self):        
        for index,value in enumerate(self.datamap): 
            print("{}: {}".format(index,value))
            
    def addValuesinHash(self,key,value):
        index = self.__hash__(key)
        if self.datamap[index] == None: 
            self.datamap[index] = []
        self.datamap[index].append([key,value])
             
    def getValuefromHash(self,key): 
        index = self.__hash__(key)
        if self.datamap[index] is not None: 
            for i in range(len(self.datamap)): 
                if self.datamap[index][i][0] == key: 
                    msg="Count: {}".format(self.datamap[index][i][1])
                    return msg
        return False
                
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
                
            
                
                
    



hush = Hashmap()
hush.addValuesinHash("banana",19)
# print(hush.getValuefromHash("banana"))
hush.removeValuefromHash("banana")

hush.print_hash()