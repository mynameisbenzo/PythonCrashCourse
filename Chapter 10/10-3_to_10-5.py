'''
	10-3: Intro to writing files.
	Let me have your name!
'''
with open('guest.txt','w') as file:
	file.write(input("What is your name? "))
	
'''
	10-4: Intro to writing files.
	Goal is to make a guest book and
	keep a references to all guests
	that have used this script.
'''
with open('guest_book.txt','a') as file:
	while True:
		response = input("Welcome.  What is your name? ")
		if response == 'q':
			break
		else:
			file.write(response + "\n")
			
'''
	10-5: We're doing the same as above
	but this time we're looking for reasons
	why someone likes programming.
'''
with open('reasons.txt','a') as file:
	while True:
		response = input("Why do you like programming? ")
		if response == 'q':
			break
		else:
			file.write(response + "\n")