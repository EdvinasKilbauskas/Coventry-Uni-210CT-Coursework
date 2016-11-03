#Write the pseudocode for a recursive program to generate the Cartesian product (product set, direct
#product, cross product) of N sets 

def CARTESIAN_PRODUCT(*sets):
	if not sets:
		return [[]]
	else:
		return [[x] + p for x in sets[0] for p in CARTESIAN_PRODUCT(*sets[1:])]
		
	
	
print(str(CARTESIAN_PRODUCT([1,2,3],[1,2,3],[1,2,3],[45,64,34])))