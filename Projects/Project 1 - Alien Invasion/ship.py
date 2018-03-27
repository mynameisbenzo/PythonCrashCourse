'''
	A class for a ship object to be used
	in alien_invasion
'''
import pygame

class Ship():
	# create ship and set position
	def __init__(self, settings, screen):
		self.screen = screen
		self.mySettings = settings
		
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
		
		'''
			decimal value for the ship's center
		'''
		self.center = float(self.rect.centerx)
		
		'''
			Movement flags
		'''
		self.moving_right = False
		self.moving_left = False
		
		
	'''
		update the position of the ship according
		to the movement flags
	'''
	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.mySettings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.mySettings.ship_speed_factor
		# update rect object using self.center
		self.rect.centerx = self.center
			
	'''
		draw the ship on the given location
	'''
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
	'''
		center the ship on the screen
	'''
	def center_ship(self):
		self.center = self.screen_rect.centerx