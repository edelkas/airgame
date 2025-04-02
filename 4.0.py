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

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

import random


# < -------------------------------------------------------------------------- >
#                            CONSTANTES GLOBALES
# < -------------------------------------------------------------------------- >

# Constantes generales del juego
NOMBRE_JUEGO    = "AIR GAME"
NOMBRE_DEFECTO  = "Jugador"
CREDITO_INICIAL = 500

# Precios de productos
PRECIO_AVO_CAZA         =  50
PRECIO_AVO_ATAQUE       =  60
PRECIO_AVO_TRANSPORTE   = 120
PRECIO_HELICOPTERO      =  21
PRECIO_DRON             =  25
PRECIO_RADAR            =  24
PRECIO_BATERIA          =  90
PRECIO_INTELIGENCIA     =  50
PRECIO_INFRAESTRUCTURA  = 100

# Características generales de la interfaz
ANCHURA                         = 1280           # Anchura de la ventana en pixeles
ALTURA                          = 720            # Altura de la ventana en pixeles
PANTALLA_COMPLETA               = False          # Para abrir el juego en ventana completa
PANTALLA_MODIFICARDIMENSION     = False          # Para poder modificar la dimensión de la ventana
FPS                             = 60             # Fotogramas por segundo
COLOR_FONDO                     = (96, 130, 182) # Color RGB del fondo de pantalla

# Propiedades del texto
COLOR_TEXTO        = (0, 0, 0)                  # Color RGB por defecto del texto
TEXTO_FUENTE       = "CENTURY GOTHIC"           # Fuente de los textos
TEXTO_TAMANOS      = [16, 20, 24, 36, 72, 180]  # Tamaños de fuente que se usaran
TEXTO_TAMANO       = 24                         # Tamaño de fuente por defecto

# Propiedades generales de todos los paneles, por defecto
PANEL_BORDE_COLOR  = (54, 69, 79)    # Color del borde de los paneles
PANEL_INT_COLOR    = (229, 228, 226) # Color del interior de los paneles
PANEL_BORDE_GROSOR = 2               # Grosor del borde (0 = sin borde)
PANEL_BORDE_RADIO  = 5               # Radio de las esquinas circulares
PANEL_SEPARACION   = 5               # Separacion entre paneles

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
MUSICA_FONDO = "topgunmusic.ogg"
IMAGEN_FONDO = "imagenairgame.png"

# Pantallazo
PANTALLAZO_COLOR_FONDO = '#325320' # Color de fondo del panel del pantallazo
PANTALLAZO_COLOR_TEXTO = '#000000' # Color de fondo del panel del pantallazo
PANTALLAZO_TIEMPO = 5000           # Tiempo que dura el pantallazo inicial en ms

# Pantallazo reglas
PANTALLAZO_REGLAS_COLOR_FONDO = (229, 228, 226) # Color de fondo del panel del pantallazo reglas
PANTALLAZO_REGLAS_COLOR_TEXTO = '#000000'       # Color de fondo del panel del pantallazo reglas
PANTALLAZO_REGLAS_TIEMPO = 10000                # Tiempo en el que desaparecera el pantallazo reglas en ms


