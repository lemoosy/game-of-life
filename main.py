from const import *
from matrix import Matrix
from square import Square
import pygame


pygame.init()
window = pygame.display.set_mode((SIZE_WINDOW_X, SIZE_WINDOW_Y))
matrix = Matrix()
clock = pygame.time.Clock()


while True:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()

		if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
			position_mouse_x = pygame.mouse.get_pos()[0]
			position_mouse_y = pygame.mouse.get_pos()[1]
			matrix.switch_cell(position_mouse_x, position_mouse_y)

	window.fill(BLACK)
	matrix.draw(window)
	pygame.display.flip()
	clock.tick(1)
	matrix.update()