
import time
import os
import copy


nb_line = 10
nb_column = 20


matrix = [[0 for j in range(nb_column)] for i in range(nb_line)]

matrix[3][1] = 1
matrix[3][2] = 1
matrix[3][3] = 1







def print_matrix():

	for line in range(nb_line):
		for column in range(nb_column):
			print(matrix[line][column], end='')
		print()

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





while True:

	old_matrix = copy.deepcopy(matrix)
	print_matrix() # O(n**2)
	time.sleep(1)
	update_stat() # O(n**2*9)
	os.system('cls')





input()