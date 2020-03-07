import pygame
from pygame.sprite import Group
from settings import Settings
from nave import Nave
import funciones_juego as fj
from estadisticas import Estadisticas
from boton import Boton
from hud import Hud
import musica as m

def run_game():
    pygame.init()
    m_settings = Settings()
    stats = Estadisticas(m_settings)
    fj.cargar_puntuacion(stats)
    screen = pygame.display.set_mode((m_settings.screen_width, m_settings.screen_height)) #dibujar pantalla
    nave = Nave(screen, m_settings) #Dibujar nave
    balas = Group() #Un grupo es una lista con funciones añadidas
    marcianitos = Group()
    fj.crear_flota(m_settings, screen, nave, marcianitos)
    icon = pygame.image.load("images/alien.bmp")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Marcianitos")
    boton = Boton(m_settings, screen, "Jugar")
    hud = Hud(m_settings, screen, stats)
    m.musica_fondo()


    while True:
        fj.comprobar_eventos(m_settings, screen, nave, balas, stats, marcianitos, boton)
        if stats.jugando:
            nave.actualizar_posicion(m_settings)
            fj.actualizar_balas(m_settings, screen, nave, marcianitos, balas, stats, hud)
            fj.actualizar_flota(m_settings, stats, screen, balas, marcianitos, nave, hud)
        fj.actualizar_pantalla(m_settings, screen, nave, marcianitos, balas, boton, stats, hud)

run_game()
