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
			

	def set_data(self, data):
		if (len(data) != self.rows*self.columns):
			print("Error Matrix.set_data(): passed array is of invalid size")
		
		self.compressed_data = {}
		for i in range(0, self.rows*self.columns):
			value = data[i]
			if value != 0:
				self.compressed_data[i] = value
				

	def dot(self, other):
		if(self.columns != other.rows):
			print("Error Matrix.dot(): matrix size mis-match")
			return self
		
		new_matrix = Matrix(self.rows, other.columns)

		for i in range(0, self.rows):
			for j in range(0, other.columns):
				new_value = 0
				for k in range(0, self.columns):
						matrix1_value = self.get(i,k)
						matrix2_value = other.get(k,j)
						new_value += matrix1_value * matrix2_value
				new_matrix.set(i,j, new_value)

		return new_matrix

	def subtract(self, other):
		if(self.rows != other.rows and self.columns != other.columns):
			print("Error Matrix.subtract(): matrix size mis-match")

		new_matrix = Matrix(self.rows, self.columns)
        
		for i in range(0, len(self.data)):
			new_matrix.data[i] = other.data[i] - self.data[i]

		return new_matrix

	def get(self, row, column):
		id = row * self.columns + column
		if id in self.compressed_data:
			return self.compressed_data[id]
		else:
			return 0

	def set(self, row, column, value):
		id = row * self.columns + column
		self.compressed_data[id] = value

# unit test
if __name__ == "__main__":
	data = []
	for i in range(0, 1000*1000):
		if random() > 0.95:
			data.append(100)
		else:
			data.append(0)
			
	a = Matrix(1000,1000)
	a.set_data(data)
	b = Matrix(1000,1000) 
	b.set_data(data)
	
	print("Compressed matrix size: " + str(sys.getsizeof(a.compressed_data)) + " bytes")
	print("Uncompressed matrix size: " + str(sys.getsizeof(data)) + " bytes")
	
	