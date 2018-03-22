'''
	6-7: Starting with our 6-1 dictionary, 
	we're gonna add some more people and loop 
	through dictionaries inside of dictionaries.
'''
person1 = {
	'first_name':'Mario',
	'last_name':'Mario',
	'age':24,
	'city':'Mushroom Kingdom'
}
person2 = {
	'first_name':'Luigi',
	'last_name': 'Mario',
	'age': 19,
	'city':'Mushroom Kingdom'
}
person3 = {
	'first_name':'Princess',
	'last_name':'Peach',
	'age':23,
	'city':'Mushroom Kingdom'
}
people = {
	'jump_man':person1,
	'ghostbuster':person2,
	'designated_damsel':person3
}
for k, v in people.items():
	print("Information on " + k + ":")
	print("\tFull name: " + v['first_name'] + " " + v['last_name'])
	print("\tAge: " + str(v['age']))
	print("\tCity: " + v['city'])
	
'''
	6-8: Gathering and showing information on pets
	we found.
'''
pets = {
	'tiny':{
		'type':'great dane',
		'owner':'anthony nym'
	},
	'slimy':{
		'type':'snake',
		'owner':'joe'
	},
	'micheal':{
		'type':'cat',
		'owner':'fluffles'
	}
}
for k, v in pets.items():
	print("Information on " + k.title() + ":")
	print("\tType of pet: " + v['type'])
	print("\tOwner name: " + v['owner'].title())
	
'''
	6-9: Favorite places.  For this one we'll reuse
	the people dictionary, add favorite_place
	to each person, and reprint the people dictionary
	with the new information.
'''
people['jump_man']['favorite_place'] = 'star road'
people['ghostbuster']['favorite_place'] = 'mansions'
people['designated_damsel']['favorite_place'] = 'castle'
for k, v in people.items():
	print("Information on " + k + ":")
	print("\tFull name: " + v['first_name'] + " " + v['last_name'])
	print("\tAge: " + str(v['age']))
	print("\tCity: " + v['city'])
	print("\tFavorite place: " + v['favorite_place'].title())
	
'''
	6-10: For this one, we'll modify and update
	the dictionary in 6-2 to allow for more than
	one favorite number.
'''
peopleNumbers ={
	'Mario': [1],
	'Luigi': [1,2,3],
	'Bowser': [1,7],
	'Peach' : [3,4],
	'Toad' : [17,24,99]
}
for k,v in peopleNumbers.items():
	print(k + "'s favorite numbers are:")
	for num in v:
		print(str(num))
		
'''
	6-11: Let's get some information about cities
	in a dictionary now.
'''
cities = {
	'visalia':{
		'country':'usa',
		'population':150000,
		'fact':'It\'s 3 hours east of Monterey.'
	},
	'monterey':{
		'country':'usa',
		'population':29000,
		'fact':'There\'s an aquarium nearby.'
	},
	'paris':{
		'country':'france',
		'population':2200000,
		'fact':'My landlords are going to vacation there this summer.'
	}
}
for k, v in cities.items():
	print("The city of " + k + " is located in " +
		v['country'].upper() + " and has a population of " +
		str(v['population']) + ".  " + v['fact'])
		
'''
	6-12: Let's take a previous exercise and try
	to improve on it in some way, like 5-8.
'''
users = {
	'George':{
		'Joined':'03/22/2018',
		'Friends':['Alex'],
		'admin':False
	},
	'admin':{
		'Joined':'05/30/2007',
		'Friends':[],
		'admin':True
	},
	'Alex':{
		'Joined':'12/25/2010',
		'Friends':['George','Edward','Raven'],
		'admin':False
	},
	'Edward':{
		'Joined':'11/01/2015',
		'Friends':['Alex','Raven'],
		'admin':False
	},
	'Raven':{
		'Joined':'01/02/2018',
		'Friends':['Alex','Edward'],
		'admin':False
	},
}
for k,v in users.items():
	if v['admin']:
		print("Hello " + k + ", would you like a status report?")
	else:
		print("Hello " + k + "!")
		print("Thank you for being a user since " + v['Joined'] + "!")
		print("Here are your friends: ")
		for name in v['Friends']:
			print("\t" + name)