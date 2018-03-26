import pygame
from pygame.sprite import Sprite

class RainDrop(Sprite):
	def __init__(self, settings, screen):
		super().__init__()
		self.screen = screen
		self.settings = settings
		
		self.image = pygame.image.load(
			"images/WaterDrop.png")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		self.x = float(self.rect.x)
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
	def update(self):
		self.x += self.settings.dropSpeed
		
	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.bottom < self.screen_rect.bottom:
			return True
			
	def toTheTop(self):
		self.rect.y = self.screen_rect.top