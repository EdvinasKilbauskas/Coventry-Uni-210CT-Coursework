#Build a Binary Search Tree (BST) to hold English language words in its nodes. Use
#a paragraph of any text in order to extract words and to determine their frequencies.
#Input: You should read the words and frequencies from a file in a suitable format,
#such as .csv. The following tree operations should be implemented: a) Listing (word,
#frequency) pairs for each of the tree nodes. b) Printing the tree in preorder. C)
#Finding a word. Regardless whether found or not found your program should output
#the path traversed in determining the answer, followed by yes if found or no,
#respectively.

class Node:
	def __init__(self, key, value):
		self.left = None
		self.right = None
		self.value = value
		self.key = key
	
	# recursive function, digs down into a tree, finds an empty slot and inserts the value
	def insert(self, key, value):
		if self.key == key:
			return False
		
		if self.key > key:
			if self.left:
				return self.left.insert(key, value)
			else:
				self.left = Node(key, value)
				return True
		else:
			if self.right:
				return self.right.insert(key, value)
			else:
				self.right = Node(key, value)
				return True
			
	def find(self, key):
		print(self.key)
		if(self.key == key):
			return True
		
		elif self.key > key:
			if self.left:
				return self.left.find(key)
			else:
				return False
		else:
			if self.right:
				return self.right.find(key)
			else:
				return False
			
	def list(self):
		if self:
			print("(" + str(self.key) + ", " + str(self.value) + ")")
			if self.left:
				self.left.list()
			if self.right:
				self.right.list()
			
	def preorder(self):
		if self:
			print(str(self.key))
			if self.left:
				self.left.preorder()
			if self.right:
				self.right.preorder()
			

class BinarySearchTree:
	def __init__(self):
		self.first = None
	
	def insert(self,key, value):
		if self.first == None:
			self.first = Node(key, value)
			return True
		else:
			return self.first.insert(key, value)
	
	def preorder(self):
		self.first.preorder()
		
	def list(self):
		self.first.list()
	
	#  Regardless whether found or not found your program should output
	# the path traversed in determining the answer, followed by yes if found or no,
	# respectively.
	def find(self, key):
		if self.first:
			return self.first.find(key)
		else:
			return False
		
# words.csv structure example:
#------------
# dog,10
# cat,15
# lion,4
#------------
def create_tree_from_file(filename):
	f = open(filename, 'r')
	data = f.read()
	while '\n' in data:
		data = data.replace('\n',',')
	
	data = data.split(',')
	
	new_tree = BinarySearchTree()
	for i in range(0, len(data),2):
		new_tree.insert(data[i],data[i+1])
	
	return new_tree
	

bst = create_tree_from_file("words.csv")
print("Tree listed (word, frequency): ")
bst.list()
print("Tree in preorder: ")
bst.preorder()

word_to_find = input("Please enter a word to find: ")
print("Finding word \"" + word_to_find+ "\"... Path:")
found = bst.find(word_to_find)
if found:
	print("Word found!")
else:
	print("Word wasn't found")