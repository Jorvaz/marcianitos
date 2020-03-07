import pygame
from pygame.sprite import Sprite

class Marciano(Sprite):
    def __init__(self, m_settings, screen):
       super().__init__()
       self.screen = screen
       self.m_settings = m_settings

       self.image = pygame.image.load("images/alien.bmp")
       self.rect = self.image.get_rect()

       self.rect.x = self.rect.width
       self.rect.y = self.rect.height

       self.x = float(self.rect.x)

    def pintar_marciano(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.m_settings.velocidad_marcianos * self.m_settings.direccion)
        self.rect.x = self.x

    def comprobar_borde(self):
        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True

        elif self.rect.left <= 0:
            return True