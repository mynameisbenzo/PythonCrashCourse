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
		
		
		self.speedup_scale = 1.1
		self.initialize_dynamic_settings()
		
	'''
		initialize settings that change throughout the game
	'''
	def initialize_dynamic_settings(self):
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
		
		''' 
			fleet direction: 1 = right, -1 = left
		'''
		self.fleet_direction = 1
		
		'''
			how quickly the game speeds up
		'''
	
	'''
		increase speed settings
	'''
	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale