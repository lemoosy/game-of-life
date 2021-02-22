import pygame


class Text:

    def __init__(self, size, message, color, x, y):

        self.font = pygame.font.SysFont(None, size)
        self.text = self.font.render(message, True, color)
        self.x = x
        self.y = y

    def draw(self, window):

        window.blit(self.text, (self.x, self.y))