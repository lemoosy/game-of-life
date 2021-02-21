from const import *
import pygame


class Square(pygame.sprite.Sprite):

    def __init__(self, x, y):

        super(Square, self).__init__()

        self.surf = pygame.Surface((SIZE_CELL_X, SIZE_CELL_Y))
        self.surf.fill(red)
        self.rect = self.surf.get_rect()
        self.rect = self.rect.move(x, y)

    def draw(self, screen):

        screen.blit(self.surf, self.rect)