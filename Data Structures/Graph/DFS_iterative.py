def dfs(vertex):
    stack=[]
    visited = [False]*graph.size
    stack.append(graph[vertex])
    
    while stack:
        n = stack.pop()
        visited[n] = True
        
        for i in range(v.child):
            if not visited[i]:
                stack.append(v[i])
        
        
        