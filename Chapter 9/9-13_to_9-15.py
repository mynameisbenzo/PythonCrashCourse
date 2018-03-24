'''
	9-13: Rewrite 6-4 (glossary dictionary)
	to work with OrderedDict
	
	Note: an ordered dictionary keeps the 
	entries in the same order that have 
	been entered.  
'''
from collections import OrderedDict
glossary = OrderedDict()
glossary['list'] = 'an assortment of elements'
glossary['dictionary'] = 'an assortment of elements with keys instead of indices'
glossary['tuples'] = 'similar to a list but can only be altered if the entire list is changed'
glossary['conditional statement'] = 'a statement that will evaluate to True or False'
glossary['loop'] = 'a block of code that can operate a set amount of times until a condition is met'
for k,v in glossary.items():
	print(k + ":")
	print("\t" + v)
	
'''
	9-14: Using the random module to 
	create Dice that may have a different
	number of sides
'''
from myClasses import Die
six = Die(6)
ten = Die(10)
twenty = Die(20)

print("Rolling six sided die.")
for i in range(1,11):
	six.roll_die()
	
print("Rolling ten sided die.")
for i in range(1,11):
	ten.roll_die()

print("Rolling twenty sided die.")
for i in range(1,11):
	twenty.roll_die()
	
'''
	9-15: Just a quick note to check
	pymotw.com on how to use modules
'''