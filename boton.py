import pygame.font

class Boton():
    def __init__(self, m_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width = 200
        self.height = 50
        self.color_boton = (0, 0, 0)
        self.color_texto = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48) #None es la fuente por defecto del sistema

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.preparar_msg(msg)

    def preparar_msg(self, msg):
        self.msg_imagen = self.font.render(msg, True, self.color_texto,
                                          self.color_boton)
        self.msg_imagen_rect = self.msg_imagen.get_rect()
        self.msg_imagen_rect.center = self.rect.center

    def pintar_boton(self):
        self.screen.fill(self.color_boton, self.rect)
        self.screen.blit(self.msg_imagen, self.msg_imagen_rect)