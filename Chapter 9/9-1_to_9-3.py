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
class Restaurant():
	
	''' 
		initializing function for the class
		in order to create an instance
	'''
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.isOpen = False
	
	'''
		print out the name and type of food for
		the restaurant if the restaurant is open
	'''
	def restaurant_description(self):
		if self.isOpen:
			print("Name: " + self.restaurant_name)
			print("Cuisine Type: " + self.cuisine_type)
		else:
			print("The restaurant isn't open yet!")
	
	'''
		open the restaurant if it's not already
		open
	'''
	def open_restaurant(self):
		if not self.isOpen:
			self.isOpen = True
			print(self.restaurant_name + " is now open!")
		
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
class User():
	# initializer
	def __init__(self, first, last, username,
					joinedOn):
		self.first = first
		self.last = last
		self.username = username
		self.joinedOn = joinedOn
	
	# user description
	def describe_user(self):
		print("This is " + self.first + " " +
			self.last + ", or " + self.username +
			". They have been a user since " + 
			self.joinedOn + ".")
			
	# say hello to the user
	def greet_user(self):
		print("Hello " + self.username)
		
me = User('Lorenzo','Hernandez','hxh_plzDONTstop','03/26/2018')
me.describe_user()
me.greet_user()