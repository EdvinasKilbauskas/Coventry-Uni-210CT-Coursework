#Write the pseudocode for a recursive program to generate the Cartesian product (product set, direct
#product, cross product) of N sets 

# takes an array of sets, for example [[1,2,3],[1,2,3]]
def cartesian_product(sets):
	if not sets:
		return [[]]
	else:
		list = []
		for x in sets[0]:
			new_sets = sets[1:]
			for p in cartesian_product(new_sets):
				list.append([x] + p)
		return list

#// takes a list of sets, example [[1,2,3],[1,2,3]]
#CARTESIAN_PRODUCT(sets)
#	if sets.length = 0
#		return empty list
#	else
#       list <- empty list
#       for all elements i in sets[0]
#           new_sets <- sets, but with first element removed
#			for all sets j in cartesian_product(new_sets)
#				x <- i converted to a list      // single int/float i is converted into a list of one element
#               append all elements of j to x   // add elements from
#				append x to list
#		return list


if __name__ == "__main__":
	print(str(cartesian_product([[1,2,3],[1,2,3]])))