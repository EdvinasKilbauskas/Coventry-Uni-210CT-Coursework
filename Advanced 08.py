#Adapt the quick sort algorithm to find the mth smallest element out of a sequence of
#n integers. 


def partition(A, lo, hi):
	pivot = A[lo]
	i = lo - 1
	j = hi + 1
	while True:
		i += 1
		while A[i] < pivot:
			i += 1
		j -= 1
		while A[j] > pivot:
			j -= 1
		if i >= j:
			return j
		a1 = A[i]
		a2 = A[j]
		A[i] = a2
		A[j] = a1


def quick_sort(sequence, lo, hi):
	if lo < hi:
		p = partition(sequence, lo, hi)
		quick_sort(sequence, lo, p)
		quick_sort(sequence, p + 1, hi)

while True:
	try:
		user_input = input("Please enter a sequence of integers separated by a space: ")
		tokens = user_input.split(' ')
		array = []
		for i in tokens:
			array.append(int(i))
	except BaseException:
		print("Please make sure that your input is a sequence of integers separated by a space and try again")
		continue
	else:
		break

if __name__ == "__main__":
	quick_sort(array, 0, len(array)-1)
	print("Sorted using quick sort: " + str(array))