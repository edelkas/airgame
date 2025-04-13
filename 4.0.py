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

import enum    # Clases que funcionan como un enum de C
import math    # Operaciones y funciones matemáticas
import os      # Manipulaciones del sistema
import pygame  # Motor del juego
import random  # Para generacion de números aleatorios
import re      # Para expresiones regulares (regex)

# Lo siguiente es para evitar que se muestre publicidad de PyGame en la consola al iniciar
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'


# < -------------------------------------------------------------------------- >
#                            CONSTANTES GLOBALES
# < -------------------------------------------------------------------------- >

# Constantes generales del juego
NOMBRE_JUEGO    = "AIR GAME"
NOMBRE_DEFECTO  = "Jugador"
CREDITO_INICIAL = 500

# Características generales de la interfaz
ANCHURA                         = 1280      # Anchura de la ventana en pixeles
ALTURA                          = 720       # Altura de la ventana en pixeles
PANTALLA_COMPLETA               = False     # Para abrir el juego en ventana completa
PANTALLA_MODIFICARDIMENSION     = False     # Para poder modificar la dimensión de la ventana
FPS                             = 60        # Fotogramas por segundo
COLOR_FONDO                     = "#cccccc" # Color RGB del fondo de pantalla
MUSICA_REPRODUCIR               = False     # Activar o desactivar la música por defecto

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
BOTON_COLOR_NORMAL = (128, 128, 128) # Color del fondo de los botones
BOTON_COLOR_SOBRE  = (192, 192, 192) # Color del fondo cuando el raton está encima
BOTON_COLOR_PULSA  = (255, 255, 255) # Color del fondo cuando está pulsado
BOTON_TAMANO_LETRA = 16              # Tamaño de la letra

# Recursos (sonidos, imágenes...)
MUSICA_FONDO  = "topgunmusic.ogg"
IMAGEN_FONDO  = "imagenairgame.png"
SONIDO_DINERO = "cajaregistradora.ogg"
SONIDO_ERROR  = "error.ogg"

# Pantallazo
PANTALLAZO_COLOR_FONDO = '#325320' # Color de fondo del panel del pantallazo
PANTALLAZO_COLOR_TEXTO = '#000000' # Color de fondo del panel del pantallazo
PANTALLAZO_TIEMPO = 5              # Tiempo que dura el pantallazo inicial en seg

# Pantallazo reglas
PANTALLAZO_REGLAS_COLOR_FONDO = (229, 228, 226) # Color de fondo del panel del pantallazo reglas
PANTALLAZO_REGLAS_COLOR_TEXTO = '#000000'       # Color de fondo del panel del pantallazo reglas
PANTALLAZO_REGLAS_TIEMPO = 5                    # Tiempo que dura el pantallazo de reglas en seg

# Escenario
MAPA_DIM_X = 25 # Anchura del mapa en casillas
MAPA_DIM_Y = 15 # Altura del mapa en casillas
MAPA_DIM_J = 11 # Número de columnas en propiedad inicial de cada jugador
MAPA_COLOR_CASILLA_NEUTRO = "#f2f2f2" # Color de casilla sin superioridad aerea
MAPA_COLOR_CASILLA_J1     = "#bdd7ee" # Color de casilla con superioridad aerea de J1
MAPA_COLOR_CASILLA_J2     = "#f8cbad" # Color de casilla con superioridad aerea de J2
MAPA_COLOR_CASILLA_J1_F   = "#2e75b6" # Color de casilla con supremacia aerea de J1
MAPA_COLOR_CASILLA_J2_F   = "#c55a11" # Color de casilla con supremacia aerea de J2
MAPA_COLOR_BASE           = "#00b050" # Color del borde de una casilla con base aérea
MAPA_COLOR_CIUDAD         = "#000000" # Color del borde de una casilla con ciudad
MAPA_COLOR_CAPITAL        = "#c09200" # Color del borde de la casilla capital
MAPA_COLOR_BORDE          = "#9900cc" # Color del borde de la casilla actualmente seleccionada
MAPA_BORDE_CASILLA = 0.25 # Proporcion de anchura de la casilla que supone el borde, en caso de tener

