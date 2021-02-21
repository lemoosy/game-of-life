from pygame.locals import *
import pygame

from const import *
from matrix import Matrix
from square import Square


pygame.init()
window = pygame.display.set_mode((SIZE_WINDOW_X, SIZE_WINDOW_Y))
matrix = Matrix()
clock = pygame.time.Clock()


while True:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()

	window.fill(BLACK)
	matrix.draw(window)
	pygame.display.flip()
	clock.tick(1)
	matrix.update()