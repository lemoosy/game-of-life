from const import *
from square import Square
import copy


class Matrix:

    def __init__(self):

        file = open('matrix.txt')

        text = file.read()
        text = text.split()
        text = [[int(j) for j in list(i)] for i in text]

        self.__matrix = text
        self.__line_count = len(self.__matrix)
        self.__column_count = len(self.__matrix[0])

        file.close()

    def print(self):

        for line in self.__matrix:
            print(*line, sep='')

    def draw(self, window):

        for line in range(self.__line_count):
            for column in range(self.__column_count):

                if self.__matrix[line][column] == 0:
                    square = Square(FIRST_POSITION_CELL_X + line * SIZE_CELL_X,FIRST_POSITION_CELL_Y + column * SIZE_CELL_Y, WHITE)
                else:
                    square = Square(FIRST_POSITION_CELL_X + line * SIZE_CELL_X,FIRST_POSITION_CELL_Y + column * SIZE_CELL_Y, RED)

                square.draw(window)

    #   refreshes the matrix, transform the cells
    def update(self):

        matrix_copy = copy.deepcopy(self.__matrix)

        for line in range(self.__line_count):
            for column in range(self.__column_count):

                cell_count = self.__cell_count_around(line, column)

                if matrix_copy[line][column] == 0 and cell_count == 3:
                    matrix_copy[line][column] = 1

                elif matrix_copy[line][column] == 1 and (cell_count > 3 or cell_count < 2):
                    matrix_copy[line][column] = 0

        self.__matrix = copy.deepcopy(matrix_copy)

    #   counts the cells number around a case
    def __cell_count_around(self, line, column):

        cell_count = -1 if self.__matrix[line][column] == 1 else 0

        for new_line in range(line - 1, line + 2):
            for new_column in range(column - 1, column + 2):
                if not (self.__out_of_dimension(new_line, new_column)):
                    cell_count += self.__matrix[new_line][new_column]

        return cell_count

    #   checks if the values are not out dimension of the matrix
    def __out_of_dimension(self, line, column):

        return line < 0 or column < 0 or line >= self.__line_count or column >= self.__column_count
