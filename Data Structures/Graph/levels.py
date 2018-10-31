
def bfs(v,g):
    q,visited,level = [],[],[]
    visited = [False]*(len(g.graph))
    level = [0]*(len(g.graph))
    
    q.append(v)
    visited[v] = True
    level[v] = 0
    
    while q:
        s = q.pop(0)
        #print s
        for i in g.graph[s]:
            if visited[i] == False:
                level[i] = level[s] + 1
                q.append(i)
                visited[i] = True
    print max(level)