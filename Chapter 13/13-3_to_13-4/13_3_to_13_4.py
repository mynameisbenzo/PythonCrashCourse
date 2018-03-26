'''
	Goals for the following exercises:
	13-3)
		1) Load a raindrop image
		2) Create grid of raindrops
		3) Raindrops will fall towards the bottom
			until they disappear
	13-4)
		1) When bottom row hits the bottom and
			disappears, new row will appear at 
			the top.
'''
import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from raindrop import RainDrop
import game_functions as gf

def run_game():
	pygame.init()
	drSettings = Settings()
	screen = pygame.display.set_mode(
		(drSettings.screenWidth,
			drSettings.screenHeight))
	pygame.display.set_caption("Rain Drop")
	
	drops = Group()
	
	gf.create_drops(drSettings, screen, drops)
	
	while True:
		gf.check_events(drSettings, screen)
		gf.update_drops(drSettings, drops)
		gf.update_screen(drSettings, screen,
			drops)

run_game()