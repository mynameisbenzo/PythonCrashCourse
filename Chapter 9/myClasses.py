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

###############################################################
	
'''
	Child class of Restaurant that is more focused
	on delivering the sweet, sweet, sugary bliss
	that is Ice Cream.
'''
class IceCreamStand(Restaurant):
	# initializer
	def __init__(self, restaurant_name, cuisine_type,
				flavors):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors
		
	'''
		Everyone's got to know what flavors the
		stand offers.
		(9-6)
	'''
	def show_flavors(self):
		print("These are the flavors we offer!")
		for flavor in self.flavors:
			print(flavor)

###############################################################

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

###############################################################

'''
	Child class of User that will creates a
	User with more permissions and privileges
'''
class Admin(User):
	# initializer
	def __init__(self, first, last, username,
				joinedOn, privileges):
		super().__init__(first, last, username,
						joinedOn)
		self.privileges = privileges
		
	'''
		Displays all the privileges the current
		Admin has.
		(9-7)
	'''
	def show_privileges(self):
		print("These are " + self.username + "'s "
				+ "privileges:")
		self.privileges.list_privileges(self.username)
			
###############################################################

'''
	Class that will contain privileges
'''
class Privileges():
	# initializer
	def __init__(self, post, delete, 
				edit, ban, permaban):
		self.post = post
		self.delete = delete
		self.edit = edit
		self.ban = ban
		self.permaban = permaban
	
	'''
		Will display all the privileges that
		a user has.
	'''
	def list_privileges(self, username):
		if self.post:
			print("\t" + username + " can post.")
		if self.delete:
			print("\t" + username + " can delete posts.")
		if self.edit:
			print("\t" + username + " can edit posts.")
		if self.ban:
			print("\t" + username + " can ban other users.")
		if self.permaban:
			print("\t" + username + " can permanently ban " +
				"other users.")
				
###############################################################
				
'''
	Parent class that will create a car's
	given information
'''
class Car():
	# initializer
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer = 0
	
	# gives some car info in string form
	def get_descriptive_name(self):
		return (str(self.year) + ' ' + self.make + 
				' ' + self.model)
	
	# displays mileage
	def read_odometer(self):
		print("This car has " + str(self.odometer) +
				" miles on it.")
	
	'''
		update odometer if mileage provided is greater
		than the current mileage
	'''
	def update_odometer(self, miles):
		if miles >= self.odometer:
			self.odometer = miles
		else:
			print("You can't roll back an odometer.")
	
	# add miles to odometer
	def increment_odometer(self, miles):
		self.odometer += miles
		
	# displays message that tank is now full
	def fill_gas_tank():
		print("Tank is now full!")
				
###############################################################

'''
	Child class to Car which will create a Car
	instance that is specifically for Electric
	cars.
'''
class ElectricCar(Car):
	# initializer
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery = Battery()
		
	'''
		override fill_gas_tank() because electric
		cars don't have gas tanks! (mostly)
	'''
	def fill_gas_tank():
		print("This car doesn't need a gas tank!")
		
###############################################################
				
'''
	Creates an instance of a battery
'''
class Battery():
	# initializer
	def __init__(self, battery_size=70):
		self.battery_size = battery_size
		
	# displays battery size information
	def describe_battery(self):
		print("This car has a " + str(self.battery_size) +
			"-kWh battery.")
			
	# gives the range of this battery
	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		
		print("This car can go approximately " +
			str(range) + " miles on a full charge.")
			
	# upgrades the size of the battery to 85
	def upgrade_battery(self):
		self.battery_size = 85
			
###############################################################