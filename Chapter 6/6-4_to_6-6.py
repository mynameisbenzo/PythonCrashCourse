'''
	6-4: This exercise is to edit 6-3 to loop
	over a dictionary using key, value loop and
	.items().  We'll go ahead and adjust glossary
	appropriately.
	Looping over dictionary key and value pairs.
'''
glossary = {
	'list' : 'an assortment of elements ',
	'dictionary': 'an assortment of elements with keys instead of indices',
	'tuples': 'similar to a list but can only be altered if the entire list is changed',
	'conditional statement': 'a statement that will evaluate to True or False',
	'loop': 'a block of code that can operate a set amount of times until a condition is met'
}
for k, v in glossary.items():
	print(k + ":\n\t" + v)
	
'''
	6-5: Now let's make a new dictionary of 
	mountains and where you can find them.
	Looping over dictionary key and value pairs.
'''
mountains = {
	'everest':'nepal',
	'mckinley':'alaska',
	'k2':'china',
	'mauna kea':'hawaii',
	'aconcagua':'argentina'
}
for k, v in mountains.items():
	print(k.title() + " is located in " + v.title() + ".")
	
'''
	6-6: We should check to see how good our
	glossary is by creating a list of words 
	to see if we have them.
	Using lists and dictionaries.
'''
wordsToCheck = ['list','dictionary','class','loop','function']
foundIt = False
for word in wordsToCheck:
	for k, v in glossary.items():
		if word == k:
			foundIt = True
			print(v)
	if not foundIt:
		print("I don't know what that is!")
	foundIt = False