# Sistema de puntos y superioridad aerea
SUP_NORMAL      = 20  # Coeficiente de sup aerea en una casilla normal
SUP_CIUDAD      = 40  # Coeficiente de sup aerea en una casilla ciudad (inicial)
SUP_CIUDAD_INC  = 5   # Coeficiente de sup aerea en una casilla ciudad (incremento por nivel)
SUP_BASE        = 60  # Coeficiente de sup aerea en una casilla base (inicial)
SUP_BASE_INC    = 5   # Coeficiente de sup aerea en una casilla base (incremento por nivel)
SUP_CAPITAL     = 100 # Coeficiente de sup aerea en una casilla capital (inicial)
SUP_CAPITAL_INC = 5   # Coeficiente de sup aerea en una casilla capital (incremento por nivel)
SUP_INICIAL     = 0.1 # Proporción de casillas iniciales con supremacia (aleatorias)

MULTIPLICADOR_SUPREMACIA = 2 # Ratio entre superioridad y supremacia aerea

# Recuadros de ayuda e informacion
AYUDA_COLOR = (255, 255, 192) # Color del fondo
AYUDA_TAMANO = 16             # Tamaño de la letra

# < -------------------------------------------------------------------------- >
#                          INICIALIZACION INTERFAZ
# < -------------------------------------------------------------------------- >

# Función que permite cargar imágenes de nuestro archivo y mostrarlas en pantalla
def cargar_imagen(nombre, trans=True):
    """Cargar un fichero de imagen en PyGame"""
    img = pygame.image.load(nombre)
    return img.convert_alpha() if trans else img.convert()

# Configuramos la pantalla (nombre, dimensiones, fotogramaje, etc)
flags = 0
if (PANTALLA_COMPLETA): flags |= pygame.FULLSCREEN
if (PANTALLA_MODIFICARDIMENSION): flags |= pygame.RESIZABLE
pygame.init()
pygame.display.set_caption(NOMBRE_JUEGO)
g_pantalla = pygame.display.set_mode((ANCHURA, ALTURA), flags)
clock = pygame.time.Clock()
texto_ayuda = None

