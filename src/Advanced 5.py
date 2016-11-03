#In addition to the normal homework task, write a function that takes four parameters
#representing the constant and multiplier of two linearly growing (as in O(m x n + k) )
#functions and determines the critical value of n (which should be an integer) at
#which the relative run-time of the two algorithms switches. That is, at which input
#size in algorithm A slower than B and at which is B slower than A? Use an iterative
#approach rather than solving the equations.

def Big_O(m1, k1, m2, k2):
	n = 0
	
	while(m1 * n + k1 >= m2 * n + k2):
		n = n + 1
		
	return n

equation1 = input("Please enter first equation (example: 2 * n + 3): ")
equation2 = input("Please enter second equation (example: 2 * n + 3): ")

equation1_tokens = equation1.split(' ')
m1 = int(equation1_tokens[0])
k1 = int(equation1_tokens[4])
equation2_tokens = equation2.split(' ')
m2 = int(equation2_tokens[0])
k2 = int(equation2_tokens[4])

print("Critical value of N at which " + equation1 + " and " + equation2 + " relative run-times switches is N = " + str(Big_O(m1,k1,m2,k2)))