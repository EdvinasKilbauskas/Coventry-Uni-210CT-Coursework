#Write a function to calculate the kth power of a square matrix, using pointers to
#access to the elements of the matrix. The resulted matrix will be displayed in natural
#form. 
from math import sqrt

def square_matrix_pow(matrix, power):
	new_matrix = matrix

	while power > 1:
		new_matrix = square_matrix_dot(new_matrix,matrix)
		power -= 1
		
	return new_matrix

def square_matrix_dot(matrix1, matrix2):
	size = int(sqrt(len(matrix1)))
	
	new_matrix_data = [0 for i in range(0,size*size)]
	
	for i in range(0, size):
		for j in range(0, size):
				new_value = 0
				for k in range(0, size):
						value1 = matrix1[i * size + k]#(i,k)
						value2 = matrix2[k * size + j]#(k,j)
						new_value += value1 * value2
				new_matrix_data[i * size + j] = new_value
				
	return new_matrix_data


matrix = []
matrix_size = 0
power = 0

while True:
	matrix = [float(x) for x in input("Enter square matrix data: ").split(' ')]
	
	matrix_size = sqrt(len(matrix))
	# if matrix is a square matrix, exit loop
	if(int(matrix_size) != matrix_size):
		print("Error: not a square matrix. Try again.")
		continue
	
	power = int(input("To which power should the matrix be raised?: "))
	
	break
		
new_matrix = square_matrix_pow(matrix,power)

print("Given matrix raised to the power of " + str(power) + ": ")

for i in range(0, int(matrix_size)):
	for j in range(0, int(matrix_size)):
		id = i*int(matrix_size) + j
		print("%6.2f " % new_matrix[id] , end = '')
		
	print()