indice_reglas = 0
REGLAS_LISTA = [
    "\n\nAIRGAME es un juego de estrategia basado en medios militares aéreos. El objetivo del juego es obtener mayor superioridad aérea que el oponente. Dicha superioridad se conseguirá mediante el empleo de diversas aeronaves y medios a lo largo del tablero establecido.\
    \n\n¿Cómo se consigue la superioridad aérea?\
    \nDurante el desarrollo del juego, la superioridad aérea (Sup.A) se conseguirá al desplegar aeronaves a lo largo del tablero. Cada medio aéreo posee un coeficiente de Sup.A que se hará efectivo cuando permanezca en una casilla determinada.\
    \nEjemplo: Si una aeronave del jugador 1(J1) con coeficiente de Sup.A = 5, permanece durante dos turnos en una casilla, a esta se le sumarán 10 puntos de Sup.A de J1. (5 Sup.A x 2 turnos = 10)\
    \n\nAl inicio del juego, cada casilla tendrá asociada un coeficiente de Sup.A de casilla y otro actual:\
        \n\t-Coeficiente de superioridad de casilla: Indica que Sup.A hay que ejercer en dicha casilla para obtener la Sup.A.\
        \n\t-Coeficiente de superioridad actual: Indica la Sup.A que actualmente está ejerciendo un jugador.\
    \nEjemplo: Una casilla está definida por [10 / 6 (J2)] (10 es el coeficiente de Sup.A de casilla y 6 el actualmente ejercido por el J2). Si como en el ejemplo anterior, una aeronave de J1 permanece 2 turnos en dicha casilla la casilla estará definida por [10 / 4 (J1)]. Si la misma aeronave es capaz de estar cuatro turnos en dicha casilla, J1 obtendrá la Sup.A en dicha casilla ya que el nivel de Sup.A actual de J1 es superior al de la casilla [10 / 14 (J1)].\
    \n\nExistirán 2 tipos de superioridad aérea, tal y como describe la NATO en el AJP 3.3.:\
        \n\t-Superioridad aérea (Sup.A): Grado de dominación que permite dirigir operaciones en un momento y lugar dado sin que la interferencia enemiga sea prohibitiva para el desarrollo de las mismas. Se conseguirá cuando el coeficiente de Sup.A de un jugador sea igual o mayor al de la casilla.\
        \n\t-Supremacía aérea (Supre.A): Grado donde la fuerza aérea enemiga es incapaz de interferir efectivamente a las operaciones propias. Se conseguirá cuando el coeficiente de Sup.A de un jugador sea igual al doble o mayor al de la casilla. Obtener la Supre.A de una casilla permite al jugador poder crear una ciudad o una base en dicha casilla.\
    \n\nEn el juego también tendrá presencia el estado de igualdad aérea, en el caso de que ninguno de los jugadores posea superioridad aérea.\
    \n\nEn la primera pantalla aparecerá el tablero de juego, la tienda de productos y el panel de información.\
        \n\t-Tablero de juego: Esta formado por casillas hexagonales. Existen diferentes tipos de casillas en función de su desempeño en el juego, diferenciándose en su color y en los coeficientes asociados a sus características:\
            \n\t\t[AZUL] Territorio 1: Casillas en propiedad del jugador 1.\
			    \n\t\t\t-Coeficiente de Sup.A de casilla: 20\
            \n\t\t[NARANJA] Territorio 2: Casillas en propiedad del jugador 2.\
	            \n\t\t\t-Coeficiente de Sup.A de casilla: 20\
            \n\t\t[NEGRA (AZUL/NARANJA)] Ciudad: Casilla que da al jugador recursos cuando es de su propiedad.\
	            \n\t\t\t-Coeficiente de Sup.A de casilla: 40\
                \n\t\t\t-Coeficiente de desarrollo: Nivel de infraestructura alcanzado. Cada ciudad otorgará al jugador (5M x nivel) de la ciudad en cada turno.\
            \n\t\t[VERDE (AZUL/NARANJA)] Base aérea: Casilla desde la que se despliegan los medios. Cada base podrá desplegar tantos medios como alto sea su nivel.\
	            \n\t\t\t-Coeficiente de Sup.A de casilla: 60\
                \n\t\t\t-Coeficiente de movilidad aérea: Nivel de infraestructura alcanzado. Desde cada base se podrán desplegar tantas aeronaves como nivel tenga la base.\
            \n\t\t[DORADO(AZUL/NARANJA)] Capital: Ciudad más importante de cada jugador. Si el adversario consigue obtener supremacía aérea en dicha casilla, gana la partida.\
	            \n\t\t\t-Coeficiente de Sup.A de casilla: 100\
	            \n\t\t\t-Coeficiente de desarrollo: Nivel de infraestructura alcanzado.\
    \n\n-Tienda de productos: Aparecen los 9 productos disponibles en el juego con una serie de características asociadas:\
		    \n\t-Medios aéreos:\
                \n\t\t[AVO. CAZA]: Único medio aéreo que puede atacar otros medios aéreos. El otro medio anti aéreo que puede hacerlo es la batería antiaérea.\
                \n\t\t[AVO. ATAQUE]: Medio aéreo capaz de atacar medios anti aéreos.\
                \n\t\t[AVO. TRANSPORTE]: Medio aéreo con más alcance.\
                \n\t\t[HELICÓPTERO]: Único medio aéreo capaz de aterrizar en una casilla que no sea una base. Además es capaz de atacar medios anti aéreos.\
                \n\t\t[DRON]: Único medio aéreo con capacidad de vigilancia y con mayor autonomía, además es capaz de atacar medios anti aéreos.\
		\n\t-Medios anti aéreos:\
            \n\t\t[RADAR]: Medio antiaéreo con el mayor alcance de vigilancia.\
            \n\t\t[BATERÍA ANTIAÉREA]: Único medio antiaéreo con capacidad de atacar medios aéreos además de tener capacidad de vigilancia.\
		\n\t-Medios estratégicos:\
            \n\t\t[INTELIGENCIA]: Medio estratégico que permite obtener diversa información sobre el adversario.\
            \n\t\t[INFRAESTRUCTURA]: Medio estratégico que permite aumentar el nivel de las ciudades y bases propias.\
    \n\n-Panel de información: En el aparecerá la información correspondiente al elemento que en ese momento este indicando el ratón. Además de una breve descripción de cada producto aparecerá la siguiente información dependiendo de si se tratan de medios aéreos, anti aéreos o estratégicos:\
		    \n\t-Medios aéreos y anti aéreos:\
			\n\t\t[COSTE]: precio del medio (€)\
            \n\t\t[VELOCIDAD]: velocidad a la que va a poder avanzar por las casillas un producto / (km/h) - (casillas/turno).\
			\n\t\t[AUTONOMÍA]: tiempo que va a poder estar fuera de la base un producto / (horas) - (turnos).\
			\n\t\t[ALCANCE]: distancia (horizontal) a la que va a poder llegar un producto / (km) - (casillas).\
			\n\t\t[HUELLA]: probabilidad de ser captado por una vigilancia 100% / (%).\
			\n\t\t[AIRE]: distancia a la que puede derribar un medio aéreo / (casillas).\
			\n\t\t[SUP]: distancia a la que puede derribar un medio antiaéreo / (casillas).\
			\n\t\t[VIGILANCIA]: probabilidad de captar un producto con huella radar 100% / (%).\
			\n\t\t[RADIOVIG.]: distancia a la que puede vigilar otro producto / (km) - (casillas).\
			\n\t\t[SUPAEREA]: peso de cada producto a la hora de aportar superioridad aérea / (número).\
		    \n\t-Medios estratégicos:\
			\n\t\t[INTELIGENCIA]:\
			    \n\t\t\t(NIVEL 1): Da la posición de una de las ciudades del oponente.\
			    \n\t\t\t(NIVEL 2): Da la posición de todas las ciudades del oponente.\
			    \n\t\t\t(NIVEL 3): Da la posición de la capital del oponente.\
			    \n\t\t\t(NIVEL 4): Da el nivel de las ciudades y bases del oponente.\
			    \n\t\t\t(NIVEL 5):  Da información sobre el número de medios de los que dispone el oponente.\
			\n\t\t[INFRAESTRUCTURA]: este medio estratégico podrá ser ejercido en las siguientes casillas:\
			    \n\t\t\t(CASILLA CON SUPREMACÍA AÉREA): Se creará una ciudad o una base de nivel 1.\
			    \n\t\t\t(CIUDAD): Cada nivel de mejora proporcionará más recursos al jugador / 10M x Nivel de ciudad.\
			    \n\t\t\t(BASE): El nivel de la base determinará el número de medios que se pueden mover de dicha base / 1 medio x Nivel de la base.\
    \n\nA continuación el jugador deberá elegir en que casillas colocar las ciudades, las bases aéreas y los medios comprados:\
        \n\t[CIUDADES Y BASES AÉREAS]: Deberán ser colocados en casillas con supremacía aérea del propio jugador.\
            \n\t\t-Al inicio de la partida el jugador contará con 3 ciudades y 3 bases aéreas que podrá colocar en las casillas en las que posee supremacía aérea.\
        \n\t[MEDIOS AÉREOS]: Deberán ser colocados en bases aéreas.\
        \n\t[MEDIOS ANTIAÉREOS]: Deberán ser colocados en casillas con superioridad aérea del propio jugador.\
    \nLa dinámica principal del juego se basa en turnar una serie de acciones entre los jugadores. Estas acciones serán:\
        \n\t-Recibir reporte del movimiento del adversario:\
            \n\t\t[Ataque del enemigo ]: Derribo, destrucción o fracasos de ataques sobre medios propios.\
            \n\t\t[Conquista de casillas]: En el caso de que el enemigo haya conseguido variar el estado de superioridad aérea de una casilla esta cambiara de color dependiendo de su estado actual.\
            \n\t\t[Captación de medios del enemigo]: Captación de medios enemigos por radares, baterías y drones propios.\
        \n\t-Recibir ingresos: Los ingresos que se recibirán serán los siguiente:\
	        \n\t\t[500M]: Al inicio de la partida.\
            \n\t\t[10M x ciudad x nivel de la ciudad]: Al principio de cada turno.\
        \n\t-Recibir inteligencia: La inteligencia recibida dependerá de su nivel.\
        \n\t-Invertir ingresos: El crédito disponible podrá ser gastado en los productos disponibles en la tienda.\
        \n\t-Movilizar aeronaves: A la hora de movilizar aeronaves hay que tener una serie de aspectos en cuenta:\
            \n\t\t[Capacidad de despliegue]: Cada base aérea podrá tener desplegados en un mismo turno tantos medios aéreos como nivel tenga.\
            \n\t\t[Despegue y aterrizaje en la misma base aérea]: Todas las aeronaves deberán despegar y aterrizar en la misma base aérea. Excepto el helicóptero y el avión de transporte.\
            \n\t\t[Caso especial, helicóptero]: Puede aterrizar y despegar en cualquier casilla. Solo ejercerá superioridad aérea cuando este en vuelo. Hasta que este no retorne a la base aérea desde la que despegó contará como medio aéreo desplegado para dicha base.\
            \n\t\t[Caso especial, avión de transporte]: Puede aterrizar y despegar en cualquier base aérea amiga o ciudad, ya se amiga o enemiga. Solo ejercerá superioridad aérea cuando este en vuelo. Hasta que este no retorne a la base aérea desde la que despegó contará como medio aéreo desplegado para dicha base.\
            \n\t\t[Alcance]: Cada aeronave tiene un alcance de casillas que es inversamente proporcional al tiempo de permanencia (turnos) que queremos que este en la casilla seleccionada. Es decir, cuanto más lejos queremos que llegue, menos tiempo podrá permanecer en dicha casilla.\
            \n\t\t[Permanencia]: Cada aeronave podrá permanecer un número determinado de turnos en la casilla seleccionada dependiendo del alcance al que se haya querido movilizar a la aeronave.\
            \n\t\t[Conquista por parte del rival de una base aérea]: Si el oponente es capaz de conseguir la superioridad aérea de una base, tanto los medios desplegados como los medios que estén en la propia base sin desplegar, serán derribados y por lo tanto eliminados del juego.\
        \n\t-Ataque: Las aeronaves con capacidad de ataque, ya sea aire-aire o aire-suelo que estén en el aire podrán atacar a una casilla en cada turno que estén en el aire. Dicho ataque será visualizado por el oponente, es decir el adversario podrá ver que casilla ha sido atacada y si ha sido un ataque aire-aire o aire-suelo. Si el ataque ha sido certero los medios aéreos (ataque aire-aire) o antiaéreos (aire-suelo) serán destruidos.\
    \nEl juego finalizará cuando se cumpla uno de los siguientes requisitos:\
        \n\t-Jx obtenga Supre.A en la capital del adversario. Gana Jx.\
        \n\t-Jx obtenga Sup.A en todas las ciudades y la capital del adversario. Gana Jx.\
        \n\t-(Jx) obtenga Sup.A en todas las bases del adversario. Gana Jx.\
        \n\t-Se acabe el número de rondas establecido previamente por los jugadores. Gana el jugador que sume más puntos de coeficiente de Sup.A."
    ]

