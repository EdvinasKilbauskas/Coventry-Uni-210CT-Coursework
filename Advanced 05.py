#In addition to the normal homework task, write a function that takes four parameters
#representing the constant and multiplier of two linearly growing (as in O(m x n + k) )
#functions and determines the critical value of n (which should be an integer) at
#which the relative run-time of the two algorithms switches. That is, at which input
#size in algorithm A slower than B and at which is B slower than A? Use an iterative
#approach rather than solving the equations.


def Big_O(m1, k1, m2, k2):
	n = 0
	# continues looping until the state changes
	while True:
		# calculates differences between equations at each N value
		dif1 = (m1 * n + k1) - (m2 * n + k2)
		n += 1
		dif2 = (m1 * n + k1) - (m2 * n + k2)

		# if sing of difference before incrementing N is different than after,
		# that means the run-time of the two algorithms swiched and we break out of the loop
		if dif1 <= 0 and dif2 > 0 or \
			dif1 >= 0 and dif2 < 0:
			break

		# limit number of iterations to prevent infinite loops in case there's no run-time switch for the given equations
		if n > 1000:
			return -1

	return n

if __name__ == "__main__":
	while True:
		equation1 = input("Please enter first equation (example: 2 * n + 3): ")
		equation2 = input("Please enter second equation (example: 3 * n + 3): ")

		try:
			equation1_tokens = equation1.split(' ')
			m1 = int(equation1_tokens[0])
			k1 = int(equation1_tokens[4])
			equation2_tokens = equation2.split(' ')
			m2 = int(equation2_tokens[0])
			k2 = int(equation2_tokens[4])
		except BaseException:
			print("Wrong equation format, please see the example and try again. ")
			continue
		else:
			break

	result = Big_O(m1, k1, m2, k2)
	answer = str(result)
	if result == -1:
		answer = "non-existent"

	print("Critical value of N at which " + equation1 + " and " + equation2 + " relative run-times switches is at N = " + answer)