'''
	A class for a ship object to be used
	in alien_invasion
'''
import pygame

class Ship():
	# create ship and set position
	def __init__(self,screen):
		self.screen = screen
		
		'''
			load the ship image and get
			its rect
		'''
		self.image = pygame.image.load(
			"images/ship.png")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		'''
			when a ship is created, always
			start it at the bottom center of
			the screen
		'''
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
	# draw the ship on the given location
	def blitme(self):
		self.screen.blit(self.image, self.rect)