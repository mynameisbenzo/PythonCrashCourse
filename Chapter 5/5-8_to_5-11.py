'''
	5-8: Find the admin and give them a special greeting!
	Using conditionals while looping through lists.
'''
users = ['George','admin','Alex','Edward','Raven']
for user in users:
	if user == 'admin':
		print('Hello ' + user + ', would you like to see' +
			' a status report?')
	else:
		print('Hello ' + user + '! Thank you for logging ' +
			'in again.')
			
'''
	5-9: Check if the list is empty! (Should've done this first!)
	Using conditionals to check if a list has entries.
'''
if len(users) > 0:
	print('Users are logged in.')
	
'''
	5-10: Let's add more users, but check if new usernames
	don't already exist.
	Comparing lists using conditionals.
'''
newUsers = ['Alex','Mike','Lebron','Raven','Gon']
exists = False
for newUser in newUsers:
	for user in users:
		if user.lower() == newUser.lower() and not exists:
			print('We already have a ' + newUser + '!')
			exists = True
	if not exists:
		print('We don\'t have a ' + newUser + ' and we\'d' +
			' be glad to have you!')
	exists = False
	
'''
	5-11: Time to mark the places in a race! There are only
	9 places (and three that actually matter), so we should
	keep that in mind.
	Checking numbers in a list using if-elif-else
'''
numbers = range(1,10)
for number in numbers:
	if number == 1:
		print(str(number) + 'st')
	elif number == 2:
		print(str(number) + 'nd')
	elif number == 3:
		print(str(number) + 'rd')
	else:
		print(str(number) + 'th')