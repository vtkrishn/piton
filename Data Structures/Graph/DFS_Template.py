DFS Template from single vertex
								def driver(graph):
									visited = []
									visited = [False] * (len(graph))
									dfs(vertex,visited)
								
								def dfs(node, visited):
									viisted[node] = True
									for child in graph[node]:
										if !visited[child]:
											dfs(child, visited)
											
DFS Template from all vertex
								def driver(graph):
									visited = []
									visited = [False] * (len(graph))
									for node in range(graph):
										dfs(node,visited)
								
								def dfs(node, visited):
									viisted[node] = True
									for child in graph[node]:
										if !visited[child]:
											dfs(child, visited)

												