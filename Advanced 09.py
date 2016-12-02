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
						value1 = matrix1[i * size + k]
						value2 = matrix2[k * size + j]
						new_value += value1 * value2
				new_matrix_data[i * size + j] = new_value
	return new_matrix_data

if __name__ == "__main__":
	matrix = []
	power = 0
	# received user input
	while True:
		try:
			matrix = [int(x) for x in input("Enter square matrix data (sequence of space separated integers): ").split(' ')]
		except BaseException:
			print("Make sure that a matrix is a sequence of space separated integers. Try again.")
			continue

		# if matrix is not square matrix, print error, continue getting user input
		if int(sqrt(len(matrix))) != sqrt(len(matrix)):
			print("Not a square matrix. Try again.")
			continue

		try:
			power = int(input("To which power should the matrix be raised?: "))
			if power <= 0:
				raise ValueError("Power must be a positive integer")
		except BaseException:
			print("Make sure that a power is a single positive integer. Try again.")
			continue

		break

	# calculates new matrix and prints it
	new_matrix = square_matrix_pow(matrix,power)
	matrix_size = sqrt(len(new_matrix))
	print("Your matrix raised to the power of " + str(power) + ": ")
	for i in range(0, int(matrix_size)):
		print('|', end='')
		for j in range(0, int(matrix_size)):
			id = i*int(matrix_size) + j
			print("%6.0f " % new_matrix[id], end='')
		print('|')