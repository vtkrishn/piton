Total number of paths from src to dest

def countPath(src, dest):
	 visited = [False] * len(vertex)
	 path = 0
	 dfs(src,dest, visited, path)
	 return path
	 
	 def dfs(src, dest, visited, path):
		visited[src] = True
		
		if src == dest:
			path = path + 1
		else:
			for child in src:
				if not visited[child]:
					dfs(child, dest,visited, path)
		
		visited[src] = False
	 
	 
	 