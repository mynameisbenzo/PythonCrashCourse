'''
	a single alien in a fleet of invading aliens
'''
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self, settings, screen):
		super().__init__()
		self.screen = screen
		self.settings = settings
		
		# load alien image and set its rect attribute
		self.image = pygame.image.load(
			"images/alien.png")
		self.rect = self.image.get_rect()
		
		# position alien close to the top left of the screen
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		# will hold alien's exact position
		self.x = float(self.rect.x)
		
	# draw alien
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
	# check if an alien is at the edge of the screen
	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
	
	# move the aliens to the right
	def update(self):
		self.x += (self.settings.alien_speed_factor *
					self.settings.fleet_direction)
		self.rect.x = self.x 