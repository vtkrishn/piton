class G:
        def __init__(self):
            self.graph = {}
        
        def addEdge(self, a,b):
            if self.graph.has_key(a):
                self.graph[a].append(b)
            else:
                self.graph[a] = [b]
            
            if self.graph.has_key(b):
                self.graph[b].append(a)
            else:
                self.graph[b] = [a]   
            self.size = len(self.graph)

        
g = G()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(1,5)
g.addEdge(2,6)
g.addEdge(2,7)
g.addEdge(3,8)
g.addEdge(3,9)

bfs(0,g)
            

    
    
            