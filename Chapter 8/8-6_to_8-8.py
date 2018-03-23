'''
	8-6: Continuing work with functions.
	
	This next function will will take in two
	parameters city and country and return 
	them formatted like this:
		City, Country
'''
def city_country(city, country):
	print(city + ", " + country)
city_country('San Francisco','United States')
city_country('Tokyo','Japan')
city_country('Mexico City','Mexico')

'''
	8-7: Continuing work with functions. 
	Returning a dictionary and work with
	optional parameters.
	
	If there is one thing I like doing more
	than most other things, then it's playing
	video games.  This next function will 
	take information about a title and return
	that information in the form of a dic-
	tionary.  The function will also allow
	the user to add optional information about
	how many times the user has beat the game.
'''
def make_game(title, year, developer, completed=-1):
	gameInfo = {
		'title': title, 
		'year': year, 
		'developer': developer
	}
	if completed >= 0:
		gameInfo['completed'] = completed
	return gameInfo
mmx = make_game('Mega Man X', 1993, 'Capcom', 23)
dk = make_game('Donkey Kong Country', 1994, 'Rare', 2)
ct = make_game('Chrono Trigger', 1995, 'Square Enix')
print(mmx)
print(dk)
print(ct)

'''
	8-8: Functions, User Inputs, and while loops.
	
	Now, we'll take that last function from 8-7 and
	allow the user to list of their own games.
'''
title = ""
developer = title
year = 0
yesNo = ""
completed = -1
gameInfo = {}
while True:
	completed = -1
	print("Hello!  Tell me a little bit about the games "
		+ "you've played! Enter 'q' at anytime to leave.")
	title = input("Name of the game? ")
	if title.lower() == 'q':
		break
	developer = input("What year was it made? ")
	if developer.lower() == 'q':
		break
	else:
		year = int(developer)
	developer = input("Who made it? ")
	if developer.lower() == 'q':
		break
	yesNo = input("Have you beat the game? (Y/N): ")
	if yesNo.lower() == 'q':
		break
	elif yesNo.lower() == 'y':
		yesNo = input("How many times? ")
		if yesNo.lower() == 'q':
			break
		else:
			completed = int(yesNo)
	gameInfo = make_game(title, year, developer, completed)
	print(gameInfo)