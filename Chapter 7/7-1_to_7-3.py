'''
	7-1: Working with user inputs!
	Let's ask for the user's name and 
	then say hello.
'''
name = input("What's your name? ")
print("Hello " + name.title() + "!")

'''
	7-2: Evaluating user inputs with conditional
	statements.  Let's see if we have a table to
	seat their party.
'''
partySize = input("How many people will be eating today? ")
if int(partySize) > 8:
	print("I'm sorry, but you'll have to wait.")
else:
	print("Your table is ready!")
	
'''
	7-3: Let's do some more user input evaluation.
	Need to make sure to have a solid grasp of it!
	We'll check if the number they enter is a
	multiple of 10.
'''
number = input("Please give me a number: ")
if int(number) % 10 == 0:
	print(number + " is a multiple of ten!")
else:
	print(number + " is not a multiple of ten...")