#Adapt the quick sort algorithm to find the mth smallest element out of a sequence of
#n integers. 

def partition(A, lo, hi):
	
	pivot = A[lo]
	i = lo - 1
	j = hi + 1
	while True:
	
		i = i + 1
		while A[i] < pivot:
			i = i + 1
		
		j = j - 1
		while A[j] > pivot:
			j = j - 1
		
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
      

        
array = [3,4,8,1,75,3,54,362,23]

quick_sort(array, 0, len(array)-1)

print(str(array))