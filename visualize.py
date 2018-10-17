import pygame


def visualize(x,y):
	pygame.draw.rect(screen, (0,0,0), (x+25,y+25,40,40), 0)
	pygame.display.update
	pygame.display.flip()

def init_pygame():
	pygame.init()
	screen = pygame.display.set_mode((400,400))
	pygame.draw.rect(screen, (255,255,255), (25,25,350,350), 0)
	pygame.display.update
