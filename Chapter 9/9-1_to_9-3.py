'''
	9-1: Time to go to Class class!
	...as in... this exercise and chapter...
	well, they're about classes.  Guess it
	would be easier to just call it Classes 101
	or something.
	
	I'll be making a Class for Restaurants that
	holds the name of the restaurant and the 
	type of food the serve.  Then, we'll call it
	to make sure everything is copasetic.
'''
from myClasses import *
		
myPlace = Restaurant("Lorenzo's", "Mexican")
myPlace.restaurant_description()
myPlace.open_restaurant()
myPlace.restaurant_description()

'''
	9-2: Let's make more instance of 
	the restaurant class with different
	information.
'''
herFavorite = Restaurant('Fabby\'s', 'Mexican')
herFavorite.open_restaurant()
herFavorite.restaurant_description()
myGramps = Restaurant('Sakura\'s Japanese Restaurant','Japanese')
myGramps.open_restaurant()
myGramps.restaurant_description()

'''
	9-3: Time for a new type of class!
	
	This next section will allow the creation
	of a User class that holds relevant infor-
	mation about the created User.
'''	
me = User('Lorenzo','Hernandez','hxh_plzDONTstop','03/26/2018')
me.describe_user()
me.greet_user()