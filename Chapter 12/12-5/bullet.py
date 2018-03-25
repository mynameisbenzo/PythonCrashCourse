import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	
	def __init__(self, settings, screen, ship):
		super().__init__()
		self.screen = screen
		
		self.rect = pygame.Rect(0,0, settings.bWidth,
			settings.bHeight)
		self.rect.centery = ship.rect.centery
		self.rect.right = ship.rect.right
		
		self.x = float(self.rect.x)
		
		self.color = settings.bullColor
		self.speed = settings.bSpeed
	
	def update(self):
		self.x += self.speed
		self.rect.x = self.x
		
	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)