REGLAS = REGLAS_LISTA[indice_reglas]

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
pantalla = pygame.display.set_mode((ANCHURA, ALTURA), flags)
clock = pygame.time.Clock()
texto_ayuda = None
texto_info  = None
texto_coste = None
texto_velocidad = None
texto_autonomia = None
texto_alcance = None
texto_huella = None
texto_aire = None
texto_sup = None
texto_vigilancia = None
texto_radiovig = None
texto_supaerea = None

# Cargar recursos
pygame.mixer.init()
pygame.mixer.music.load(MUSICA_FONDO)
SONIDO_DINERO = pygame.mixer.Sound("cajaregistradora.ogg")
SONIDO_ERROR = pygame.mixer.Sound("error.ogg")
imagen_pantallazo = cargar_imagen(IMAGEN_FONDO)
fuentes = { tam: pygame.font.SysFont(TEXTO_FUENTE, tam) for tam in TEXTO_TAMANOS}
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

# < -------------------------------------------------------------------------- >
#                              CLASES DEL JUEGO
# < -------------------------------------------------------------------------- >

class Producto:
    """Clase genérica que representa cualquier cosa comprable"""
    def __init__(self, nombre, precio, icono, info, coste, velocidad, autonomia, alcance, huella, aire, sup, vigilancia, radiovig, supaerea):
        self.nombre     = nombre
        self.precio     = precio
        self.icono      = icono
        self.info       = info
        self.coste      = coste
        self.velocidad  = velocidad
        self.autonomia  = autonomia
        self.alcance    = alcance
        self.huella     = huella
        self.aire       = aire
        self.sup        = sup
        self.vigilancia = vigilancia
        self.radiovig   = radiovig
        self.supaerea   = supaerea

