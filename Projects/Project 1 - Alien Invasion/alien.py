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