#. Implement the structure for an unweighted, undirected graph G, where nodes
#consist of positive integers. Also, implement a function isPath(v, w), where v and w
#are vertices in the graph, to check if there is a path between the two nodes. The
#path found will be printed to a text file as a sequence of integer numbers (the node
#values).

class Node:
	
	def __init__(self, id, neighbour_ids):
		self.id = id
		self.neighbours = neighbour_ids.copy()
		
	def has_neighbour(self, id):
		return id in self.neighbours
		
class Graph:
	
	def __init__(self):
		self.nodes = []
		
	def add_node(self, node):
		self.nodes.append(node)
	
	def is_path(self, start, end):
		path = [start]
		visited = [False for x in range(0,len(self.nodes))]
		visited[start] = True
		current_node = start
		
		while(True):
			if(current_node == end):
				print(path)
				return True
			
			neighbours = self.nodes[current_node].neighbours
			
			
			found = False
			# iterate through all neighbouring nodes
			for node in range(0, len(neighbours)):
				if(visited[node] == False):
					# find new unvisited node
					found = True
					current_node = node
					visited[current_node] = True
					path.push(current_node)
					if(current_node == end):
						print(path)
						return True
										
				
			# if there was no neighbouring nodes, go back one step
			# and repeat the sequence
			if(found == False):
				current_node = path.pop()
				continue
			
			all_visited = True
			for i in visited:
				if(i == False):
					all_visited = False
					break
				
			if(all_visited == True):
				return False
		
	
	def is_connected(self):
		for node in nodes:
			id = node.id
			
	
graph = Graph()
graph.add_node(Node(0,[1,4,3]))
graph.add_node(Node(1,[0,2,5,4]))
graph.add_node(Node(2,[1,4,3]))
graph.add_node(Node(3,[0,4,2]))
graph.add_node(Node(4,[0,2,3,1]))
graph.add_node(Node(5,[1,6]))
graph.add_node(Node(6,[5]))

print(graph.is_path(0,6))