#Consider having n cubes, each being characterized by their edge length and their
#colour. Use the cubes (not necessarily all of them) in order to build a tower of
#maximum height, under the following conditions:
# a) any two neighbouring cubes must be of different colours.
# b) the edge length of a cube is lower than the edge length of the cube placed
#below it.

from random import random

class Cube:
	color_names = ["Red","Green","Blue","Orange","Yellow","Purple"]
	
	def __init__(self, size, color):
		self.size = size
		self.color = color
		
	def __str__(self):
		return "Size: " + str(self.size) + ", color: " + str(self.color_names[self.color]) 

"""
	Sorts cubes by size in ascending order using bubble sort
"""
def sort_cubes(cubes):
	while True:
		
		finished = True
		for i in range(0, len(cubes)-1):
			cube1 = cubes[i]
			cube2 = cubes[i+1]
			
			if(cube2.size > cube1.size):
				cubes[i] = cube2
				cubes[i+1] = cube1
				finished = False
				
		if(finished == True):
			break
		
	return cubes

def generate_random_cubes(n):
	return [Cube(int(random()*10)+1, int(random()*6)) for x in range(0, n)]


def build_cube_tower(n):
	cubes = generate_random_cubes(n)
	sort_cubes(cubes)
	cube_tower = []
	
	for cube in cubes:
		# if there are no cubes in tower, add the first cube from sorted list (largest cube first)
		if(len(cube_tower) == 0):
			cube_tower.append(cube)
		else:
			if(cube.color != cube_tower[len(cube_tower)-1].color and \
			   cube.size < cube_tower[len(cube_tower)-1].size):
				cube_tower.append(cube)
			
	return cube_tower
	
	
if __name__ == "__main__":
	n = int(input("Enter an number of cubes to be generated: n = "))

	tower = build_cube_tower(n)

	print("Cube tower generated: ")
	print("-"*50)
	size = 0
	for i in range(0, len(tower)):
		print("Cube nr. " + str(i+1) + ": " + str(tower[i]))
		size += tower[i].size
	print("-"*50)
	print("Total tower size: " + str(size))
