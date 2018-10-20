Find Mother Vertex

def findMother(self):
        visited = [False] * len(self.V)
        
        v = 0
        for i in self.V:
            if visited[v] == False:
                dfs(i, visited)
            v = i
        
        visited = [False] * len(self.V)
        
        dfs(v, visited)
        if any(i == False for i in visited):
            return -1
        return v
		
