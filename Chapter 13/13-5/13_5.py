import sys

import pygame
from settings import Settings
from catcher import Catcher
from apple import Apple
import game_functions as gf

def run_game():
	pygame.init()
	catchSettings = Settings()
	screen = pygame.display.set_mode(
		(catchSettings.screen_width,
			catchSettings.screen_height))
	pygame.display.set_caption("Apple Catcher!")
	
	catcher = Catcher(catchSettings, screen)
	
	apple = Apple(catchSettings, screen)
	
	while True:
		gf.check_events(catchSettings, screen, catcher, apple)
		catcher.update()
		gf.update_apple(catchSettings, apple, catcher)
		gf.update_screen(catchSettings, screen, 
			catcher, apple)
			
run_game()