class Medio(Producto):
    """Representa cualquier medio militar"""

    @classmethod
    def ayuda(cls):
        return {
            'help':       "%s (%dM)" % (cls.nombre, cls.precio),
            'info':       cls.info,
            'coste':      cls.coste,
            'velocidad':  cls.velocidad,
            'autonomia':  cls.autonomia,
            'alcance':    cls.alcance,
            'huella':     cls.huella,
            'aire':       cls.aire,
            'sup':        cls.sup,
            'vigilancia': cls.vigilancia,
            'radiovig':   cls.radiovig,
            'supaerea':   cls.supaerea,
        }

class MedioAereo(Medio):
    """Representa cualquier medio aéreo"""

class MedioAntiaereo(Medio):
    """Representa cualquier medio anti-aéreo"""

class MedioEstrategico(Medio):
    """Representa cualquier medio estratégico"""

class AvionCaza(MedioAereo):
    """Representa un avión de caza"""
    nombre      = "Avo. Caza"
    precio      = PRECIO_AVO_CAZA
    icono       = iconos['AvionCaza']
    info        = 'Único medio aéreo que puede atacar otros medios aéreos. El otro medio que puede hacerlo es la batería antiaérea.'
    coste       = '50'
    velocidad   = '2100'
    autonomia   = '1.62'
    alcance     = '3400'
    huella      = '4'
    aire        = '170'
    sup         = '0'
    vigilancia  = '0'
    radiovig    = '0'
    supaerea    = '10'
