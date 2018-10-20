Graph Adjacency list
	
	class AdjList:
		def __init__(self,data):
			self.vertex = data
			self.next = None
		
	class Graph:
		def __init__(self,size):
			self.size = size
			self.graph = [False] * self.size
		
		def add_edge(self, src, dest):
			node = AdjList(src)
			node.next = self.graph[dest]
			self.graph[src] = node
			
			node = AdjList(dest)
			node.next = self.graph[src]
			self.graph[src] = node