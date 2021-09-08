import collections

# BFS algorithm
def bfs(graph, root):
	path = list()
	visited, queue = list(), collections.deque([root])
	visited.append(root)


	while queue:

		# Dequeue a vertex from queue
		vertex = queue.popleft()
		
		for neighbour in graph[vertex]:
			
			if neighbour not in visited:
				visited.append(neighbour)
				queue.append(neighbour)
				path.append((vertex,neighbour))
				
			
	print(path)	
	return path


				

	
def detectCycle(graph,root):
	
	edges = bfs(graph, root)
	parent = dict()
	for edge in edges:
		parent[edge[1]] = edge[0]
	print(parent)
	queue = collections.deque(graph.keys())
	while queue:
		vertex = queue.popleft()
		for neighbour in graph[vertex]:
			print(neighbour)
			if neighbour!=root and parent.get(neighbour) !=vertex and parent.get(vertex)!=neighbour:
				print("cycle detected")
				edges.append((neighbour,vertex))
				print(edges)
				return edges
	


if __name__ == '__main__':
	# graph = {1: [2], 2: [5,3], 3: [4,2], 4: [3, 6],5:[2,6],6:[4,5]}
	graph = {0:[1,2],2:[0,1],1:[0,2,3],3:[1]}
	print("Following is Breadth First Traversal: ")
	edges = detectCycle(graph,3)
	


	