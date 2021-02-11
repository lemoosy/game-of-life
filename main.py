





nb_line = 10
nb_column = 20


matrix = [[0 for j in range(nb_column)] for i in range(nb_line)]



def print_matrix():

	for line in range(nb_line):
		for column in range(nb_column):
			print(matrix[line][column], end='')
		print()





print_matrix()

input()