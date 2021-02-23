from const import *
import pygame


def draw(window, images):
    window.blit(images['stop.png'], POSITION_FIRST_BUTTON)
    window.blit(images['restart.png'], POSITION_SECOND_BUTTON)
    window.blit(images['export.png'], POSITION_THIRD_BUTTON)


def check():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            mouse_position = pygame.mouse.get_pos()

            if mouse_on_button_1(*mouse_position):
                return 1

            if mouse_on_button_2(*mouse_position):
                return 2

            if mouse_on_button_3(*mouse_position):
                return 3

        if event.type == pygame.QUIT:
            return 4


def mouse_on_button_1(x, y):
    if (POSITION_FIRST_BUTTON[0] <= x <= POSITION_FIRST_BUTTON[0] + SIZE_BUTTON_X and
            POSITION_FIRST_BUTTON[1] <= y <= POSITION_FIRST_BUTTON[1] + SIZE_BUTTON_Y):
        return True

    return False


def mouse_on_button_2(x, y):
    if (POSITION_SECOND_BUTTON[0] <= x <= POSITION_SECOND_BUTTON[0] + SIZE_BUTTON_X and
            POSITION_SECOND_BUTTON[1] <= y <= POSITION_SECOND_BUTTON[1] + SIZE_BUTTON_Y):
        return True

    return False


def mouse_on_button_3(x, y):
    if (POSITION_THIRD_BUTTON[0] <= x <= POSITION_THIRD_BUTTON[0] + SIZE_BUTTON_X and
            POSITION_THIRD_BUTTON[1] <= y <= POSITION_THIRD_BUTTON[1] + SIZE_BUTTON_Y):
        return True

    return False
