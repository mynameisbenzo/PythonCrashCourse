import pygame
class MyCharacter():
	def __init__(self, screen):
		self.screen = screen
		
		# load image
		self.image = pygame.image.load(
			"images/alien.png")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# positions
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		
		# decimal value for center
		self.centerx = float(self.rect.centerx)
		self.centery = float(self.rect.centery)
		
		# movement flags
		self.right = False
		self.left = False
		self.up = False
		self.down = False
	
	def update(self):
		if self.right and self.rect.right < self.screen_rect.right:
			self.centerx += 1
		if self.left and self.rect.left > 0:
			self.centerx -= 1
		if self.up and self.rect.top > 0:
			self.centery -= 1
		if self.down and self.rect.bottom < self.screen_rect.bottom:
			self.centery += 1
		self.rect.centerx = self.centerx
		self.rect.centery = self.centery
	
	def blitme(self):
		self.screen.blit(self.image, self.rect)