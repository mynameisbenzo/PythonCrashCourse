import pygal
class DieSimulator():
	def __init__(self, operation, die_1, die_2, die_3=None):
		self.operation = operation
		self.die_1 = die_1
		self.die_2 = die_2
		self.die_3 = die_3
		
		self.get_num_die()
	
	'''
		adds a third die
	'''
	def add_third_die(self, die):
		self.die_3 = die
	
	'''
		called to simulate die throws and create histogram
	'''
	def simulate(self):
		results = []
		for roll_num in range(1000):
			if self.operation == '+':
				result = self.die_1.roll() + self.die_2.roll()
				if self.die_3 != None:
					result += self.die_3.roll()
				results.append(result)
			else:
				result = self.die_1.roll() * self.die_2.roll()
				results.append(result)
		
		frequencies = []
		max_result = self.die_1.num_sides + self.die_2.num_sides
		if self.die_3 != None:
			max_result += self.die_3.num_sides
		for value in range(1, max_result+1):
			frequency = results.count(value)
			frequencies.append(frequency)
		
		hist = pygal.Bar()
		hist.title = self.get_title()
		hist.x_labels = [str(x) for x in range(1, max_result+1)]
		hist.x_title = "Result"
		hist.y_title = "Frequency of Result"
		
		addThis = (self.die_1.d_val + " + " + self.die_2.d_val)
		if self.die_3 != None:
			addThis += " + " + self.die_3.d_val
		hist.add(addThis, frequencies)
		hist.render_to_file('die_simulator_result.svg')
		
	'''
		return title for histogram based off of the number
		of dice and the amount sides on each die
	'''
	def get_title(self):
		title = "Result of rolling a " + self.die_1.d_val 
		if self.die_3 != None:
			title += (", " + self.die_2.d_val + ", and " + 
				self.die_3.d_val)
		else:
			title += " and " + self.die_2.d_val
		title += " 1000 times"
		return title
		
	'''
		set number of dice going through the simulation
	'''
	def get_num_die(self):
		if self.die_3 == None:
			self.num_die = 2
		else:
			self.num_die = 3