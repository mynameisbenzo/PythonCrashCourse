import pygame
from pygame.sprite import Sprite
from random import randint

class Target(Sprite):
	def __init__(self, settings, screen):
		super().__init__()
		self.screen = screen
		self.settings = settings
		
		self.image = pygame.image.load(
			"images/Target.png")
		self.rect = self.image.get_rect()
		self.screenRect = screen.get_rect()
		
		self.rect.right = self.screenRect.right
		self.rect.centery = self.screenRect.centery
		
		self.y = float(self.rect.centery)
		self.speed = self.getSpeed()
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
	def check_edges(self):
		if self.rect.top < self.screenRect.top:
			self.speed = self.getSpeed()
			return True
		if self.rect.bottom > self.screenRect.bottom:
			self.speed = self.getSpeed()
			return True
	
	def resetPosition(self):
		self.y = randint(self.screenRect.top, self.screenRect.bottom)
		self.rect.centery = self.y
	
	def update(self):
		self.y += (self.speed * self.settings.targetDirection)
		self.rect.centery = self.y 
		
	def getSpeed(self):
		return randint(self.settings.targetSpeed['lower'],
						self.settings.targetSpeed['upper'])