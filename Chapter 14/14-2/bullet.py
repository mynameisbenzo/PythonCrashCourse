import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, settings, screen, ship):
		super().__init__()
		self.screen = screen
		
		self.rect = pygame.Rect(0, 0, settings.bulletWidth,
								settings.bulletHeight)
		self.rect.centery = ship.rect.centery
		self.rect.right = ship.rect.right
		
		self.x = float(self.rect.x)
		
		self.color = settings.bulletColor
		self.speed = settings.bulletSpeed
		
	def update(self):
		self.x += self.speed
		self.rect.x = self.x
		
	def drawBullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)