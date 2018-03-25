import sys
import pygame

def check_events(c):
	for event in pygame.event.get():
		print(event)
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			keydown_events(event, c)
		elif event.type == pygame.KEYUP:
			keyup_events(event, c)
			
def keydown_events(event, c):
	if event.key == pygame.K_RIGHT:
		# move the ship right
		c.right = True
	if event.key == pygame.K_LEFT:
		# move the ship left
		c.left = True
	if event.key == pygame.K_UP:
		# move the ship right
		c.up = True
	if event.key == pygame.K_DOWN:
		# move the ship left
		c.down = True
		
def keyup_events(event, c):
	if event.key == pygame.K_RIGHT:
		# move the ship right
		c.right = False
	if event.key == pygame.K_LEFT:
		# move the ship left
		c.left = False
	if event.key == pygame.K_UP:
		# move the ship right
		c.up = False
	if event.key == pygame.K_DOWN:
		# move the ship left
		c.down = False
	
	
def update_screen(settings, screen, character):
	screen.fill(settings.bg_color)
	character.blitme()
	
	pygame.display.flip()