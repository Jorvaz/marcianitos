import pygame
from pygame.sprite import Sprite

class Bala(Sprite):

    def __init__(self, m_settings, screen, nave):
        super().__init__()
        self.screen = screen

        """
        Crear rectángulo: coordenadas esquina sup izquierda,
        ancho y alto.
        """
        self.rect = pygame.Rect(0, 0, m_settings.ancho_bala,
                                 m_settings.longitud_bala)
        self.rect.centerx = nave.rect.centerx
        self.rect.top = nave.rect.top

        self.y = float(self.rect.y)

        self.color = m_settings.color_bala
        self.velocidad_balas = m_settings.velocidad_balas

    def update(self):
        self.y -= self.velocidad_balas
        self.rect.y = self.y

    def pintar_bala(self):
        pygame.draw.rect(self.screen, self.color, self.rect)