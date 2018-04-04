'''
	Track statistics for alien invasion
'''
class GameStats():
	def __init__(self, settings):
		self.settings = settings
		self.reset_stats()
		
		# state alien invasion in active state
		self.game_active = False
		
		# high score should never be reset
		self.get_high_score()
	
	'''
		initialize statistics that will
		change during the game
	'''
	def reset_stats(self):
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1
		
	'''
		get high score at the start of every game
	'''
	def get_high_score(self):
		try:
			with open('highscore.txt') as file:
				self.high_score = int(file.read())
		except FileNotFoundError:
			self.high_score = 0