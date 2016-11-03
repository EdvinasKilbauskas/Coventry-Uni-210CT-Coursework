#Given two strings of n and m integer elements, write the pseudocode to compute:
#a) The string that contains all the elements belonging to both strings.
#b) The string of all the elements of the two given strings, written once.
#c) The string of the elements from the first string, without the elements that are also
#in the second string.
#What's the run time?

# O(n*n)
#FUNCTION_A(string1, string2)
#	new_string <- ''
#	
#	for i <- in string1.length
#		for j in string2.length
#			if string1[i] = string2[j]
#				append string1[i] to new_string
#
#return new_string

def functionA(string1, string2):
	new_string = ""
	
	for i in string1:
		for j in string2:
			if i == j:
				new_string += i
#				break		uncomment to remove repeating characters
						
	return new_string

#FUNCTION_B(string1, string2)
#	new_string <- ''
#	
#	both_strings <- append string2 to string1
#	
#	for i <- in both_strings.length
#		add <- True
#		for j in new_string.length
#			if both_strings[i] = new_string[j]
#				add <- False
#		if add = True
#			append both_strings[i] to new_string
#				
#	return new_string


def functionB(string1, string2):
	new_string = ""
	
	both_strings = string1 + string2
	
	for i in both_strings:
		add = True
		for j in new_string:
			if i == j:
				add = False
		if add == True:
			new_string += i
	
	return new_string

#FUNCTION_C(string1, string2)
#	new_string <- ''
#
#	for i <- in string1.length
#		add <- True
#		for j in string2.length
#			if string1[i] = string2[j]
#				add <- False
#		if add = True
#			append string1[i] to new_string
#				
#	return new_string

def functionC(string1, string2):
	new_string = ""
	
	for i in string1:
		add = True
		for j in string2:
			if i == j: # don't add element
				add = False
		if add == True:
			new_string += i
	return new_string


strings = input("Enter two strings seperated by spaces: ").split(' ')

string1 = strings[0]
string2 = strings[1]

print(functionC(string1, string2))