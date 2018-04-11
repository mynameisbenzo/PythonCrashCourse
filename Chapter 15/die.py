from random import randint

'''
	class representing a single die
'''

class Die():
	def __init__(self, num_sides=6):
		# assume six sided die
		self.num_sides = num_sides
		
		# added to easily print die information
		self.d_val = "D" + str(self.num_sides)
		
	'''
		return random number between 1 and number of
		sides
	'''
	def roll(self):
		return randint(1, self.num_sides)
		
	'''
		update number of sides on the die
	'''
	def update_sides(self, num):
		self.num_sides = num
		self.d_val = "D" + str(self.num_sides)