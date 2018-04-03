import sys
import pygame

from bullet import Bullet

def check_events(settings, screen, ship, bullets,
			target, stats, play):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			keyDown(event, settings, screen, ship, 
					bullets, stats, target)
		elif event.type == pygame.KEYUP:
			keyUp(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mX, mY = pygame.mouse.get_pos()
			check_play_button(ship, bullets,
					stats, play, mX, mY)
			
def keyUp(event, ship):
	if event.key == pygame.K_UP:
		ship.up = False
	elif event.key == pygame.K_DOWN:
		ship.down = False
			
def keyDown(event, settings, screen, ship, bullets,
			stats, target):
	if event.key == pygame.K_UP:
		ship.up = True
	elif event.key == pygame.K_DOWN:
		ship.down = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(settings, screen, ship, bullets)
	elif event.key == pygame.K_p:
		if not stats.game_active:
			start_game(stats, bullets, ship)
	elif event.key == pygame.K_q:
		sys.exit()
			
def fire_bullet(settings, screen, ship, bullets):
	if len(bullets) < settings.maxBullets:
		newBullet = Bullet(settings, screen, ship)
		bullets.add(newBullet)
			
def check_play_button(ship, bullets,
					stats, play, mX, mY):
	button_clicked = play.rect.collidepoint(mX, mY)
	if button_clicked and not stats.game_active:
		start_game(stats, bullets, ship)
					
def start_game(stats, bullets, ship):
	pygame.mouse.set_visible(False)
	
	stats.reset_stats()
	stats.game_active = True
	
	bullets.empty()
	
	ship.center_ship()
	
def stop_game(stats, bullets, ship):
	pygame.mouse.set_visible(True)
	
	stats.reset_stats()
	stats.game_active = False
	
	bullets.empty()
	
	ship.center_ship()
	
def update_screen(settings, screen, stats, ship,
					target, bullets, play):
	screen.fill(settings.bgColor)
	
	for bullet in bullets.sprites():
		bullet.drawBullet()
		
	ship.blitme()
	target.blitme()
	
	if not stats.game_active:
		play.drawButton()
	
	pygame.display.flip()
	
def update_bullets(settings, screen, ship, target,
					bullets, stats):
	bullets.update()
	
	screenRect = screen.get_rect()
	
	checkBulletTargetCollision(ship, target, bullets, stats)
							
def update_target(settings, stats, screen,
				ship, target, bullets):
	if settings.currentFrame > settings.updateOnFrame:
		checkTargetEdges(settings, screen, target)
		target.update()
		
		settings.currentFrame = 0
	else:
		settings.currentFrame += 1
							
def checkTargetEdges(settings, screen, target):
	if target.check_edges():
		settings.targetDirection *= -1
		target.resetPosition()
		
def checkBulletTargetCollision(ship, target, bullets, stats):
	if pygame.sprite.spritecollideany(target, 
					bullets):
		stop_game(stats, bullets, ship)