import sys
import pygame
from random import randint
from star import Star

def check_events(settings, screen):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			keydownEvents(event)

def keydownEvents(event):
	if event.key == pygame.K_q:
		sys.exit()
			
def update_screen(settings, screen, stars):
	screen.fill(settings.bgColor)
	stars.draw(screen)
	pygame.display.flip()
	
def getNumStarsX(settings, sWidth):
	space_x = (settings.scWidth - (2 * sWidth)) * 2
	numStarsX = int(space_x / (2 * sWidth))
	return randint(1, numStarsX)
	
def getNumRows(settings, sHeight):
	space_y = (settings.scHeight -
		(3 * sHeight)) * 2
	numRows = int(space_y / (2 * sHeight))
	return numRows
	
def create_star(settings, screen, stars,
		sNum, rowNum):
	star = Star(settings, screen)
	sWidth = star.rect.width
	star.x = sWidth + 2 * sWidth * sNum
	star.rect.x = star.x * randint(-2 , 2)
	star.rect.y = star.rect.height + 2 * star.rect.height * rowNum * randint(1 , 3)
	stars.add(star)
	
def create_sky(settings, screen, stars):
	star = Star(settings, screen)
	numRows = getNumRows(settings, star.rect.height)
	
	for rowNum in range(numRows):
		numStarsX = getNumStarsX(settings, star.rect.width)
		while numStarsX > 0:
			sNum = randint(0, numStarsX)
			create_star(settings, screen, stars, sNum,
				rowNum)
			numStarsX -= randint(0,numStarsX)