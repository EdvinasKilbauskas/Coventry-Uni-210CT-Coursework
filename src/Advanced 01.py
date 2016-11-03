#Write a program to predict the number of creatures in a fictional alien invasion. An alien lays X eggs
#each day (there are no genders in this species) and the eggs hatch after Y days. If X is 3 and Y is 5, how
#many aliens will there be 30 days after a single alien invades? Hint: Make an array/list and use each
#slot to represent a day. Put a 1 in the first position and then calculate how many eggs are laid and
#when they will hatch. Put this value in the correct cell and then add the value for the current day to the
#following one (they don't die off) and move along.

days = 30
eggs_per_alien = 3 		# count of eggs layed by alien
starting_aliens = 1

aliens = [0 for i in range(0,30)]
aliens[0] = starting_aliens

def get_aliens(day):
	return aliens[day] + aliens[day-1] + aliens[day-5] * eggs_per_alien
			   
for day in range(1, days):
	aliens[day] = get_aliens(day)
	print(str(day+1) + ". " + str(aliens[day]))

