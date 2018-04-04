import pygame.font
from pygame.sprite import Group

from ship import Ship

'''
	a class to report scoring information
'''
class Scoreboard():
	
	def __init__(self, settings, screen, stats):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.settings = settings
		self.stats = stats
		
		# font settings for scoring information
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)
		
		# prepare initial score image
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()
		
	'''
		turn score into a rendered image
	'''
	def prep_score(self):
		rounded_score = int(round(self.stats.score, -1))
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, 
						self.text_color, self.settings.bg_color)
		
		# display score at the top right of the screen
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20
		
	'''
		turn high score into a rendered image
	'''
	def prep_high_score(self):
		high_score = int(round(self.stats.high_score, -1))
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True,
						self.text_color, self.settings.bg_color)
						
		# center high score at top of the screen
		self.high_score_rect = self.score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top
		
	'''
		turn the level into a rendered image
	'''
	def prep_level(self):
		self.level_image = self.font.render(str(self.stats.level), True,
						self.text_color, self.settings.bg_color)
		
		# position level below the score
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10
		
	'''
		show how many ships are left
	'''
	def prep_ships(self):
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.settings, self.screen)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)
		
	'''
		draw score to the screen
	'''
	def show_score(self):
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		
		# draw ships
		self.ships.draw(self.screen)