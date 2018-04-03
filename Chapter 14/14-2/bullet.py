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
		
		self.onScreen = True
		
	def update(self):
		self.x += self.speed
		self.rect.x = self.x
		
	def drawBullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
		
	def edgeHit(self):
		screenRect = self.screen.get_rect()
		if not self.onScreen:
			return False
		if self.rect.right > screenRect.right:
			self.onScreen = False
			return True
		else:
			return False