'''
	10-11b: Intro to JSONs
	
	This exercise will require two
	separate scripts.  One will ask
	for the user's favorite number 
	while the other will grab that 
	favorite number.
	
	This one will read the json.
'''
import json

file = 'fav_user_number.json'
with open(file) as c_json:
	favNumber = json.load(c_json)
	print("Your favorite number is " + str(favNumber))