class AvionAtaque(MedioAereo):
    """Representa un avión de ataque"""
    nombre      = "Avo. Ataque"
    precio      = PRECIO_AVO_ATAQUE
    icono       = iconos['AvionAtaque']
    info        = 'Medio aéreo capaz de atacar medios anti aéreos.'
    coste       = '65'
    velocidad   = '1350'
    autonomia   = '5,04'
    alcance     = '6800'
    huella      = '15'
    aire        = '0'
    sup         = '240'
    vigilancia  = '0'
    radiovig    = '0'
    supaerea    = '6'
class AvionTransporte(MedioAereo):
    """Representa un avión de transporte"""
    nombre      = "Avo. Transporte"
    precio      = PRECIO_AVO_TRANSPORTE
    icono       = iconos['AvionTransporte']
    info        = 'Medio aéreo con más alcance.'
    coste       = '120'
    velocidad   = '820'
    autonomia   = '12,93'
    alcance     = '10600'
    huella      = '60'
    aire        = '0'
    sup         = '0'
    vigilancia  = '0'
    radiovig    = '0'
    supaerea    = '3'

class Helicoptero(MedioAereo):
    """Representa un helicóptero"""
    nombre      = "Helicóptero"
    precio      = PRECIO_HELICOPTERO
    icono       = iconos['Helicoptero']
    info        = 'Único medio aéreo capaz de aterrizar en una casilla que no sea una base. Además es capaz de atacar medios anti aéreos.'
    coste       = '21'
    velocidad   = '260'
    autonomia   = '2,58'
    alcance     = '670'
    huella      = '10'
    aire        = '0'
    sup         = '10'
    vigilancia  = '0'
    radiovig    = '0'
    supaerea    = '4'
    
class Dron(MedioAereo):
    """Representa un dron"""
    nombre      = "Dron"
    precio      = PRECIO_DRON
    icono       = iconos['Dron']
    info        = 'Único medio aéreo con capacidad de vigilancia y con mayor autonomía, además es capaz de atacar medios anti aéreos.'
    coste       = '25'
    velocidad   = '240'
    autonomia   = '13,5'
    alcance     = '3240'
    huella      = '2'
    aire        = '0'
    sup         = '100'
    vigilancia  = '20'
    radiovig    = '240'
    supaerea    = '2'

class Radar(MedioAntiaereo):
    """Representa un radar"""
    nombre      = "Radar"
    precio      = PRECIO_RADAR
    icono       = iconos['Radar']
    info        = 'Medio antiaéreo con el mayor alcance de vigilancia.'
    coste       = '24'
    velocidad   = '0'
    autonomia   = '0'
    alcance     = '0'
    huella      = '100'
    aire        = '0'
    sup         = '0'
    vigilancia  = '90'
    radiovig    = '440'
    supaerea    = '0'

class Bateria(MedioAntiaereo):
    """Representa una batería anti-aérea"""
    nombre      = "Batería"
    precio      = PRECIO_BATERIA
    icono       = iconos['Bateria']
    info        = 'Único medio antiaéreo con capacidad de vigilancia.'
    coste       = '90'
    velocidad   = '0'
    autonomia   = '0'
    alcance     = '0'
    huella      = '100'
    aire        = '240'
    sup         = '0'
    vigilancia  = '60'
    radiovig    = '260'
    supaerea    = '0'

class Inteligencia(MedioEstrategico):
    """Clase genérica para representar inteligencia"""
    nombre      = "Inteligencia"
    precio      = PRECIO_INTELIGENCIA
    icono       = iconos['Inteligencia']
    info        = 'Medio estratégico que permite obtener diversa información sobre el adversario.'
    coste       = '-'
    velocidad   = '-'
    autonomia   = '-'
    alcance     = '-'
    huella      = '-'
    aire        = '-'
    sup         = '-'
    vigilancia  = '-'
    radiovig    = '-'
    supaerea    = '-'

class Infraestructura(MedioEstrategico):
    """Clase genérica que representa una infraestructura"""
    nombre      = "Infraestructura"
    precio      = PRECIO_INFRAESTRUCTURA
    icono       = iconos['Infraestructura']
    info        = 'Medio estratégico que permite aumentar el nivel de las ciudades y las bases propias.'
    coste       = '-'
    velocidad   = '-'
    autonomia   = '-'
    alcance     = '-'
    huella      = '-'
    aire        = '-'
    sup         = '-'
    vigilancia  = '-'
    radiovig    = '-'
    supaerea    = '-'

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
            surface     = pantalla            # Superficie donde dibujar panel
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
            texto(self.nombre.capitalize(), (self.pos[0] + self.dim[0] / 2, self.pos[1]), 24, alineado = 'c', subrayado = True, surface=self.surface)

