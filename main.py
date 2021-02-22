from const import *
from matrix import Matrix
from square import Square
import pygame


pygame.init()
window = pygame.display.set_mode((SIZE_WINDOW_X, SIZE_WINDOW_Y))
matrix = Matrix()
clock = 0


while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            position_mouse_x = pygame.mouse.get_pos()[0]
            position_mouse_y = pygame.mouse.get_pos()[1]
            matrix.switch_cell(position_mouse_x, position_mouse_y)

    if clock != pygame.time.get_ticks() // 1000:
        window.fill(BLACK)
        matrix.draw(window)
        pygame.display.flip()
        matrix.update()
        clock = pygame.time.get_ticks() // 1000
