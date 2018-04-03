'''
	Creating a settings class to be used
	to hold all settings in alien_invasion.
'''
class Settings():
	def __init__(self):
		# screen settings
		self.screen_width = 600
		self.screen_height = 800
		self.bg_color = (230,230,230)
		
		'''
			frame limit
		'''
		self.frameCount = 1
		self.currentFrame = 0
		
		'''
			ship settings
		'''
		self.ship_speed_factor = 1
		self.ship_limit = 3
		
		'''
			bullet settings
		'''
		self.bullet_speed = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.max_bullets = 6
		
		'''
			alien settings
		'''
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		
		# fleet direction: 1 = right, -1 = left
		self.fleet_direction = 1