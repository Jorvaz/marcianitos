class Settings():
    def __init__(self):
        #Configuración pantalla
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #Nave
        self.vidas = 0

        #Configuración balas

        self.ancho_bala = 3
        self.longitud_bala = 15
        self.color_bala = 60, 60, 60
        self.numero_balas = 1

        #Marcianos
        self.velocidad_avance = 10
        self.aumento_dificultad = 1.1
        self.opciones_variables()
        self.aumento_puntuacion = 1.5

    def opciones_variables(self):
        self.velocidad_nave = 0.5
        self.velocidad_balas = 0.8
        self.velocidad_marcianos = 0.6
        self.direccion = 1
        self.puntuacion_m = 50

    def aumentar_velocidad(self):
        self.velocidad_nave *= self.aumento_dificultad
        self.velocidad_balas *= self.aumento_dificultad
        self.velocidad_marcianos *= self.aumento_dificultad
        self.puntuacion_m = int(self.puntuacion_m * self.aumento_puntuacion)