# Código del juego de estrategia que acompaña al Trabajo de Fin de Grado
# A.A. Daniel García Cañada (2025)
#
# Indice del código:
#   - Constantes:
#       En esta sección se definen muchos parámetros generales que
#       controlan el funcionamiento del programa, su aspecto, etc.
#   - Inicialización interfaz:
#       Crear y configurar la ventana, cargar recursos necesarios
#        (fuentes, imágenes, etc) y demás operaciones con PyGame.
#   - Clases del juego:
#       En esta sección se definen todas las clases empleadas por el
#       propio juego (sus elementos y partes).
#   - Clases de la interfaz:
#       Clases auxiliares para facilitar la construcción de la
#       interfaz gráfica haciendo uso de PyGame.
#   - Funciones auxiliares de la interfaz:
#       Métodos para realizar operaciones con la interfaz de manera
#       más cómoda (p. ej. escribir texto).
#   - Inicialización del juego:
#       Establecer el estado inicial del juego, crear las variables
#       globales que se van a usar, etc.
#   - Actualización del juego:
#       Funciones que se encargan de actualizar el estado del juego
#       en cada fotograma.
#   - Bucle principal del juego:
#       Esqueleto del proceso en cada fotograma: escanear eventos,
#       actualizar estado, y dibujar en pantalla.

import math    # Operaciones y funciones matemáticas
import os      # Manipulaciones del sistema
import pygame  # Motor del juego
import random  # Para generacion de números aleatorios

# Lo siguiente es para evitar que se muestre publicidad de PyGame en la consola al iniciar
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


# < -------------------------------------------------------------------------- >
#                            CONSTANTES GLOBALES
# < -------------------------------------------------------------------------- >

# Constantes generales del juego
NOMBRE_JUEGO    = "AIR GAME"
CREDITO_INICIAL = 500

# Características generales de la interfaz
ANCHURA                         = 1280      # Anchura de la ventana en pixeles
ALTURA                          = 720       # Altura de la ventana en pixeles
PANTALLA_COMPLETA               = False     # Para abrir el juego en ventana completa
PANTALLA_MODIFICARDIMENSION     = False     # Para poder modificar la dimensión de la ventana
FPS                             = 60        # Fotogramas por segundo
COLOR_FONDO                     = "#cccccc" # Color RGB del fondo de pantalla
MUSICA_REPRODUCIR               = False     # Activar o desactivar la música por defecto
MUSICA_VOLUMEN                  = 0.5       # Volumen relativo de la musica (0.0 - 1.0)

# Carpetas de ficheros del juego
CARPETA_AUDIO      = "audio" # Localización de los sonidos y música
CARPETA_IMAGENES   = "img"   # Localización de las imágenes, sprites, etc
CARPETA_DOCUMENTOS = "docs"  # Localización de la documentación del juego

# Propiedades del texto
COLOR_TEXTO        = (0, 0, 0)        # Color RGB por defecto del texto
TEXTO_FUENTE       = "Century Gothic" # Fuente de los textos
TEXTO_FUENTE_MONO  = "Mono"           # Fuente para textos monoespaciados
TEXTO_TAMANO       = 24               # Tamaño de fuente por defecto
TEXTO_TAMANOS = [14, 16, 20, 24, 36, 72, 180] # Tamaños de fuente que se usaran

# Propiedades generales de todos los paneles, por defecto
PANEL_BORDE_COLOR  = "#006600" # Color del borde de los paneles
PANEL_INT_COLOR    = "#e6ffe6" # Color del interior de los paneles
PANEL_BORDE_GROSOR = 2         # Grosor del borde (0 = sin borde)
PANEL_BORDE_RADIO  = 5         # Radio de las esquinas circulares
PANEL_SEPARACION   = 5         # Separacion entre paneles

# Dimensiones de los 3 paneles principales (en proporción)
ANCHURA_JUEGO       = 0.86
ANCHURA_ACCIONES    = 0.14
ANCHURA_INFORMACION = 1
ALTURA_JUEGO        = 0.65
ALTURA_ACCIONES     = 0.65
ALTURA_INFORMACION  = 0.35

# Propiedades botones
BOTON_COLOR_NORMAL = "#74cefa" # Color del fondo de los botones
BOTON_COLOR_SOBRE  = "#a9e0fb" # Color del fondo cuando el raton está encima
BOTON_COLOR_PULSA  = "#a9b7fb" # Color del fondo cuando está pulsado
BOTON_TAMANO_LETRA = 16        # Tamaño de la letra

# Recursos (sonidos, imágenes...)
IMAGEN_FONDO       = "imagenairgame.jpg"
MUSICA_FONDO       = "topgunmusic.ogg"

SONIDO_PAGAR       = "cajaregistradora.ogg"
SONIDO_COBRAR      = "monedas.ogg"
SONIDO_ERROR       = "error.ogg"
SONIDO_BOTON_SEL   = 'click.ogg'
SONIDO_BOTON_PUL   = 'switch.ogg'
SONIDO_CASILLA_SEL = 'glass.ogg'
SONIDO_CASILLA_PUL = 'casilla.ogg'

TEXTURA_ESCENARIO  = 'textura_hierba.png'
TEXTURA_TIENDA     = 'textura_ladrillos.png'
TEXTURA_INFO       = 'textura_piedras.png'
TEXTURA_REGLAS     = 'textura_malla.png'
TEXTURA_BOTON      = 'textura_gotele.png'

TEXTURA_ESCENARIO_COLOR = '#33cc3340'
TEXTURA_TIENDA_COLOR    = '#cc330080'
TEXTURA_INFO_COLOR      = '#66669920'
TEXTURA_REGLAS_COLOR    = '#80808020'
TEXTURA_BOTON_COLOR     = '#0675ac20'

# Escenario
MAPA_DIM_X = 25 # Anchura del mapa en casillas
MAPA_DIM_Y = 15 # Altura del mapa en casillas
MAPA_DIM_J = 11 # Número de columnas en propiedad inicial de cada jugador
MAPA_COLOR_NEUTRO  = "#f2f2f2" # Color de casilla sin superioridad aerea
MAPA_COLOR_J1      = "#bdd7ee" # Color de casilla con superioridad aerea de J1
MAPA_COLOR_J2      = "#f8cbad" # Color de casilla con superioridad aerea de J2
MAPA_COLOR_J1_F    = "#2e75b6" # Color de casilla con supremacia aerea de J1
MAPA_COLOR_J2_F    = "#c55a11" # Color de casilla con supremacia aerea de J2
MAPA_COLOR_BORDE   = "#9900cc" # Color del borde de la casilla actualmente seleccionada

# Sistema de puntos y superioridad aerea
COEF_SUP        = 20  # Coeficiente de sup aerea en una casilla normal
SUP_INICIAL     = 0.1 # Proporción de casillas iniciales con supremacia (aleatorias)
MULT_SUPREMACIA = 2   # Ratio entre superioridad y supremacia aerea

# Reglas
CANTIDAD_CAPITAL = 1 # Cantidad inicial de capitales
CANTIDAD_CIUDAD  = 2 # Cantidad inicial de ciudades normales
CANTIDAD_BASE    = 3 # Cantidad inicial de bases aéreas

# Recuadros de ayuda e informacion
AYUDA_COLOR = (255, 255, 192) # Color del fondo
AYUDA_TAMANO = 16             # Tamaño de la letra

# < -------------------------------------------------------------------------- >
#                          INICIALIZACION INTERFAZ
# < -------------------------------------------------------------------------- >

def cargar_imagen(nombre, trans=True):
    """Cargar un fichero de imagen en PyGame"""
    img = pygame.image.load(os.path.join(CARPETA_IMAGENES, nombre))
    return img.convert_alpha() if trans else img.convert()

def cargar_textura(nombre, color, fondo = '#000000'):
    """
    Cargar una imagen para usar como textura monocromo. Las texturas suelen ser en blanco
    y negro: el blanco se tinta de un color, y el negro se hace transparente.
    """
    imagen = cargar_imagen(nombre)

    # Tintar blanco
    imagen.fill(color, special_flags = pygame.BLEND_RGBA_MULT)

    # Transparentar negro
    fondo = pygame.Color(fondo)
    r1, g1, b1 = fondo.r, fondo.g, fondo.b
    w, h = imagen.get_size()
    imagen.lock()
    for y in range(h):
        for x in range(w):
            r2, g2, b2, _ = imagen.get_at((x, y))
            if (r2, g2, b2) == (r1, g1, b1):
                imagen.set_at((x, y), (r2, g2, b2, 0))
    imagen.unlock()

    return imagen

def cargar_sonido(nombre):
    """Cargar un fichero de audio en PyGame"""
    return pygame.mixer.Sound(os.path.join(CARPETA_AUDIO, nombre))

def reproducir_sonido(nombre):
    """Reproducir uno de los sonidos cargados"""
    g_sonidos[nombre].play()