class Boton:
    """Clase que representa un boton clickable"""
    def __init__(self, pos, texto=None, imagen=None, ayuda=None, info=None, coste=None, velocidad=None, autonomia=None, alcance=None, huella=None, aire=None, sup=None, vigilancia=None, radiovig=None, supaerea=None, accion=None, args=()):
        if not texto and not imagen:
            return
        self.pos = pos            # Posición del botón en pantalla
        self.ayuda = ayuda        # Pequeña descripción del botón, para cuando es seleccionado
        self.info = info          # Descripción más detallada del botón seleccionado
        self.coste = coste
        self.velocidad = velocidad
        self.autonomia = autonomia
        self.alcance = alcance
        self.huella = huella
        self.aire = aire
        self.sup = sup
        self.vigilancia = vigilancia
        self.radiovig = radiovig
        self.supaerea = supaerea
        self.accion = accion      # Función a ejecutar si el botón es pulsado
        self.args = args          # Argumentos que mandar a la función acción, si son necesarios
        self.indice = 0           # Pequeño número que aparezca en la esquina del botón

        # Calculamos el tamaño del boton
        if texto:
            self.texto = texto
            fuente = fuentes[BOTON_TAMANO_LETRA]
            self.imagen = fuente.render(texto, True, (0, 0, 0))
        else:
            self.imagen = imagen
        x, y = self.imagen.get_size()
        self.dim = (x + 2, y + 2) # Dimensiones del botón

        # Logica
        self.selec = False        # Verdadero si el ratón está encima del botón
        self.pulsado = False      # Verdadero si el botón está siendo pulsado

        # Otros elementos
        self.panel = Panel(self.pos, self.dim, None, BOTON_COLOR_NORMAL)

    def raton(self, pos):
        """Detecta si el ratón está sobre el botón"""
        return self.panel.rect.collidepoint(pos)

    def actualizar(self):
        """Actualizar estado y propiedades del boton"""
        # Actualizar color
        if self.pulsado:
            self.panel.color = BOTON_COLOR_PULSA
        elif self.selec:
            self.panel.color = BOTON_COLOR_SOBRE
        else:
            self.panel.color = BOTON_COLOR_NORMAL

        # Ejecutar acción si está pulsado
        if self.pulsado:
            self.accion(*self.args)

    def dibujar(self):
        """Renderizar el boton en pantalla"""
        global texto_ayuda
        global texto_info
        global texto_coste
        global texto_velocidad
        global texto_autonomia
        global texto_alcance
        global texto_huella
        global texto_aire
        global texto_sup
        global texto_vigilancia
        global texto_radiovig
        global texto_supaerea

        self.panel.dibujar()
        pantalla.blit(self.imagen, self.pos)
        fuente = fuentes[AYUDA_TAMANO]
        x, y = self.pos
        w1, h1 = self.dim
        w2, h2 = fuente.size(str(self.indice))
        texto(str(self.indice), (x + w1 - 2, y + h1 - h2), AYUDA_TAMANO, (0, 0, 0), 'd')
        if self.selec and self.ayuda:
            texto_ayuda = self.ayuda
        if self.selec and self.info:
            texto_info = self.info
        if self.selec and self.coste:
            texto_coste = self.coste
        if self.selec and self.velocidad:
            texto_velocidad = self.velocidad
        if self.selec and self.autonomia:
            texto_autonomia = self.autonomia
        if self.selec and self.alcance:
            texto_alcance = self.alcance
        if self.selec and self.huella:
            texto_huella = self.huella
        if self.selec and self.aire:
            texto_aire = self.aire
        if self.selec and self.sup:
            texto_sup = self.sup
        if self.selec and self.vigilancia:
            texto_vigilancia = self.vigilancia
        if self.selec and self.radiovig:
             texto_radiovig = self.radiovig
        if self.selec and self.supaerea:
            texto_supaerea = self.supaerea

# < -------------------------------------------------------------------------- >
#                         FUNCIONES AUXILIARES INTERFAZ
# < -------------------------------------------------------------------------- >

def tiempo():
    return pygame.time.get_ticks()

