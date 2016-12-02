#Using the model of a circular single-linked list, implement the following scenario: 
#N children stand in a circle; one of the children starts counting the others clockwise.
#Every Nth child leaves the game. The winner is the one who remains.
#Notes: Read the number of children, the childrens' names and the one starting to
#count from the standard input. Input: 4; Diana, Michael, David, Mary; Start: Diana;
#Winner: Michael.

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		
	def set_next(self, next):
		self.next = next
	
	def set_data(self, data):
		self.data = data

	def __str__(self):
		return "Node " + str(self.data) + ", next: " + str(self.next.data)
		
class LinkedList:
	def __init__(self):
		self.first = None
		
	def insert_after(self, node, new_node):
		# if list is empty
		if node is None:
			new_node.next = new_node
		else:
			new_node.next = node.next
			node.next = new_node

	def find(self, value):
		node = self.first
		if node is None:
			return None
		
		while True:	
			if node.data == value:
				return node
			node = node.next

	def remove_after(self, node):
		if node is None:
			return False
		# if this node points to itself, means it's the last node
		elif node.next == node:
			# list marked as empty
			node.next = None
			return True
		else:
			if node.next is None:
				return False
			node.next = node.next.next
			return True
		
if __name__ == "__main__":
	names = str()
	# gets user input
	while True:
		try:
			names = input("Input the names of the children (separated by spaces): ").split(" ")
		except BaseException:
			print("Bad input. Please make sure names are separated by spaces and try again.")
			continue
		else:
			break

	n = 0
	while True:
		try:
			n = int(input("Every N'th child leaves the game, N = ?: "))
			if n <= 0:
				raise ValueError()
		except BaseException:
			print("N must be a positive integer. Try again.")
			continue
		else:
			break

	starting_child_name = str()
	while True:
		starting_child_name = input("Who starts the game?: ")
		if starting_child_name not in names:
			print(starting_child_name + " is not in the game. Try again.")
			continue
		else:
			break

	# populates the linked list with children names
	children = LinkedList()
	children.first = Node(names[0])
	children.first.next = children.first
	node = children.first
	for i in range(1, len(names)):
		children.insert_after(node, Node(names[i]))
		node = node.next
	# last element points to first element in the list
	node.next = children.first
	
	count_to_removal = n-1
	node = children.find(starting_child_name)
	# the main game calculation loop
	while True:
		count_to_removal -= 1
		if count_to_removal == 0:
			removed = children.remove_after(node)
			count_to_removal = n-1
		# if there's only one node left, finish
		if node == node.next:
			break
		# iterates to next node
		node = node.next

	print("Winner: " + node.data)
