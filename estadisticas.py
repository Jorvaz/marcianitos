class Estadisticas():
    def __init__(self, m_settings):
        self.m_settings = m_settings
        self.reiniciar()
        self.jugando = False
        self.mejor_puntuacion = 0
        self.derrotado = False

    def reiniciar(self):
        self.vidas_restantes = self.m_settings.vidas
        self.puntuacion = 0