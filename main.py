from const import *
from matrix import Matrix
from square import Square
from text import Text
import pygame
import time


pygame.init()
window = pygame.display.set_mode((SIZE_WINDOW_X, SIZE_WINDOW_Y))
matrix = Matrix()


def check_click_button():

    return 0


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            position_mouse_x = pygame.mouse.get_pos()[0]
            position_mouse_y = pygame.mouse.get_pos()[1]
            matrix.switch_cell(position_mouse_x, position_mouse_y)

        button = check_click_button()

        if button == 1:
            None

        if button == 2:
            None

        if button == 3:
            None

    window.fill(BLACK)
    matrix.draw(window)
    Text(50, 'PAUSE', RED, *FIRST_TXT_POSITION).draw(window)
    Text(50, 'RESET', RED, *SECOND_TXT_POSITION).draw(window)
    Text(50, 'EXPORT', RED, *THIRD_TXT_POSITION).draw(window)
    Square(FIRST_TXT_POSITION[0] + 200, FIRST_TXT_POSITION[1], BLUE).draw(window)
    pygame.display.flip()
    matrix.update()
    time.sleep(1)