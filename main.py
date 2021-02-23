from button import *
from const import *
from matrix import Matrix
from square import Square

import button
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

    if not pause:
        window.fill(BLUE)
        matrix.draw(window)
        button.draw(window, images)
        pygame.display.flip()
        matrix.update()
        time.sleep(1 / 3)



    button = button.click()

    if button == 1:
        pause = not pause

    if button == 2:
        matrix = copy.deepcopy(default_matrix)

    if button == 3:
        matrix.export()

    if button == 4:
        pygame.quit()
        break
