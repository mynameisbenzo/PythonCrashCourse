'''
	10-13: Remembering users and 
	validating them.
	
	The exercise will open up a JSON,
	check the username stored there,
	and ask the current user if this is
	them.
'''
import json

def newUser(file):
	user = input("Hello new user! What is your username? ")
	with open(file, 'w') as c_json:
		json.dump(user, c_json)
	print("Greetings " + user + "! I'll remember you for next time.")

def openAndValidate(file):
	try:
		with open(file) as c_json:
			user = json.load(c_json)
	except FileNotFoundError:
		newUser(file)
	else:
		print("Are you " + user + "?")
		response = input("(Y/N) ")
		while True:
			if response.lower() == 'y':
				print("Hello " + user + "!")
				break
			elif response.lower() == 'n':
				newUser(file)
				break
			else:
				print('Command unrecognized.')
		
file = 'lastUser.json'
openAndValidate(file)

