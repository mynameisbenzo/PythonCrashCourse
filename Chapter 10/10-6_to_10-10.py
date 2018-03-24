'''
	10-6: Learning about Errors.
	
	Sometimes you'll ask for a specific
	type of input but the user has other
	thoughts.  For this exercise, we'll
	be asking for numbers to add together
	but then checking for a ValueError
	when trying to convert user input 
	into an integer.
'''
def get_number():
	while True:
		try:
			number = int(input("Number to add: "))
		except ValueError:
			print("That's not a number.")
		else:
			return number

first = get_number()
second = get_number()
print(str(first + second))