# Configuramos la pantalla (nombre, dimensiones, fotogramaje, etc)
flags = 0
if (PANTALLA_COMPLETA): flags |= pygame.FULLSCREEN
if (PANTALLA_MODIFICARDIMENSION): flags |= pygame.RESIZABLE
pygame.init()
pygame.display.set_caption(NOMBRE_JUEGO)
g_pantalla = pygame.display.set_mode((ANCHURA, ALTURA), flags)
g_reloj = pygame.time.Clock()
g_ayuda = None

# Cargar recursos
pygame.mixer.init()
pygame.mixer.music.load(os.path.join(CARPETA_AUDIO, MUSICA_FONDO))
g_pantallazo = cargar_imagen(IMAGEN_FONDO)
g_fuentes = { tam: pygame.font.SysFont(TEXTO_FUENTE, tam) for tam in TEXTO_TAMANOS }
g_fuentes_mono = { tam: pygame.font.SysFont(TEXTO_FUENTE_MONO, tam) for tam in TEXTO_TAMANOS }
g_iconos = {
    'AvionCaza':       cargar_imagen('icono_caza.png'),
    'AvionAtaque':     cargar_imagen('icono_ataque.png'),
    'AvionTransporte': cargar_imagen('icono_transporte.png'),
    'Helicoptero':     cargar_imagen('icono_helicoptero.png'),
    'Dron':            cargar_imagen('icono_dron.png'),
    'Radar':           cargar_imagen('icono_radar.png'),
    'Bateria':         cargar_imagen('icono_bateria.png'),
    'Inteligencia':    cargar_imagen('icono_inteligencia.png'),
    'Ciudad':          cargar_imagen('icono_ciudad.png'),
    'Base':            cargar_imagen('icono_base.png')
}
g_sonidos = {
    'pagar':       cargar_sonido(SONIDO_PAGAR),
    'cobrar':      cargar_sonido(SONIDO_COBRAR),
    'error':       cargar_sonido(SONIDO_ERROR),
    'boton_sel':   cargar_sonido(SONIDO_BOTON_SEL),
    'boton_pul':   cargar_sonido(SONIDO_BOTON_PUL),
    'casilla_sel': cargar_sonido(SONIDO_CASILLA_SEL),
    'casilla_pul': cargar_sonido(SONIDO_CASILLA_PUL)
}
g_texturas = {
    'hierba':    cargar_textura(TEXTURA_ESCENARIO, TEXTURA_ESCENARIO_COLOR),
    'ladrillos': cargar_textura(TEXTURA_TIENDA,    TEXTURA_TIENDA_COLOR),
    'piedras':   cargar_textura(TEXTURA_INFO,      TEXTURA_INFO_COLOR),
    'malla':     cargar_textura(TEXTURA_REGLAS,    TEXTURA_REGLAS_COLOR),
    'gotele':    cargar_textura(TEXTURA_BOTON,     TEXTURA_BOTON_COLOR),
}

# < -------------------------------------------------------------------------- >
#                              CLASES DEL JUEGO
# < -------------------------------------------------------------------------- >

class Medio:
    """Clase genérica que representa cualquier medio militar"""
    NOMBRE     = None
    ICONO      = None
    DESC       = None
    PRECIO     = None
    VELOCIDAD  = None
    AUTONOMIA  = None
    ALCANCE    = None
    HUELLA     = None
    AIRE       = None
    SUP        = None
    VIGILANCIA = None
    RADIOVIG   = None
    SUPAEREA   = None

    def __init__(self, jugador):
        self.jugador = jugador

    @classmethod
    def info(cls):
        texto = f"Descripción:  {cls.DESC}\n"
        if cls.PRECIO:     texto += f"Precio:       {cls.PRECIO}\n"
        if cls.VELOCIDAD:  texto += f"Velocidad:    {cls.VELOCIDAD}\n"
        if cls.AUTONOMIA:  texto += f"Autonomía:    {cls.AUTONOMIA}\n"
        if cls.ALCANCE:    texto += f"Alcance:      {cls.ALCANCE}\n"
        if cls.HUELLA:     texto += f"Huella:       {cls.HUELLA}\n"
        if cls.AIRE:       texto += f"Aire-aire:    {cls.AIRE}\n"
        if cls.SUP:        texto += f"Aire-sup:     {cls.SUP}\n"
        if cls.VIGILANCIA: texto += f"Vigilancia:   {cls.VIGILANCIA}\n"
        if cls.RADIOVIG:   texto += f"Radio vigil.: {cls.RADIOVIG}\n"
        if cls.SUPAEREA:   texto += f"Sup. aérea:   {cls.SUPAEREA}"
        return texto

class MedioAereo(Medio):
    """Representa cualquier medio aéreo"""

class MedioAntiaereo(Medio):
    """Representa cualquier medio anti-aéreo"""

class MedioEstrategico(Medio):
    """Representa cualquier medio estratégico"""

class AvionCaza(MedioAereo):
    """Representa un avión de caza"""
    NOMBRE     = "Avo. Caza"
    ICONO      = g_iconos['AvionCaza']
    DESC       = 'Único medio aéreo que puede atacar otros medios aéreos. El otro medio que puede hacerlo es la batería antiaérea.'
    PRECIO     = 50
    VELOCIDAD  = 2100
    AUTONOMIA  = 1.62
    ALCANCE    = 3400
    HUELLA     = 4
    AIRE       = 170
    SUP        = 0
    VIGILANCIA = 0
    RADIOVIG   = 0
    SUPAEREA   = 10

class AvionAtaque(MedioAereo):
    """Representa un avión de ataque"""
    NOMBRE     = "Avo. Ataque"
    ICONO      = g_iconos['AvionAtaque']
    DESC       = 'Medio aéreo capaz de atacar medios anti aéreos.'
    PRECIO     = 65
    VELOCIDAD  = 1350
    AUTONOMIA  = 5.04
    ALCANCE    = 6800
    HUELLA     = 15
    AIRE       = 0
    SUP        = 240
    VIGILANCIA = 0
    RADIOVIG   = 0
    SUPAEREA   = 6

class AvionTransporte(MedioAereo):
    """Representa un avión de transporte"""
    NOMBRE     = "Avo. Transporte"
    ICONO      = g_iconos['AvionTransporte']
    DESC       = 'Medio aéreo con más alcance.'
    PRECIO     = 120
    VELOCIDAD  = 820
    AUTONOMIA  = 12.93
    ALCANCE    = 10600
    HUELLA     = 60
    AIRE       = 0
    SUP        = 0
    VIGILANCIA = 0
    RADIOVIG   = 0
    SUPAEREA   = 3

class Helicoptero(MedioAereo):
    """Representa un helicóptero"""
    NOMBRE     = "Helicóptero"
    ICONO      = g_iconos['Helicoptero']
    DESC       = 'Único medio aéreo capaz de aterrizar en una casilla que no sea una base. Además es capaz de atacar medios anti aéreos.'
    PRECIO     = 21
    VELOCIDAD  = 260
    AUTONOMIA  = 2.58
    ALCANCE    = 670
    HUELLA     = 10
    AIRE       = 0
    SUP        = 10
    VIGILANCIA = 0
    RADIOVIG   = 0
    SUPAEREA   = 4

class Dron(MedioAereo):
    """Representa un dron"""
    NOMBRE     = "Dron"
    ICONO      = g_iconos['Dron']
    DESC       = 'Único medio aéreo con capacidad de vigilancia y con mayor autonomía, además es capaz de atacar medios anti aéreos.'
    PRECIO     = 25
    VELOCIDAD  = 240
    AUTONOMIA  = 13.5
    ALCANCE    = 3240
    HUELLA     = 2
    AIRE       = 0
    SUP        = 100
    VIGILANCIA = 20
    RADIOVIG   = 240
    SUPAEREA   = 2

class Radar(MedioAntiaereo):
    """Representa un radar"""
    NOMBRE     = "Radar"
    ICONO      = g_iconos['Radar']
    DESC       = 'Medio antiaéreo con el mayor alcance de vigilancia.'
    PRECIO     = 24
    HUELLA     = 100
    AIRE       = 0
    SUP        = 0
    VIGILANCIA = 90
    RADIOVIG   = 440
    SUPAEREA   = 0

class Bateria(MedioAntiaereo):
    """Representa una batería anti-aérea"""
    NOMBRE     = "Batería"
    ICONO      = g_iconos['Bateria']
    DESC       = 'Único medio antiaéreo con capacidad de vigilancia.'
    PRECIO     = 90
    HUELLA     = 100
    AIRE       = 240
    SUP        = 0
    VIGILANCIA = 60
    RADIOVIG   = 260
    SUPAEREA   = 0

class Inteligencia(MedioEstrategico):
    """Clase genérica para representar inteligencia"""
    NOMBRE     = "Inteligencia"
    PRECIO     = 50
    ICONO      = g_iconos['Inteligencia']
    DESC       = 'Medio estratégico que permite obtener diversa información sobre el adversario.'

