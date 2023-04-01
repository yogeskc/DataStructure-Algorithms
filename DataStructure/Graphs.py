class Graphs: 
    def __init__(self): 
        self.adjs_list = {}
          
    def print(self): 
        for vertex in self.adjs_list: 
            print ("{}:{}".format(vertex,self.adjs_list[vertex]))
            
    def add_vertex(self,vertex): 
        if vertex not in self.adjs_list.keys():
            self.adjs_list[vertex] = []
            return True
    
    def addEdge(self,v1, v2): 
        if v1 in self.adjs_list.keys() and v2 in self.adjs_list.keys(): 
            self.adjs_list[v1].append(v2)
            self.adjs_list[v2].append(v1)
            return True 
        return False
    
    def removeEdge(self,v1, v2): 
        if v1 in self.adjs_list.keys() and v2 in self.adjs_list.keys():
           try:
             self.adjs_list[v1].remove(v2)
             self.adjs_list[v2].remove(v1)
           except ValueError:
                pass
           return True 
        return False
    
    def remove_vertex(self, vertex): 
        if vertex in self.adjs_list.keys():
            for other_vertex in self.adjs_list[vertex]: 
                self.adjs_list[other_vertex].remove(vertex)
            del self.adjs_list[vertex]
            return True 
        return False
            
                
        
        
            
myGraph = Graphs()
myGraph.add_vertex('A')
myGraph.add_vertex('B')
myGraph.add_vertex('C')
myGraph.add_vertex('D')


myGraph.addEdge('A','B')
myGraph.addEdge('A','C')
myGraph.addEdge('A','D')
myGraph.addEdge('B','D')
myGraph.addEdge('C','D')

myGraph.remove_vertex('D')

myGraph.print()
