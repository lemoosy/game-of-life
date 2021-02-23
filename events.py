import pygame


def click():

    for event in pygame.event.get():
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1


def position_mouse():

    for event in pygame.event.get():
        return pygame.mouse.get_pos()