class Infraestructura(MedioEstrategico):
    """Clase genérica que representa una infraestructura"""
    INC     = 5 # Incremento del coeficiente de superioridad por cada nivel extra
    BONUS   = 0 # Crédito (en M) otorgado al jugador por turno y nivel
    NIVELES = 9 # Maximo nivel de una infraestructura

    def __init__(self, jugador, casilla):
        super().__init__(jugador)
        self.casilla = casilla
        self.nivel = 1

    def destruir(self):
        """Eliminar la infraestructura"""
        self.casilla.infraestructura = None
        self.jugador.infraestructuras.remove(self)

    def mejorar(self):
        """Mejorar el nivel y las propiedades de la infraestructura"""
        if self.jugador.pagar(self.PRECIO_MEJORA):
            self.nivel += 1

    def cosechar(self):
        """Obtener el bonus económico que otorga la infraestructura"""
        self.jugador.cobrar(self.BONUS)

class Ciudad(Infraestructura):
    """Infraestructura que otorga recursos al jugador"""
    NOMBRE        = "Ciudad"
    ICONO         = g_iconos['Ciudad']
    DESC          = "Infraestructura que cosecha recursos cada turno."
    PRECIO        = 200
    PRECIO_MEJORA = 100
    SUP           = 40
    BONUS         = 10
    COLOR         = "#000000"

class Base(Infraestructura):
    """Infraestructura que permite desplegar medios aéreos"""
    NOMBRE        = "Base aérea"
    ICONO         = g_iconos['Base']
    DESC          = "Infraestructura que permite desplegar medios aéreos."
    PRECIO        = 300
    PRECIO_MEJORA = 150
    SUP           = 60
    COLOR         = "#00b050"

class Capital(Ciudad):
    """Ciudad principal del jugador. Además, perderla implica perder la partida."""
    NOMBRE        = "Capital"
    PRECIO        = 500
    PRECIO_MEJORA = 250
    SUP           = 100
    COLOR         = "#c09200"

class Casilla:
    ESCALA  = 0.6
    BORDE   = 0.9
    RADIO   = min(ESCALA * ANCHURA * ANCHURA_JUEGO / MAPA_DIM_X, ESCALA * ALTURA * ALTURA_JUEGO / MAPA_DIM_Y)
    INRADIO = 0.85 * RADIO
    DIM_X   = RADIO * 3 ** 0.5
    DIM_Y   = RADIO * 1.5
    DIM     = pygame.math.Vector2(DIM_X, DIM_Y)

    def __init__(self, esc, x, y):
        self.x = x
        self.y = y
        self.centro = pygame.math.Vector2(Escenario.ORIGEN_X + self.DIM_X * (x + (y % 2) / 2), Escenario.ORIGEN_Y + self.DIM_Y * y)
        self.verts = [self.centro + v for v in esc.hex_vertices]
        self.infraestructura = None
        self.resetear()

    def resetear(self):
        """Inicializar todas las propiedades y contenidos de la casilla"""
        self.sel = False
        self.pul = False
        self.asignar()
        self.destruir()
        self.recalcular()
        self.colorear()

    def asignar(self):
        """Determinar propietario de la casilla, que tiene inicialmente la superioridad aerea"""
        if self.x < MAPA_DIM_J:
            self.jugador = g_jugadores[0]
        elif self.x >= MAPA_DIM_X - MAPA_DIM_J:
            self.jugador = g_jugadores[1]
        else:
            self.jugador = None

    def recalcular(self):
        """Recalcular coeficientes de superioridad"""

        # Coeficiente de superioridad de casilla
        infra = self.infraestructura
        self.supCas = infra.SUP + infra.INC * infra.nivel if infra else COEF_SUP

        # Coeficiente de superioridad actual
        if not self.jugador:
            self.sup = 0
        elif self.jugador.indice == 0:
            self.sup = self.supCas
        else:
            self.sup = -self.supCas

    def destruir(self):
        """Destruir la infraestructura de la casilla"""
        if self.infraestructura:
            self.infraestructura.destruir()

    def raton(self, pos_vec):
        """Detecta si el ratón está sobre la casilla. Aproximamos el hexágono por el círculo inscrito."""
        return pos_vec.distance_squared_to(self.centro) < self.INRADIO ** 2

    def hay_superioridad(self):
        """Detecta si el jugador actual tiene superioridad aérea en la casilla"""
        return g_jugador.indice == 0 and self.sup >= self.supCas or g_jugador.indice == 1 and self.sup <= self.supCas

    def hay_supremacia(self):
        """Detecta si el jugador actual tiene supremacia aérea en la casilla"""
        return g_jugador.indice == 0 and self.sup >= MULT_SUPREMACIA * self.supCas or g_jugador.indice == 1 and self.sup <= MULT_SUPREMACIA * self.supCas

    def colorear(self):
        """Determinar color"""
        if self.sup <= -MULT_SUPREMACIA * self.supCas:
            self.color = MAPA_COLOR_J2_F
        elif self.sup <= -self.supCas:
            self.color = MAPA_COLOR_J2
        elif self.sup < self.supCas:
            self.color = MAPA_COLOR_NEUTRO
        elif self.sup < MULT_SUPREMACIA * self.supCas:
            self.color = MAPA_COLOR_J1
        else:
            self.color = MAPA_COLOR_J1_F

    def dibujar(self, surface):
        """Dibujar casilla en pantalla"""
        pygame.draw.polygon(surface, self.color, self.verts)
        infra = self.infraestructura
        if infra:
            pygame.draw.polygon(surface, infra.COLOR, self.verts, 4)
            texto(str(infra.nivel), self.centro, 12, infra.COLOR, alineado_h = 'c', alineado_v = 'c', negrita = True, surface = surface)
        if self.sel:
            pygame.draw.polygon(surface, MAPA_COLOR_BORDE, self.verts, 2)
        if self.pul:
            pygame.draw.polygon(surface, MAPA_COLOR_BORDE, self.verts, 4)

    def seleccionar(self):
        """Seleccionar la casilla cuando el raton pasa por encima"""
        if self.sel:
            return
        self.sel = True
        g_escenario.casilla_sobre = self
        reproducir_sonido('casilla_sel')

    def deseleccionar(self):
        """Deseleccionar la casilla"""
        if not self.sel:
            return
        self.sel = False
        g_escenario.casilla_sobre = None

    def pulsar(self):
        """Pulsar la casilla cuando el raton hace click"""
        if self.pul:
            return
        self.pul = True
        g_escenario.casilla_pulsa = self
        reproducir_sonido('casilla_pul')

    def despulsar(self):
        """Despulsar la casilla"""
        if not self.pul:
            return
        self.pul = False
        g_escenario.casilla_pulsa = None

class Escenario:
    ORIGEN_X = (ANCHURA * ANCHURA_JUEGO - MAPA_DIM_X * Casilla.DIM_X) / 2
    ORIGEN_Y = ALTURA * ALTURA_JUEGO - MAPA_DIM_Y * Casilla.DIM_Y
    ORIGEN = pygame.Vector2(ORIGEN_X, ORIGEN_Y)

    def __init__(self, panel):
        self.panel = panel

        # Calcular las dimensiones de las casillas
        hex_vert = pygame.math.Vector2.from_polar((Casilla.RADIO * Casilla.BORDE, 90))
        self.hex_vertices = [hex_vert.rotate(60 * i) for i in range(6)]

        # Array de casillas
        self.casillas = [[Casilla(self, x, y) for y in range(MAPA_DIM_Y)] for x in range(MAPA_DIM_X)]
        self.resetear()

    def semillear(self):
        """Cambiar la seleccion de celdas aleatorias que tienen supremacia inicial (OJO: resetea las celdas!)"""
        # Resetear los valores de superioridad
        for col in self.casillas:
            for casilla in col:
                casilla.resetear()

        # Generar nuevas casillas aleatorias con supremacia
        supremacia = int(MAPA_DIM_J * MAPA_DIM_Y * SUP_INICIAL)
        for j in range(2):
            casillas = [c for col in self.casillas for c in col if c.jugador == g_jugadores[j]]
            for casilla in random.sample(casillas, supremacia):
                casilla.sup *= MULT_SUPREMACIA
                casilla.colorear()

        # Reajustar los colores de las casillas
        for col in self.casillas:
            for casilla in col:
                casilla.colorear()

    def actualizar(self):
        """Detectar si alguna casilla esta seleccionada o ha sido pulsada"""

        # Si el ratón no está sobre el panel del escenario, no hay nada que actualizar
        if not self.panel.raton():
            return

        # Aproximar la casilla en la que estamos, para evitar testearlas todas
        pos_vec = pygame.Vector2(g_raton)
        d = (pos_vec - self.ORIGEN).elementwise() / Casilla.DIM
        x1 = max(round(d.x) - 1, 0)
        x2 = min(round(d.x) + 1, MAPA_DIM_X - 1)
        y1 = max(round(d.y) - 1, 0)
        y2 = min(round(d.y) + 1, MAPA_DIM_Y - 1)

        # Realizar chequeo
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                casilla = self.casillas[x][y]
                if not casilla.raton(pos_vec):
                    continue

                # Casilla seleccionada
                if self.casilla_sobre and self.casilla_sobre != casilla:
                    self.casilla_sobre.deseleccionar()
                casilla.seleccionar()
                if not g_click:
                    return

                # Casilla pulsada
                if self.casilla_pulsa and self.casilla_pulsa != casilla:
                    self.casilla_pulsa.despulsar()
                casilla.pulsar()
                return

        # Si llegamos aquí, ninguna casilla está seleccionada
        if self.casilla_sobre:
            self.casilla_sobre.deseleccionar()
        if self.casilla_pulsa and g_click:
            self.casilla_pulsa.despulsar()

    def dibujar(self):
        """Dibujar todas las celdas en pantalla"""
        self.panel.dibujar()
        for columna in self.casillas:
            for casilla in columna:
                casilla.dibujar(self.panel.surface)

    def resetear(self):
        """Resetear los contenidos de todas las celdas"""
        for col in self.casillas:
            for casilla in col:
                casilla.resetear()
        self.semillear()
        self.casilla_sobre = None # Casilla actualmente seleccionada con el raton
        self.casilla_pulsa = None # Casilla actualmente pulsada por el raton

