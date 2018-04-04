'''
	Common functions that alien_invasion can
	or will use
'''
import sys
import pygame
from time import sleep

from bullet import Bullet
from alien import Alien

# look for keypresses and mouse events
def check_events(settings, screen, ship, bullets, aliens,
					stats, play, sb, sounds):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			save_high_score(stats)
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			keydown_events(event, settings, screen, ship, 
				bullets, stats, aliens, sb, sounds)
		elif event.type == pygame.KEYUP:
			keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(settings, screen, ship, aliens, 
								bullets, stats, play, mouse_x, 
								mouse_y, sb, sounds)

'''
	save high score
'''					
def save_high_score(stats):
	with open('highscore.txt', 'w') as file:
		file.write(str(stats.high_score))

# start the game
def start_game(stats, aliens, bullets, settings, screen,
					ship, sb, sounds):
	# reset game settings
	settings.initialize_dynamic_settings()
	
	# hide the mouse
	pygame.mouse.set_visible(False)
	
	# play bgmusic
	sounds.bg.play()
	
	# reset stats and start game
	stats.reset_stats()
	stats.game_active = True
	
	# reset scoreboard images
	sb.prep_score()
	sb.prep_high_score()
	sb.prep_level()
	sb.prep_ships()
	
	# empty list of aliens/bullets
	aliens.empty()
	bullets.empty()
	
	# create new fleet and center ship
	create_fleet(settings, screen, ship, aliens)
	ship.center_ship()
		
# start a new game when the player clicks Play
def check_play_button(settings, screen, ship, aliens, 
						bullets, stats, play, mX, mY,
						sb, sounds):
	button_clicked = play.rect.collidepoint(mX, mY)
	if button_clicked and not stats.game_active:
		start_game(stats, aliens, bullets, settings, 
					screen, ship, sb, sounds)
			
# checks keydown
def keydown_events(event, settings, screen, ship, bullets,
			stats, aliens, sb, sounds):
	if event.key == pygame.K_RIGHT:
		# move the ship right
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		# move the ship left
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(settings, screen, ship, bullets, sounds, stats)
	elif event.key == pygame.K_p:
		if not stats.game_active:
			start_game(stats, aliens, bullets, settings, 
					screen, ship, sb, sounds)
	elif event.key == pygame.K_q:
		save_high_score(stats)
		sys.exit()
	
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
def update_screen(settings, screen, stats, 
		ship, aliens, bullets, play, sb):
	# redraw screen
	screen.fill(settings.bg_color)
	
	# redraw bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	ship.blitme()
	aliens.draw(screen)
	
	# draw score information
	sb.show_score()
	
	# draw play button if game is inactive
	if not stats.game_active:
		play.draw_button()
	
	# display screen
	pygame.display.flip()
	
'''
	update position of the bullets and get rid
	of the old bullets
'''
def update_bullets(settings, screen, ship,
		aliens, bullets, stats, sb, sounds):
	# update positions
	bullets.update()
	
	# delete bullets not on screen
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	
	check_bullet_alien_collisions(settings, screen,
		ship, aliens, bullets, stats, sb, sounds)

'''
	respond to bullet -> alien collisions
'''
def check_bullet_alien_collisions(settings, screen, 
		ship, aliens, bullets, stats, sb, sounds):
	collisions = pygame.sprite.groupcollide(bullets, 
		aliens, True, True)
		
	if collisions:
		for aliens in collisions.values():
			stats.score += settings.alien_points * len(aliens)
			sb.prep_score()
			sounds.alienExplode.play()
		check_high_score(stats, sb)
		
	if len(aliens) == 0:
		start_new_level(bullets, settings, stats, sb, screen, ship, aliens)
		
'''
	start new level when all aliens are destroyed
'''
def start_new_level(bullets, settings, stats, sb, screen, ship, aliens):
	# destroy existing bullets and make new fleet
	bullets.empty()
	settings.increase_speed()
	
	# increase level
	stats.level += 1
	sb.prep_level()
	
	create_fleet(settings, screen, ship, aliens)
		
