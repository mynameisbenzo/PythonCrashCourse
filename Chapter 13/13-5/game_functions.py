import sys
import pygame
from apple import Apple

def check_events(settings, screen, catcher, apple):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			keydownEvents(event, catcher)
		elif event.type == pygame.KEYUP:
			keyupEvents(event, catcher)
			
def keydownEvents(event, catcher):
	if event.key == pygame.K_RIGHT:
		catcher.right = True
	elif event.key == pygame.K_LEFT:
		catcher.left = True
	elif event.key == pygame.K_q:
		sys.exit()
		
def keyupEvents(event, catcher):
	if event.key == pygame.K_RIGHT:
		catcher.right = False
	elif event.key == pygame.K_LEFT:
		catcher.left = False
		
def update_apple(settings, stats, apple, catcher):
	if not apple.check_edges():
		bottomCollision(stats, apple)
	else:
		appleDrop(settings, apple)	
	checkCollisions(apple, catcher)
	
def bottomCollision(stats, apple):
	stats.livesLeft -= 1
	if stats.livesLeft == 0:
		stats.game_active = False
		print("Game Over!")
	else:
		apple.toTheTop()
	
def checkCollisions(apple, catcher):
	if pygame.sprite.collide_rect(apple, catcher):
		apple.toTheTop()
		
def appleDrop(settings, apple):
	if settings.currentFrame == settings.frameCount:
		apple.rect.y += settings.appleDropSpeed
		settings.currentFrame = 0
	else:
		settings.currentFrame += 1
		
def update_screen(settings, screen, catcher, apple):
	screen.fill(settings.bg_color)
	catcher.blitme()
	apple.blitme()
	pygame.display.flip()