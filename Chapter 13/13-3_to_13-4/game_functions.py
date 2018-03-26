import sys
import pygame
from raindrop import RainDrop

def check_events(settings, screen):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			keydownEvents(event)

def keydownEvents(event):
	if event.key == pygame.K_q:
		sys.exit()
		
def update_screen(settings, screen, drops):
	screen.fill(settings.bgColor)
	drops.draw(screen)
	pygame.display.flip()
		
def getNumDropsX(settings, dWidth):
	space_x = settings.screenWidth - (2 * dWidth)
	numDropsX = int(space_x / (2 * dWidth))
	return numDropsX
	
def getNumRows(settings, dHeight):
	space_y = (settings.screenHeight -
		(3 * dHeight))
	numRows = int(space_y / (2 * dHeight))
	return numRows
	
def create_drop(settings, screen, drops, dNum, rowNum):
	drop = RainDrop(settings, screen)
	dWidth = drop.rect.width
	drop.x = dWidth + 2 * dWidth * dNum
	drop.rect.x = drop.x
	drop.rect.y = drop.rect.height + 2 * drop.rect.height * rowNum
	drops.add(drop)
		
def create_drops(settings, screen, drops):
	drop = RainDrop(settings, screen)
	numDropsX = getNumDropsX(settings, drop.rect.width)
	numRows = getNumRows(settings, drop.rect.height)
	
	for rowNum in range(numRows):
		for dNumber in range(numDropsX):
			create_drop(settings, screen, drops, dNumber,
				rowNum)
				
def update_drops(settings, drops):
	checkDropEdges(settings, drops)
	drops.update()
	
def checkDropEdges(settings, drops):
	for drop in drops.sprites():
		goDown(settings, drops)
		if not drop.check_edges():
			drop.toTheTop()
			
			
def goDown(settings, drops):
	for drop in drops.sprites():
		drop.rect.y += settings.dropSpeed
		