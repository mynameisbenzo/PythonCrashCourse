'''
	The goals here are:
		1) Find an image of a star
		2) Make a grid of stars
		3) Try placing stars randomly!
'''
import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from star import Star
import game_functions as gf

def run_game():
	pygame.init()
	stSettings = Settings()
	screen = pygame.display.set_mode(
		(stSettings.scWidth,
			stSettings.scHeight))
	pygame.display.set_caption("Star grid")
	
	stars = Group()
	
	gf.create_sky(stSettings, screen, stars)
	
	while True:
		gf.check_events(stSettings, screen)
		gf.update_screen(stSettings, screen,
			stars)

run_game()