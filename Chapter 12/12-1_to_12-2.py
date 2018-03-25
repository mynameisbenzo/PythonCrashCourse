'''
	Objectives:
		Create a game window with:
		
		12-1:
			A blue background
		12-2:
			Load an image in the center
			of the screen
'''
import sys
import pygame
from settings import Settings
from character import MyCharacter
import game_functions as gf

def run_game():
	pygame.init()
	mySettings = Settings()
	screen = pygame.display.set_mode(
		(mySettings.screen_width,
			mySettings.screen_height))
	pygame.display.set_caption("12-1 and 12-2")
	
	myChar = MyCharacter(screen)
	
	while True:
		gf.check_events(myChar)
		myChar.update()
		gf.update_screen(mySettings, screen, myChar)
		
run_game()