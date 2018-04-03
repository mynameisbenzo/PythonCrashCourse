import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from target import Target
from gameStats import GameStats
from button import Button
import game_functions as gf

def run_game():
	pygame.init()
	targetSettings = Settings()
	screen = pygame.display.set_mode(
		(targetSettings.screenWidth,
			targetSettings.screenHeight))
	pygame.display.set_caption("Shoot the Target!")
	
	play = Button(targetSettings, screen, "Play")
	
	stats = GameStats(targetSettings)
	
	ship = Ship(targetSettings, screen)
	
	bullets = Group()
	
	target = Target(targetSettings, screen)
	
	while True:
		gf.check_events(targetSettings, screen, ship, bullets,
			target, stats, play)
		if stats.game_active:
			ship.update()
			gf.update_bullets(targetSettings, screen, ship, 
				target, bullets, stats)
			gf.update_target(targetSettings, stats, screen,
				ship, target, bullets)
		gf.update_screen(targetSettings, screen, stats, ship,
			target, bullets, play)
			
run_game()