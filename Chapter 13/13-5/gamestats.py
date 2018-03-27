class GameStats():
	def __init__(self, settings):
		self.settings = settings
		self.reset_stats()
		
		self.game_active = True
		
	def reset_stats(self):
		self.livesLeft = self.settings.lives_AMT