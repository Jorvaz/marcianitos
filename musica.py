import pygame

def musica_fondo():
    pygame.mixer.music.load("sonidos/spaceinvaders1.mpeg")
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)

def disparo():
    disparo = pygame.mixer.Sound("sonidos/shoot.wav")
    disparo.play()

def m_destruido():
    m_destruido = pygame.mixer.Sound("sonidos/invaderkilled.wav")
    m_destruido.play()

def nave_destruida():
    explosion = pygame.mixer.Sound("sonidos/explosion.wav")
    explosion.play()