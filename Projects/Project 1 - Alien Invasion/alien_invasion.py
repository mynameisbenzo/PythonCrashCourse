'''
	Alien Invasion examples from the text
'''
import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from soundboard import Soundboard
import game_functions as gf

def run_game():
	# initialize game and create screen object
	pygame.init()
	alien_settings = Settings()
	screen = pygame.display.set_mode(
		(alien_settings.screen_width,
			alien_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# create the play button
	play_button = Button(alien_settings, screen, "Play")
	
	# create an instance to store game statistics
	stats = GameStats(alien_settings)
	
	# create instance of the scoreboard
	sb = Scoreboard(alien_settings, screen, stats)
	
	# create soundboard
	sounds = Soundboard()
	
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
		gf.check_events(alien_settings, screen, ship, bullets,
			aliens, stats, play_button, sb, sounds)
		if stats.game_active:
			ship.update()
			gf.update_bullets(alien_settings, screen, ship,
				aliens, bullets, stats, sb, sounds)
			gf.update_aliens(alien_settings, stats, screen, ship, 
				aliens, bullets, sb, sounds)
		gf.update_screen(alien_settings, screen, stats,
			ship, aliens, bullets, play_button, sb)

run_game()