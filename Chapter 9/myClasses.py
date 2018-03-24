'''
	Creates an instance of a restaurant
	alongside relevant information
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
		self.number_served = 0
	
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
			
	'''
		set the number people served
		(added for 9-4)
	'''
	def set_number_served(self, number):
		self.number_served = number
		
	'''
		increments number served by the amount
		given
		(added for 9-4)
	'''
	def increment_number_served(self, number):
		self.number_served += number
		
'''
	Creates instance of user class with personal
	and user information
'''
class User():
	# initializer
	def __init__(self, first, last, username,
					joinedOn):
		self.first = first
		self.last = last
		self.username = username
		self.joinedOn = joinedOn
		self.login_attempts = 0
	
	# user description
	def describe_user(self):
		print("This is " + self.first + " " +
			self.last + ", or " + self.username +
			". They have been a user since " + 
			self.joinedOn + ".")
			
	# say hello to the user
	def greet_user(self):
		print("Hello " + self.username)
		
	'''
		increase login attempts by 1
		(added for 9-5)
	'''
	def increment_login_attempts(self):
		self.login_attempts += 1
	
	'''
		will reset the amount of login attempts
		that have been made
		(added for 9-5)
	'''
	def reset_login_attempts(self):
		self.login_attempts = 0