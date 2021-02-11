
import time
import os
import copy



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

while True:

	old_matrix = copy.deepcopy(matrix)
	print_matrix() # O(n**2)
	time.sleep(1)
	update_stat() # O(n**2*9)
	os.system('cls')





input()