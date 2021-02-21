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
        self.line_count = len(self.__matrix)
        self.column_count = len(self.__matrix[0])

        file.close()

    def print(self):

        for line in self.__matrix:
            print(*line, sep='')

    def draw(self, window):

        for line in range(self.line_count):
            for column in range(self.column_count):
                if self.__matrix[line][column] != 0:
                    square = Square(line * SIZE_CELL_X, column * SIZE_CELL_Y)
                    square.draw(window)

    def cell_count_around(self, line, column):

        cell_count = -1 if self.__matrix[line][column] == 1 else 0

        for new_line in range(line - 1, line + 2):
            for new_column in range(column - 1, column + 2):
                if not (self.__out_of_dimension(new_line, new_column)):
                    cell_count += self.__matrix[new_line][new_column]

        return cell_count

    def update(self):

        matrix_copy = copy.deepcopy(self.__matrix)

        for line in range(self.line_count):
            for column in range(self.column_count):

                cell_count = self.cell_count_around(line, column)

                if matrix_copy[line][column] == 0 and cell_count == 3:
                    self.__matrix[line][column] = 1

                elif matrix_copy[line][column] == 1 and (cell_count > 3 or cell_count < 2):
                    self.__matrix[line][column] = 0

    def __out_of_dimension(self, line, column):

        return line < 0 or column < 0 or line >= self.line_count or column >= self.column_count
