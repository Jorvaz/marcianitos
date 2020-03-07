import pygame.font

class Hud():
    def __init__(self, m_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.m_settings = m_settings
        self.stats = stats

        self.color_texto = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.preparar_puntuacion()
        self.preparar_mejor_puntuacion()
        self.gameover()

    def gameover(self):
        gameover = "GAME OVER!"
        color_gameover = (255, 0, 0)
        self.gameover_imagen = self.font.render(gameover, True,
                                color_gameover, self.m_settings.bg_color)

        self.gameover_imagen_rect = self.gameover_imagen.get_rect()
        self.gameover_imagen_rect.centerx = self.screen_rect.centerx
        self.gameover_imagen_rect.top = self.m_settings.screen_height/3


    def mostrar_gameover(self):
        self.screen.blit(self.gameover_imagen, self.gameover_imagen_rect)
        pygame.display.flip()

    def preparar_mejor_puntuacion(self):
        mejor_puntuacion = str(self.stats.mejor_puntuacion)
        self.mejor_puntuacion_imagen = self.font.render(mejor_puntuacion, True,
                                        self.color_texto, self.m_settings.bg_color)


        self.mejor_puntuacion_rect = self.mejor_puntuacion_imagen.get_rect()
        self.mejor_puntuacion_rect.centerx = self.screen_rect.centerx
        self.mejor_puntuacion_rect.top = 20


    def preparar_puntuacion(self):
        puntuacion = str(self.stats.puntuacion)
        self.puntuacion_imagen = self.font.render(puntuacion, True,
                                self.color_texto, self.m_settings.bg_color)


        self.puntuacion_rect = self.puntuacion_imagen.get_rect()
        self.puntuacion_rect.right = self.screen_rect.right - 20
        self.puntuacion_rect.top = 20

    def mostrar_hud(self):
        self.screen.blit(self.puntuacion_imagen, self.puntuacion_rect)
        self.screen.blit(self.mejor_puntuacion_imagen, self.mejor_puntuacion_rect)
