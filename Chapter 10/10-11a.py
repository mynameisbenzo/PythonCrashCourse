'''
	10-11a: Intro to JSONs
	
	This exercise will require two
	separate scripts.  One will ask
	for the user's favorite number 
	while the other will grab that 
	favorite number.
	
	This one will write a json.
'''
import json

while True:
	try:	
		number = int(input("What's your favorite number? "))
	except ValueError:
		print("That's not a number.")
	else:
		break

file = 'fav_user_number.json'
with open(file, 'w') as c_json:
	json.dump(number, c_json)
	print("I'll remember your favorite number is " + str(number))