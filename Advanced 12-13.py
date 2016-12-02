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
		self.connected = None
		
	def add_node(self, node):
		self.nodes.append(node)

	# finds a path using modified djikstra's algorithm
	def is_path(self, start, end):
		came_from = [-1 for x in range(0, len(self.nodes))]
		visited = [False for x in range(0, len(self.nodes))]
		visited[start] = True
		# TODO, change distances[x], to distances.get(x, -1)
		distances = dict()
		distances[start] = 0
		current_node_id = start

		while True:
			# set closest_node_distance to infinity (-1)
			# calculates new distances for neighbours
			for neighbour_id in self.nodes[current_node_id].neighbours:
				if not visited[neighbour_id]:
					if distances.get(neighbour_id, -1) == -1 or distances.get(current_node_id, -1) + 1 < distances.get(neighbour_id, -1):
						distances[neighbour_id] = distances.get(current_node_id, -1) + 1
						came_from[neighbour_id] = current_node_id

				closest_node_distance = -1
				closest_node_id = -1
				# unvisited node with shortest distance path
				for j in range(0, len(self.nodes)):
					# if node is unvisited and the distance isn't infinity
					if visited[j] == False and distances.get(self.nodes[j].id, -1) != -1 :
						if closest_node_distance == -1 or distances.get(self.nodes[j].id, -1) <= closest_node_distance:
							closest_node_distance = distances.get(self.nodes[j].id, -1)
							closest_node_id = j

			visited[current_node_id] = True
			current_node_id = closest_node_id

			if current_node_id == -1:
				break

		# checks whether the graph is connected or not
		# by looking if all node distances,
		# if at least a single node doesn't have a distance associated with it
		# it means that it's not connected
		self.connected = True
		for i in distances:
			if i == -1:
				self.connected = False

		# builds a path from start to end nodes
		path = [end]
		while True:
			path.insert(0,came_from[path[0]])
			if path[0] == start:
				return path
			elif path[0] == -1:
				return None

	def is_connected(self):
		if len(self.nodes) == 0:
			return False
		else:
			# is_path() checks whether graph is strongly connected or not
			self.is_path(0,0)
			return self.connected
			
if __name__ == "__main__":
	graph = Graph()
	graph.add_node(Node(0,[1,4,3]))
	graph.add_node(Node(1,[0,2,5,4,10]))
	graph.add_node(Node(2,[1,4,3]))
	graph.add_node(Node(3,[0,4,2]))
	graph.add_node(Node(4,[0,2,3,1]))
	graph.add_node(Node(5,[1,6]))
	graph.add_node(Node(6,[5,7]))
	graph.add_node(Node(7,[6,8]))
	graph.add_node(Node(8,[7,9]))
	graph.add_node(Node(9,[10,8]))
	graph.add_node(Node(10,[9]))

	print("Strongly connected: " + str(graph.is_connected()))
	print("See path_output.txt for path")
	f = open("path_output.txt",'w')
	f.write(str(graph.is_path(0,6)))