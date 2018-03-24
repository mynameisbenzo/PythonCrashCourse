'''
	10-12: Combining both parts of 10-11.
'''
import json

file = 'fav_number_10-12.json'
try:
	with open(file) as c_json:
		number = json.load(c_json)
		print("Your favorite number is " + str(number))
except FileNotFoundError:
	while True:
		try:
			number = int(input("What is your favorite number? "))
		except ValueError:
			print("That's not a number")
		else:
			with open(file, 'w') as c_json:
				json.dump(number, c_json)
				print("I'll remember that your favorite number " +
					"is " + str(number) + "!")
				break