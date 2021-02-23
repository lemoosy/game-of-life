import pygame


class Square(pygame.sprite.Sprite):

    def __init__(self, length, height, x, y, color):

        super(Square, self).__init__()

        self.surf = pygame.Surface((length, height))
        self.rect = self.surf.get_rect()
        self.rect = self.rect.move(x, y)
        self.surf.fill(color)

    def draw(self, window):

        window.blit(self.surf, self.rect)