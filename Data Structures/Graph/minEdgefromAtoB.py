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

        def minDistance(self,a,b):
            q = []
            visited = [False]*self.size #5 nodes
            
            q.append(a)
            visited[a] = True
            distance = [0]*self.size
            
            while q:
                s = q.pop(0)
                for i in self.graph[s]:
                    
                    if visited[i]:
                        continue
                    
                    q.append(i)
                    visited[i]= True
                    distance[i] = distance[s] + 1
            
            print distance[b]
        
g = G()
g.addEdge(0, 1); 
g.addEdge(0, 7); 
g.addEdge(1, 7); 
g.addEdge(1, 2); 
g.addEdge(2, 3); 
g.addEdge(2, 5); 
g.addEdge(2, 8); 
g.addEdge(3, 4); 
g.addEdge(3, 5); 
g.addEdge(4, 5); 
g.addEdge(5, 6); 
g.addEdge(6, 7); 
g.addEdge(7, 8); 

g.minDistance(1,5)