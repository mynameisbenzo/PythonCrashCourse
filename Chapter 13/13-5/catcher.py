import pygame

class Catcher():
	def __init__(self, settings, screen):
		self.screen = screen
		self.settings = settings
		
		self.image = pygame.image.load(
			"images/CatcherAnimated.gif")
		self.rect = self.image.get_rect()
		self.screenRect = screen.get_rect()
		
		self.rect.centerx = self.screenRect.centerx
		self.rect.bottom = self.screenRect.bottom - 100
		
		self.center = float(self.rect.centerx)
		
		self.right = False
		self.left = False
		# self.notMoving = True
		
	def update(self):
		if self.right and self.rect.right < self.screenRect.right:
			self.center += self.settings.catcherSpeed
		if self.left and self.rect.left > 0:
			self.center -= self.settings.catcherSpeed
		self.rect.centerx = self.center
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)