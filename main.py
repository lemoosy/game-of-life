from button import *
from const import *
from matrix import Matrix
from square import Square
from text import Text
import copy
import pygame
import time


pygame.init()
window = pygame.display.set_mode((SIZE_WINDOW_X, SIZE_WINDOW_Y))
matrix = Matrix()
pause = False
copy_matrix = copy.deepcopy(matrix)


def draw_game():

    window.fill(BLACK)
    matrix.draw(window)
    Text(50, 'PAUSE', RED, *FIRST_TXT_POSITION).draw(window)
    Text(50, 'RESET', RED, *SECOND_TXT_POSITION).draw(window)
    Text(50, 'EXPORT', RED, *THIRD_TXT_POSITION).draw(window)
    Square(FIRST_TXT_POSITION[0] + 200, FIRST_TXT_POSITION[1], BLUE).draw(window)
    Square(SECOND_TXT_POSITION[0] + 200, SECOND_TXT_POSITION[1], BLUE).draw(window)
    Square(THIRD_TXT_POSITION[0] + 200, THIRD_TXT_POSITION[1], BLUE).draw(window)


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            position_mouse_x = pygame.mouse.get_pos()[0]
            position_mouse_y = pygame.mouse.get_pos()[1]

            matrix.switch_cell(position_mouse_x, position_mouse_y)
            button = check_click_button(position_mouse_x, position_mouse_y)

            if button == 1:
                pause = False if pause else True
                draw_game()
                pygame.display.flip()

            if button == 2:
                matrix = copy.deepcopy(copy_matrix)
                draw_game()
                pygame.display.flip()

            if button == 3:
                matrix.export()

    if not pause:

        draw_game()
        pygame.display.flip()
        matrix.update()
        time.sleep(1)