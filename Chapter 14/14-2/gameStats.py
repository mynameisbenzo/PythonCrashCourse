class GameStats():
	def __init__(self, settings):
		self.settings = settings
		self.reset_stats()
		
		self.game_active = False
		self.targetHit = False
		
	def reset_stats(self):
		self.bulletsLeft = self.settings.maxBullets