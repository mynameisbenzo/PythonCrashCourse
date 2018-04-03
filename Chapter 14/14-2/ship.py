import pygame

class Ship():
	def __init__(self, settings, screen):
		self.screen = screen
		self.settings = settings
		
		self.image = pygame.image.load(
			"images/UpDownPlane.png")
		self.rect = self.image.get_rect()
		self.screenRect = screen.get_rect()
		
		self.rect.centery = self.screenRect.centery
		self.rect.left = self.screenRect.left
		
		self.centery = float(self.rect.centery)
		
		self.up = False
		self.down = False
		
	def update(self):
		if self.up and self.rect.top > 0:
			self.centery -= self.settings.shipSpeed
		if self.down and self.rect.bottom < self.screenRect.bottom:
			self.centery += self.settings.shipSpeed
		self.rect.centery = self.centery
	
	def blitme(self):
		self.screen.blit(self.image, self.rect)
		
	def center_ship(self):
		self.center = self.screenRect.centery