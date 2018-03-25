'''
	Alien Invasion examples from the text
'''
import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	# initialize game and create screen object
	pygame.init()
	alien_settings = Settings()
	screen = pygame.display.set_mode(
		(alien_settings.sWidth,
			alien_settings.sHeight))
	pygame.display.set_caption("Alien Invasion")
	
	# create a ship
	ship = Ship(alien_settings, screen)
	
	# a group to store bullets in
	bullets = Group()
	
	# start the game loop
	while True:
		gf.check_events(alien_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets, screen.get_rect())
		gf.update_screen(alien_settings, screen, ship, bullets)

run_game()