'''
	Common functions that alien_invasion can
	or will use
'''
import sys
import pygame

# look for keypresses and mouse events
def check_events(ship):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			keydown_events(event, ship)
		elif event.type == pygame.KEYUP:
			keyup_events(event, ship)

# checks keydown
def keydown_events(event, ship):
	if event.key == pygame.K_RIGHT:
		# move the ship right
		ship.moving_right = True
	if event.key == pygame.K_LEFT:
		# move the ship left
		ship.moving_left = True

# checks keyup
def keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
				
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