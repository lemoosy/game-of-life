import copy
import pygame
from const import *
from square import Square
from pygame.locals import *


pygame.init()
window = pygame.display.set_mode((SIZE_WINDOW_X, SIZE_WINDOW_Y))



matrix = None



def out_of_dimension(line, column):

	return line < 0 or column < 0 or line >= nb_line or column >= nb_column

def count_neighboorn(line, column):

	nb_cells = 0

	for i in range(line - 1, line + 2):
		for j in range(column - 1, column + 2):
			if not(out_of_dimension(i, j)):
				if (i != line or j != column) and old_matrix[i][j] != 0:
					nb_cells += 1

	return nb_cells

def update_stat():

	for i in range(nb_line):
		for j in range(nb_column):

			nb_neighboorn = count_neighboorn(i, j)

			if old_matrix[i][j] == 0 and nb_neighboorn == 3:
				matrix[i][j] = 1
				continue

			if old_matrix[i][j] == 1 and (nb_neighboorn > 3 or nb_neighboorn < 2):
				matrix[i][j] = 0



init_matrix()
clock = pygame.time.Clock()







while True:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	old_matrix = copy.deepcopy(matrix)
	screen.fill(black)
	draw_matrix() # O(n**2)
	pygame.display.flip()
	clock.tick(1)
	update_stat() # O(n**2*9)



input()