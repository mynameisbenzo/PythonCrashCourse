'''
	4-13: Tuples and lists!? What's the difference?
	...well for one you can't change a tuple...
	A list of constants pretty much, so let's work
	with them.
'''
buffetFood = ('pizza','mac & cheese','tater tots','salad, I guess','banana')
for food in buffetFood:
	print(food)
	
# this won't work, so we'll keep it commented out.

# food[0] = 'eggs'

# in order to change a tuple, we have to change the whole thing... so!
buffetFood = ('eggs','mac & cheese','biscuits & gravy','salad, I guess','banana')
for food in buffetFood:
	print(food)