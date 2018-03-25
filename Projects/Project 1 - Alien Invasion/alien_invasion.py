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
	
	# set background color
	bg_color = (230,230,230)
	
	# start the game loop
	while True:
		# look for keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
				
		# redraw screen
		screen.fill(bg_color)
				
		# display screen
		pygame.display.flip()

run_game()