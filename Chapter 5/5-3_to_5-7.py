'''
	5-3: Aliens and what happens when you shoot
	them.
	Using if statements to assign points.
'''
alien = 'green'
if alien == 'green':
	print('5 points!')
	alien = 'red'
	
if alien == 'green':
	print('5 points!')

'''
	5-4: The aliens never top invading.  Man
	the firing stations.
	Using if-else statements to assign points.
'''
if alien == 'green':
	print('5 points!')
else:
	print('10 points!')
	alien = 'yellow'
	
if alien == 'yellow' or alien == 'red':
	print('10 points!')
	alien = 'green'
else:
	print('5 points!')
	
'''
	5-5: Why would the Mother ship keep sending
	their Children ships to their doom!?
	Using if-elif-else statements to assign points.
'''
if alien == 'yellow':
	print('10 points!')
	alien = 'green'
elif alien == 'red':
	print('15 points!')
else:
	print('5 points!')

if alien == 'yellow':
	print('10 points!')
elif alien == 'red':
	print('15 points!')
else:
	print('5 points!')
	alien = 'red'
	
if alien == 'yellow':
	print('10 points!')
elif alien == 'red':
	print('15 points!')
	alien = 'yellow'
else:
	print('5 points!')
	
'''
	5-6: What stage of person are you!?  
	(Definitely not what a robot would ask.)
	Using if-elif-else statements to determine age group.
'''
age = 29
if age >= 65:
	print('elder')
elif age >= 20 and age < 65:
	print('adult')
elif age >= 13 and age < 20:
	print('teenager')
elif age >= 4 and age < 13:
	print('kid')
elif age >= 2 and age < 4:
	print('toddler')
else:
	print('baby')
	
'''
	5-7: Let's take a look at my favorite fruits!
	Using in, not in on lists/tuples.
'''
myFavoriteFruits = ('banana','granny smith apple','pineapple','strawberry')
if 'banana' in myFavoriteFruits:
	print('Yeah.  Can\'t go a day without those ' + myFavoriteFruits[1] + 's.')
if 'tomato' not in myFavoriteFruits:
	print('Technically a fruit.  Definitely do NOT like them.')
if 'blueberry' in myFavoriteFruits:
	print('This won\'t print')
else:
	print('I like blueberries, but they\'re not my favorite.')
if 'mango' in myFavoriteFruits:
	print('This won\'t print.')
else:
	print('Y\'know, I completely forgot about mangoes...')
	myFavoriteFruits = ('banana','granny smith apple','pineapple','strawberry', 'mango')
if 'mango' in myFavoriteFruits:
	print('Absolutely delicious!')