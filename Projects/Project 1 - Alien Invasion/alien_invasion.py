'''
	Alien Invasion examples from the text
'''
import sys

import pygame

def run_game():
	# initialize game and create screen object
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption("Alien Invasion")
	
	# start the game loop
	while True:
		# look for keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
		# display screen
		pygame.display.flip()

run_game()