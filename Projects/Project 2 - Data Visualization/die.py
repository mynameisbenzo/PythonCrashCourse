from random import randint

'''
	class representing a single die
'''

class Die():
	def __init__(self, num_sides=6):
		# assume six sided die
		self.num_sides = num_sides
		
	'''
		return random number between 1 and number of
		sides
	'''
	def roll(self):
		return randint(1, self.num_sides)