# Cargar recursos
pygame.mixer.init()
pygame.mixer.music.load(MUSICA_FONDO)
imagen_pantallazo = cargar_imagen(IMAGEN_FONDO)
fuentes = { tam: pygame.font.SysFont(TEXTO_FUENTE, tam) for tam in TEXTO_TAMANOS }
fuentes_mono = { tam: pygame.font.SysFont(TEXTO_FUENTE_MONO, tam) for tam in TEXTO_TAMANOS }
iconos = {
    'AvionCaza':       cargar_imagen('icono_caza.png'),
    'AvionAtaque':     cargar_imagen('icono_ataque.png'),
    'AvionTransporte': cargar_imagen('icono_transporte.png'),
    'Helicoptero':     cargar_imagen('icono_helicoptero.png'),
    'Dron':            cargar_imagen('icono_dron.png'),
    'Radar':           cargar_imagen('icono_radar.png'),
    'Bateria':         cargar_imagen('icono_bateria.png'),
    'Inteligencia':    cargar_imagen('icono_inteligencia.png'),
    'Infraestructura': cargar_imagen('icono_infraestructura.png'),
}
g_sonidos = {
    'dinero': pygame.mixer.Sound(SONIDO_DINERO),
    'error':  pygame.mixer.Sound(SONIDO_ERROR),
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

    @classmethod
    def ayuda(cls):
        return "%s (%dM)" % (cls.NOMBRE, cls.PRECIO)

    @classmethod
    def info(cls):
        texto = f"""
            Descripción:  {cls.DESC}
            Precio:       {cls.PRECIO}
            Velocidad:    {cls.VELOCIDAD}
            Autonomía:    {cls.AUTONOMIA}
            Alcance:      {cls.ALCANCE}
            Huella:       {cls.HUELLA}
            Aire-aire:    {cls.AIRE}
            Aire-sup:     {cls.SUP}
            Vigilancia:   {cls.VIGILANCIA}
            Radio vigil.: {cls.RADIOVIG}
            Sup. aérea:   {cls.SUPAEREA}
        """
        return re.sub(r"^\s+", "", texto, flags = re.MULTILINE)

class MedioAereo(Medio):
    """Representa cualquier medio aéreo"""

class MedioAntiaereo(Medio):
    """Representa cualquier medio anti-aéreo"""
    VELOCIDAD  = 0
    AUTONOMIA  = 0
    ALCANCE    = 0

class MedioEstrategico(Medio):
    """Representa cualquier medio estratégico"""

class AvionCaza(MedioAereo):
    """Representa un avión de caza"""
    NOMBRE     = "Avo. Caza"
    ICONO      = iconos['AvionCaza']
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
    ICONO      = iconos['AvionAtaque']
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
    ICONO      = iconos['AvionTransporte']
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
    ICONO      = iconos['Helicoptero']
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
    ICONO      = iconos['Dron']
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
    ICONO      = iconos['Radar']
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
    ICONO      = iconos['Bateria']
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
    ICONO      = iconos['Inteligencia']
    DESC       = 'Medio estratégico que permite obtener diversa información sobre el adversario.'

class Infraestructura(MedioEstrategico):
    """Clase genérica que representa una infraestructura"""
    NOMBRE     = "Infraestructura"
    PRECIO     = 100
    ICONO      = iconos['Infraestructura']
    DESC       = 'Medio estratégico que permite aumentar el nivel de las ciudades y las bases propias.'

class Casilla:
    ESCALA = 0.6
    BORDE = 0.9
    RADIO  = min(ESCALA * ANCHURA * ANCHURA_JUEGO / MAPA_DIM_X, ESCALA * ALTURA * ALTURA_JUEGO / MAPA_DIM_Y)
    DIM_X  = RADIO * 3 ** 0.5
    DIM_Y  = RADIO * 1.5

    def __init__(self, esc, x, y):
        self.x = x
        self.y = y

        # Determinar jugador que tiene inicialmente la superioridad aerea
        if x < MAPA_DIM_J:
            self.jugador = 1
        elif x >= MAPA_DIM_X - MAPA_DIM_J:
            self.jugador = 2
        else:
            self.jugador = None

        # Determinar coeficientes de superioridad de la casilla y actuales
        self.supCas = SUP_NORMAL
        if self.jugador == 1:
            self.sup = self.supCas
        elif self.jugador == 2:
            self.sup = -self.supCas
        else:
            self.sup = 0
        self.colorear()

        # Calcular posicion en el mapa y coordenadas de cada vertice
        self.centro = pygame.math.Vector2(Escenario.ORIGEN_X + self.DIM_X * (x + (y % 2) / 2), Escenario.ORIGEN_Y + self.DIM_Y * y)
        self.verts = [self.centro + v for v in esc.hex_vertices]

    def raton(self, pos_vec):
        """Detecta si el ratón está sobre el botón"""
        return pos_vec.distance_squared_to(g_escenario.origen + self.centro) <= self.RADIO ** 2

    def colorear(self):
        """Determinar color"""
        if self.sup <= -MULTIPLICADOR_SUPREMACIA * self.supCas:
            color = MAPA_COLOR_CASILLA_J2_F
        elif self.sup <= -self.supCas:
            color = MAPA_COLOR_CASILLA_J2
        elif self.sup < self.supCas:
            color = MAPA_COLOR_CASILLA_NEUTRO
        elif self.sup < MULTIPLICADOR_SUPREMACIA * self.supCas:
            color = MAPA_COLOR_CASILLA_J1
        else:
            color = MAPA_COLOR_CASILLA_J1_F
        self.color = pygame.Color(color)

    def dibujar(self, surface):
        """Dibujar casilla en pantalla"""
        pygame.draw.polygon(surface, self.color, self.verts)

    def seleccionar(self, surface):
        """Destacar visualmente la casilla cuando el raton pasa por encima"""
        pygame.draw.polygon(surface, MAPA_COLOR_BORDE, self.verts, 2)

    def pulsar(self, surface):
        """Destacar visualmente la casilla cuando el raton hace click"""
        pygame.draw.polygon(surface, MAPA_COLOR_BORDE, self.verts, 4)

class Escenario:
    ORIGEN_X = (ANCHURA * ANCHURA_JUEGO - MAPA_DIM_X * Casilla.DIM_X) / 2
    ORIGEN_Y = ALTURA * ALTURA_JUEGO - MAPA_DIM_Y * Casilla.DIM_Y

    def __init__(self, panel):
        self.panel = panel
        self.origen = pygame.Vector2(panel.pos)

        # Calcular las dimensiones de las casillas
        hex_vert = pygame.math.Vector2.from_polar((Casilla.RADIO * Casilla.BORDE, 90))
        self.hex_vertices = [hex_vert.rotate(60 * i) for i in range(6)]

        # Array de casillas
        self.casillas = [[Casilla(self, x, y) for y in range(MAPA_DIM_Y)] for x in range(MAPA_DIM_X)]
        supremacia = int(MAPA_DIM_J * MAPA_DIM_Y * SUP_INICIAL)
        for jugador in range(1, 3):
            casillas = [c for col in self.casillas for c in col if c.jugador == jugador]
            for casilla in random.sample(casillas, supremacia):
                casilla.sup *= 2

        # Casillas especiales
        self.casilla_sobre = None # Casilla actualmente seleccionada con el raton
        self.casilla_pulsa = None # Casilla actualmente pulsada por el raton

    def raton(self):
        """Seleccionar casillas en funcion del raton"""
        pos_vec = pygame.Vector2(g_raton)
        self.casilla_sobre = None
        for columna in self.casillas:
            for casilla in columna:
                if casilla.raton(pos_vec):
                    self.casilla_sobre = casilla
                    if g_click:
                        self.casilla_pulsa = casilla

    def dibujar(self):
        """Dibujar todas las celdas en pantalla"""
        for columna in self.casillas:
            for casilla in columna:
                casilla.dibujar(self.panel.surface)
        if self.casilla_sobre:
            self.casilla_sobre.seleccionar(self.panel.surface)
        if self.casilla_pulsa:
            self.casilla_pulsa.pulsar(self.panel.surface)

class Informacion:
    """Representa el panel informativo"""
    def __init__(self, panel):
        self.panel = panel
        self.texto = None

    def escribir(self, texto):
        """Cambiar el texto del panel"""
        self.texto = texto

    def borrar(self):
        """Eliminar el texto del panel"""
        self.texto = None

    def dibujar(self):
        """Renderizar el texto en pantalla"""
        if self.texto:
            x, y, w, h = self.panel.rect
            texto_multilinea(self.texto, (x + 10, y + 30), 14, mono = True, max_ancho = w)

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
    LINEAS_POR_PAGINA = 20 # Numero de lineas por pagina de reglas
    TAMANO_FUENTE     = 16 # Tamaño de fuente del resto de texto
    TAMANO_TITULO     = 72 # Tamaño de fuente del titulo
    MARGEN_EXTERNO    = 20 # Margen entre el panel y la pantalla
    MARGEN_INTERNO    = 30 # Margen entre el panel y el texto

    def __init__(self):
        # Crear superficie auxiliar con todo el contenido, para evitar re-renderizar cada fotograma
        dim = (ANCHURA - 2 * self.MARGEN_EXTERNO, ALTURA - 2 * self.MARGEN_EXTERNO)
        self.surface = pygame.Surface(dim, pygame.SRCALPHA)
        self.panel = Panel((0,0), dim, radio=20, color=PANTALLAZO_REGLAS_COLOR_FONDO, surface=self.surface)
        x = (g_pantalla.get_width() - self.surface.get_width()) / 2
        y = (g_pantalla.get_height() - self.surface.get_height()) / 2
        self.origen = (x, y)

        # Calcular numero de paginas totales
        fuente = fuentes[self.TAMANO_FUENTE]
        lineas = dividir_texto(self.REGLAS, fuente, self.panel.rect.w - 2 * self.MARGEN_INTERNO)
        self.paginas = math.ceil(len(lineas) / self.LINEAS_POR_PAGINA)
        self.pagina = 0
        
        # Botones de control
        x, y, w, h = self.panel.rect
        x += self.MARGEN_INTERNO
        y += self.TAMANO_TITULO + 10 + self.LINEAS_POR_PAGINA * fuente.get_linesize() + 40
        self.botones = [
            Boton((x, y), origen=self.origen, texto='Anterior', tamaño=36, accion=self.pagina_anterior, surface=self.surface)
        ]
        x += self.botones[-1].dim[0] + 10
        self.botones.append(Boton((x, y), origen=self.origen, texto='Siguiente', tamaño=36, accion=self.pagina_siguiente, surface=self.surface))
        x += self.botones[-1].dim[0] + 10
        self.botones.append(Boton((x, y), origen=self.origen, texto='Salir', tamaño=36, accion=self.resetear, surface=self.surface))

        # Renderizar la superficie, habra que hacerlo cada vez que haya un cambio (ver self.actualizar)
        self.resetear()

    def renderizar(self):
        """Renderizar el contenido del reglamento. Hay que llamarlo cada vez que cambie (e.g. al paginar)."""
        x, y, w, h = self.panel.rect
        self.surface.fill(COLOR_FONDO)
        self.panel.dibujar()
        texto('REGLAS', (x + ANCHURA / 2, y), color=PANTALLAZO_REGLAS_COLOR_TEXTO, tamaño=self.TAMANO_TITULO, alineado='c', surface=self.surface)
        texto_multilinea(
            Reglamento.REGLAS, (x + self.MARGEN_INTERNO, y + self.TAMANO_TITULO + 10), color=PANTALLAZO_REGLAS_COLOR_TEXTO, tamaño=self.TAMANO_FUENTE,
            max_ancho=w-2*self.MARGEN_INTERNO, max_alto=self.LINEAS_POR_PAGINA, surface=self.surface, pagina=self.pagina
        )
        for boton in self.botones:
            boton.dibujar()

    def pagina_anterior(self):
        """Cambiar a la pagina anterior"""
        if self.pagina > 0:
            self.pagina -= 1
        else:
            g_sonidos['error'].play()
        self.renderizar()

    def pagina_siguiente(self):
        """Cambiar a la pagina siguiente"""
        if self.pagina < self.paginas - 1:
            self.pagina += 1
        else:
            g_sonidos['error'].play()
        self.renderizar()

    def resetear(self):
        """Inicializar paginacion"""
        global g_mostrar_reglas
        self.pagina = 0
        self.renderizar()
        g_mostrar_reglas = False
    
    def actualizar(self):
        """Actualiza el estado del panel de reglas. Si hay algun cambio, vuelve a renderizar. Ejecutar cada fotograma."""
        cambio = False
        for boton in self.botones:
            cambio = cambio or boton.actualizar()
        if cambio:
            self.renderizar()

    def dibujar(self):
        """Dibujar el reglamento en pantalla. Hay que llamarlo cada fotograma."""
        g_pantalla.blit(self.surface, self.origen)

# < -------------------------------------------------------------------------- >
#                             CLASES DE LA INTERFAZ
# < -------------------------------------------------------------------------- >

class Panel:
    """Clase que representa un panel que contiene informacion"""
    def __init__(
            self,
            pos, # Posicion (par de coordenadas)
            dim, # Dimensiones (par de coordenadas)
            nombre      = None,               # Nombre del panel
            color       = PANEL_INT_COLOR,    # Color del interior
            color_borde = PANEL_BORDE_COLOR,  # Color del borde
            grosor      = PANEL_BORDE_GROSOR, # Grosor del borde
            radio       = PANEL_BORDE_RADIO,  # Radio de curvatura de las esquinas
            surface     = g_pantalla,         # Superficie donde dibujar panel
            origen      = (0, 0)              # Posicion de la superficie en la pantalla
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

        # Crear otros elementos útiles
        self.rect = pygame.Rect(pos, dim)

    def dibujar(self):
        """Dibujar el panel rectangular en pantalla"""
        # Interior
        pygame.draw.rect(self.surface, self.color, self.pos + self.dim, border_radius = self.radio)

        # Borde
        if self.grosor > 0 and self.color_borde:
            pygame.draw.rect(self.surface, self.color_borde, self.pos + self.dim, width = self.grosor, border_radius = self.radio)

        # Nombre
        if self.nombre:
            texto(self.nombre.capitalize(), (self.pos[0] + self.dim[0] / 2, self.pos[1]), 24, alineado = 'c', subrayado = True, surface = self.surface)

    def raton(self):
        """Devuelve si el raton está sobre el panel"""
        return self.rect.collidepoint((g_raton[0] - self.origen[0], g_raton[1] - self.origen[1]))

class Boton:
    """Clase que representa un boton clickable"""
    def __init__(self, pos, origen=(0,0), texto=None, tamaño=BOTON_TAMANO_LETRA, imagen=None, ayuda=None, info=None, indice=None, accion=None, args=(), surface=g_pantalla):
        if not texto and not imagen:
            return
        self.pos     = pos        # Posición del botón en pantalla
        self.texto   = None       # Texto del boton
        self.imagen  = None       # Imagen del boton
        self.ayuda   = ayuda      # Pequeña descripción del botón, para cuando es seleccionado
        self.info    = info       # Descripción más detallada del botón seleccionado
        self.accion  = accion     # Función a ejecutar si el botón es pulsado
        self.args    = args       # Argumentos que mandar a la función acción, si son necesarios
        self.surface = surface    # Superficie sobre la que se renderiza en boton
        self.indice  = indice     # Pequeño número que aparezca en la esquina del botón

        # Calculamos el tamaño del boton
        if texto:
            if not tamaño in TEXTO_TAMANOS:
                tamaño = BOTON_TAMANO_LETRA
            self.texto = texto
            self.imagen = fuentes[tamaño].render(texto, True, (0, 0, 0))
        else:
            self.imagen = imagen
        x, y = self.imagen.get_size()
        self.dim = (x + 5, y + 5) # Dimensiones del botón

        # Logica
        self.selec = False        # Verdadero si el ratón está encima del botón
        self.pulsado = False      # Verdadero si el botón está siendo pulsado

        # Otros elementos
        self.panel = Panel(self.pos, self.dim, None, BOTON_COLOR_NORMAL, surface=self.surface, origen=origen)

    def actualizar(self):
        """Actualizar estado y propiedades del boton"""
        # Estado
        selec_viejo = self.selec
        pulsado_viejo = self.pulsado
        self.selec = self.panel.raton()
        self.pulsado = self.selec and g_click

        # Actualizar color
        if self.pulsado:
            self.panel.color = BOTON_COLOR_PULSA
        elif self.selec:
            self.panel.color = BOTON_COLOR_SOBRE
        else:
            self.panel.color = BOTON_COLOR_NORMAL

        # Mostrar información en el panel informativo
        if self.selec and self.info:
            global texto_ayuda
            g_info.escribir(self.info)
            texto_ayuda = self.ayuda

        # Ejecutar acción si está pulsado
        if self.pulsado:
            self.accion(*self.args)

        # Devolver si ha habido cambio de estado
        return selec_viejo != self.selec or pulsado_viejo != self.pulsado

    def dibujar(self):
        """Renderizar el boton en pantalla"""
        x, y = self.pos
        self.panel.dibujar()
        self.surface.blit(self.imagen, (x + 2, y + 2))
        if not self.indice:
            return
        fuente = fuentes[AYUDA_TAMANO]
        w1, h1 = self.dim
        w2, h2 = fuente.size(str(self.indice))
        texto(str(self.indice), (x + w1 - 2, y + h1 - h2), AYUDA_TAMANO, (0, 0, 0), 'd', surface=self.surface)

class Fase(enum.IntEnum):
    """Representa cada posible fase del juego"""
    PANTALLAZO = 1
    REGLAS     = 2
    TURNOS     = 3
    FINAL      = 4

# < -------------------------------------------------------------------------- >
#                         FUNCIONES AUXILIARES INTERFAZ
# < -------------------------------------------------------------------------- >

def tiempo():
    """Milisegundos (entero) desde inicio del programa"""
    return round(pygame.time.get_ticks())

def ayuda():
    """Muestra un pequeño rectángulo con información de ayuda y las info asociada a cada producto cuando el ratón esta sobre su botón"""
    x, y = g_raton
    pos = (x - 80, y + 20)
    fuente = fuentes[AYUDA_TAMANO]
    dim = fuente.size(texto_ayuda)
    pygame.draw.rect(g_pantalla, AYUDA_COLOR, pos + dim)
    texto(texto_ayuda, pos, AYUDA_TAMANO)

def texto(
        cadena,
        posicion,
        tamaño    = TEXTO_TAMANO,
        color     = COLOR_TEXTO,
        alineado  = 'i',
        negrita   = False,
        cursiva   = False,
        subrayado = False,
        mono      = False,
        surface   = g_pantalla
    ):
    """Escribir un texto en la pantalla"""
    # Aseguramos que el tamaño de fuente deseado esta disponible
    if not tamaño in TEXTO_TAMANOS:
        tamaño = TEXTO_TAMANO

    # Ajustamos la posicion para respetar el alineado
    fuente = fuentes_mono[tamaño] if mono else fuentes[tamaño]
    longitud = fuente.size(cadena)[0]
    x = posicion[0] - (longitud if alineado == 'd' else longitud / 2 if alineado == 'c' else 0)
    y = posicion[1]

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
        tamaño    = TEXTO_TAMANO,
        color     = COLOR_TEXTO,
        alineado  = 'i',
        negrita   = False,
        cursiva   = False,
        subrayado = False,
        mono      = False,
        surface   = g_pantalla,
        pagina    = 1,
        max_ancho = 200,
        max_alto  = 20
    ):
    """
    Permite dividir el texto, producir saltos de línea y tabulaciones
    Devuelve un booleano que indica si faltan paginas por dibujar
    """
    if not tamaño in TEXTO_TAMANOS:
        tamaño = TEXTO_TAMANO
    fuente = fuentes_mono[tamaño] if mono else fuentes[tamaño]
    x, y = posicion
    lineas = dividir_texto(cadena.replace('\t', '    '), fuente, max_ancho)
    paginas = math.ceil(len(lineas) / max_alto)
    pagina = min(max(0, pagina), paginas - 1)
    for linea in lineas[max_alto * pagina : max_alto * (pagina + 1)]:
        texto(linea, (x, y), tamaño, color, alineado, negrita, cursiva, subrayado, mono, surface)
        y += fuente.get_linesize()
    return pagina < paginas - 1

# < -------------------------------------------------------------------------- >
#                       ACTUALIZACION DEL ESTADO DEL JUEGO
# < -------------------------------------------------------------------------- >

def comprar(medio):
    """"Ejecuta la acción de comprar un producto"""
    global credito
    if credito < medio.PRECIO:
        g_sonidos['error'].play()
        return
    g_sonidos['dinero'].play()
    inventario[medio] += 1
    g_botones[medio].indice += 1
    credito -= medio.PRECIO

def actualizar_fondo():
    """Dibujar el fondo (primera capa del display)"""
    g_pantalla.fill(COLOR_FONDO)

def actualizar_paneles():
    """Actualizar el contenido de cada panel"""
    for panel in paneles.values():
        panel.dibujar()
    for boton in g_botones.values():
        boton.actualizar()
        boton.dibujar()

def actualizar_textos():
    """Actualizar textos en pantalla"""
    texto(f"Crédito: {credito}M", (ANCHURA * ANCHURA_JUEGO + sep, sep), 24)
    texto('Tienda', (ANCHURA * (ANCHURA_JUEGO + 1) / 2, 65), 24, alineado = 'c', subrayado = True)
    g_info.dibujar()

def actualizar_escenario():
    g_escenario.raton()
    g_escenario.dibujar()

def siguiente_fotograma():
    """Avanzar fotograma"""
    pygame.display.flip() # Renderizar fotograma en pantalla y cambiar buffer
    clock.tick(FPS)       # Avanzar reloj y limitar frecuencia de fotogramas

def siguiente_fase():
    """Avanzar a la siguiente fase del juego"""
    global g_fase
    if g_fase < Fase.FINAL:
        g_fase += 1
    else:
        g_fase = Fase.PANTALLAZO

def actualizar_variables():
    """Actualizacion de variables en cada fotograma"""
    global texto_ayuda, g_raton
    texto_ayuda = None
    g_info.borrar()
    g_raton = pygame.mouse.get_pos()

def actualizar_fase_pantallazo():
    """Dibujar pantallazo inicial"""
    x = (g_pantalla.get_width() - imagen_pantallazo.get_width()) / 2
    y = (g_pantalla.get_height() - imagen_pantallazo.get_height()) / 2
    g_pantalla.blit(imagen_pantallazo, (x, y))

def actualizar_fase_reglas():
    """Dibujar pantallazo reglas"""
    g_reglas.actualizar()
    g_reglas.dibujar()

def actualizar_fase_turnos():
    """Actualizar estado en la fase de turnos"""
    actualizar_paneles()
    actualizar_textos()
    actualizar_escenario()
    if texto_ayuda:
        ayuda()
    if g_mostrar_reglas:
        actualizar_fase_reglas()

# < -------------------------------------------------------------------------- >
#                           INICIALIZACIÓN DEL JUEGO
# < -------------------------------------------------------------------------- >

# Comenzar musica
if MUSICA_REPRODUCIR:
    pygame.mixer.music.play(-1)

# Inicializar variables básicas
credito = CREDITO_INICIAL
productos  = [
    AvionCaza, AvionAtaque, AvionTransporte, Helicoptero, Dron, Radar, Bateria, Inteligencia, Infraestructura]
inventario = { producto: 0 for producto in productos }

# Configurar paneles
sep = PANEL_SEPARACION
paneles = {
    'escenario':   Panel((sep, sep), (ANCHURA * ANCHURA_JUEGO - 1.5 * sep, ALTURA * ALTURA_JUEGO - 1.5 * sep), 'escenario'),
    'acciones':    Panel((ANCHURA * ANCHURA_JUEGO + sep / 2, sep), (ANCHURA * ANCHURA_ACCIONES - 1.5 * sep, ALTURA * ALTURA_ACCIONES - 1.5 * sep)),
    'informacion': Panel((sep, ALTURA * ALTURA_JUEGO + sep / 2), (ANCHURA - 2 * sep, ALTURA * ALTURA_INFORMACION - 1.5 * sep), 'información')
}

# Configurar botones
g_botones = { producto: None for producto in productos }
cols = 2
i = 0
x0 = ANCHURA * ANCHURA_JUEGO + 20
y0 = 100
x = x0
y = y0
for producto in productos:
    g_botones[producto] = Boton((x, y), imagen=producto.ICONO, ayuda=producto.ayuda(), info=producto.info(), indice=0, accion=comprar, args=(producto,))
    x = x + g_botones[producto].dim[0] + 5 if i % cols < cols - 1 else x0
    y += g_botones[producto].dim[1] + 5 if i % cols == cols - 1 else 0
    i += 1

# Inicializar escenario (casillas y su contenido)
g_escenario = Escenario(paneles['escenario'])

# Inicializar clases informativas
g_info = Informacion(paneles['informacion'])
g_reglas = Reglamento()

# Inicializar juego en la primera fase
g_fase = Fase.PANTALLAZO

# Estado
g_raton = pygame.mouse.get_pos()
g_click = False
g_mostrar_reglas = False

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
    if g_fase == Fase.PANTALLAZO:       # Pantallazo inicial
        actualizar_fase_pantallazo()
        if g_click:
            g_mostrar_reglas = True
            siguiente_fase()
    elif g_fase == Fase.REGLAS:         # Pantallazo de reglas
        actualizar_fase_reglas()
        if not g_mostrar_reglas:
            siguiente_fase()
    elif g_fase == Fase.TURNOS:         # Fase central del juego
        actualizar_fase_turnos()
    else:
        pass

    siguiente_fotograma()