import pygame


def visualize(x,y):
	pygame.draw.rect(screen, (255,255,255), (x,y,40,40), 1)
	pygame.display.update


pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.draw.rect(screen, (255,255,255), (0,0,200,200), 1)
pygame.display.update

done = False

while not done:
		visualize(40,40)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True
		pygame.display.flip()