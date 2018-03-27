import pygame
from pygame.sprite import Sprite
from random import randint

class Apple(Sprite):
	def __init__(self, settings, screen):
		super().__init__()
		self.screen = screen
		self.settings = settings
		
		self.image = pygame.image.load(
			"images/Apple.png")
		self.rect = self.image.get_rect()
		self.screen_rect = self.screen.get_rect()
		
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		self.x = float(self.rect.x)
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
	def check_edges(self):
		if self.rect.bottom < self.screen_rect.bottom:
			return True
	
	def toTheTop(self):
		self.rect.y = self.screen_rect.top
		self.rect.x = randint(
			0,
			self.settings.screen_width - self.rect.width)