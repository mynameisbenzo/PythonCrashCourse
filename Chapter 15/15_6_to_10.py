'''
	15-6:
		Goal:
			Modify x label to generate the list with
			a for-loop/list comprehension.  
	15-7:
		Goal:
			Create a simulation for two 8 sided die.
	15-8:
		Goal:
			Create a simulation for three 6 sided die.
	15-9:
		Goal:
			Multiply instead of add the result of two
			rolled dice.
	15-10:
		Goal:
			Flip the script.  Use Pygal for a random
			walk and matplotlib for die results.
			
	Approach:
		User input that takes the amount of die, the 
		amount of sides per die, and the operation to
		be performed(+/*).  This will cover problems
		7 through 9.
		
		Problem 10 I will approach in separate files.
'''

from die import Die
from die_simulator import DieSimulator

def get_sides():
	while True:
		try:
			num_sides = int(input("How many sides does the" +
				" die have ? "))
			break
		except ValueError:
			print("That's not a number.")
	return num_sides

def get_dice(num):
	dice = []
	for x in range(num):
		print("Die #" + str(x + 1))
		die = Die()
		user_answer = input("Would you like to change the " +
			"number sides your die has? (y/n)")
		if user_answer == 'y':
			die.update_sides(get_sides())
		dice.append(die)
	return dice


print("Hello! Welcome to the Die Simulator!")

num_die_allowed = (2,3)
operations_allowed = ('+', '*')

while True:
	try:
		num_die = int(input("How many die are we rolling? "))
		if num_die not in num_die_allowed:
			raise Exception("We can't handle that much dice at "
				+ "the moment")
				
		operation = input("Will we be adding or multiplying " +
			"die results? (*/+) ")
		if operation not in operations_allowed:
			raise Exception("That's not an operation I recognize. "
				+ "Please enter '+' or '*'.")
		elif operation == '*' and num_die > 2:
			raise Exception("For now, we can only multiply the result "
				+ "of two die at a time. Sorry!")
				
		dice = get_dice(num_die)
		die_sim = DieSimulator(operation, dice[0], dice[1])
		if len(dice) > 2:
			die_sim.add_third_die(dice[2])
		
		die_sim.simulate()
		
		break
	except ValueError:
		print("That's not a number!")
	except Exception as error:
		print(error)
		
	
print("Simulation has been run! Please check the svg file created!")