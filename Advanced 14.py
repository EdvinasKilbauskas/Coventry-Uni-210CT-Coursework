# Consider the structure of a undirected weighed graph. Implement an algorithm to find
# its maximum cost spanning tree. The output should be the pre-order and post-order
# traversal of the tree. Describe the running time of this algorithm.


class GraphNode:
	def __init__(self, id, neighbours):
		self.id = id
		self.neighbours = neighbours.copy()

	def has_neighbour(self, id):
		return id in self.neighbours


class TreeNode:
	def __init__(self, value):
		self.left = None
		self.right = None
		self.value = value

	# recursive function, digs down into a tree, finds an empty slot and inserts the value
	def insert(self, value):
		if self.value == value:
			return False

		if self.value > value:
			if self.left:
				return self.left.insert(value)
			else:
				self.left = TreeNode(value)
				return True
		else:
			if self.right:
				return self.right.insert(value)
			else:
				self.right = TreeNode(value)
				return True


	def preorder(self):
		# check if node is null
		if self:
			print(str(self.value))
			if self.left:
				self.left.preorder()
			if self.right:
				self.right.preorder()

	def postorder(self):
		if self:
			if self.left:
				self.left.postorder()
			if self.right:
				self.right.postorder()
			print(str(self.value))


class GraphEdge:
	def __init__(self, node1_id, node2_id, weight):
		self.node1_id = node1_id
		self.node2_id = node2_id
		self.weight = weight

	def __str__(self):
		return str(self.weight) + ": " + str(self.node1_id) + ", " + str(self.node2_id)


class Tree:
	def __init__(self):
		self.first = None

	def insert(self, value):
		if self.first is None:
			self.first = TreeNode(value)
			return True
		else:
			return self.first.insert(value)

	def preorder(self):
		self.first.preorder()

	def postorder(self):
		self.first.postorder()


class Graph:
	def __init__(self):
		self.edges = []
		self.nodes = []

	# returns the edges of the maximum spanning tree in ascending order by edge weight
	def maximum_spanning_tree(self):
		i = 0
		while i < len(self.edges):
			self.sort_edges()
			edge = self.edges[0]
			self.edges.remove(edge)
			if not self.is_connected():
				self.add_edge(edge)
			i += 1

		tree = Tree()
		for i in self.edges:
			tree.insert(i.node1_id)
			tree.insert(i.node2_id)

		return tree

	# uses Djikstra's algorithm to find whether the graph is connected or not
	def is_connected(self):
		if len(self.nodes) == 0:
			return False

		start = self.nodes[0].id
		came_from = [-1 for x in range(0, len(self.nodes))]
		visited = [False for x in range(0, len(self.nodes))]
		visited[start] = True
		distances = dict()
		distances[start] = 0
		current_node_id = start

		while True:
			# set closest_node_distance to infinity (-1)
			# calculates new distances for neighbours
			for neighbour_id in self.nodes[current_node_id].neighbours:
				if not visited[neighbour_id]:
					# distances.get() returns a value for key neighbours_id, if there's no such key, returns -1
					if distances.get(neighbour_id, -1) == -1 or distances.get(current_node_id, -1) + 1 < distances.get(neighbour_id, -1):
						distances[neighbour_id] = distances.get(current_node_id, -1) + 1
						came_from[neighbour_id] = current_node_id

				closest_node_distance = -1
				closest_node_id = -1
				# unvisited node with shortest distance path
				for j in range(0, len(self.nodes)):
					# if node is unvisited and the distance isn't infinity
					if visited[j] is False and distances.get(self.nodes[j].id, -1) != -1:
						if closest_node_distance == -1 or distances.get(self.nodes[j].id, -1) <= closest_node_distance:
							closest_node_distance = distances.get(self.nodes[j].id, -1)
							closest_node_id = j

			visited[current_node_id] = True
			current_node_id = closest_node_id

			if current_node_id == -1:
				break

		# checks whether the graph is connected or not
		# by looking at all node distances,
		# if at least a single node doesn't have a distance associated with it
		# it means that it's not connected
		connected = True
		for i in distances:
			if i == -1:
				connected = False

		return connected

	# sorts edges in ascending order
	def sort_edges(self):
		while True:
			finished = True
			for i in range(0, len(self.edges) - 1):
				edge1 = self.edges[i]
				edge2 = self.edges[i + 1]
				if edge1.weight > edge2.weight: # change > to < for descending order
					self.edges[i] = edge2
					self.edges[i + 1] = edge1
					finished = False
			if finished:
				break

	# adds/updates nodes and their neighbours from the given edge
	def add_nodes(self, edge):

		# finds if either nodes of the edge are in the node list already
		# if so, adds node as a neighbour
		found_node1 = False
		found_node2 = False
		for node in self.nodes:
			if node.id == edge.node1_id:
				node.neighbours.append(edge.node2_id)
				found_node1 = True
			if node.id == edge.node2_id:
				node.neighbours.append(edge.node1_id)
				found_node2 = True

		if not found_node1:
			self.nodes.append(GraphNode(edge.node1_id, [edge.node2_id]))
		if not found_node2:
			self.nodes.append(GraphNode(edge.node2_id, [edge.node1_id]))

	# removes node neighbours associated with the edge
	def remove_nodes(self, edge):
		# removes associations b
		for node in self.nodes:
			if node.id == edge.node1_id:
				node.neighbours.remove(edge.node2_id)
			if node.id == edge.node2_id:
				node.neighbours.remove(edge.node1_id)

	def remove_edge(self, edge):
		if edge in self.edges:
			self.edges.remove(edge)
			self.remove_nodes(edge)

	def add_edge(self, new_edge):

		replaced = False
		# searches for edges with same nodes, if it finds one, it updates it with new one
		# this is because we don't want to have same two nodes connected with multiple edges with different weights
		for i in range(0, len(self.edges)):
			edge = self.edges[i]
			if (edge.node1_id == new_edge.node1_id and edge.node2_id == new_edge.node2_id) or \
				(edge.node1_id == new_edge.node2_id and edge.node2_id == new_edge.node1_id):
				self.edges[i] = new_edge
				replaced = True

		if not replaced:
			self.edges.append(new_edge)
			self.add_nodes(new_edge)

graph = Graph()
graph.add_edge(GraphEdge(0, 1, 100))
graph.add_edge(GraphEdge(0, 2, 50))
graph.add_edge(GraphEdge(0, 3, 60))
graph.add_edge(GraphEdge(0, 4, 3))
graph.add_edge(GraphEdge(0, 5, 150))
graph.add_edge(GraphEdge(1, 2, 10))
graph.add_edge(GraphEdge(1, 5, 10))
graph.add_edge(GraphEdge(2, 3, 2))
graph.add_edge(GraphEdge(3, 4, 80))
graph.add_edge(GraphEdge(4, 5, 5))

spanning_tree = graph.maximum_spanning_tree()
print("Maximum cost spanning tree node ids in pre-order: ")
spanning_tree.preorder()
print("Maximum cost spanning tree node ids in post-order: ")
spanning_tree.postorder()


