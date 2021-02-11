
import time
import os
import copy


nb_line = 10
nb_column = 20


matrix = [[0 for j in range(nb_column)] for i in range(nb_line)]

matrix[3][1] = 1
matrix[3][2] = 1
matrix[3][3] = 1


old_matrix = copy.deepcopy(matrix)





def print_matrix():

	for line in range(nb_line):
		for column in range(nb_column):
			print(matrix[line][column], end='')
		print()


def count_neighboorn(line, column):

	nb_cells = 0

	for i in range(line - 1, line + 2):
		for j in range(column - 1, column + 2):
			if (i != line or j != column) and old_matrix[i][j] != 0:
				nb_cells += 1

	return nb_cells







print_matrix()

print(count_neighboorn(2,1))
print(count_neighboorn(3,3))

input()





while True:


	print_matrix()
	time.sleep(1)
	os.system('cls')





input()