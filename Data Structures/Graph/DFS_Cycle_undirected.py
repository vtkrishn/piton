DFS cycle detection - undirected
	
	def driver(graph):
		visited = [False]*len(graph)
		
		for i in graph:
			if visited[i] == False:
				isCycleExist(i, visited, -1)
					return True
		return False
	
	def isCycleExist(vertex, visited, parent):
		visited[vertex] = True
		
		for child in graph[vertex]:
			if visited[child] == False:
				isCycleExist(child,visited,vertex):
					return True
			elif parent != child:
				return True
		
		return False
		
		
		