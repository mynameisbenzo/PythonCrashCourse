'''
	Alien Invasion examples from the text
'''
import sys

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

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
	
	# start the game loop
	while True:
		gf.check_events()
		gf.update_screen(alien_settings, screen, ship)

run_game()