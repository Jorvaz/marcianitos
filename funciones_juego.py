import sys
import pygame
from bala import Bala
from marciano import Marciano
from time import sleep
import musica as m


def comprobar_eventos(m_settings, screen, nave, balas, stats, marcianitos, boton):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #evento "hacer click en cerrar"
            guardar_puntuacion(stats)
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            comprobar_evento_pulsar(event, m_settings, screen, nave, balas, stats, marcianitos)

        elif event.type == pygame.KEYUP:
            comprobar_evento_soltar(event, nave)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            ratonx, ratony = pygame.mouse.get_pos()
            comprobar_boton(stats, boton, ratonx, ratony, m_settings, screen, nave,
                    balas, marcianitos)


def actualizar_pantalla(m_settings, screen, nave, marcianitos, balas, boton, stats, hud):
    screen.fill(m_settings.bg_color)  # pintar con el color de fondo
    nave.pinta_nave()
    marcianitos.draw(screen)
    hud.mostrar_hud()
    for bala in balas.sprites():
        bala.pintar_bala()

    if not stats.jugando:
        boton.pintar_boton()

    if stats.derrotado:
        hud.mostrar_gameover()

    pygame.display.flip()  # refresca pantalla


def nueva_partida(m_settings, screen, nave, balas, stats, marcianitos):
    if stats.jugando == False:
        stats.reiniciar()
        m_settings.opciones_variables()
        stats.jugando = True
        stats.derrotado = False
        pygame.mouse.set_visible(False)
        marcianitos.empty()
        balas.empty()
        crear_flota(m_settings, screen, nave, marcianitos)
        nave.centrar_nave()
        sleep(1)
        m.musica_fondo()





def comprobar_evento_pulsar(event, m_settings, screen, nave, balas, stats, marcianitos):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            nave.mover_derecha = True

        elif event.key == pygame.K_LEFT:
            nave.mover_izquierda = True

        elif event.key == pygame.K_SPACE:
            disparar_balas(m_settings, screen, nave, balas)

        elif event.key == pygame.K_p:
            nueva_partida(m_settings, screen, nave, balas, stats, marcianitos)

        elif event.key == pygame.K_q:
            guardar_puntuacion(stats)
            sys.exit()

def comprobar_boton(stats, boton, ratonx, ratony, m_settings, screen, nave,
                    balas, marcianitos):
    if boton.rect.collidepoint(ratonx, ratony):
        nueva_partida(m_settings, screen, nave, balas, stats, marcianitos)


def comprobar_evento_soltar(event, nave):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            nave.mover_derecha = False

        elif event.key == pygame.K_LEFT:
            nave.mover_izquierda = False


def actualizar_balas(m_settings, screen, nave, marcianitos, balas, stats, hud):
    balas.update()

    for bala in balas.copy():
        if bala.rect.bottom <= 0:
            balas.remove(bala)

    comprobar_colision_balas(m_settings, screen, nave, marcianitos, balas, stats, hud)


def comprobar_colision_balas(m_settings, screen, nave, marcianitos, balas, stats, hud):
    colision = pygame.sprite.groupcollide(balas, marcianitos, True, True)

    if colision:
        m.m_destruido()
        stats.puntuacion += m_settings.puntuacion_m
        hud.preparar_puntuacion()
        comprobar_mejor_puntuacion(stats, hud)

    if len(marcianitos) == 0:
        balas.empty()
        m_settings.aumentar_velocidad()
        crear_flota(m_settings, screen, nave, marcianitos)


def disparar_balas(m_settings, screen, nave, balas):
    if len(balas) < m_settings.numero_balas:
        m.disparo()
        nueva_bala = Bala(m_settings, screen, nave)
        balas.add(nueva_bala)


def crear_flota(m_settings, screen, nave, marcianitos):
    marciano = Marciano(m_settings, screen)
    numero_marciano = get_num_marcianos(m_settings, marciano.rect.width)
    num_filas = get_num_filas(m_settings, marciano.rect.height, nave.rect.height)

    for num_f in range(num_filas):
        for num_m in range(numero_marciano):
            crear_marciano(m_settings, screen, marcianitos, num_m, num_f)


def get_num_marcianos(m_settings, ancho_marciano):
    espacio_disponible = m_settings.screen_width - 2 * ancho_marciano
    numero_marcianos = int(espacio_disponible / (2 * ancho_marciano))

    return numero_marcianos


def crear_marciano(m_settings, screen, marcianitos, numero_marciano, num_fila):
    marciano = Marciano(m_settings, screen)
    ancho_marciano = marciano.rect.width
    marciano.x = ancho_marciano + 2 * ancho_marciano * numero_marciano
    marciano.rect.x = marciano.x
    marciano.rect.y = marciano.rect.height + 2 * marciano.rect.height * num_fila
    marcianitos.add(marciano)


def get_num_filas(m_settings, altura_marciano, altura_nave):
    espacio_disponible = (m_settings.screen_height - (3 * altura_marciano) - altura_nave)
    numero_filas = int(espacio_disponible / (2 * altura_marciano))

    return numero_filas


def comprobar_extremo_flota(m_settings, marcianitos):
    for marciano in marcianitos.sprites():
        if marciano.comprobar_borde():
            cambiar_direccion (m_settings, marcianitos)
            break


def cambiar_direccion(m_settings, marcianitos):
    for marciano in marcianitos.sprites():
        marciano.rect.y += m_settings.velocidad_avance

    m_settings.direccion *= -1


def actualizar_flota(m_settings, stats, screen, balas, marcianitos, nave, hud):
    comprobar_extremo_flota(m_settings, marcianitos)
    marcianitos.update()

    if pygame.sprite.spritecollideany(nave, marcianitos):
        m.nave_destruida()
        nave_damage(m_settings, stats, screen, nave, marcianitos, balas, hud)

    marcianos_llegan(m_settings, stats, screen, nave, marcianitos, balas, hud)

def nave_damage(m_settings, stats, screen, nave, marcianitos, balas, hud):
    if stats.vidas_restantes > 0:

        stats.vidas_restantes -= 1
        marcianitos.empty()
        balas.empty()

        crear_flota(m_settings, screen, nave, marcianitos)
        nave.centrar_nave()

        sleep(1)

    else:
        stats.jugando = False
        stats.derrotado = True
        pygame.mouse.set_visible(True)

def marcianos_llegan (m_settings, stats, screen, nave, marcianitos, balas, hud):
    screen_rect = screen.get_rect()
    for marciano in marcianitos.sprites():
        if marciano.rect.bottom >= screen_rect.bottom:
            m.nave_destruida()
            nave_damage(m_settings, stats, screen, nave, marcianitos, balas, hud)
            break

def comprobar_mejor_puntuacion(stats, hud):
    if stats.puntuacion > stats.mejor_puntuacion:
        stats.mejor_puntuacion = stats.puntuacion
        hud.preparar_mejor_puntuacion()

def guardar_puntuacion(stats):
    file = "mejor_puntuacion.txt"

    with open(file, 'w') as file_object:
        file_object.write(str(stats.mejor_puntuacion))

def cargar_puntuacion(stats):
    file = "mejor_puntuacion.txt"
    try:
        with open(file) as file_object:
            stats.mejor_puntuacion = int(file_object.read())
    except FileNotFoundError:
        with open(file, 'w') as file_object:
            file_object.write(str(stats.mejor_puntuacion))
