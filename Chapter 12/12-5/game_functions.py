import sys
import pygame
from bullet import Bullet

def check_events(settings, screen, ship, bullets):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			keydown_events(event, settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			keyup_events(event, ship)

def keydown_events(event, settings, screen, ship, bullets):
	if event.key == pygame.K_UP:
		ship.up = True
	elif event.key == pygame.K_DOWN:
		ship.down = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(settings, screen, ship, bullets)
	
def keyup_events(event, ship):
	if event.key == pygame.K_UP:
		ship.up = False
	elif event.key == pygame.K_DOWN:
		ship.down = False
			
def update_screen(settings, screen, ship, bullets):
	screen.fill(settings.bgColor)
	
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	ship.blitme()

	pygame.display.flip()
	
def update_bullets(bullets, screen):
	bullets.update()
	
	for bullet in bullets.copy():
		if bullet.rect.right >= screen.right:
			bullets.remove(bullet)
			
def fire_bullet(settings, screen, ship, bullets):
	# create a bullet
	if len(bullets) < settings.maxBullets:
		new_bullet = Bullet(settings, screen, ship)
		bullets.add(new_bullet)