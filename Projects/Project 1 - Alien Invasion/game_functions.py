'''
	Common functions that alien_invasion can
	or will use
'''
import sys
import pygame

# look for keypresses and mouse events
def check_events():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			
'''
	update images on the screen and flip to
	the new screen
'''
def update_screen(settings, screen, ship):
	# redraw screen
	screen.fill(settings.bg_color)
	ship.blitme()
	
	# display screen
	pygame.display.flip()