class Informacion:
    """Representa el panel informativo"""
    def __init__(self, panel):
        self.panel = panel
        self.texto = None
        x, y, w, h = self.panel.rect
        self.botones = [
            Boton((0, 0), texto="Jugar",     anchura=80, accion=siguiente_jugador),
            Boton((0, 0), texto="Música",    anchura=80, accion=cambiar_musica),
            Boton((0, 0), texto="Reglas",    anchura=80, accion=g_reglas.mostrar),
            Boton((0, 0), texto="Reiniciar", anchura=80, accion=resetear),
            Boton((0, 0), texto="Salir",     anchura=80, accion=salir)
        ]
        for i, b in enumerate(reversed(self.botones)):
            b.mover(x + w - b.dim[0], y + h - (i + 1) * b.dim[1])

    def escribir(self, texto):
        """Cambiar el texto del panel"""
        self.texto = texto

    def borrar(self):
        """Eliminar el texto del panel"""
        self.texto = None

    def actualizar(self):
        """Actualizar los contenidos del panel"""
        for boton in self.botones:
            boton.actualizar()

    def dibujar(self):
        """Renderizar el texto en pantalla"""
        self.panel.dibujar()
        x, y, w, h = self.panel.rect
        nombres = "Fase:\nTurno:"
        valores = f"{g_fase}\nJugador {g_jugador.indice + 1}"
        texto_multilinea(nombres, (x + w - 150, y), 16, negrita = True)
        texto_multilinea(valores, (x + w - 100, y), 16)
        if self.texto:
            texto_multilinea(self.texto, (x + 10, y + 30), 14, mono = True, max_ancho = w)
        for boton in self.botones:
            boton.dibujar()

    def resetear(self):
        """Reiniciar los contenidos del panel informativo"""
        for boton in self.botones:
            boton.resetear()

