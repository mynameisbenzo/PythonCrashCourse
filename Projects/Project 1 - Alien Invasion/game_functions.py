'''
	Common functions that alien_invasion can
	or will use
'''
import sys
import pygame
from bullet import Bullet

# look for keypresses and mouse events
def check_events(settings, screen, ship, bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			keydown_events(event, settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			keyup_events(event, ship)

# checks keydown
def keydown_events(event, settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		# move the ship right
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		# move the ship left
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(settings, screen, ship, bullets)
	
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
def update_screen(settings, screen, ship, bullets):
	# redraw screen
	screen.fill(settings.bg_color)
	
	# redraw bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	ship.blitme()
	
	# display screen
	pygame.display.flip()
	
'''
	update position of the bullets and get rid
	of the old bullets
'''
def update_bullets(bullets):
	# update positions
	bullets.update()
	
	# delete bullets not on screen
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
			
'''
	fire a bullet if the limit has not been reached
'''
def fire_bullet(settings, screen, ship, bullets):
	# create a bullet
	if len(bullets) < settings.max_bullets:
		new_bullet = Bullet(settings, screen, ship)
		bullets.add(new_bullet)