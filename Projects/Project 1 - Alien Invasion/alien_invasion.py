'''
	Alien Invasion examples from the text
'''
import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
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
	ship = Ship(alien_settings, screen)
	
	# a group to store bullets in
	bullets = Group()
	
	# make an alien
	aliens = Group()
	
	# create a fleet of aliens
	gf.create_fleet(alien_settings, screen, ship, aliens)
	
	# start the game loop
	while True:
		gf.check_events(alien_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(alien_settings, screen, 
			ship, aliens, bullets)

run_game()