class Reglamento:
    """Representa el conjunto de reglas, para el pantallazo inicial"""

    REGLAS = """
    AIRGAME es un juego de estrategia basado en medios militares aéreos. El objetivo del juego es obtener mayor superioridad aérea que el oponente. Dicha superioridad se conseguirá mediante el empleo de diversas aeronaves y medios a lo largo del tablero establecido.
    ¿Cómo se consigue la superioridad aérea?
    Durante el desarrollo del juego, la superioridad aérea (Sup.A) se conseguirá al desplegar aeronaves a lo largo del tablero. Cada medio aéreo posee un coeficiente de Sup.A que se hará efectivo cuando permanezca en una casilla determinada.
    Ejemplo: Si una aeronave del jugador 1(J1) con coeficiente de Sup.A = 5, permanece durante dos turnos en una casilla, a esta se le sumarán 10 puntos de Sup.A de J1. (5 Sup.A x 2 turnos = 10)
    Al inicio del juego, cada casilla tendrá asociada un coeficiente de Sup.A de casilla y otro actual:
        -Coeficiente de superioridad de casilla: Indica que Sup.A hay que ejercer en dicha casilla para obtener la Sup.A.
        -Coeficiente de superioridad actual: Indica la Sup.A que actualmente está ejerciendo un jugador.
    Ejemplo: Una casilla está definida por [10 / 6 (J2)] (10 es el coeficiente de Sup.A de casilla y 6 el actualmente ejercido por el J2). Si como en el ejemplo anterior, una aeronave de J1 permanece 2 turnos en dicha casilla la casilla estará definida por [10 / 4 (J1)]. Si la misma aeronave es capaz de estar cuatro turnos en dicha casilla, J1 obtendrá la Sup.A en dicha casilla ya que el nivel de Sup.A actual de J1 es superior al de la casilla [10 / 14 (J1)].
    Existirán 2 tipos de superioridad aérea, tal y como describe la NATO en el AJP 3.3.:
        -Superioridad aérea (Sup.A): Grado de dominación que permite dirigir operaciones en un momento y lugar dado sin que la interferencia enemiga sea prohibitiva para el desarrollo de las mismas. Se conseguirá cuando el coeficiente de Sup.A de un jugador sea igual o mayor al de la casilla.
        -Supremacía aérea (Supre.A): Grado donde la fuerza aérea enemiga es incapaz de interferir efectivamente a las operaciones propias. Se conseguirá cuando el coeficiente de Sup.A de un jugador sea igual al doble o mayor al de la casilla. Obtener la Supre.A de una casilla permite al jugador poder crear una ciudad o una base en dicha casilla.
    En el juego también tendrá presencia el estado de igualdad aérea, en el caso de que ninguno de los jugadores posea superioridad aérea.
    En la primera pantalla aparecerá el tablero de juego, la tienda de productos y el panel de información.
        -Tablero de juego: Esta formado por casillas hexagonales. Existen diferentes tipos de casillas en función de su desempeño en el juego, diferenciándose en su color y en los coeficientes asociados a sus características:
            [AZUL] Territorio 1: Casillas en propiedad del jugador 1.
                -Coeficiente de Sup.A de casilla: 20
            [NARANJA] Territorio 2: Casillas en propiedad del jugador 2.
                -Coeficiente de Sup.A de casilla: 20
            [NEGRA (AZUL/NARANJA)] Ciudad: Casilla que da al jugador recursos cuando es de su propiedad.
                -Coeficiente de Sup.A de casilla: 40
                -Coeficiente de desarrollo: Nivel de infraestructura alcanzado. Cada ciudad otorgará al jugador (5M x nivel) de la ciudad en cada turno.
            [VERDE (AZUL/NARANJA)] Base aérea: Casilla desde la que se despliegan los medios. Cada base podrá desplegar tantos medios como alto sea su nivel.
                -Coeficiente de Sup.A de casilla: 60
                -Coeficiente de movilidad aérea: Nivel de infraestructura alcanzado. Desde cada base se podrán desplegar tantas aeronaves como nivel tenga la base.
            [DORADO(AZUL/NARANJA)] Capital: Ciudad más importante de cada jugador. Si el adversario consigue obtener supremacía aérea en dicha casilla, gana la partida.
                -Coeficiente de Sup.A de casilla: 100
                -Coeficiente de desarrollo: Nivel de infraestructura alcanzado.
    -Tienda de productos: Aparecen los 9 productos disponibles en el juego con una serie de características asociadas:
            -Medios aéreos:
                [AVO. CAZA]: Único medio aéreo que puede atacar otros medios aéreos. El otro medio anti aéreo que puede hacerlo es la batería antiaérea.
                [AVO. ATAQUE]: Medio aéreo capaz de atacar medios anti aéreos.
                [AVO. TRANSPORTE]: Medio aéreo con más alcance.
                [HELICÓPTERO]: Único medio aéreo capaz de aterrizar en una casilla que no sea una base. Además es capaz de atacar medios anti aéreos.
                [DRON]: Único medio aéreo con capacidad de vigilancia y con mayor autonomía, además es capaz de atacar medios anti aéreos.
        -Medios anti aéreos:
            [RADAR]: Medio antiaéreo con el mayor alcance de vigilancia.
            [BATERÍA ANTIAÉREA]: Único medio antiaéreo con capacidad de atacar medios aéreos además de tener capacidad de vigilancia.
        -Medios estratégicos:
            [INTELIGENCIA]: Medio estratégico que permite obtener diversa información sobre el adversario.
            [INFRAESTRUCTURA]: Medio estratégico que permite aumentar el nivel de las ciudades y bases propias.
    -Panel de información: En el aparecerá la información correspondiente al elemento que en ese momento este indicando el ratón. Además de una breve descripción de cada producto aparecerá la siguiente información dependiendo de si se tratan de medios aéreos, anti aéreos o estratégicos:
            -Medios aéreos y anti aéreos:
            [PRECIO]: coste del medio (€)
            [VELOCIDAD]: velocidad a la que va a poder avanzar por las casillas un producto / (km/h) - (casillas/turno).
            [AUTONOMÍA]: tiempo que va a poder estar fuera de la base un producto / (horas) - (turnos).
            [ALCANCE]: distancia (horizontal) a la que va a poder llegar un producto / (km) - (casillas).
            [HUELLA]: probabilidad de ser captado por una vigilancia 100% / (%).
            [AIRE]: distancia a la que puede derribar un medio aéreo / (casillas).
            [SUP]: distancia a la que puede derribar un medio antiaéreo / (casillas).
            [VIGILANCIA]: probabilidad de captar un producto con huella radar 100% / (%).
            [RADIOVIG.]: distancia a la que puede vigilar otro producto / (km) - (casillas).
            [SUPAEREA]: peso de cada producto a la hora de aportar superioridad aérea / (número).
            -Medios estratégicos:
            [INTELIGENCIA]:
                (NIVEL 1): Da la posición de una de las ciudades del oponente.
                (NIVEL 2): Da la posición de todas las ciudades del oponente.
                (NIVEL 3): Da la posición de la capital del oponente.
                (NIVEL 4): Da el nivel de las ciudades y bases del oponente.
                (NIVEL 5): Da información sobre el número de medios de los que dispone el oponente.
            [INFRAESTRUCTURA]: este medio estratégico podrá ser ejercido en las siguientes casillas:
                (CASILLA CON SUPREMACÍA AÉREA): Se creará una ciudad o una base de nivel 1.
                (CIUDAD): Cada nivel de mejora proporcionará más recursos al jugador / 10M x Nivel de ciudad.
                (BASE): El nivel de la base determinará el número de medios que se pueden mover de dicha base / 1 medio x Nivel de la base.
    A continuación el jugador deberá elegir en que casillas colocar las ciudades, las bases aéreas y los medios comprados:
        [CIUDADES Y BASES AÉREAS]: Deberán ser colocados en casillas con supremacía aérea del propio jugador.
            -Al inicio de la partida el jugador contará con 3 ciudades y 3 bases aéreas que podrá colocar en las casillas en las que posee supremacía aérea.
        [MEDIOS AÉREOS]: Deberán ser colocados en bases aéreas.
        [MEDIOS ANTIAÉREOS]: Deberán ser colocados en casillas con superioridad aérea del propio jugador.
    La dinámica principal del juego se basa en turnar una serie de acciones entre los jugadores. Estas acciones serán:
        -Recibir reporte del movimiento del adversario:
            [Ataque del enemigo ]: Derribo, destrucción o fracasos de ataques sobre medios propios.
            [Conquista de casillas]: En el caso de que el enemigo haya conseguido variar el estado de superioridad aérea de una casilla esta cambiara de color dependiendo de su estado actual.
            [Captación de medios del enemigo]: Captación de medios enemigos por radares, baterías y drones propios.
        -Recibir ingresos: Los ingresos que se recibirán serán los siguiente:
            [500M]: Al inicio de la partida.
            [10M x ciudad x nivel de la ciudad]: Al principio de cada turno.
        -Recibir inteligencia: La inteligencia recibida dependerá de su nivel.
        -Invertir ingresos: El crédito disponible podrá ser gastado en los productos disponibles en la tienda.
        -Movilizar aeronaves: A la hora de movilizar aeronaves hay que tener una serie de aspectos en cuenta:
            [Capacidad de despliegue]: Cada base aérea podrá tener desplegados en un mismo turno tantos medios aéreos como nivel tenga.
            [Despegue y aterrizaje en la misma base aérea]: Todas las aeronaves deberán despegar y aterrizar en la misma base aérea. Excepto el helicóptero y el avión de transporte.
            [Caso especial, helicóptero]: Puede aterrizar y despegar en cualquier casilla. Solo ejercerá superioridad aérea cuando este en vuelo. Hasta que este no retorne a la base aérea desde la que despegó contará como medio aéreo desplegado para dicha base.
            [Caso especial, avión de transporte]: Puede aterrizar y despegar en cualquier base aérea amiga o ciudad, ya se amiga o enemiga. Solo ejercerá superioridad aérea cuando este en vuelo. Hasta que este no retorne a la base aérea desde la que despegó contará como medio aéreo desplegado para dicha base.
            [Alcance]: Cada aeronave tiene un alcance de casillas que es inversamente proporcional al tiempo de permanencia (turnos) que queremos que este en la casilla seleccionada. Es decir, cuanto más lejos queremos que llegue, menos tiempo podrá permanecer en dicha casilla.
            [Permanencia]: Cada aeronave podrá permanecer un número determinado de turnos en la casilla seleccionada dependiendo del alcance al que se haya querido movilizar a la aeronave.
            [Conquista por parte del rival de una base aérea]: Si el oponente es capaz de conseguir la superioridad aérea de una base, tanto los medios desplegados como los medios que estén en la propia base sin desplegar, serán derribados y por lo tanto eliminados del juego.
        -Ataque: Las aeronaves con capacidad de ataque, ya sea aire-aire o aire-suelo que estén en el aire podrán atacar a una casilla en cada turno que estén en el aire. Dicho ataque será visualizado por el oponente, es decir el adversario podrá ver que casilla ha sido atacada y si ha sido un ataque aire-aire o aire-suelo. Si el ataque ha sido certero los medios aéreos (ataque aire-aire) o antiaéreos (aire-suelo) serán destruidos.
    El juego finalizará cuando se cumpla uno de los siguientes requisitos:
        -Jx obtenga Supre.A en la capital del adversario. Gana Jx.
        -Jx obtenga Sup.A en todas las ciudades y la capital del adversario. Gana Jx.
        -(Jx) obtenga Sup.A en todas las bases del adversario. Gana Jx.
        -Se acabe el número de rondas establecido previamente por los jugadores. Gana el jugador que sume más puntos de coeficiente de Sup.A.
    """
    LINEAS_POR_PAGINA = 20        # Numero de lineas por pagina de reglas
    TAMANO_FUENTE     = 16        # Tamaño de fuente del resto de texto
    TAMANO_TITULO     = 72        # Tamaño de fuente del titulo
    TAMANO_BOTONES    = 36        # Tamaño de fuente de los botones
    MARGEN_EXTERNO    = 20        # Margen entre el panel y la pantalla
    MARGEN_INTERNO    = 30        # Margen entre el panel y el texto
    COLOR_FONDO       = "#E5E4E2" # Color de fondo del panel del pantallazo reglas
    COLOR_TEXTO       = '#000000' # Color de fondo del panel del pantallazo reglas

    def __init__(self):
        # Crear superficie auxiliar con todo el contenido, para evitar re-renderizar cada fotograma
        x, y = (self.MARGEN_EXTERNO, self.MARGEN_EXTERNO)
        dim = (ANCHURA - 2 * x, ALTURA - 2 * y)
        self.panel = Panel((x, y), dim, radio=20, color=self.COLOR_FONDO, textura='malla')
        self.visible = False

        # Calcular numero de paginas totales
        fuente = g_fuentes[self.TAMANO_FUENTE]
        lineas = dividir_texto(self.REGLAS, fuente, self.panel.rect.w - 2 * self.MARGEN_INTERNO)
        self.paginas = math.ceil(len(lineas) / self.LINEAS_POR_PAGINA)
        self.pagina = 0

        # Botones de control
        w = self.panel.rect.w
        dy = self.TAMANO_TITULO + 10 + self.LINEAS_POR_PAGINA * fuente.get_linesize() + 40
        self.botones = [
            Boton((0, dy), texto='Anterior',  tamaño=self.TAMANO_BOTONES, accion=self.pagina_anterior,  surface=self.panel.lienzo, origen=(x,y)),
            Boton((0, dy), texto='Siguiente', tamaño=self.TAMANO_BOTONES, accion=self.pagina_siguiente, surface=self.panel.lienzo, origen=(x,y)),
            Boton((0, dy), texto='Salir',     tamaño=self.TAMANO_BOTONES, accion=self.resetear,         surface=self.panel.lienzo, origen=(x,y))
        ]
        anchura = sum(boton.dim[0] for boton in self.botones) + 10 * (len(self.botones) - 1)
        diff = 0
        for boton in self.botones:
            boton.mover((w - anchura) / 2 + diff, 0)
            diff += boton.dim[0] + 10


        # Renderizar la superficie, habra que hacerlo cada vez que haya un cambio (ver self.actualizar)
        self.resetear()

    def renderizar(self):
        """Renderizar el contenido del reglamento. Hay que llamarlo cada vez que cambie (e.g. al paginar)."""
        x, y, w, h = self.panel.rect
        self.panel.renderizar()
        texto('REGLAS', (x + ANCHURA / 2, y), color=self.COLOR_TEXTO, tamaño=self.TAMANO_TITULO, alineado_h='c', surface=self.panel.lienzo)
        texto_multilinea(
            Reglamento.REGLAS, (x + self.MARGEN_INTERNO, y + self.TAMANO_TITULO + 10), color=self.COLOR_TEXTO, tamaño=self.TAMANO_FUENTE,
            max_ancho=w-2*self.MARGEN_INTERNO, max_alto=self.LINEAS_POR_PAGINA, surface=self.panel.lienzo, pagina=self.pagina
        )
        for boton in self.botones:
            boton.dibujar()

    def pagina_anterior(self):
        """Cambiar a la pagina anterior"""
        if self.pagina > 0:
            self.pagina -= 1
        else:
            reproducir_sonido('error')
        self.renderizar()

    def pagina_siguiente(self):
        """Cambiar a la pagina siguiente"""
        if self.pagina < self.paginas - 1:
            self.pagina += 1
        else:
            reproducir_sonido('error')
        self.renderizar()

    def resetear(self):
        """Inicializar paginacion"""
        self.pagina = 0
        self.renderizar()
        self.ocultar()

    def actualizar(self):
        """Actualiza el estado del panel de reglas. Si hay algun cambio, vuelve a renderizar. Ejecutar cada fotograma."""
        cambio = False
        for boton in self.botones:
            cambio = cambio or boton.actualizar()
        if cambio:
            self.renderizar()

    def mostrar(self):
        """Mostrar las reglas en pantalla"""
        self.visible = True

    def ocultar(self):
        """Ocultar el panel de reglas en pantalla"""
        self.visible = False

    def dibujar(self):
        """Dibujar el reglamento en pantalla. Hay que llamarlo cada fotograma."""
        if self.visible:
            self.panel.dibujar()

