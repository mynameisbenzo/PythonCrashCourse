'''
	bullet class to use to manage all 
	behaviors of bullets shot by the 
	ship
'''
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	
	# initializer / create the bullet
	def __init__(self, settings, screen, ship):
		super().__init__()
		self.screen = screen
		
		# create bullet at 0,0 and then set position correctly
		self.rect = pygame.Rect(0,0, settings.bullet_width,
			settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		# keep track of decimal version of bullet position
		self.y = float(self.rect.y)
		
		self.color = settings.bullet_color
		self.speed = settings.bullet_speed
	
	# move bullet up the screen
	def update(self):
		# update decimal position
		self.y -= self.speed
		# update rect position
		self.rect.y = self.y
		
	# draw bullet on screen
	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)