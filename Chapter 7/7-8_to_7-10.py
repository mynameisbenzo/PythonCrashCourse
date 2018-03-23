'''
	7-8: I want a sandwich and so do my 
	friends, so I'm gonna go ahead and 
	send a list of sandwiches I want made.  
	When each is done, James Jonathan's 
	should tell me it's done so I know 
	when to pick it up.  
'''
my_sandwiches = ['turkey', 'chicken parm', 'tuna', 'blt', 
	'chicken bacon ranch', 'pastrami', 'grilled cheese', 'ham']
finished_sandwiches = []
while True:
	if len(my_sandwiches) < 1:
		break
	order = my_sandwiches.pop()
	finished_sandwiches.append(order)
	print("Your " + order + " sandwich is done!")

'''
	7-9: Whoops! James Jonathan's is 
	out of pastrami.  No pastrami orders
	will be made!
'''
my_sandwiches = finished_sandwiches[:]
my_sandwiches.insert(1,'pastrami')
my_sandwiches.insert(6,'pastrami')
while len(finished_sandwiches):
	finished_sandwiches.pop()
print("Sorry, but James Jonathan's is all out of " +
	"pastrami!")
while True:
	if len(my_sandwiches) < 1:
		break
	order = my_sandwiches.pop()
	if order == 'pastrami':
		print("Sorry we're out of " + order + "...")
		continue
	finished_sandwiches.append(order)
	print("Your " + order + " sandwich is done!")
	
'''
	7-10: I want to the popular vacation 
	spots!  We'll use a while loop and a
	dictionary to keep track of the places
	and how many people picked each.
'''
vacationSpots = {}
while True:
	userInput = input("Where is your dream vacation spot? ('quit' to exit): ")
	if userInput == 'quit':
		break
	if userInput in vacationSpots:
		vacationSpots[userInput] += 1
	else:
		vacationSpots[userInput] = 1
for k,v in vacationSpots.items():
	print(k + ": " + str(v))