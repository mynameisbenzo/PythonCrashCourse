'''
	7-4: We're back to pizza!  Heck yes!
	This time we'll ask the user what they
	want and we'll only stop if they enter
	the right value.  To do this, we'll 
	use a while loop!
'''
topping = input("What would you like on your pizza? ('quit' to stop): ")
while topping != 'quit':
	print("Alright! We'll add " + topping + " to your pizza!")
	topping = input("What will you add next? ('quit' to stop): ")
	
'''
	7-5: Alright, let's move to movie tickets.
	Instead of adding toppings, we'll check 
	the users age and depending on where it 
	falls we'll give them the ticket cost.
'''
age = input("To buy a ticket, we need to know your age.  " +
	"Please enter your age ('quit' to exit): ")
while age != 'quit':
	if int(age) < 3:
		print("Ticket is free!")
	elif int(age) >= 3 and int(age) < 12:
		print("Ticket is $10.")
	else:
		print("Ticket is $15.")
	age = input("To buy a ticket, we need to know your age.  " +
		"Please enter your age ('quit' to exit): ")
		
'''
	7-6: Okay! We've got a fair grasp of while loops,
	BUT let's use a infinite loop that doesn't check
	input.  We'll check the input inside the loop and
	and break out of the loop based on our check.
'''
# directions you can go
directions = ['left','right','forward','backward','up','down']
userSelections = []
active = True
while active:
	# Check if all directions have been explored
	if len(userSelections) == 6:
		print("Congrats!  You've went all the ways!")
		break
	
	# get next direction
	direction = input("Which way will you go? ")
	
	# check if direction is valid
	if direction not in directions:
		print("Command unrecognized. Exiting.")
		active = False
	# add to directions used
	elif direction not in userSelections:
		userSelections.append(direction)
	# don't use the same direction!
	else:
		print("You've already went that way. " +
			"The ground crumbles and you fell!")
		break

'''
	7-7: For this exercise, we take a look at infinite
	loops.  The infinite loop will be commented out.
	We'll use the 7-6 to create it.
'''
'''
active = True
while active:
	# Check if all directions have been explored
	if len(userSelections) == 6:
		print("Congrats!  You've went all the ways!")
		# break
	
	# get next direction
	direction = input("Which way will you go? ")
	
	# check if direction is valid
	if direction not in directions:
		print("Command unrecognized. Exiting.")
		# active = False
	# add to directions used
	elif direction not in userSelections:
		userSelections.append(direction)
	# don't use the same direction!
	else:
		print("You've already went that way. " +
			"The ground crumbles and you fell!")
		# break
'''
'''
	If this code were to run, then it wouldn't stop
	asking for the next direction.  Notice line 74, 
	82, and 90 are commented out and will not execute.
	In 7-6, our active variable is set to False to 
	exit the loop or break is called to leave the while
	loop if the user has used all directions or used
	the same direction twice.
'''