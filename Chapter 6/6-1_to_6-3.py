'''
	6-1: Some Mario information!
	Introduction to dictionaries
'''
mario ={
	'first_name':'Mario',
	'last_name':'Mario',
	'age':24,
	'city':'Mushroom Kingdom'
}
print(mario['first_name'])
print(mario['last_name'])
print(str(mario['age']))
print(mario['city'])

'''
	6-2: People and their favorite numbers!
	Using dictionaries to display information
'''
peopleNumbers = [
	{ 	
		'name': 'Mario',
		'num' : 1
	},
	{ 	
		'name': 'Luigi',
		'num' : 2
	},
	{ 	
		'name': 'Bowser',
		'num' : 7
	},
	{ 	
		'name': 'Peach',
		'num' : 4
	},
	{ 	
		'name': 'Toad',
		'num' : 99
	},
]
for info in peopleNumbers:
	print(info['name'])
	print(str(info['num']))
	
'''
	6-3: Creating a glossary!  Let's define
	some words!
	Using dictionaries to create... a dictionary.
'''
glossary = [
	{
		'word': 'list',
		'definition' : 'an assortment of elements '
	},
	{
		'word': 'dictionary',
		'definition' : 'an assortment of elements with keys instead of indices'
	},
	{
		'word': 'tuples',
		'definition' : 'similar to a list but can only be altered if the entire list is changed'
	},
	{
		'word': 'conditional statement',
		'definition' : 'a statement that will evaluate to True or False'
	},
	{
		'word': 'loop',
		'definition' : 'a block of code that can operate a set amount of times until a condition is met'
	},
]
for word in glossary:
	print(word['word'] + ':\n')
	print('\t' + word['definition'])