class Jugador:
    """Representa a cada uno de los jugadores"""
    jugadores = 0

    def __init__(self):
        self.indice = self.jugadores
        type(self).jugadores += 1
        self.resetear()

    def resetear(self):
        """Reiniciar el estado del jugador"""
        self.medios           = []
        self.infraestructuras = []
        self.credito          = CREDITO_INICIAL

    def comprar(self, producto):
        """Adquirir un medio y añadirlo al inventario"""
        if not self.pagar(producto.PRECIO):
            return
        if producto in g_tienda.MEDIOS:
            self.medios.append(producto(self))

    def construir(self, producto, casilla):
        """Construir o mejorar una infraestructura en el mapa"""
        infra = casilla.infraestructura
        if infra:
            if type(infra) is not producto:
                reproducir_sonido('error')
            else:
                infra.mejorar()
        elif self.pagar(producto.PRECIO):
            infra = producto(self, casilla)
            casilla.infraestructura = infra
            self.infraestructuras.append(infra)

    def pagar(self, cantidad):
        """Desembolsar una cierta cantidad, si hay crédito disponible"""
        if self.credito < cantidad:
            reproducir_sonido('error')
            return False
        reproducir_sonido('pagar')
        self.credito -= cantidad
        return True

    def cobrar(self, cantidad):
        """Obtener una cierta cantidad de crédito"""
        self.credito += cantidad
        reproducir_sonido('cobrar')

class Tienda:
    """Contiene todos los productos que se pueden adquirir y se encarga de su funcionalidad y renderizado"""
    BOTON_SEP = 5
    TAM_FUENTE = 24
    MEDIOS = [AvionCaza, AvionAtaque, AvionTransporte, Helicoptero, Dron, Radar, Bateria, Inteligencia]
    INFRAESTRUCTURAS = [Ciudad, Base]

    def __init__(self, panel):
        self.panel = panel

        # Crear los botones de medios
        self.botones = {}
        cols = 2
        linea = g_fuentes[self.TAM_FUENTE].get_linesize()
        x = ANCHURA * ANCHURA_JUEGO + 20
        y = 2 * (PANEL_SEPARACION + linea)
        for i, producto in enumerate(self.MEDIOS + self.INFRAESTRUCTURAS):
            boton = self.crear_boton(producto)
            self.botones[producto] = boton
            boton.mover(x, y)
            dx, dy = boton.dim
            x += dx + self.BOTON_SEP if i % cols  < cols - 1 else -(dx + self.BOTON_SEP) * (cols - 1)
            y += dy + self.BOTON_SEP if i % cols == cols - 1 else 0

    def crear_boton(self, producto):
        """Crear cada uno de los botones de la tienda"""
        accion = None
        args = ()
        if producto in self.MEDIOS:
            accion = lambda p: g_jugador.comprar(p)
            args = (producto,)
        elif producto is Ciudad:
            accion = lambda: g_jugador.construir(Ciudad, g_escenario.casilla_pulsa)
        elif producto is Base:
            accion = lambda: g_jugador.construir(Base, g_escenario.casilla_pulsa)
        return Boton((0, 0), imagen=producto.ICONO, ayuda=f"{producto.NOMBRE} ({producto.PRECIO}M)", info=producto.info(), indice=0, accion=accion, args=args, audio_pul=None)

    def actualizar(self):
        """Actualizar estado del contenido de la tienda"""

        # Actualizar botones de medios
        for medio in self.MEDIOS:
            boton = self.botones[medio]
            if g_fase == 'Preparación':
                boton.bloquear()
            else:
                boton.desbloquear()
            boton.indice = sum(1 for producto in g_jugador.medios if type(producto) is medio)
            boton.actualizar()

        # Actualizar botones de infraestructuras
        casilla = g_escenario.casilla_pulsa
        visibles = casilla and casilla.hay_supremacia()
        for infra in self.INFRAESTRUCTURAS:
            boton = self.botones[infra]
            boton.visible = visibles
            if casilla and type(casilla.infraestructura) is infra and casilla.infraestructura.jugador == g_jugador:
                boton.ayuda = f"Mejorar {infra.NOMBRE} ({infra.PRECIO_MEJORA}M)"
            else:
                boton.ayuda = f"{infra.NOMBRE} ({infra.PRECIO}M)"
            boton.indice = sum(1 for producto in g_jugador.infraestructuras if type(producto) is infra)
            boton.actualizar()

    def dibujar(self):
        """Renderizar la tienda en pantalla"""
        self.panel.dibujar()
        linea = g_fuentes[self.TAM_FUENTE].get_linesize()
        texto(f"Crédito: {g_jugador.credito}M", (ANCHURA * ANCHURA_JUEGO + PANEL_SEPARACION, PANEL_SEPARACION), tamaño=self.TAM_FUENTE)
        texto('Tienda', (ANCHURA * (ANCHURA_JUEGO + 1) / 2, PANEL_SEPARACION + linea), tamaño=self.TAM_FUENTE, alineado_h='c', subrayado=True)
        for boton in self.botones.values():
            boton.dibujar()

    def resetear(self):
        """Reiniciar el contenido de la tienda"""
        for producto, boton in self.botones.items():
            boton.resetear()

# < -------------------------------------------------------------------------- >
#                             CLASES DE LA INTERFAZ
# < -------------------------------------------------------------------------- >

class Panel:
    """Clase que representa un panel que contiene informacion"""
    def __init__(
            self,
            pos,                              # Posicion del panel en la superficie
            dim,                              # Dimensiones del panel
            nombre      = None,               # Nombre del panel
            color       = PANEL_INT_COLOR,    # Color del interior
            color_borde = PANEL_BORDE_COLOR,  # Color del borde
            grosor      = PANEL_BORDE_GROSOR, # Grosor del borde
            radio       = PANEL_BORDE_RADIO,  # Radio de curvatura de las esquinas
            surface     = g_pantalla,         # Superficie donde dibujar panel
            origen      = (0, 0),             # Posicion de la superficie en la pantalla
            textura     = None                # Textura para teselar el fondo del panel
        ):
        # Guardar parámetros del panel
        self.pos         = pos
        self.dim         = dim
        self.color       = color
        self.color_borde = color_borde
        self.grosor      = grosor
        self.radio       = radio
        self.nombre      = nombre
        self.surface     = surface
        self.origen      = origen
        self.lienzo      = pygame.Surface(dim, pygame.SRCALPHA)
        self.textura     = g_texturas[textura] if textura else None

        # Crear otros elementos útiles
        self.rect = pygame.Rect(pos, dim)
        self.renderizar()

    def renderizar(self):
        """Pre-renderizar el panel. Solo hace falta hacer esto una vez, pues su contenido no cambia."""
        # Interior
        pygame.draw.rect(self.lienzo, self.color, (0, 0) + self.dim, border_radius = self.radio)
        if self.textura:
            w, h = self.textura.get_size()
            for y in range(0, int(self.dim[1]), h):
                for x in range(0, int(self.dim[0]), w):
                    self.lienzo.blit(self.textura, (x, y))

        # Borde
        if self.grosor > 0 and self.color_borde:
            pygame.draw.rect(self.lienzo, self.color_borde, (0, 0) + self.dim, width = self.grosor, border_radius = self.radio)

        # Nombre
        if self.nombre:
            texto(self.nombre.capitalize(), (self.dim[0] / 2, 0), tamaño = 24, alineado_h = 'c', subrayado = True, surface = self.lienzo)

    def mover(self, dx, dy):
        """Cambiar la posicion del panel"""
        self.pos = (self.pos[0] + dx, self.pos[1] + dy)
        self.rect = pygame.Rect(self.pos, self.dim)

    def dibujar(self):
        """Dibujar el panel rectangular en pantalla"""
        self.surface.blit(self.lienzo, self.pos)

    def raton(self):
        """Devuelve si el raton está sobre el panel"""
        return self.rect.collidepoint((g_raton[0] - self.origen[0], g_raton[1] - self.origen[1]))

