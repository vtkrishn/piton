Trasitive Closure
	
	def drive(vertex):
		tc = [[0 for j in range(self.V)] for i in range(self.V)] 
		
		for i in (self.V):
			dfs(i, i,tc)

        print tc
        
	def dfs(s,v,tc):
		tc[s][v] = 1
		
		for i in v:
			if tc[s][i] == 0:
				dfs(s, i,tc)
		
		
		
		