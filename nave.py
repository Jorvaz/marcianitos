import pygame

class Nave():
    def __init__(self, screen, m_settings):
        self.screen = screen
        self.m_settings=m_settings

        self.image = pygame.image.load("images\ship.bmp")
        self.rect = self.image.get_rect() #Rectángulo de la nave
        self.screen_rect = screen.get_rect() #Rectángulo de la pantalla

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.centro = float(self.rect.centerx) #Para cambiar la velocidad con float


        self.mover_derecha = False
        self.mover_izquierda = False


    #Dibujar la nave
    def pinta_nave(self):
        self.screen.blit(self.image, self.rect)

    def actualizar_posicion(self, m_settings):
        if self.mover_derecha and self.rect.right < self.screen_rect.right:
                self.centro += m_settings.velocidad_nave

        elif self.mover_izquierda and self.rect.left > 0:
                self.centro -= m_settings.velocidad_nave

        self.rect.centerx=self.centro


    def centrar_nave(self):
        self.centro = self.screen_rect.centerx