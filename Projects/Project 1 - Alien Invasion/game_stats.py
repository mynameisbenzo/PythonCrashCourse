'''
	Track statistics for alien invasion
'''
class GameStats():
	def __init__(self, settings):
		self.settings = settings
		self.reset_stats()
		
		# state alien invasion in active state
		self.game_active = True
	
	'''
		initialize statistics that will
		change during the game
	'''
	def reset_stats(self):
		self.ships_left = self.settings.ship_limit