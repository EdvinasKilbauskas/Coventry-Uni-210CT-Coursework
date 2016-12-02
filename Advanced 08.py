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

array = []
while True:
	try:
		user_input = input("Please enter a sequence of integers separated by a space: ")
		tokens = user_input.split(' ')
		for i in tokens:
			array.append(int(i))
	except BaseException:
		print("Please make sure that your input is a sequence of integers separated by a space and try again")
		continue
	else:
		break
		
m = 0
while True:
	try:
		m = int(input("Please enter which smallest number you want to get out of this sequence (number id): "))
		if m < 1 or m > len(array):
			  raise ValueError()
	except BaseException:
		print("Number must be an integer between 0 and " + str(len(array)))
		continue
	else:
		break
		

unsorted = array.copy()
quick_sort(array, 0, len(array)-1)

string = 'th'
if m == 1:
	string = 'st'
if m == 2:
	string = 'nd'
if m == 3:
	string = 'rd'

print(str(m) + string + " smallest element out of sequence " + str(unsorted) + " is " + str(array[m-1]))
