#Let's consider a labyrinth as a n � m matrix, where the corridors are denoted by 1s
#situated in consecutive positions on the same line or column. The rest of the
#elements are 0. Within the labyrinth, a person is considered to be in position (i, j).
#Write a program that lists all exit routes which do not pass the same place twice.
#Input: n, m, the rows of the matrix, the coordinates of the exit and the coordinates of
#the person (row, column). Output: a sequence of row/column pairs representing the
#person's successive position.

from math import *


class Node:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y

	def __hash__(self):
		return hash(tuple((self.x, self.y)))

	def __str__(self):
		return "x:" + str(self.x) + " y:" + str(self.y)


class Labyrinth:
	"""As a constructior it takes a 2D array with 0's where the robot can go and 1's where it cant"""

	def __init__(self, data):
		self.data = data

	def find_paths(self, start, goal):
		width = len(self.data)
		height = len(self.data[0])
		closed = []
		# Set of discovered nodes to be evaluated
		open = [start]
		came_from = dict()
		# distance from start to key node
		g_score = dict()
		# total estimated cost to goal from key node
		f_score = dict()

		g_score[start] = 0
		f_score[start] = self.heuristic_distance(start, goal)

		keep_looping = True
		while keep_looping:
			current = self.find_node_closest_to_goal(open, f_score)
			if current.x == goal.x and current.y == goal.y:
				return self.build_path(came_from, goal)

			open.remove(current)
			closed.append(current)

			neighbors = self.get_neighbours(current)

			for neighbor in neighbors:
				if neighbor in closed:
					continue
				tentative_g_score = g_score[current] + 1  # 1 being distance between nodes
				if neighbor not in open:
					open.append(neighbor)
				elif tentative_g_score >= g_score[neighbor]:
					continue
				# if it got here that means it is the best possible route
				came_from[neighbor] = current
				g_score[neighbor] = tentative_g_score
				f_score[neighbor] = g_score[neighbor] + self.heuristic_distance(neighbor, goal)
			if not open:
				keep_looping = False

		return False

	def get_neighbours(self, node):
		neighbors = []
		if node.x > 0:
			if self.data[node.x - 1][node.y] == 0:
				neighbors.append(Node(node.x - 1, node.y))
		if node.y > 0:
			if self.data[node.x][node.y - 1] == 0:
				neighbors.append(Node(node.x, node.y - 1))
		if node.x != width - 1:
			if self.data[node.x + 1][node.y] == 0:
				neighbors.append(Node(node.x + 1, node.y))
		if node.y != height - 1:
			if self.data[node.x][node.y + 1] == 0:
				neighbors.append(Node(node.x, node.y + 1))

		return neighbors

	def heuristic_distance(self, start, end):
		x = abs(start.x - end.x)
		y = abs(start.y - end.y)
		return sqrt(x * x + y * y)

	def find_node_closest_to_goal(self, open_set, dic):
		lowest_val = None
		lowest_key = ""

		# for all nodes which are open (univisited)
		for val in open_set:
			score = dic[val]
			if lowest_val is None or score < lowest_val:
				lowest_key = val
				lowest_val = score
		return lowest_key

	# build a reversed path
	def build_path(self, came_from, last_node):
		path = [last_node]
		while last_node in came_from:
			last_node = came_from[last_node]
			path.insert(0, last_node)      # insert node into beginning to get reversed list
		return path

	def __str__(self):
		string = ""
		width = len(self.data[0])
		height = len(self.data)
		for y in range(0, height):
			for x in range(0, width):
				string += str(self.data[x][y])
			string += '\n'
		return string

if __name__ == '__main__':
	# gets labyrinth's size and handles input errors
	while True:
		try:
			user_input = input("Specify the width and height of the labyrinth (example: 5 5): ")
			width = int(user_input.split(' ')[0])
			height = int(user_input.split(' ')[1])
		except BaseException:
			print("Wrong format. Please see example and try again.")
			continue
		else:
			break

	labyrinth_data = [[0 for x in range(0, width)] for y in range(0, height)]

	# gets labyrinth's data and handles input errors
	for y in range(0,height):
		while True:
			try:
				user_input = input("Enter data for the row nr. " + str(y+1) + " of the labyrinth: ")
				if len(user_input) != width:
					print("Width of this row doesn't match the width you have specified earlier. Please try again with " + str(width) + " characters in a row")
					continue
				for x in range(0,len(user_input)):
					if user_input[x] != '0' and user_input[x] != '1':
						raise ValueError()

					labyrinth_data[x][y] = int(user_input[x])
			except ValueError:
				print("Labyrinth data can only contain 1's (for walls) and 0's (for empty space). Please try again.")
				continue
			except Exception:
				print("Something went wrong with the data you typed. Try again.")
				continue
			else:
				break

	# gets person's coordinates and handles input errors
	while True:
		try:
			user_input = input("Specify the starting coordinates of the person (example: 2 0): ")
			start = Node(int(user_input.split(' ')[0]), int(user_input.split(' ')[1]))
		except BaseException:
			print("Wrong format. Please see example and try again.")
			continue
		else:
			break

	# gets exit coordinates and handles input errors
	while True:
		try:
			user_input = input("Specify the coordinates of the exit (example: 0 4): ")
			exit = Node(int(user_input.split(' ')[0]), int(user_input.split(' ')[1]))
		except BaseException:
			print("Wrong format. Please see example and try again.")
			continue
		else:
			break

	# creates a labyrinth, finds paths and displays them
	labyrinth = Labyrinth(labyrinth_data)
	for x in range(0, width):
		for y in range(0, height):
			if labyrinth_data[x][y] == 1:
				labyrinth.data[x][y] = '*'

	print()
	path_no = 0
	while True:
		path_found = labyrinth.find_paths(start, exit)
		print("-" * 20)
		if path_found:
			path_no += 1
			print("Path number " + str(path_no) + " (excluding start/end coordinates): ")
			for i in range(1, len(path_found)-1):
				point = path_found[i]
				labyrinth.data[point.x][point.y] = path_no
				print("step " + str(i) + " - " + str(point))

		else:
			if path_no == 0:
				print("No path found")
			break

	if path_no > 0:
		labyrinth.data[start.x][start.y] = 'S'
		labyrinth.data[exit.x][exit.y] = 'X'

		print()
		print("Labyrinth with paths visualized: ")
		print("[S] - person starting position (" + str(start.x) + ", " + str(start.y) + ")")
		print("[X] - exit position (" + str(exit.x) + ", " + str(exit.y) + ")")
		print("[*] - wall")
		print("[0] - empty space")
		print("[any number] - the ID of the drawn path")
		print()
		print(str(labyrinth))

