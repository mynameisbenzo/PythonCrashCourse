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
			userInput = input("Number to add: ('q' to exit program) ")
			if userInput == 'q':
				exit()
			number = int(userInput)
		except ValueError:
			print("That's not a number.")
		else:
			return number

first = get_number()
second = get_number()
print(str(first + second))

'''
	10-7: While loop
	
	Above I went ahead and incorporated a
	while loop for number entry.  The goal
	now is to incorporate the entire process
	in a while loop, so a + b = c then dis-
	play the result. If 'q' is entered, then
	leave.
'''
def add_two_numbers():
	while True:
		first = get_number()
		second = get_number()
		print(str(first + second))
		userInput = input("Continue? (y/n) ")
		if userInput.lower() == 'y':
			print("Okay.  Let's keep adding")
		elif userInput.lower() == 'n':
			print("Goodbye!")
			break
		else:
			print("Don't understand your input" +
				". We'll keep adding.")
				
add_two_numbers()

'''
	10-8: Triggering a FileNotFoundError
	
	The exercise is asking us to create a 
	cats.txt and a dogs.txt with different
	types of cats and dogs and then move
	a file to a different directory to 
	trigger a FileNotFoundError.  Instead
	of moving files around, I'm going to
	not call a file properly.
'''
openThis = 'dog.txt'
try:
	with open(openThis) as file:
		contents = file.read()
except FileNotFoundError:
		print("Can't find " + openThis)
		
'''
	10-9: Silently failing.
	
	The last exercise printed out a error
	message for the error, but what if 
	don't want to print anything out.  
	This next exercise will not notify
	the user of the error by using pass 
	allowing for a silent fail.
'''
try: 
	with open(openThis) as file:
		contents = file.read()
except FileNotFoundError:
	pass
	
'''
	10-10: Opening files and counting
	occurences.
	
	This exercise is focused on counting the
	number times a word pops up in a text
	document.  The document I'm using is 
	from gutenberg.org called Hints on 
	Driving by C. Morley Knight.
'''

count = 0
try: 
	'''
		UnicodeDecodeError kept popping up so 
		here the open function is getting the
		file, what we'll be doing ('r'=read),
		and what encoding we'll be using.
	'''
	with open('gutenberg.txt','r',encoding='utf8') as file:
		for line in file:
			count += line.count('the')
except FileNotFoundError:
	print('Can\'t find file.')
else:
	print(str(count))