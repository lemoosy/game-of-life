import time
import os
import copy
import pygame
from constants import *
from square import Square
from pygame.locals import *



pygame.init()
screen = pygame.display.set_mode((windowX, windowY))



matrix = None
nb_line = None
nb_column = None



def matrix_load():

	file = open('matrix.txt')

	text = file.read() # text = '11111\n10100\n00001\n10101\n11111'
	text = text.split() # text = ['11111', '10100', '00001', '10101', '11111']
	text = [[int(k) for k in list(i)] for i in text] # text = [[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], ...]
	
	file.close()

	return text

def init_matrix():

	global matrix, nb_line, nb_column

	matrix = matrix_load()
	nb_line = len(matrix)
	nb_column = len(matrix[0])

def print_matrix():

	for line in range(nb_line):
		for column in range(nb_column):
			print(matrix[line][column], end='')
		print()

def draw_matrix():

	for line in range(nb_line):
		for column in range(nb_column):
			if matrix[line][column] != 0:
				my_square = Square(line * size_cellX, column * size_cellY)
				my_square.draw(screen)

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
	os.system('cls')



input()