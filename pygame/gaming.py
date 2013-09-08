import pygame

def run_game():
	SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
    	BG_COLOR = 150, 150, 80
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    	#clock = pygame.time.Clock()
	screen.fill(BG_COLOR)
	#pygame.display.flip()

#def exit_game():
#    sys.exit()

run_game()