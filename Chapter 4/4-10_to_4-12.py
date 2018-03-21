'''
	4-10: Slicing and dicing.  Learning to slice
	up arrays so I think it's only natural to 
	reuse the pizza one from 4-1... with some
	added entries.
'''
pizzas = [	'Hawaiian','Pizzas with Feta Cheese on them',
			'Stuffed Crust', 'Pepperoni', 'Cheese', 
			'Combination'
		]
		
# printing the beginning
print('The first three items of the list are...')
for pizza in pizzas[:3]:
	print(pizza)
	
# printing the middle
print('Three items in the middle are...')
for pizza in pizzas[2:5]:
	print(pizza)
	
# printing the last parts
for pizza in pizzas[3:]:
	print(pizza)
	
'''
	4-11: Sharing a list with a friend who likes 
	all the same pizza as you can be pretty easy.
	Sharing the pizza is a different story...
'''
myFriendsPizzas = pizzas[:]

# ...my friend really doesn't care for Hawaiian.  MORE FOR ME.
myFriendsPizzas.remove('Hawaiian')

# let's see who likes what now.
print('The best pizzas ever are...')
for pizza in pizzas:
	print(pizza)
print('An incomplete list of the best pizzas are...')
for pizza in myFriendsPizzas:
	print(pizza)
	
'''
	4-12: Book has a foods.py example which hasn't
	been using a for loop to print out the contents
	of the list, so let's fix that.
'''
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

# for loop time
for food in my_foods:
	print(food)
for food in friend_foods:
	print(food)