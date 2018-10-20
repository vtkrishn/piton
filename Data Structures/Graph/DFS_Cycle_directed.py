DFS Cycle detection

	def driver(vertex):
		visited = [False] * len(graph)
		stack = [False] * len(graph)
		
		for i in graph;
			if visited[i] == False:
				isCycleExist(i,visited, stack):
					return True
	
	def isCycleExist(vertex, visited, stack):
		visited[i] = True
		stack[i] = True
		
		for neighbors in vertex:
			if visited[neighbors] == False:
				isCycleExist(neighbors,visited, stack):
					return True
			elif stack[neighbors] == True:
				return True
		
		stack[i] = False
		return False
		
		
			