import sys
from random import random


class Matrix:

	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns
		self.compressed_data = {}

	def __str__(self):
		string = ''
		for y in range(0, self.rows):
			for x in range(0, self.columns):
				string += str(self.get(y,x)) + " "
			string += '\n'
		string += ''
		return string

	# takes an array of size self.rows*self.columns
	def set_data(self, data):
		if len(data) != self.rows*self.columns:
			raise ValueError("passed array is of invalid size")
		
		self.compressed_data = {}
		for i in range(0, self.rows*self.columns):
			value = data[i]
			if value != 0:
				self.compressed_data[i] = value

	# takes a matrix object, returns a dot product as a result
	def dot(self, other):
		if self.columns != other.rows:
			raise ValueError("matrix size mis-match")
			return self
		
		new_matrix = Matrix(self.rows, other.columns)

		for i in range(0, self.rows):
			for j in range(0, other.columns):
				new_value = 0
				for k in range(0, self.columns):
						matrix1_value = self.get(i, k)
						matrix2_value = other.get(k, j)
						new_value += matrix1_value * matrix2_value
				new_matrix.set(i, j, new_value)

		return new_matrix

	# takes a matrix object, returns result
	def sub(self, other):
		if self.rows != other.rows and self.columns != other.columns:
			raise ValueError("matrix size mis-match")

		new_matrix = Matrix(self.rows, self.columns)
		for i in range(0, len(self.data)):
			new_matrix.data[i] = other.data[i] - self.data[i]

		return new_matrix

	# takes a matrix object, returns result
	def add(self, other):
		if self.rows != other.rows and self.columns != other.columns:
			raise ValueError("matrix size mis-match")

		new_matrix = Matrix(self.rows, self.columns)
		for i in range(0, len(self.data)):
			new_matrix.data[i] = other.data[i] + self.data[i]

		return new_matrix

	# checks whether element at the given position exists, if it does then it returns the element,
	# if not, assumes it is zero and returns 0
	def get(self, row, column):
		id = row * self.columns + column
		if id in self.compressed_data:
			return self.compressed_data[id]
		else:
			return 0

	# puts the element in the matrix
	def set(self, row, column, value):
		id = row * self.columns + column
		self.compressed_data[id] = value

# memory usage comparison test
if __name__ == "__main__":
	raw_data = []
	for i in range(0, 1000*1000):
		# 97% of elements in the matrix are non-zero
		if random() > 0.97:
			raw_data.append(1)
		else:
			raw_data.append(0)
			
	a = Matrix(1000,1000)
	a.set_data(raw_data)

	compressed_size = sys.getsizeof(a.compressed_data)
	uncompressed_size = sys.getsizeof(raw_data)
	size_difference = (uncompressed_size/compressed_size)*100   # in percents
	print("1000x1000 element matrix (with 3% of elements being non-zero) memory usage comparison:")
	print("Uncompressed matrix size: \t" + str(uncompressed_size) + " bytes")
	print("Compressed matrix size: \t" + str(compressed_size) + " bytes (" + ('%.0f' % size_difference) + "% less memory usage)")
