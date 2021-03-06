from random import choice
'''
	a class to generate random walks
'''
class RandomWalk():
	def __init__(self, num_points=5000):
		self.num_points = num_points
		
		# walks always start at 0,0
		self.x_values = [0]
		self.y_values = [0]
		
	'''
		calculate all points in the walk
	'''
	def fill_walk(self):
		# take a step until the walk is the desired length
		while len(self.x_values) < self.num_points:
			# which way do you go and how far do you go that way
			
			x_step = self.get_step()
			y_step = self.get_step()
			
			# reject moves that go nowhere
			if x_step == 0 and y_step == 0:
				continue
				
			# get next x and y values
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step
			
			self.x_values.append(next_x)
			self.y_values.append(next_y)
			
	'''
		determine next step in walk and return it
	'''
	def get_step(self):
		dir = choice([1,-1])
		dis = choice(list(range(-4,10)))
		return (dir * dis)