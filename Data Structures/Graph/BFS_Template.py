BFS

def driver(vertex):
    visited = [False] * size
    queue = []

    queue.append(vertex)
    visited[vertex] = True

    while q:
        s = q.pop(0)

        for i in vertex.neighbors:
            if visited[i] == False:
                visited[i] = True
                q.append(i)
        