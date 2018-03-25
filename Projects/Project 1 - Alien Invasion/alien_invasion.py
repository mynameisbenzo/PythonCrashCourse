'''
	Alien Invasion examples from the text
'''
import sys

import pygame
from settings import Settings
from ship import Ship

def run_game():
	# initialize game and create screen object
	pygame.init()
	alien_settings = Settings()
	screen = pygame.display.set_mode(
		(alien_settings.screen_width,
			alien_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# create a ship
	ship = Ship(screen)
	
	# set background color
	bg_color = (230,230,230)
	
	# start the game loop
	while True:
		# look for keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
		# redraw screen
		screen.fill(alien_settings.bg_color)
		ship.blitme()
		
		# display screen
		pygame.display.flip()

run_game()