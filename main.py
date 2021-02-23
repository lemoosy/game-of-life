from button import *
from const import *
from matrix import Matrix
from square import Square
import copy
import pygame
import time


pygame.init()
window = pygame.display.set_mode((SIZE_WINDOW_X, SIZE_WINDOW_Y))
images = dict()
images['stop.png'] = pygame.image.load('img/stop.png')
images['restart.png'] = pygame.image.load('img/restart.png')
images['export.png'] = pygame.image.load('img/export.png')

matrix = Matrix()
pause = False
default_matrix = copy.deepcopy(matrix)


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
                matrix = copy.deepcopy(default_matrix)
                draw_game()
                pygame.display.flip()

            if button == 3:
                matrix.export()

    if not pause:

        window.fill(BLUE)
        matrix.draw(window)
        button.draw(window)
        pygame.display.flip()

        matrix.update()
        time.sleep(1/3)


main()