class Boton:
    """Clase que representa un boton clickable"""
    def __init__(
            self, pos, origen=(0,0), texto=None, tamaño=BOTON_TAMANO_LETRA, imagen=None, ayuda=None, textura='gotele',
            info=None, indice=None, accion=None, args=(), surface=g_pantalla, audio_sel='boton_sel', audio_pul='boton_pul',
            anchura=None, altura=None, bloqueado=False, visible=True
        ):
        if not texto and not imagen:
            return
        self.pos        = pos       # Posición del botón en pantalla
        self.texto      = None      # Texto del boton
        self.imagen     = None      # Imagen del boton
        self.ayuda      = ayuda     # Pequeña descripción del botón, para cuando es seleccionado
        self.info       = info      # Descripción más detallada del botón seleccionado
        self.accion     = accion    # Función a ejecutar si el botón es pulsado
        self.args       = args      # Argumentos que mandar a la función acción, si son necesarios
        self.surface    = surface   # Superficie sobre la que se renderiza en boton
        self.indice     = indice    # Pequeño número que aparezca en la esquina del botón
        self.audio_sel  = audio_sel # Sonido que se reproduce al seleccionar el boton
        self.audio_pul  = audio_pul # Sonido que se reproduce al pulsar el boton
        self.textura    = textura   # Textura a usar para el boton
        self.anchura    = anchura   # Anchura mínima del botón
        self.altura     = altura    # Altura mínima del botón
        self.block_orig = bloqueado # Un botón bloqueado no puede usarse. Copia del valor original, que puede cambiar.
        self.visible    = visible   # Un botón no visible no se actualiza ni dibuja
        self.selec      = False     # Verdadero si el ratón está encima del botón
        self.pulsado    = False     # Verdadero si el botón está siendo pulsado

        # Calculamos el tamaño del boton
        if texto:
            if not tamaño in TEXTO_TAMANOS:
                tamaño = BOTON_TAMANO_LETRA
            self.texto = texto
            self.imagen = g_fuentes[tamaño].render(texto, True, (0, 0, 0))
        else:
            self.imagen = imagen
        x, y = self.tamaño = self.imagen.get_size()
        if anchura and x + 5 < anchura:
            x = anchura - 5
        else:
            self.anchura = x + 5
        if altura and y + 5 < altura:
            y = altura - 5
        else:
            self.altura = y + 5
        self.dim = (x + 5, y + 5)

        # Otros elementos
        self.panel = Panel(self.pos, self.dim, None, BOTON_COLOR_NORMAL, surface=self.surface, origen=origen, textura=self.textura)

        self.resetear()

    def mover(self, dx, dy):
        """Cambiar la posicion del boton"""
        self.panel.mover(dx, dy)
        self.pos = (self.pos[0] + dx, self.pos[1] + dy)

    def bloquear(self):
        """Bloquear el boton para impedir que pueda usarse"""
        self.block = True

    def desbloquear(self):
        """Desbloquear el boton para que pueda volver a usarse"""
        self.block = False

    def mostrar(self):
        """Hacer el botón visible"""
        self.visible = True

    def ocultar(self):
        """Hacer el botón invisible (y, por ende, desactivado)"""
        self.visible = False

    def actualizar(self):
        """Actualizar estado y propiedades del boton"""
        if not self.visible:
            return

        # Modificar estado (seleccionado / pulsado) y detectar cambios
        selec_antes = self.selec
        pulsado_antes = self.pulsado
        self.selec = self.panel.raton()
        self.pulsado = self.selec and g_click
        cambio = selec_antes != self.selec or pulsado_antes != self.pulsado

        # Reproducir sonidos
        if not selec_antes and self.selec and self.audio_sel:
            reproducir_sonido(self.audio_sel)
        if not pulsado_antes and self.pulsado and self.audio_pul:
            reproducir_sonido(self.audio_pul)
        if self.pulsado and self.block:
            reproducir_sonido('error')

        # Actualizar color y renderizar boton
        if self.pulsado:
            self.panel.color = BOTON_COLOR_PULSA
        elif self.selec:
            self.panel.color = BOTON_COLOR_SOBRE
        else:
            self.panel.color = BOTON_COLOR_NORMAL
        if cambio:
            self.renderizar()

        # Mostrar información en el panel informativo
        if self.selec and self.info:
            global g_ayuda
            g_info.escribir(self.info)
            g_ayuda = self.ayuda

        # Ejecutar acción si está pulsado
        if self.pulsado and self.accion and not self.block:
            self.accion(*self.args)

        # Devolver si ha habido cambio de estado
        return selec_antes != self.selec or pulsado_antes != self.pulsado

    def renderizar(self):
        """Volver a renderizar el contenido del boton. Solo hace falta hacerlo cuando ha cambiado."""
        self.panel.renderizar()
        self.panel.lienzo.blit(self.imagen, ((self.anchura - self.tamaño[0]) / 2, (self.altura - self.tamaño[1]) / 2))
        if not self.indice:
            return
        fuente = g_fuentes[AYUDA_TAMANO]
        w1, h1 = self.dim
        w2, h2 = fuente.size(str(self.indice))
        texto(str(self.indice), (w1 - 2, h1 - h2), tamaño = AYUDA_TAMANO, color = "#ff0000", alineado_h = 'd', surface = self.panel.lienzo)

    def dibujar(self):
        """Dibujar el botón en pantalla. Hay que llamarlo cada fotograma."""
        if self.visible:
            self.panel.dibujar()

    def resetear(self):
        """Reiniciar los valores del botón <<a fábica>>"""
        self.block   = self.block_orig
        if self.indice:
            self.indice = 0
        self.renderizar()

# < -------------------------------------------------------------------------- >
#                         FUNCIONES AUXILIARES INTERFAZ
# < -------------------------------------------------------------------------- >

def tiempo():
    """Milisegundos (entero) desde inicio del programa"""
    return round(pygame.time.get_ticks())

def entre(n, a, b):
    """Mete el numero n en el intervalo [a, b]"""
    return min(max(a, n), b)

def ayuda():
    """Muestra un pequeño rectángulo con información de ayuda y las info asociada a cada producto cuando el ratón esta sobre su botón"""
    x, y = g_raton
    pos = (x - 80, y + 20)
    fuente = g_fuentes[AYUDA_TAMANO]
    dim = fuente.size(g_ayuda)
    pygame.draw.rect(g_pantalla, AYUDA_COLOR, pos + dim)
    texto(g_ayuda, pos, AYUDA_TAMANO)

def texto(
        cadena,                    # Cadena de texto a renderizar
        posicion,                  # Posicion del texo con respecto a la superficie
        tamaño     = TEXTO_TAMANO, # Tamaño de la fuente en píxeles
        color      = COLOR_TEXTO,  # Color del texto (hex, tripla de ints...)
        alineado_h = 'i',          # Alineacion [i(zquierda), c(entro), d(erecha)]
        alineado_v = 'a',          # Alineacion [a(rriba), c(entro), b(ase)]
        negrita    = False,
        cursiva    = False,
        subrayado  = False,
        mono       = False,        # Usar fuente monoespaciada
        surface    = g_pantalla    # Superficie donde renderizar texto
    ):
    """Escribir un texto en la pantalla"""
    # Aseguramos que el tamaño de fuente deseado esta disponible
    if not tamaño in TEXTO_TAMANOS:
        tamaño = TEXTO_TAMANO

    # Ajustamos la posicion para respetar el alineado
    fuente = g_fuentes_mono[tamaño] if mono else g_fuentes[tamaño]
    dx, dy = fuente.size(cadena)
    if type(posicion) is pygame.math.Vector2:
        x, y = posicion.x, posicion.y
    else:
        x, y = posicion
    x -= (dx if alineado_h == 'd' else dx / 2 if alineado_h == 'c' else 0)
    y -= (dy if alineado_v == 'b' else dy / 2 if alineado_v == 'c' else 0)

    # Configuramos y renderizamos el texto
    subrayado_original = fuente.underline
    negrita_original = fuente.bold
    cursiva_original = fuente.italic
    fuente.underline = subrayado
    fuente.bold = negrita
    fuente.italic = cursiva
    imagen = fuente.render(cadena, True, color)
    fuente.underline = subrayado_original
    fuente.bold = negrita_original
    fuente.italic = cursiva_original

    # Copiamos el texto a la imagen en la posicion deseada
    surface.blit(imagen, (x, y))

