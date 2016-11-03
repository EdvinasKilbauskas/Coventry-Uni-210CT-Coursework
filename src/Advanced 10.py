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
		self.data = next
		
class LinkedList:
	def __init__(self):
		self.first = None
		
	def insert_after(self, node, new_node):
		# if list is empty
		if node == None:
			new_node.next = new_node
		else:
			new_node.next = node.next
			node.next = new_node

	def find(self, value):
		node = self.first
		if(node == None):
			return None
		
		while True:	
			if(node.data == value):
				return node
			node = node.next
				 
	def remove_after(self, node):
		if(node == None):
			return False
		# if this node points to itself, means it's the last node
		elif(node.next == node):
			# list marked as empty
			node.next = None
			return True
		else:
			if(node.next == None):
				return False
			node.next = node.next.next
			return True
		
if __name__ == "__main__":
	
	# gets user input
	names = input("Input the names of the children: ").split(" ")
	n = int(input("Every N'th child leaves the game, N = ?: "))
	starting_child_name = input("Who starts the game?: ")

	if starting_child_name in names == False:
		print(starts + " is not in the game.")

	# populates the linked list with children names
	children = LinkedList()
	
	children.first = Node(names[0])
	children.first.next = children.first
	
	node = children.first
	
	for i in range(1, len(names)):
		children.insert_after(node, Node(names[i]))
		node = node.next
		
	node.next = children.first
	
	counter = n
	node = children.find(starting_child_name)

	# the main game calculation loop
	for i in range(0, 10):
		#if(node != None):
		#	print(str(node.data))
			
		if(counter == 1):
			removed = children.remove_after(node)
			
			if(removed == True):
				print("Removed: " + str(node.data))
				counter = n
			else:
				print("Couldn't remove")
			
		counter -= 1
				
		# iterates to next node
		node = node.next
		
		
		
