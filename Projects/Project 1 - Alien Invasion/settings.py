'''
	Creating a settings class to be used
	to hold all settings in alien_invasion.
'''
class Settings():
	def __init__(self):
		# screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		
		'''
			ship settings
		'''
		self.ship_speed_factor = 0.25
		
		'''
			bullet settings
		'''
		self.bullet_speed = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60