def dividir_texto(texto, fuente, max_ancho):
    """Permite dividir el texto, producir saltos de línea y tabulaciones"""
    palabras = texto.split(' ')
    lineas = []
    linea_actual = ""

    for palabra in palabras:
        if '\n' in palabra:
            sub_palabras = palabra.split('\n')
            for sub_palabra in sub_palabras[:-1]:
                if fuente.size(linea_actual + sub_palabra)[0] <= max_ancho:
                    linea_actual += sub_palabra + " "
                else:
                    lineas.append(linea_actual)
                    linea_actual = sub_palabra + " "
                lineas.append(linea_actual)
                linea_actual = ""
            linea_actual = sub_palabras[-1] + " "
        elif fuente.size(linea_actual + palabra)[0] <= max_ancho:
            linea_actual += palabra + " "
        else:
            lineas.append(linea_actual)
            linea_actual = palabra + " "
    lineas.append(linea_actual)
    return lineas

def texto_multilinea(
        cadena,
        posicion,
        tamaño     = TEXTO_TAMANO,
        color      = COLOR_TEXTO,
        alineado_h = 'i',
        alineado_v = 'a',
        negrita    = False,
        cursiva    = False,
        subrayado  = False,
        mono       = False,
        surface    = g_pantalla,
        pagina     = 0,
        max_ancho  = 200,
        max_alto   = 20
    ):
    """
    Permite dividir el texto, producir saltos de línea y tabulaciones
    Devuelve un booleano que indica si faltan paginas por dibujar
    """
    if not tamaño in TEXTO_TAMANOS:
        tamaño = TEXTO_TAMANO
    fuente = g_fuentes_mono[tamaño] if mono else g_fuentes[tamaño]
    x, y = posicion
    lineas = dividir_texto(cadena.replace('\t', '    '), fuente, max_ancho)
    paginas = math.ceil(len(lineas) / max_alto)
    pagina = entre(pagina, 0, paginas - 1)
    for linea in lineas[max_alto * pagina : max_alto * (pagina + 1)]:
        texto(linea, (x, y), tamaño, color, alineado_h, alineado_v, negrita, cursiva, subrayado, mono, surface)
        y += fuente.get_linesize()
    return pagina < paginas - 1

# < -------------------------------------------------------------------------- >
#                       ACTUALIZACION DEL ESTADO DEL JUEGO
# < -------------------------------------------------------------------------- >

def actualizar_fondo():
    """Dibujar el fondo (primera capa del display)"""
    g_pantalla.fill(COLOR_FONDO)

def cambiar_musica():
    """Mutear o no la música de fondo"""
    if g_config['musica']:
        pygame.mixer.music.set_volume(0)
        g_config['musica'] = False
    else:
        pygame.mixer.music.set_volume(MUSICA_VOLUMEN)
        g_config['musica'] = True

def siguiente_fotograma():
    """Avanzar fotograma"""
    pygame.display.flip()   # Renderizar fotograma en pantalla y cambiar buffer
    g_reloj.tick(FPS)       # Avanzar reloj y limitar frecuencia de fotogramas

def siguiente_jugador():
    """Cambiar de turno"""
    global g_jugador
    if not g_jugador:
        g_jugador = g_jugadores[0]
    else:
        g_jugador = g_jugadores[(g_jugador.indice + 1) % 2]

def siguiente_fase():
    """Avanzar a la siguiente fase del juego"""
    global g_fase
    indice = g_fases.index(g_fase)
    if indice < len(g_fases) - 1:
        g_fase = g_fases[indice + 1]
    else:
        resetear_fase()

def cambiar_fase(nombre):
    """Cambiar a otra fase del juego"""
    global g_fase
    if nombre in g_fases:
        g_fase = nombre
        return True
    return False

def resetear_fase():
    """Volver a la primera fase del juego"""
    global g_fase
    g_fase = g_fases[0]

def actualizar_variables():
    """Actualizacion de variables en cada fotograma"""
    global g_ayuda, g_raton
    g_ayuda = None
    g_info.borrar()
    g_raton = pygame.mouse.get_pos()

def actualizar_fase_pantallazo():
    """Dibujar pantallazo inicial"""
    x = (g_pantalla.get_width() - g_pantallazo.get_width()) / 2
    y = (g_pantalla.get_height() - g_pantallazo.get_height()) / 2
    g_pantalla.blit(g_pantallazo, (x, y))

def actualizar_fase_reglas():
    """Dibujar pantallazo reglas"""
    g_reglas.mostrar()
    g_reglas.actualizar()
    g_reglas.dibujar()

def actualizar_fase_turnos():
    """Actualizar estado en la fase de turnos"""
    visible = not g_reglas.visible

    # Actualizar estado sólo si el escenario es visible
    if visible:
        g_escenario.actualizar()
        g_tienda.actualizar()
        g_info.actualizar()

    # Dibujar contenido de los paneles
    g_escenario.dibujar()
    g_tienda.dibujar()
    g_info.dibujar()

    # Paneles adicionales opcionales
    if g_ayuda:
        ayuda()
    if g_reglas.visible:
        actualizar_fase_reglas()

def resetear():
    g_reglas.resetear()
    g_escenario.resetear()
    g_tienda.resetear()
    g_info.resetear()
    for jugador in g_jugadores:
        jugador.resetear()
    resetear_fase()

def salir():
    pygame.event.post(pygame.event.Event(pygame.QUIT))

# < -------------------------------------------------------------------------- >
#                           INICIALIZACIÓN DEL JUEGO
# < -------------------------------------------------------------------------- >

# Comenzar musica
pygame.mixer.music.set_volume(MUSICA_VOLUMEN if MUSICA_REPRODUCIR else 0)
pygame.mixer.music.play(-1)

# Configurar paneles
sep = PANEL_SEPARACION
paneles = {
    'escenario':   Panel((sep, sep), (ANCHURA * ANCHURA_JUEGO - 1.5 * sep, ALTURA * ALTURA_JUEGO - 1.5 * sep), textura='hierba'),
    'tienda':      Panel((ANCHURA * ANCHURA_JUEGO + sep / 2, sep), (ANCHURA * ANCHURA_ACCIONES - 1.5 * sep, ALTURA * ALTURA_ACCIONES - 1.5 * sep), textura='ladrillos'),
    'informacion': Panel((sep, ALTURA * ALTURA_JUEGO + sep / 2), (ANCHURA - 2 * sep, ALTURA * ALTURA_INFORMACION - 1.5 * sep), 'información', textura='piedras')
}

# Inicializar algunas variables globales (no cambiar estas líneas de orden)
g_jugadores = [Jugador() for _ in range(2)]         # Lista de jugadores
g_jugador   = g_jugadores[0]                        # Jugador actual
g_reglas    = Reglamento()                          # Paginador de reglas
g_escenario = Escenario(paneles['escenario'])       # Casillas del mapa y su contenido
g_tienda    = Tienda(paneles['tienda'])             # Tienda de productos
g_info      = Informacion(paneles['informacion'])   # Panel informativo inferior

# Fases del juego
g_fases = ['Pantallazo', 'Reglas', 'Preparación', 'Turnos', 'Final']
g_fase = g_fases[0]

# Configuracion
g_config = {
    'musica': MUSICA_REPRODUCIR
}

# Estado
g_raton = pygame.mouse.get_pos()
g_click = False

# < -------------------------------------------------------------------------- >
#                          BUCLE PRINCIPAL DEL JUEGO
# < -------------------------------------------------------------------------- >

while True:
    # Escanear eventos (pulsaciones de teclas, movimientos de ratón, etc)
    cerrar = False
    g_click = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cerrar = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            g_click = True
    if cerrar:
        pygame.quit()
        break

    actualizar_variables() # Inicializar estado
    actualizar_fondo()     # Colorear fondo

    # Ejecutar cada fase del juego
    if g_fase == 'Pantallazo':                        # Pantallazo inicial
        actualizar_fase_pantallazo()
        if g_click:
            siguiente_fase()
    elif g_fase == 'Reglas':                          # Pantallazo de reglas
        actualizar_fase_reglas()
        if not g_reglas.visible:
            siguiente_fase()
    elif g_fase in ['Preparación', 'Turnos']:         # Fase central del juego
        actualizar_fase_turnos()
    else:
        pass

    siguiente_fotograma()