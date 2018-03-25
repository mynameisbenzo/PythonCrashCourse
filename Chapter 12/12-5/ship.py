import pygame

class Ship():
	def __init__(self, settings, screen):
		self.screen = screen
		self.settings = settings
		
		self.image = pygame.image.load(
			"images/right_left_ship.png")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		self.rect.centery = self.screen_rect.centery
		self.rect.left = self.screen_rect.left
		
		self.centery = float(self.rect.centery)
		
		self.up = False
		self.down = False
		
	def update(self):
		if self.up and self.rect.top > 0:
			self.centery -= self.settings.shipSpeed
		if self.down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += self.settings.shipSpeed
		self.rect.centery = self.centery
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)