'''
	fire a bullet if the limit has not been reached
'''
def fire_bullet(settings, screen, ship, bullets, sounds, stats):
	# create a bullet
	if len(bullets) < settings.max_bullets:
		if stats.game_active:
			sounds.shoot()
		new_bullet = Bullet(settings, screen, ship)
		bullets.add(new_bullet)

'''
	find the number of aliens that fit in a row
'''
def getNumAliensX(settings, aWidth):
	space_x = settings.screen_width - (2 * aWidth)
	numAliensX = int(space_x / (2 * aWidth))
	return numAliensX
	
'''
	get number of rows of aliens that can fit on 
	the screen
'''
def getNumRows(settings, sHeight, aHeight):
	space_y = (settings.screen_height -
		(3 * aHeight) - sHeight)
	numRows = int(space_y / (2 * aHeight))
	return numRows
		
'''
	create and place an alien
'''
def create_alien(settings, screen, aliens, 
		aNumber, rowNum):
	alien = Alien(settings, screen)
	aWidth = alien.rect.width
	alien.x = aWidth + 2 * aWidth * aNumber
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * rowNum
	aliens.add(alien)
	
'''
	creating the fleet of aliens by finding the 
	spacing between allowed between aliens
'''
def create_fleet(settings, screen, ship, aliens):
	alien = Alien(settings, screen)
	numAliensX = getNumAliensX(settings, alien.rect.width)
	numRows = getNumRows(settings, ship.rect.height, 
		alien.rect.height)
	
	# creating first row of aliens
	for rowNum in range(numRows):
		for aNumber in range(numAliensX):
			create_alien(settings, screen, aliens, aNumber,
					rowNum)

'''
	check if aliens have reached the bottom of the screen
'''
def check_aliens_bottom(settings, stats, screen, ship, aliens,
		bullets, sb, sounds):
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# the same as if the ship was hit
			ship_hit(settings, stats, screen, ship, aliens, 
				bullets, sb, sounds)
			break
					
'''
	update alien positions
'''
def update_aliens(settings, stats, screen, ship, aliens, bullets, sb, sounds):
	if settings.currentFrame > settings.frameCount:
		check_fleet_edges(settings, aliens)
		aliens.update()
		
		# look for alien -> ship collisions
		if pygame.sprite.spritecollideany(ship, aliens):
			ship_hit(settings, stats, screen, ship, aliens, bullets, sb, sounds)
		
		# look for aliens -> bottom of screen collisions
		check_aliens_bottom(settings, stats, screen, ship, aliens,
			bullets, sb, sounds)
		settings.currentFrame = 0
	else:
		settings.currentFrame += 1

'''
	if an alien reaches the edge, switch fleet
	direction
'''
def check_fleet_edges(settings, aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(settings, aliens)
			break

'''
	drop the fleet and change direction
'''
def change_fleet_direction(settings, aliens):
	for alien in aliens.sprites():
		alien.rect.y += settings.fleet_drop_speed
	settings.fleet_direction *= -1
	
'''
	respond to ship hit
'''
def ship_hit(settings, stats, screen, ship, aliens, bullets, sb, sounds):
	if stats.ships_left > 0:
		# decrement ships left
		stats.ships_left -= 1
		
		# update scoreboard
		sb.prep_ships()
		
		# empty list of aliens and bullets
		aliens.empty()
		bullets.empty()
		
		# create a new fleet and center the ship
		create_fleet(settings, screen, ship, aliens)
		ship.center_ship()
		
		# pause
		sleep(0.5)
	else:
		stats.game_active = False
		sounds.bg.stop()
		pygame.mouse.set_visible(True)
		
'''
	check to see if there's a new high score
'''
def check_high_score(stats, sb):
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()