def ayuda():
    """Muestra un pequeño rectángulo con información de ayuda y las info asociada a cada producto cuando el ratón esta sobre su botón"""
    x, y = pygame.mouse.get_pos()
    pos = (x - 80, y + 20)
    fuente = fuentes[AYUDA_TAMANO]
    dim = fuente.size(texto_ayuda)
    pygame.draw.rect(pantalla, AYUDA_COLOR, pos + dim)
    texto(texto_ayuda, pos, AYUDA_TAMANO)
    texto(texto_info, (sep*5, 510), 16)
    texto(texto_coste, (40, 580), 16)
    texto(texto_velocidad, (160, 580), 16)
    texto(texto_autonomia, (310, 580), 16)
    texto(texto_alcance, (440, 580), 16)
    texto(texto_huella, (560, 580), 16)
    texto(texto_aire, (680, 580), 16)
    texto(texto_sup, (800, 580), 16)
    texto(texto_vigilancia, (930, 580), 16)
    texto(texto_radiovig, (1060, 580), 16)
    texto(texto_supaerea, (1190, 580), 16)
    texto('  COSTE              VELOCIDAD           AUTONOMÍA           ALCANCE             HUELLA             AIRE-AIRE           AIRE-SUP             VIGILANCIA          RADIO VIGIL.         SUP.AÉREA', (sep*3, 550), 16, alineado = 'l' )


