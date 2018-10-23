Backtracking template

def backtracking(vertex):
	result = []
	temp_result = []
	dfs(vertex, result, temp_result, 0)
	return result
	
	def dfs(reuslt, temp_result, vertex, position):
		if isSolution(vertex, position):
			result.append(temp_result)
		
		for i in range of position:
			dosomething(temp_result, vertex, i)
				dfs(vertex, result, temp_result, i)
			undosomething(temp_result, vertex, i)
	