def texto(
        cadena,
        posicion,
        tamaño    = TEXTO_TAMANO,
        color     = COLOR_TEXTO,
        alineado  = 'i',
        negrita   = False,
        cursiva   = False,
        subrayado = False,
        surface   = pantalla
    ):
    """Escribir un texto en la pantalla"""
    # Aseguramos que el tamaño de fuente deseado esta disponible
    if not tamaño in TEXTO_TAMANOS:
        tamaño = TEXTO_TAMANO

    # Ajustamos la posicion para respetar el alineado
    fuente = fuentes[tamaño]
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
        tamaño=TEXTO_TAMANO,
        color=COLOR_TEXTO,
        alineado='i',
        negrita=False,
        cursiva=False,
        subrayado=False,
        surface=None,
        max_ancho=200
    ):
    """Permite dividir el texto, producir saltos de línea y tabulaciones"""
    pygame.font.init()
    # Cargar la fuente "Century Gothic"
    fuente = pygame.font.SysFont('Century Gothic', tamaño)
    fuente.set_bold(negrita)
    fuente.set_italic(cursiva)
    fuente.set_underline(subrayado)

    # Asegurarse de que 'cadena' sea una cadena de texto
    if not isinstance(cadena, str):
        cadena = str(cadena)

    lineas = dividir_texto(cadena.replace('\t', '    '), fuente, max_ancho)
    x, y = posicion

    for linea in lineas:
        texto_renderizado = fuente.render(linea, True, color)
        texto_rect = texto_renderizado.get_rect()

        if alineado == 'c':
            texto_rect.center = (x + max_ancho // 2, y)
        elif alineado == 'i':
            texto_rect.topleft = (x, y)
        elif alineado == 'd':
            texto_rect.topright = (x + max_ancho, y)
        surface.blit(texto_renderizado, texto_rect)
        y += fuente.get_height()





# < -------------------------------------------------------------------------- >
#                       ACTUALIZACION DEL ESTADO DEL JUEGO
# < -------------------------------------------------------------------------- >

def comprar(medio):
    """"Ejecuta la acción de comprar un producto"""
    global credito
    if credito < medio.precio:
        SONIDO_ERROR.play()
        return
    SONIDO_DINERO.play()
    inventario[medio] += 1
    botones[medio].indice += 1
    credito -= medio.precio

def analizar_raton(click):
    """Según la posición del ratón, ver si tenemos que realizar alguna acción"""
    pos = pygame.mouse.get_pos()

    # Cambiar estado de los botones (seleccionado y/o pulsado, si procede)
    for boton in botones.values():
        sel = boton.raton(pos)
        boton.selec = sel
        boton.pulsado = sel and click

def actualizar_pantallazo():
    """Dibujar pantallazo inicial"""
    x = (pantalla.get_width() - pantallazo.get_width()) / 2
    y = (pantalla.get_height() - pantallazo.get_height()) / 2
    pantalla.blit(pantallazo, (x, y))

def actualizar_pantallazo_reglas():
    """Dibujar pantallazo reglas"""
    x = (pantalla.get_width() - pantallazo_reglas.get_width()) / 2
    y = (pantalla.get_height() - pantallazo_reglas.get_height()) / 2
    pantalla.blit(pantallazo_reglas, (x, y))

def actualizar_paneles():
    """Actualizar el contenido de cada panel"""
    for panel in paneles.values():
        panel.dibujar()
    for boton in botones.values():
        boton.actualizar()
        boton.dibujar()

def actualizar_textos():
    """Actualizar textos en pantalla"""
    texto(f"Crédito: {credito}M", (ANCHURA * ANCHURA_JUEGO + sep, sep), 24)
    texto('Tienda', (ANCHURA * (ANCHURA_JUEGO + 1) / 2, 65), 24, alineado = 'c', subrayado = True)

def siguiente_fotograma():
    pygame.display.flip()
    clock.tick(FPS)

# < -------------------------------------------------------------------------- >
#                           INICIALIZACIÓN DEL JUEGO
# < -------------------------------------------------------------------------- >

# Comenzar musica
pygame.mixer.music.play(-1)

# Inicializar variables básicas
nombre  = NOMBRE_DEFECTO
credito = CREDITO_INICIAL
productos  = [
    AvionCaza, AvionAtaque, AvionTransporte, Helicoptero, Dron, Radar, Bateria, Inteligencia, Infraestructura]
inventario = { producto: 0 for producto in productos }

# Configurar paneles
sep = PANEL_SEPARACION
paneles = {
    'gráficas':        Panel((sep, sep), (ANCHURA * ANCHURA_JUEGO - 1.5 * sep, ALTURA * ALTURA_JUEGO - 1.5 * sep), 'gráficas'),
    'acciones':    Panel((ANCHURA * ANCHURA_JUEGO + sep / 2, sep), (ANCHURA * ANCHURA_ACCIONES - 1.5 * sep, ALTURA * ALTURA_ACCIONES - 1.5 * sep)),
    'informacion': Panel((sep, ALTURA * ALTURA_JUEGO + sep / 2), (ANCHURA - 2 * sep, ALTURA * ALTURA_INFORMACION - 1.5 * sep), 'información')
}

# Configurar pantallazo reglas
dim = (1280, 720)
pantallazo_reglas = pygame.Surface(dim, pygame.SRCALPHA)
pantallazo_reglas.fill((0, 0, 0, 0))
panel_pantallazo_reglas = Panel((0, 0), dim, radio=20, color=PANTALLAZO_REGLAS_COLOR_FONDO, surface=pantallazo_reglas)
panel_pantallazo_reglas.dibujar()
texto('REGLAS', (pantallazo_reglas.get_width() / 2, 0), color=PANTALLAZO_REGLAS_COLOR_TEXTO, tamaño=72, alineado='c', surface=pantallazo_reglas)
texto_multilinea(REGLAS, (30, 90), color=PANTALLAZO_REGLAS_COLOR_TEXTO,tamaño=16, alineado='i', surface=pantallazo_reglas, max_ancho=1200)

# Configurar pantallazo inicial
dim = (imagen_pantallazo.get_width() + 20, imagen_pantallazo.get_height() + 20)
pantallazo = pygame.Surface(dim, pygame.SRCALPHA)
pantallazo.fill((0, 0, 0, 0))
panel_pantallazo = Panel((0, 0), dim, radio=20, color=PANTALLAZO_COLOR_FONDO, surface=pantallazo)
panel_pantallazo.dibujar()
pantallazo.blit(imagen_pantallazo, (10, 10))
texto(NOMBRE_JUEGO, (pantallazo.get_width() / 2, pantallazo.get_height() / 3), color=PANTALLAZO_COLOR_TEXTO, tamaño=180, alineado='c', surface=pantallazo)

# Configurar botones
botones = { producto: None for producto in productos }
cols = 2
i = 0
x0 = ANCHURA * ANCHURA_JUEGO + 20
y0 = 100
x = x0
y = y0
for producto in productos:
    botones[producto] = Boton((x, y), imagen=producto.icono, ayuda=producto.ayuda()['help'], info=producto.ayuda()['info'], coste=producto.ayuda()['coste'], velocidad=producto.ayuda()['velocidad'], autonomia=producto.ayuda()['autonomia'], alcance=producto.ayuda()['alcance'], huella=producto.ayuda()['huella'], aire=producto.ayuda()['aire'], sup=producto.ayuda()['sup'], vigilancia=producto.ayuda()['vigilancia'], radiovig=producto.ayuda()['radiovig'], supaerea=producto.ayuda()['supaerea'], accion=comprar, args=(producto,))
    x = x + botones[producto].dim[0] + 5 if i % cols < cols - 1 else x0
    y += botones[producto].dim[1] + 5 if i % cols == cols - 1 else 0
    i += 1

# < -------------------------------------------------------------------------- >
#                          BUCLE PRINCIPAL DEL JUEGO
# < -------------------------------------------------------------------------- >

while True:
    # Escanear eventos (pulsaciones de teclas, movimientos de ratón, etc)
    cerrar = False
    click = False
    texto_ayuda= None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cerrar = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click = True
    if (cerrar):
        pygame.quit()
        break

    # Colorear fondo
    pantalla.fill(COLOR_FONDO)

    # Si estamos en el pantallazo, no hacer nada mas
    if tiempo() <= PANTALLAZO_TIEMPO:
        actualizar_pantallazo()
        siguiente_fotograma()
        continue

    # Si estamos en el pantallazo reglas, no hacer nada mas
    if  PANTALLAZO_TIEMPO <= tiempo() <= PANTALLAZO_REGLAS_TIEMPO:
        actualizar_pantallazo_reglas()
        siguiente_fotograma()
        continue

    # Reaccionar a las acciones del raton
    analizar_raton(click)

    # Renderizar fotograma en pantalla
    actualizar_paneles()
    actualizar_textos()
    if texto_ayuda:
        ayuda()


    siguiente_fotograma()