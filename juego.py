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

# Configuraciones
MUSICA_REPRODUCIR  = True  # Activar o desactivar la música por defecto
MUSICA_VOLUMEN     = 0.5   # Volumen relativo de la musica (0.0 - 1.0)
SALTAR_PREPARACION = False # Saltar la primera fase, útil para testear

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

SONIDO_PAGAR         = 'cajaregistradora.ogg'
SONIDO_COBRAR        = 'monedas.ogg'
SONIDO_ERROR         = 'error.ogg'
SONIDO_BOTON_SEL     = 'click.ogg'
SONIDO_BOTON_PUL     = 'switch.ogg'
SONIDO_CASILLA_SEL   = 'glass.ogg'
SONIDO_CASILLA_PUL   = 'casilla.ogg'
SONIDO_PAGINA        = 'pagina.ogg'
SONIDO_PUERTA_ABRE   = 'puerta_abre.ogg'
SONIDO_PUERTA_CIERRA = 'puerta_cierra.ogg'
SONIDO_CONSTRUIR     = 'maquina.ogg'

ICONO_AVIONCAZA       = 'icono_caza.png'
ICONO_AVIONATAQUE     = 'icono_ataque.png'
ICONO_AVIONTRANSPORTE = 'icono_transporte.png'
ICONO_HELICOPTERO     = 'icono_helicoptero.png'
ICONO_DRON            = 'icono_dron.png'
ICONO_RADAR           = 'icono_radar.png'
ICONO_BATERIA         = 'icono_bateria.png'
ICONO_INTELIGENCIA    = 'icono_inteligencia.png'
ICONO_CIUDAD          = 'icono_ciudad.png'
ICONO_BASE            = 'icono_base.png'

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
MAPA_COLOR_BORDE2  = "#ffee00" # Color del borde de la casilla actualmente seleccionada cuando estamos situando
MAPA_COLOR_BORDE3  = "#000000" # Color del borde de la casilla actualmente seleccionada cuando está en rango

# Sistema de puntos y superioridad aerea
COEF_SUP        = 20  # Coeficiente de sup aerea en una casilla normal
SUP_INICIAL     = 0.1 # Proporción de casillas iniciales con supremacia (aleatorias)
MULT_SUPREMACIA = 2   # Ratio entre superioridad y supremacia aerea

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

def reproducir_sonido(nombre, canal = None):
    """Reproducir uno de los sonidos cargados por el canal especificado"""
    if not canal:
        canal = pygame.mixer.find_channel(True)
    g_canales[canal].play(g_sonidos[nombre])

# Configuramos la pantalla (nombre, dimensiones, fotogramaje, etc)
flags = 0
if (PANTALLA_COMPLETA): flags |= pygame.FULLSCREEN
if (PANTALLA_MODIFICARDIMENSION): flags |= pygame.RESIZABLE
pygame.init()
pygame.display.set_caption(NOMBRE_JUEGO)
g_pantalla = pygame.display.set_mode((ANCHURA, ALTURA), flags)
g_reloj = pygame.time.Clock()

# Cargar recursos
pygame.mixer.init()
pygame.mixer.music.load(os.path.join(CARPETA_AUDIO, MUSICA_FONDO))
g_pantallazo = cargar_imagen(IMAGEN_FONDO)
g_fuentes = { tam: pygame.font.SysFont(TEXTO_FUENTE, tam) for tam in TEXTO_TAMANOS }
g_fuentes_mono = { tam: pygame.font.SysFont(TEXTO_FUENTE_MONO, tam) for tam in TEXTO_TAMANOS }
g_iconos = {
    'AvionCaza':       cargar_imagen(ICONO_AVIONCAZA),
    'AvionAtaque':     cargar_imagen(ICONO_AVIONATAQUE),
    'AvionTransporte': cargar_imagen(ICONO_AVIONTRANSPORTE),
    'Helicoptero':     cargar_imagen(ICONO_HELICOPTERO),
    'Dron':            cargar_imagen(ICONO_DRON),
    'Radar':           cargar_imagen(ICONO_RADAR),
    'Bateria':         cargar_imagen(ICONO_BATERIA),
    'Inteligencia':    cargar_imagen(ICONO_INTELIGENCIA),
    'Ciudad':          cargar_imagen(ICONO_CIUDAD),
    'Base':            cargar_imagen(ICONO_BASE)
}
g_sonidos = {
    'pagar':         cargar_sonido(SONIDO_PAGAR),
    'cobrar':        cargar_sonido(SONIDO_COBRAR),
    'error':         cargar_sonido(SONIDO_ERROR),
    'boton_sel':     cargar_sonido(SONIDO_BOTON_SEL),
    'boton_pul':     cargar_sonido(SONIDO_BOTON_PUL),
    'casilla_sel':   cargar_sonido(SONIDO_CASILLA_SEL),
    'casilla_pul':   cargar_sonido(SONIDO_CASILLA_PUL),
    'pagina':        cargar_sonido(SONIDO_PAGINA),
    'puerta_abre':   cargar_sonido(SONIDO_PUERTA_ABRE),
    'puerta_cierra': cargar_sonido(SONIDO_PUERTA_CIERRA),
    'construir':     cargar_sonido(SONIDO_CONSTRUIR)
}
g_texturas = {
    'hierba':    cargar_textura(TEXTURA_ESCENARIO, TEXTURA_ESCENARIO_COLOR),
    'ladrillos': cargar_textura(TEXTURA_TIENDA,    TEXTURA_TIENDA_COLOR),
    'piedras':   cargar_textura(TEXTURA_INFO,      TEXTURA_INFO_COLOR),
    'malla':     cargar_textura(TEXTURA_REGLAS,    TEXTURA_REGLAS_COLOR),
    'gotele':    cargar_textura(TEXTURA_BOTON,     TEXTURA_BOTON_COLOR),
}

# Canales de sonido. Un canal sólo puede reproducir un sonido al mismo tiempo,
# de manera que ordenando los sonidos por canales evitamos que se solapen
# sonidos que no queremos. Por defecto puede haber 8 canales.
g_canales = {
    'interfaz': pygame.mixer.Channel(0),
    'efectos':  pygame.mixer.Channel(1)
}

# < -------------------------------------------------------------------------- >
#                              CLASES DEL JUEGO
# < -------------------------------------------------------------------------- >

class Medio:
    """Clase genérica que representa cualquier medio militar"""
    NOMBRE        = None # Nombre del medio
    ICONO         = None # Icono del botón en la tienda
    DESC          = None # Breve descripción informativa
    PRECIO        = None # Precio de compra (M€)
    PRECIO_MEJORA = None # Precio de mejora - sólo para infraestructuras (M€)
    VELOCIDAD     = None # Velocidad de avance de un medio aéreo (casillas por turno)
    AUTONOMIA     = None # Tiempo que puede permanecer fuera de la base un medio aéreo (turnos)
    ALCANCE       = None # Distancia de la base que puede recorrer un medio aéreo (turnos)
    HUELLA        = None # Probabilidad de ser captado por una vigilancia (%)
    DIST_AIRE     = None # Distancia a la que puede derribar un medio aéreo (casillas)
    DIST_SUP      = None # Distancia a la que puede derribar un medio anti-aéreo (casillas)
    VIGILANCIA    = None # Probabilidad de captar un medio aéreo con radar (%)
    RADIOVIG      = None # Distancia a la que puede vigilar otros medios aéreos (casillas)
    SUPAEREA      = None # Peso del medio a la hora de aportar superioridad aérea (puntos)

    def __init__(self, jugador, casilla = None):
        self.jugador = jugador
        self.casilla = casilla
        self.texto   = Texto(self.NOMBRE, (0, 0), 16, alineado_h = 'd', surface = g_escenario.panel.lienzo)

    @classmethod
    def info(cls):

        # Información breve en la ayuda del ratón
        texto_ayuda = cls.NOMBRE
        if cls.PRECIO:
            texto_ayuda += f" ({cls.PRECIO}M)"
        if cls.PRECIO_MEJORA:
            casilla = g_escenario.casilla_pulsa
            if casilla and casilla.infraestructura:
                infra = casilla.infraestructura
                if type(infra) is cls and infra.jugador == g_jugador:
                    texto_ayuda = f"Mejorar {cls.NOMBRE} ({cls.PRECIO_MEJORA}M)"
        g_ayuda.cambiar(texto_ayuda)

        # Texto informativo extenso en el panel inferior
        y0 = g_fuentes[Informacion.TAMANO_TITULO].get_linesize()
        y1 = g_fuentes[Informacion.TAMANO_TEXTO].get_linesize()
        g_info.borrar()
        g_info.escribir("Descripción:", (10, y0), negrita = True)
        g_info.escribir(cls.DESC, (120, y0))
        nombres = ""
        valores = ""
        if cls.PRECIO:        nombres += "\nPrecio:";        valores += f"\n{cls.PRECIO}"
        if cls.PRECIO_MEJORA: nombres += "\nPrecio mejora:"; valores += f"\n{cls.PRECIO_MEJORA}"
        if cls.VELOCIDAD:     nombres += "\nVelocidad:";     valores += f"\n{cls.VELOCIDAD}"
        if cls.AUTONOMIA:     nombres += "\nAutonomía:";     valores += f"\n{cls.AUTONOMIA}"
        if cls.ALCANCE:       nombres += "\nAlcance:";       valores += f"\n{cls.ALCANCE}"
        if cls.HUELLA:        nombres += "\nHuella:";        valores += f"\n{cls.HUELLA}"
        if cls.DIST_AIRE:     nombres += "\nAire-aire:";     valores += f"\n{cls.DIST_AIRE}"
        if cls.DIST_SUP:      nombres += "\nAire-sup:";      valores += f"\n{cls.DIST_SUP}"
        if cls.VIGILANCIA:    nombres += "\nVigilancia:";    valores += f"\n{cls.VIGILANCIA}"
        if cls.RADIOVIG:      nombres += "\nRadio-vigil.:";  valores += f"\n{cls.RADIOVIG}"
        if cls.SUPAEREA:      nombres += "\nSup.-aerea:";    valores += f"\n{cls.SUPAEREA}"
        g_info.escribir(nombres, ( 10, y0 + 1 * y1), negrita = True)
        g_info.escribir(valores, (120, y0 + 1 * y1))

    def actualizar(self):
        """
            Prototipo de función que realiza la lógica interna de cada medio
            Cada tipo de medio debería implementar la suya propia
        """
        pass

class MedioAtaque(Medio):
    """Representa cualquier medio con la capacidad de atacar, ya sea aéreo o anti-aéreo"""
    ESCALA = 50.0 # Kilómetros por casilla, para convertir los datos

    def __init__(self, jugador, casilla):
        super().__init__(jugador, casilla)
        self.ataque_aire = self.DIST_AIRE and self.DIST_AIRE > 0 # Tiene la capacidad de atacar a medios aéreos
        self.ataque_sup  = self.DIST_SUP  and self.DIST_SUP  > 0 # Tiene la capacidad de atacar a medios en superficie
        self.vigilancia  = self.RADIOVIG  and self.RADIOVIG  > 0 # Tiene la capacidad de vigilar su entorno

    def radio_ataque(self):
        """Calcular el radio de ataque en casillas"""
        # El medio no tiene la capacidad de atacar
        if not self.ataque_aire and not self.ataque_sup:
            return -1

        # El medio es de ataque aéreo (p. ej. Caza)
        if self.ataque_aire:
            return math.ceil(self.DIST_AIRE / self.ESCALA)

        # El medio es de ataque superficie (p. ej. Helicóptero)
        if self.ataque_sup:
            return math.ceil(self.DIST_SUP / self.ESCALA)

    def radio_vigilancia(self):
        """Calcular el radio de vigilancia en casillas"""
        if not self.vigilancia:
            return -1
        return math.ceil(self.RADIOVIG / self.ESCALA)

    def vigilar(self):
        """
            Escanear las casillas dentro del radio de vigilancia para intentar
            detectar medios aéreos enemigos no detectados aún.
        """
        if not self.vigilancia:
            return
        avos = [medio for medio in self.jugador.adversario().medios if isinstance(medio, MedioAereo) and medio.vigilado(self) and not medio.detectado(self)]
        for avo in avos:
            if random.random() <= (self.VIGILANCIA / 100.0) * (avo.HUELLA / 100.0):
                avo.detectar(self)

    def destruir(self, manual, verdugo):
        """
            Destruir el medio como consecuencia de un ataque.
            El ataque manual es el efectuado por aeronaves. El automático es el efectuado por medios antiaéreos.
        """

        # Si se trata de un medio aéreo, ejercer puntos de superioridad
        if isinstance(self, MedioAereo):
            self.casilla.ejercer(self.sup)

        # Reportar información (ahora o después) a ambos jugadores
        mensaje = f"Derribado {self.NOMBRE} enemigo con {verdugo.NOMBRE} en casilla {self.casilla.id()}"
        if manual:
            g_info.medio(mensaje)
        else:
            verdugo.jugador.reportar(mensaje)
        self.jugador.reportar(f"Tu {self.NOMBRE} fue derribado en la casilla {self.casilla.id()}")

        # Eliminar medio del juego
        self.jugador.medios.remove(self)
        for medio in self.jugador.adversario().medios:
            if isinstance(medio, MedioAereo) and medio.detectado(self):
                medio.detectores.remove(self)

    def puntuar(self):
        """Devolver los puntos AIRGAME otorgados por este medio"""
        return self.SUPAEREA

class MedioEstrategico(Medio):
    """Representa cualquier medio estratégico (inteligencia, infraestructuras)"""

class MedioAereo(MedioAtaque):
    """Representa cualquier medio aéreo"""

    def __init__(self, jugador, casilla):
        super().__init__(jugador, casilla)
        self.base = self.casilla
        x, y = g_escenario.panel.pos
        self.botones = [
            Boton((0,0), texto="D", anchura=20, origen=(x,y), info=lambda: g_ayuda.cambiar('Desplegar'), surface=g_escenario.panel.lienzo, accion=self.desplegar),
            Boton((0,0), texto="R", anchura=20, origen=(x,y), info=lambda: g_ayuda.cambiar('Retornar'),  surface=g_escenario.panel.lienzo, accion=self.aterrizar),
            Boton((0,0), texto="A", anchura=20, origen=(x,y), info=lambda: g_ayuda.cambiar('Atacar'),    surface=g_escenario.panel.lienzo, accion=self.atacar)
        ]
        self.detectores = [] # Lista de medios que han detectado a este medio
        self.resetear()

    def resetear(self):
        """Inicializar los valores del medio"""
        self.casilla    = self.base # La casilla en la que este medio está actualmente
        self.desplegado = False     # Si este medio está actualmente desplegado
        self.turnos     = 0         # Número de turnos desde que este medio fue desplegado
        self.atacado    = False     # Si este medio ha atacado ya en este turno
        self.sup        = 0         # Puntos de superioridad acumulados

    def alcance(self):
        """Calcular el alcance en casillas"""
        return 2 * math.ceil(self.ALCANCE / 1000.0)

    def autonomia(self, casilla = None):
        """
            Calcular la autonomía en turnos, que depende de la distancia a la base.
            Si no se pasa una casilla, se toma la casilla actual.
        """
        distancia = self.base.distancia(casilla or self.casilla)
        alcance = self.alcance()
        if distancia > alcance:
            return -1
        return math.ceil(self.AUTONOMIA * (1 - distancia / alcance))

    def desplegar(self, casilla = None):
        """Desplegar el medio aéreo"""
        # Realizar chequeos para asegurarnos de que el despliegue es posible
        if g_paso != 'Despliegue':
            emitir_error('Sólo se pueden desplegar medios aéreos en el paso de despliegue')
            return
        if self.desplegado:
            emitir_error(f'Este {self.NOMBRE} ya está desplegado')
            return
        if len(self.base.infraestructura.avos_desplegados()) >= self.base.infraestructura.nivel:
            emitir_error(f'Ya no puedes desplegar más medios desde esta base')
            return

        # Si no pasamos casilla, permitimos que el jugador escoja la casilla
        if not casilla:
            g_jugador.situar_on(self)
            return

        # Chequeamos que la casilla es correcta
        radio = self.alcance()
        if self.casilla.distancia(casilla) > radio:
            emitir_error(f'Este medio tiene un alcance de {radio} casillas')
            return

        # Realizamos el despliegue
        self.desplegado = True
        self.casilla = casilla
        g_jugador.situar_off()
        g_info.medio(f"{self.NOMBRE} desplegado en casilla {casilla.id()} (límite {self.autonomia()} turnos)")

    def aterrizar(self, auto = False):
        """Retornar el medio aéreo a la base de origen"""
        # Chequeos para asegurar que es posible aterrizar el medio
        if g_paso != 'Despliegue' and not auto:
            emitir_error('Sólo se pueden retornar medios aéreos en el paso de despliegue')
            return
        if not self.desplegado:
            emitir_error(f'Este {self.NOMBRE} no está desplegado')
            return
        if self.turnos == 0 and not auto:
            emitir_error('No puedes desplegar y aterrizar un medio en el mismo turno')
            return

        # Aterrizar el avión (ejercer puntos de superioridad, resetear variables...)
        self.desplegado = False
        self.casilla.ejercer(self.sup)
        g_info.medio(f"{self.NOMBRE} retornado{' automáticamente' if auto else ''}")
        self.resetear()

    def atacar(self, casilla = None):
        """Usar el medio aéreo para atacar otra casilla"""
        # Chequeos para asegurar que el ataque es posible
        if not self.ataque_aire and not self.ataque_sup:
            emitir_error('Este medio no tiene capacidad de ataque')
            return
        if g_paso != 'Despliegue':
            emitir_error('Sólo se puede atacar con medios aéreos en el paso de despliegue')
            return
        if not self.desplegado:
            emitir_error(f'Este {self.NOMBRE} no está desplegado')
            return
        if self.atacado:
            emitir_error('Ya has atacado con este medio este turno')
            return

        # Si no pasamos casilla, permitimos que el jugador escoja la casilla
        if not casilla:
            g_jugador.atacar_on(self)
            return

        # Chequeamos que la casilla es correcta
        radio = self.radio_ataque()
        if self.casilla.distancia(casilla) > radio:
            emitir_error(f'Este medio tiene un radio de ataque de {radio} casillas')
            return

        # Realizamos el ataque
        g_jugador.atacar_off()
        self.atacado = True
        medios = casilla.medios(g_adversario)
        if self.ataque_aire:
            medios = [medio for medio in medios if isinstance(medio, MedioAereo) and medio.desplegado]
        else:
            medios = [medio for medio in medios if isinstance(medio, MedioAntiaereo)]
        if len(medios) == 0:
            g_info.medio(f"Ataque fallido con {self.NOMBRE} en casilla {casilla.id()}")
            g_adversario.reportar(f"Ataque adversario fallido a la casilla {casilla.id()}")
            return
        for medio in medios:
            medio.destruir(True, self)

    def detectar(self, medio):
        """Hemos sido detectados por el medio"""
        self.detectores.append(medio)
        medio.jugador.reportar(f"Detectado {self.NOMBRE} enemigo en la casilla {self.casilla.id()}")
        if type(medio) is Bateria:
            self.destruir(False, medio)

    def detectado(self, medio):
        """Determinar si hemos sido detectados por el medio"""
        return medio in self.detectores

    def vigilado(self, medio):
        """Determinar si estamos dentro del radio de vigilancia del medio"""
        return self.casilla.distancia(medio.casilla) <= medio.radio_vigilancia()

    def visible(self):
        """
            Devuelve si el medio es actualmente visible por el adversario porque
            está dentro del radio de vigilancia de un medio que ya lo ha detectado
        """
        return sum(1 for medio in self.detectores if self.vigilado(medio)) > 0

    def actualizar(self):
        """Ejecutar lógica del medio aéreo"""
        self.atacado = False
        if self.desplegado:
            if self.turnos < self.autonomia():
                self.turnos += 1
                self.sup += self.SUPAEREA
            else:
                self.aterrizar(True)

class MedioAntiaereo(MedioAtaque):
    """Representa cualquier medio anti-aéreo"""

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
    DIST_AIRE  = 170
    DIST_SUP   = 0
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
    DIST_AIRE  = 0
    DIST_SUP   = 240
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
    DIST_AIRE  = 0
    DIST_SUP   = 0
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
    DIST_AIRE  = 0
    DIST_SUP   = 10
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
    DIST_AIRE  = 0
    DIST_SUP   = 100
    VIGILANCIA = 20
    RADIOVIG   = 240
    SUPAEREA   = 2

class Radar(MedioAntiaereo):
    """Representa un radar"""
    NOMBRE     = "Radar"
    ICONO      = g_iconos['Radar']
    DESC       = 'Medio antiaéreo con el mayor alcance de vigilancia.'
    PRECIO     = 24
    DIST_AIRE  = 0
    DIST_SUP   = 0
    VIGILANCIA = 90
    RADIOVIG   = 440
    SUPAEREA   = 0

class Bateria(MedioAntiaereo):
    """Representa una batería anti-aérea"""
    NOMBRE     = "Batería"
    ICONO      = g_iconos['Bateria']
    DESC       = 'Único medio antiaéreo con capacidad de vigilancia.'
    PRECIO     = 90
    DIST_AIRE  = 240
    DIST_SUP   = 0
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
    INC     = 5   # Incremento del coeficiente de superioridad por cada nivel extra
    BONUS   = 0   # Crédito (en M) otorgado al jugador por turno y nivel
    NIVELES = 9   # Maximo nivel de una infraestructura
    PRECIO  = 200 # Precio de construcción

    def __init__(self, jugador, casilla):
        super().__init__(jugador, casilla)
        self.nivel = 1

    def destruir(self):
        """Eliminar la infraestructura"""
        self.casilla.infraestructura = None
        self.casilla.numero = None
        if self in self.jugador.infraestructuras:
            self.jugador.infraestructuras.remove(self)

    def mejorar(self):
        """Mejorar el nivel y las propiedades de la infraestructura"""
        if self.nivel == self.NIVELES:
            emitir_error(f'Esta {self.NOMBRE} ya está al máximo nivel')
            return
        if self.jugador.pagar(self.PRECIO_MEJORA):
            self.nivel += 1
            reproducir_sonido('construir', 'efectos')
            g_info.medio(f'Has mejorado tu {self.NOMBRE} de la casilla {self.casilla.id()} a nivel {self.nivel}')
            self.casilla.numerar()

    def cosechar(self):
        """Obtener el bonus económico que otorga la infraestructura"""
        cantidad = self.BONUS * self.nivel
        self.jugador.cobrar(cantidad)
        return cantidad

    def puntuar(self):
        """Obtener los puntos AIRGAME correspondientes"""
        return self.PUNTOS

class Ciudad(Infraestructura):
    """Infraestructura que otorga recursos al jugador"""
    NOMBRE        = "Ciudad"
    ICONO         = g_iconos['Ciudad']
    DESC          = "Infraestructura que cosecha recursos cada turno."
    PRECIO_MEJORA = 100
    SUP           = 40
    BONUS         = 10
    CANTIDAD      = 2
    COLOR         = "#000000"
    PUNTOS        = 30

class Base(Infraestructura):
    """Infraestructura que permite desplegar medios aéreos"""
    NOMBRE        = "Base aérea"
    ICONO         = g_iconos['Base']
    DESC          = "Infraestructura que permite desplegar medios aéreos."
    PRECIO_MEJORA = 150
    SUP           = 60
    CANTIDAD      = 3
    COLOR         = "#00b050"
    PUNTOS        = 50

    def avos(self):
        """Devuelve la lista de medios aéreos del jugador correspondientes a esta base"""
        return [medio for medio in self.casilla.medios() if isinstance(medio, MedioAereo)]

    def avos_desplegados(self):
        """Devueve la lista de medios aéreos desplegados de esta base del jugador"""
        return [avo for avo in self.avos() if avo.desplegado]

class Capital(Ciudad):
    """Ciudad principal del jugador. Además, perderla implica perder la partida."""
    NOMBRE        = "Capital"
    DESC          = "Ciudad principal del jugador. Conquistarla implica ganar la partida."
    PRECIO        = None
    PRECIO_MEJORA = None
    SUP           = 100
    CANTIDAD      = 1
    COLOR         = "#c09200"

class Casilla:
    ESCALA   = 0.6
    BORDE    = 0.9
    RADIO    = min(ESCALA * ANCHURA * ANCHURA_JUEGO / MAPA_DIM_X, ESCALA * ALTURA * ALTURA_JUEGO / MAPA_DIM_Y)
    INRADIO  = 0.85 * RADIO
    DIM_X    = RADIO * 3 ** 0.5
    DIM_Y    = RADIO * 1.5
    DIM      = pygame.math.Vector2(DIM_X, DIM_Y)
    BONUS    = 1 # Crédito otorgado al jugador con superioridad aérea en la casilla por turno
    BONUS_F  = 2 # Ídem, pero con supremacía aérea
    PUNTOS   = 1 # Puntos AIRGAME otorgados al final de la partida por una casilla con superioridad aérea
    PUNTOS_F = 3 # Puntos AIRGAME otorgados al final de la partida por una casilla con supremacía aérea

    def __init__(self, esc, x, y):
        self.x = x
        self.y = y
        self.centro = pygame.math.Vector2(Escenario.ORIGEN_X + self.DIM_X * (x + (y % 2) / 2), Escenario.ORIGEN_Y + self.DIM_Y * y)
        self.verts = [self.centro + v for v in esc.hex_vertices]
        self.infraestructura = None
        cx, cy = self.centro
        r = self.RADIO
        self.numero = Texto(
            '1',
            (cx - r * 0.4, cy),
            12,
            self.infraestructura.COLOR if self.infraestructura else '#000000',
            alineado_h = 'l',
            alineado_v = 'c',
            negrita = True,
            surface = esc.panel.lienzo
        )
        self.indicador  = Texto('*', (cx + 0.25 * r, cy - 0.85 * r), 12, '#000000', surface = esc.panel.lienzo)
        self.indicador2 = Texto('!', (cx - 0.75 * r, cy - 0.85 * r), 12, '#000000', surface = esc.panel.lienzo)
        self.resetear()

    def id(self):
        """Cadena de texto informativa que identifica a la casilla"""
        return f"({self.x + 1}, {MAPA_DIM_Y - self.y})"

    def resetear(self):
        """Inicializar todas las propiedades y contenidos de la casilla"""
        self.infraestructura = None # Infraestructura construida en esta casilla
        self.sel = False            # Si el ratón está sobre esta casilla
        self.pul = False            # Si esta casilla está actualmente pulsada
        self.auto = -1              # Cantidad de turnos que puede permanecer el medio seleccionado en esta casilla
        self.numero.ocultar()
        self.destruir()
        self.recalcular()
        self.inicializar_coeficientes()
        self.asignar()
        self.colorear()

    def asignar(self):
        """Determinar propietario de la casilla, que tiene inicialmente la superioridad aerea"""
        self.jugador = g_jugadores[0] if self.sup >= self.supCas else g_jugadores[1] if self.sup <= -self.supCas else None

    def inicializar_coeficientes(self):
        """Especificar valor inicial del coeficiente de superioridad aérea"""
        if self.x < MAPA_DIM_J:
            self.sup = self.supCas
        elif self.x >= MAPA_DIM_X - MAPA_DIM_J:
            self.sup = -self.supCas
        else:
            self.sup = 0

    def recalcular(self):
        """Determinar coeficiente de superioridad de casilla"""
        infra = self.infraestructura
        self.supCas = infra.SUP + infra.INC * infra.nivel if infra else COEF_SUP

    def ejercer(self, puntos):
        """Ejercer una cierta cantidad de superioridad aérea sobre la casilla"""

        # Guardamos el estado previo de la casilla
        hay_supre1 = self.hay_supremacia(g_adversario)
        hay_super1 = self.hay_superioridad(g_adversario)

        # Modificamos el coeficiente de superioridad aérea de la casilla
        self.sup += puntos if g_jugador.indice == 0 else -puntos

        # Guardamos el estado posterior de la casilla
        hay_supre2 = self.hay_supremacia(g_adversario)
        hay_super2 = self.hay_superioridad(g_adversario)

        # Reportamos cambios en el estado de la casilla
        if hay_supre1 and not hay_supre2:
            g_adversario.reportar(f'Has perdido la supremacía aérea en la casilla {self.id()}!')
        if hay_super1 and not hay_super2:
            g_adversario.reportar(f'Has perdido la superioridad aérea en la casilla {self.id()}!')

        # Cambiamos el color de la casilla si es necesario
        self.colorear()

    def numerar(self):
        """Cambiar el número de la casilla"""
        if not self.infraestructura:
            return
        self.numero.editar(str(self.infraestructura.nivel))
        self.numero.colorear(self.infraestructura.COLOR)
        self.numero.mostrar()
        g_escenario.cambio = True

    def cosechar(self):
        """Otorgar bonus de crédito al jugador"""
        if self.hay_supremacia():
            g_jugador.cobrar(self.BONUS_F)
            return self.BONUS_F
        elif self.hay_superioridad():
            g_jugador.cobrar(self.BONUS)
            return self.BONUS
        return 0

    def puntuar(self, jugador):
        """Otorgar puntos AIRGAME al jugador"""
        return self.PUNTOS_F if self.hay_supremacia(jugador) else self.PUNTOS if self.hay_superioridad(jugador) else 0

    def construir(self, tipo):
        """Construir una infraestructura en esta casilla"""
        infra = tipo(g_jugador, self)
        self.infraestructura = infra
        self.recalcular()
        self.sup = round((self.sup / abs(self.sup)) * self.supCas)
        self.numerar()
        return infra

    def destruir(self):
        """Destruir la infraestructura de la casilla"""
        if self.infraestructura:
            self.infraestructura.destruir()

    def raton(self, pos_vec):
        """Detecta si el ratón está sobre la casilla. Aproximamos el hexágono por el círculo inscrito."""
        return pos_vec.distance_squared_to(self.centro + g_escenario.panel.pos) < self.INRADIO ** 2

    def hay_superioridad(self, jugador = None):
        """Detecta si el jugador actual tiene superioridad aérea en la casilla"""
        if not jugador:
            jugador = g_jugador
        return jugador.indice == 0 and self.sup >= self.supCas or jugador.indice == 1 and self.sup <= -self.supCas

    def hay_supremacia(self, jugador = None):
        """Detecta si el jugador actual tiene supremacia aérea en la casilla"""
        if not jugador:
            jugador = g_jugador
        return jugador.indice == 0 and self.sup >= MULT_SUPREMACIA * self.supCas or jugador.indice == 1 and self.sup <= -MULT_SUPREMACIA * self.supCas

    def es_base(self):
        """Detecta si el jugador actual tiene una base aérea en la casilla"""
        infra = self.infraestructura
        return infra and type(infra) is Base and infra.jugador == g_jugador

    def medios(self, jugador = None):
        """Devuelve la lista de medios que el jugador actual tiene en esta casilla (desplegados o no)"""
        if not jugador:
            jugador = g_jugador
        return [medio for medio in jugador.medios if medio.casilla == self]

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

    def bordear(self, surface, color, grosor):
        """Dibujar el borde hexagonal de la casilla"""
        pygame.draw.polygon(surface, color, self.verts, grosor)

    def dibujar(self, surface):
        """Dibujar casilla en pantalla"""

        # Hexágono e indicador de infraestructura
        pygame.draw.polygon(surface, self.color, self.verts)
        if self.infraestructura:
            self.bordear(surface, self.infraestructura.COLOR, 4)
            self.numero.dibujar()

        # Indicadores de medios (propios y enemigos detectados)
        if g_jugador and sum(1 for medio in g_jugador.medios if medio.casilla == self) > 0:
            self.indicador.dibujar()
        if g_adversario and sum(1 for medio in g_adversario.medios if medio.casilla == self and isinstance(medio, MedioAereo) and medio.visible()) > 0:
            self.indicador2.dibujar()

        # Bordes de selección
        color_borde = MAPA_COLOR_BORDE if not g_jugador or not g_jugador.situando and not g_jugador.atacando else MAPA_COLOR_BORDE2
        if self.auto >= 0:
            self.bordear(surface, MAPA_COLOR_BORDE3, 1)
        if self.sel:
            self.bordear(surface, color_borde, 2)
        if self.pul:
            self.bordear(surface, color_borde, 4)

    def seleccionar(self):
        """Seleccionar la casilla cuando el raton pasa por encima"""
        if self.sel:
            return
        self.sel = True
        g_escenario.casilla_sobre = self
        g_escenario.cambio = True
        reproducir_sonido('casilla_sel', 'interfaz')

    def deseleccionar(self):
        """Deseleccionar la casilla"""
        if not self.sel:
            return
        self.sel = False
        g_escenario.casilla_sobre = None
        g_escenario.cambio = True

    def pulsar(self):
        """Pulsar la casilla cuando el raton hace click"""
        if self.pul:
            return
        self.pul = True
        g_escenario.casilla_pulsa = self
        g_escenario.cambio = True
        if g_jugador and g_jugador.situando:
            g_jugador.situando.desplegar(self)
        if g_jugador and g_jugador.atacando:
            g_jugador.atacando.atacar(self)
        reproducir_sonido('casilla_pul', 'interfaz')

    def despulsar(self, final = False):
        """Despulsar la casilla"""
        if not self.pul:
            return
        self.pul = False
        g_escenario.casilla_pulsa = None
        g_escenario.cambio = True
        if g_jugador and final:
            g_jugador.situar_off()
            g_jugador.atacar_off()

    def ayuda(self):
        """Mostrar el recuadro de ayuda al pasar el ratón sobre la casilla"""

        # Coeficientes de superioridad y jugador
        texto_ayuda = f"{self.supCas} / {abs(self.sup)}"
        if self.sup != 0:
            indice = 1 if self.sup > 0 else 2
            texto_ayuda += f" (J{indice})"

        # Información de la infraestructura
        infra = self.infraestructura
        if infra:
            texto_ayuda += f"\n{type(infra).__name__} ({infra.nivel})"

            # Bases aéreas: Medios aéreos movilizados
            avos = [medio for medio in self.medios() if isinstance(medio, MedioAereo)]
            movil = [avo for avo in avos if avo.desplegado]
            if len(avos) > 0 or type(infra) is Base:
                texto_ayuda += f"\nAvos: {len(movil)} / {infra.nivel} ({len(avos)})"

        # Turnos de autonomía disponibles al desplegar
        if self.auto >= 0:
            texto_ayuda += f"\nTurnos: {self.auto}"

        # Cambiar texto y hacerlo visible
        g_ayuda.cambiar(texto_ayuda)
        g_ayuda.mostrar()

    def axial(self):
        """Calcula la coordenadas axiales de la casilla (lugar de cartesianas)"""
        return (self.x - (self.y - (self.y & 1)) / 2, self.y)

    def distancia(self, casilla):
        """Calcula la distancia a otra casilla"""
        q1, r1 = self.axial()
        q2, r2 = casilla.axial()
        return round((abs(q1 - q2) + abs(q1 + r1 - q2 - r2) + abs(r1 - r2)) / 2)

class Escenario:
    ORIGEN_X = 2 * Casilla.DIM_X # (ANCHURA * ANCHURA_JUEGO - MAPA_DIM_X * Casilla.DIM_X) / 2
    ORIGEN_Y = ALTURA * ALTURA_JUEGO - MAPA_DIM_Y * Casilla.DIM_Y
    ORIGEN = pygame.Vector2(ORIGEN_X, ORIGEN_Y)
    FUENTE  = 24

    def __init__(self, panel):
        self.panel = panel
        self.cambio = False

        # Calcular las dimensiones de las casillas
        hex_vert = pygame.math.Vector2.from_polar((Casilla.RADIO * Casilla.BORDE, 90))
        self.hex_vertices = [hex_vert.rotate(60 * i) for i in range(6)]

        # Array de casillas
        self.casillas = [[Casilla(self, x, y) for y in range(MAPA_DIM_Y)] for x in range(MAPA_DIM_X)]
        self.resetear()

        # Panel de acción
        w = self.panel.dim[0]
        self.texto = Texto('Medios', (0.9 * w, 0), self.FUENTE, alineado_h = 'c', subrayado = True, surface = self.panel.lienzo)

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

        # Fuerza un re-renderizado
        self.cambio = True

    def actualizar_casillas(self, despulsar = True):
        """Detectar si alguna casilla esta seleccionada o ha sido pulsada"""

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
        if self.casilla_pulsa and g_click and despulsar:
            self.casilla_pulsa.despulsar(True)

    def actualizar(self):
        """Ejecutar la lógica del contenido del escenario cada fotograma"""

        # Si el ratón no está sobre el escenario, muchas cosas no pueden cambiar
        if self.panel.raton():

            # Detectar cambios en los botones de acción
            accionado = False
            if self.casilla_pulsa:
                avos = [medio for medio in self.casilla_pulsa.medios() if isinstance(medio, MedioAereo)]
                for avo in avos:
                    for boton in avo.botones:
                        accionado = accionado or boton.actualizar()
                        if boton.selec:
                            g_ayuda.mostrar()
            self.cambio = self.cambio or accionado

            # Detectar cambios en casillas seleccionadas o pulsadas
            self.actualizar_casillas(not accionado)

        # Si ha habido algún cambio en el contenido del escenario, renderizarlo de nuevo
        if self.cambio:
            self.renderizar()
        self.cambio = False

    def renderizar(self):
        """Generar gráficos del escenario de nuevo. Sólo ejecutar cuando algo haya cambiado."""
        # Panel de fondo e indicador de turno
        self.panel.renderizar()
        if g_jugador:
            color = MAPA_COLOR_J1_F if g_jugador.indice == 0 else MAPA_COLOR_J2_F
            x = Escenario.ORIGEN_X + Casilla.DIM_X * ((MAPA_DIM_X + 1.25) * g_jugador.indice - 1)
            y = Escenario.ORIGEN_Y + MAPA_DIM_Y * Casilla.DIM_Y / 2 - 50
            rect = (x, y, 10, 100)
            pygame.draw.rect(self.panel.lienzo, color, rect, 0, 5)
            pygame.draw.rect(self.panel.lienzo, '#000000', rect, 1, 5)

        # Mapa de celdas
        for columna in self.casillas:
            for casilla in columna:
                casilla.dibujar(self.panel.lienzo)

        # Panel de acciones con los medios
        self.texto.dibujar()
        if not self.casilla_pulsa:
            return
        w = self.panel.dim[0]
        dy = g_fuentes[self.FUENTE].get_linesize()
        x0, y0 = (0.9 * w, dy)
        x, y = x0, y0
        for medio in self.casilla_pulsa.medios():
            medio.texto.mover((x, y), 'd')
            medio.texto.dibujar()
            if isinstance(medio, MedioAereo):
                for boton in medio.botones:
                    boton.situar(x, y)
                    boton.dibujar()
                    x += 1.25 * boton.panel.dim[0]
                    dy = 1.25 * boton.panel.dim[1]
            y += dy
            x = x0

    def dibujar(self):
        """Dibujar todo el contenido del escenario en pantalla. Ejecutar cada fotograma."""
        self.panel.dibujar()
        if self.casilla_sobre:
            self.casilla_sobre.ayuda()

    def cosechar(self):
        """Adquirir crédito adicional debido a las casillas con superioridad aérea"""
        return sum(casilla.cosechar() for columna in self.casillas for casilla in columna)

    def puntuar(self, jugador):
        """Calcular puntos AIRGAME totales del jugador"""
        return sum(casilla.puntuar(jugador) for columna in self.casillas for casilla in columna)

    def resetear(self):
        """Resetear los contenidos de todas las celdas"""
        for col in self.casillas:
            for casilla in col:
                casilla.resetear()
        self.semillear()
        self.casilla_sobre = None # Casilla actualmente seleccionada con el raton
        self.casilla_pulsa = None # Casilla actualmente pulsada por el raton

class Informacion:
    TAMANO_TEXTO   = 14        # Tamaño de la fuente empleada en el panel
    TAMANO_TITULO  = 24        # Tamaño de la fuente de los títulos grandes
    MENSAJE_LIMITE = 12        # Limite de mensajes de error (o similares) en pantalla
    COLOR_ERROR    = '#c00000' # Color del texto "Error"
    COLOR_INFO     = '#0000c0' # Color del texto "Info"
    COLOR_DINERO   = '#c0c000' # Color del texto "Dinero"
    COLOR_INTEL    = '#00c000' # Color del texto "Intel"
    COLOR_MEDIO    = '#c000c0' # Color del texto "Medio"
    COLOR_REPORTE  = '#00c0c0' # Color del texto "Reporte"
    ANCHURA        = 550       # Anchura en píxeles de la sección de información

    """Representa el panel informativo"""
    def __init__(self, panel):
        # Inicializamos las variables
        self.panel    = panel
        x, y, w, h    = self.panel.rect
        self.renders  = {}   # Textos generales, títulos, etc
        self.textos   = []   # Textos específicos añadidos por otras funciones
        self.mensajes = []   # Mensajes informativos (errores, info, etc)
        self.fps      = None # Indicador de fps, para llevar un control
        self.cambio   = False

        # Creamos (y colocamos) los botones de acciones
        self.botones = [
            Boton((0,0), texto="Jugar",     anchura=80, surface=self.panel.lienzo, origen=(x,y), accion=siguiente_jugador),
            Boton((0,0), texto="Mover",     anchura=80, surface=self.panel.lienzo, origen=(x,y), accion=siguiente_paso),
            Boton((0,0), texto="Música",    anchura=80, surface=self.panel.lienzo, origen=(x,y), accion=cambiar_musica),
            Boton((0,0), texto="Reglas",    anchura=80, surface=self.panel.lienzo, origen=(x,y), accion=g_reglas.mostrar, audio_pul='puerta_abre'),
            Boton((0,0), texto="Reiniciar", anchura=80, surface=self.panel.lienzo, origen=(x,y), accion=resetear),
            Boton((0,0), texto="Terminar",  anchura=80, surface=self.panel.lienzo, origen=(x,y), accion=terminar),
            Boton((0,0), texto="Salir",     anchura=80, surface=self.panel.lienzo, origen=(x,y), accion=salir)
        ]
        for i, b in enumerate(reversed(self.botones)):
            b.mover(w - b.dim[0], h - (i + 1) * b.dim[1])

        # Pre-renderizamos los textos que vamos a usar, para optimizar
        self.renders['nombres']  = Texto("Fase:\nTurno:", (w - 150, 0), 16, negrita = True, surface = self.panel.lienzo)
        self.renders['valores']  = Texto(f"{g_fase}\nJugador 0", (w - 100, 0), 16, surface = self.panel.lienzo)
        self.renders['mensajes'] = Texto('Mensajes', (self.ANCHURA + 20, 0), self.TAMANO_TITULO, subrayado = True, surface = self.panel.lienzo)
        self.renders['info']     = Texto('Información', (10, 0), self.TAMANO_TITULO, subrayado = True, surface = self.panel.lienzo)
        self.fps = Texto(f"{g_reloj.get_fps():.2f} fps", (x + w - 80, y + h - 20), 14, alineado_h = 'd')
        self.resetear()

    def escribir(self, texto, pos, tamaño = 14, color = '#000000', negrita = False):
        """Cambiar el texto del panel"""
        self.textos.append(Texto(texto, pos, tamaño, color, negrita = negrita, max_ancho = self.ANCHURA + 20 - pos[0], surface = self.panel.lienzo))
        self.cambio = True

    def borrar(self):
        """Eliminar el texto del panel"""
        if self.textos:
            self.textos = []
            self.cambio = True

    def añadir_mensaje(self, tipo, texto):
        """Añadir un mensaje al panel y renderizarlo"""

        # Configurar texto
        if g_jugador:
            texto = f'[J{g_jugador.indice + 1}] {texto}'
        color = {
            'error':  self.COLOR_ERROR,
            'info':   self.COLOR_INFO,
            'dinero': self.COLOR_DINERO,
            'intel':  self.COLOR_INTEL,
            'medio':  self.COLOR_MEDIO,
            'report': self.COLOR_REPORTE
        }[tipo]
        cabecera = tipo.capitalize() + ':'
        imagen1 = Texto(cabecera, (0, 0), self.TAMANO_TEXTO, surface = self.panel.lienzo, color = color, negrita = True)
        imagen2 = Texto(texto,    (0, 0), self.TAMANO_TEXTO, surface = self.panel.lienzo)

        # Insertar nuevo mensaje en la lista, y eliminar los últimos si pasan del límite
        self.mensajes.insert(0, imagen2)
        self.mensajes.insert(0, imagen1)
        del self.mensajes[2 * self.MENSAJE_LIMITE:]

        # Recolocar textos correctamente para que se vayan moviendo para abajo
        dy0 = g_fuentes[self.TAMANO_TITULO].get_linesize()
        dy = g_fuentes[self.TAMANO_TEXTO].get_linesize() - 1
        for i, texto in enumerate(self.mensajes):
            texto.mover((self.ANCHURA + 20 + 50 * (i % 2), dy0 + (i // 2) * dy))

        # Indicar que ha habido un cambio este fotograma, para renderizar el panel de nuevo
        self.cambio = True

    def error(self, texto):
        """Guardar un mensaje especial de error (una única línea)"""
        self.añadir_mensaje('error', texto)

    def info(self, texto):
        """Guardar un mensaje informativo (una única línea)"""
        self.añadir_mensaje('info', texto)

    def dinero(self, texto):
        """Guardar un mensaje relativo al dinero del jugador"""
        self.añadir_mensaje('dinero', texto)

    def intel(self, texto):
        """Guardar un mensaje con la inteligencia recibida"""
        self.añadir_mensaje('intel', texto)

    def medio(self, texto):
        """Guardar un mensaje relacionado con acciones de medios (ataques, despliegues...)"""
        self.añadir_mensaje('medio', texto)

    def reporte(self, texto):
        """Guardar un mensaje relacionado con el reporte inicial"""
        self.añadir_mensaje('report', texto)

    def actualizar(self):
        """Actualizar los contenidos del panel. Llamar cada fotograma."""
        for boton in self.botones:
            self.cambio = self.cambio or boton.actualizar()
        if self.cambio:
            self.renderizar()
        self.fps.editar(f"{g_reloj.get_fps():.2f} fps")
        self.cambio = False

    def actualizar_texto(self):
        """Actualizar un texto (o todos) y renderizarlo de nuevo"""
        indice = g_jugador.indice + 1 if g_jugador else -1
        if g_fase != 'Principal':
            self.renders['nombres'].editar("Fase:\nTurno:")
            self.renders['valores'].editar(f"{g_fase}\nJugador {indice}")
        else:
            self.renders['nombres'].editar("Fase:\nTurno:\nPaso:")
            self.renders['valores'].editar(f"{g_fase}\nJugador {indice}\n{g_paso}")

    def renderizar(self):
        """Renderizar el panel de información. Sólo hay que hacerlo cada vez que su contenido cambie."""
        self.panel.renderizar()
        for texto in self.renders.values():
            texto.dibujar()
        for texto in self.mensajes:
            texto.dibujar()
        for texto in self.textos:
            texto.dibujar()
        for boton in self.botones:
            boton.dibujar()

    def dibujar(self):
        """Dibujar el panel en pantalla. Hay que hacerlo cada fotograma."""
        self.panel.dibujar()
        self.fps.dibujar()

    def resetear(self):
        """Reiniciar los contenidos del panel informativo"""
        self.cambio   = False
        self.textos   = []
        self.mensajes = []
        self.actualizar_texto()
        for boton in self.botones:
            boton.resetear()
        self.renderizar()

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
            [DISTAIRE]: distancia a la que puede derribar un medio aéreo / (casillas).
            [DISTSUP]: distancia a la que puede derribar un medio antiaéreo / (casillas).
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
        w, h = dim = (ANCHURA - 2 * x, ALTURA - 2 * y)
        self.panel = Panel((x, y), dim, radio=20, color=self.COLOR_FONDO, textura='malla')
        self.visible = False

        # Pre-renderizar texto e inicializar paginación
        self.textos = [
            Texto('REGLAS', (ANCHURA / 2, 0), color=self.COLOR_TEXTO, tamaño=self.TAMANO_TITULO, alineado_h='c', surface=self.panel.lienzo),
            Texto(
                Reglamento.REGLAS, (self.MARGEN_INTERNO, self.TAMANO_TITULO + 10), color=self.COLOR_TEXTO, tamaño=self.TAMANO_FUENTE,
                max_ancho=w-2*self.MARGEN_INTERNO, max_alto=self.LINEAS_POR_PAGINA, surface=self.panel.lienzo
            )
        ]
        self.paginas = self.textos[1].paginas
        self.pagina = 0

        # Botones de control
        w = self.panel.rect.w
        dy = self.TAMANO_TITULO + 10 + self.LINEAS_POR_PAGINA * g_fuentes[self.TAMANO_FUENTE].get_linesize() + 40
        self.botones = [
            Boton((0, dy), texto='Anterior',  tamaño=self.TAMANO_BOTONES, accion=self.pagina_anterior,  surface=self.panel.lienzo, origen=(x,y), audio_pul='pagina'),
            Boton((0, dy), texto='Siguiente', tamaño=self.TAMANO_BOTONES, accion=self.pagina_siguiente, surface=self.panel.lienzo, origen=(x,y), audio_pul='pagina'),
            Boton((0, dy), texto='Salir',     tamaño=self.TAMANO_BOTONES, accion=self.resetear,         surface=self.panel.lienzo, origen=(x,y), audio_pul='puerta_cierra')
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
        self.textos[0].dibujar()
        self.textos[1].dibujar(self.pagina)
        for boton in self.botones:
            boton.dibujar()

    def pagina_anterior(self):
        """Cambiar a la pagina anterior"""
        if self.pagina > 0:
            self.pagina -= 1
        else:
            reproducir_sonido('error', 'interfaz')
        self.renderizar()

    def pagina_siguiente(self):
        """Cambiar a la pagina siguiente"""
        if self.pagina < self.paginas - 1:
            self.pagina += 1
        else:
            reproducir_sonido('error', 'interfaz')
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
    MAX_INTELIGENCIA = 5

    jugadores = 0

    def __init__(self):
        self.indice = self.jugadores
        type(self).jugadores += 1
        self.resetear()

    def resetear(self):
        """Reiniciar el estado del jugador"""
        self.medios           = []              # Lista de medios de ataque (aéreos o antiaéreos) adquiridos (y no destruidos)
        self.infraestructuras = []              # Lista de infraestructuras construidas
        self.reporte          = []              # Lista de acciones hechas por el adversario en el turno anterior
        self.credito          = CREDITO_INICIAL # Crédito disponible (en M$) para gastar en la tienda
        self.cosechado        = 0               # Crédito obtenido en el último turno
        self.preparado        = False           # Ha concluído su fase de preparación
        self.situando         = None            # Ha pulsado "Desplegar" o "Aterrizar" y está situando esta aeronave
        self.atacando         = None            # Ha pulsado "Atacar" y está escogiendo objetivo para esta aeronave
        self.inteligencia     = 0               # Nivel de inteligencia actualmente contratado
        self.situar_off()
        self.atacar_off()

    def comprar(self, producto):
        """Adquirir un medio de ataque (aéreo o antiaéreo) y añadirlo al inventario"""
        if not self.pagar(producto.PRECIO):
            return
        if not issubclass(producto, MedioAtaque):
            return
        self.medios.append(producto(self, g_escenario.casilla_pulsa))
        g_info.dinero(f'Has adquirido un {producto.NOMBRE} en la casilla {g_escenario.casilla_pulsa.id()}')
        g_escenario.cambio = True

    def contratar(self):
        """Contratar inteligencia, que proporciona información adicional al comienzo de cada turno"""
        if self.inteligencia == self.MAX_INTELIGENCIA:
            emitir_error('Ya tienes el máximo nivel de inteligencia')
        elif not self.pagar(Inteligencia.PRECIO):
            return
        else:
            self.inteligencia += 1
            g_info.info(f'Contrada inteligencia de nivel {self.inteligencia}')

    def construir(self, producto, casilla):
        """Construir o mejorar una infraestructura en el mapa"""
        infra = casilla.infraestructura
        if infra:
            if type(infra) is not producto: # Infraestructura de otro tipo -> Error
                emitir_error('Ya hay una infraestructura de otro tipo en esta casilla')
            elif g_fase != 'Preparación':   # Infraestructura del mismo tipo -> Mejorar
                infra.mejorar()
            else:                           # No se puede mejorar en fase de preparación
                emitir_error('No se pueden mejorar infraestructuras en fase de preparación')
        else:                               # No hay infraestructura -> Construir
            if g_fase == 'Preparación':
                cantidad = sum(1 for infra in self.infraestructuras if type(infra) is producto)
                if cantidad >= producto.CANTIDAD:
                    emitir_error(f"Ya has construido todas las {producto.NOMBRE.lower()} iniciales")
                    return
            elif not self.pagar(producto.PRECIO):
                return
            infra = casilla.construir(producto)
            self.infraestructuras.append(infra)
            reproducir_sonido('construir', 'efectos')
            g_info.medio(f'Has construido una {producto.NOMBRE} en la casilla {casilla.id()}')
            g_escenario.cambio = True

    def pagar(self, cantidad):
        """Desembolsar una cierta cantidad, si hay crédito disponible"""
        if self.credito < cantidad:
            emitir_error('No tienes crédito suficiente!')
            return False
        reproducir_sonido('pagar', 'efectos')
        self.credito -= cantidad
        g_tienda.actualizar_textos()
        return True

    def cobrar(self, cantidad):
        """Obtener una cierta cantidad de crédito"""
        self.credito += cantidad

    def cosechar(self):
        """Adquirir crédito adicional debido a la superioridad aérea y las infraestructuras"""
        self.cosechado = g_escenario.cosechar()
        for infra in self.infraestructuras:
            self.cosechado += infra.cosechar()
        g_info.dinero(f"Has cosechado {self.cosechado}M€")
        if self.cosechado:
            reproducir_sonido('cobrar', 'efectos')
            g_tienda.actualizar_textos()

    def puntuar(self):
        """Recontar todos los puntos AIRGAME obtenidos en la partida"""
        puntos = g_escenario.puntuar(self)
        for infra in self.infraestructuras:
            puntos += infra.puntuar()
        for medio in self.medios:
            puntos += medio.puntuar()
        g_info.info(f'El jugador {self.indice + 1} ha obtenido {puntos} puntos AIRGAME')
        return puntos

    def preparar(self):
        """Realizar automáticamente la fase de preparación. Esta función está simplemente para facilitar el testeo."""
        for producto in Tienda.INFRAESTRUCTURAS:
            casillas = [casilla for columna in g_escenario.casillas for casilla in columna if casilla.hay_supremacia() and not casilla.infraestructura]
            for casilla in random.sample(casillas, producto.CANTIDAD):
                self.construir(producto, casilla)
        self.preparado = True

    def situar_on(self, medio):
        """Comenzar a situar un medio en el mapa"""
        self.situando = medio
        if not g_escenario:
            return
        for col in g_escenario.casillas:
            for casilla in col:
                casilla.auto = medio.autonomia(casilla)

    def situar_off(self):
        """Terminar de situar un medio en el mapa"""
        self.situando = None
        if not g_escenario:
            return
        for col in g_escenario.casillas:
            for casilla in col:
                casilla.auto = -1

    def atacar_on(self, medio):
        """Comenzar a atacar con un medio"""
        self.atacando = medio
        if not g_escenario:
            return
        for col in g_escenario.casillas:
            for casilla in col:
                casilla.auto = 1 if medio.casilla.distancia(casilla) <= medio.radio_ataque() else -1

    def atacar_off(self):
        """Terminar de atacar con un medio"""
        self.atacando = None
        if not g_escenario:
            return
        for col in g_escenario.casillas:
            for casilla in col:
                casilla.auto = -1

    def reportar(self, msg):
        """
            Añadir un mensaje informativo acerca de una acción llevada a cabo
            por el adversario, que será reportada al jugador en el turno siguiente
        """
        self.reporte.append(msg)

    def validar_reporte(self):
        """Ejecutar una vez vistos los reportes"""
        self.reporte = []

    def adversario(self):
        """Devolver el adversario de este jugador"""
        return g_jugadores[self.indice ^ 1]

class Tienda:
    """Contiene todos los productos que se pueden adquirir y se encarga de su funcionalidad y renderizado"""
    BOTON_SEP = 5
    TAM_FUENTE = 24
    MEDIOS = [AvionCaza, AvionAtaque, AvionTransporte, Helicoptero, Dron, Radar, Bateria, Inteligencia]
    INFRAESTRUCTURAS = [Ciudad, Base, Capital]

    def __init__(self, panel):
        self.panel = panel

        # Crear los botones de medios
        self.botones = {}
        cols = 2
        linea = g_fuentes[self.TAM_FUENTE].get_linesize()
        x = ANCHURA * ANCHURA_JUEGO + 20
        y = 2 * (PANEL_SEPARACION + linea) - 5
        for i, producto in enumerate(self.MEDIOS + self.INFRAESTRUCTURAS[:2]):
            boton = self.crear_boton(producto)
            self.botones[producto] = boton
            boton.mover(x, y)
            dx, dy = boton.dim
            x += dx + self.BOTON_SEP if i % cols  < cols - 1 else -(dx + self.BOTON_SEP) * (cols - 1)
            y += dy + self.BOTON_SEP if i % cols == cols - 1 else 0

        # El botón de la capital es especial
        self.botones[Capital] = Boton(
            (x, y), texto="Capital", info=Capital.info, indice=0, accion=lambda: g_jugador.construir(Capital, g_escenario.casilla_pulsa),
            audio_pul=None, anchura=2 * dx + self.BOTON_SEP, textura=None, negrita=True, color='#ffffff', color_selec='#ffffff', color_pulsado='#ffffff'
        )

        # Pre-renderizar textos, para optimizar
        self.textos = {
            'dinero': Texto(f"Dinero: 0", (ANCHURA * ANCHURA_JUEGO + PANEL_SEPARACION, PANEL_SEPARACION), self.TAM_FUENTE),
            'tienda': Texto('Tienda', (ANCHURA * (ANCHURA_JUEGO + 1) / 2, PANEL_SEPARACION + linea - 5), self.TAM_FUENTE, alineado_h = 'c', subrayado = True)
        }

    def crear_boton(self, producto):
        """Crear cada uno de los botones de la tienda"""
        accion = None
        args = ()
        if producto is Inteligencia:
            accion = lambda: g_jugador.contratar()
        elif issubclass(producto, MedioAtaque):
            accion = lambda p: g_jugador.comprar(p)
            args = (producto,)
        elif issubclass(producto, Infraestructura):
            accion = lambda: g_jugador.construir(producto, g_escenario.casilla_pulsa)
        return Boton((0, 0), imagen=producto.ICONO, info=producto.info, indice=0, accion=accion, args=args, audio_pul=None)

    def actualizar_textos(self):
        """Actualizar los textos de la tienda. Llamar sólo cuando ha habido cambios relevantes."""
        self.textos['dinero'].editar(f"Dinero: {g_jugador.credito}")

    def actualizar(self):
        """Actualizar estado del contenido de la tienda"""
        casilla = g_escenario.casilla_pulsa

        # Actualizar botones de medios
        for medio in self.MEDIOS:
            boton = self.botones[medio]

            # Condiciones para que el botón es activo
            if g_fase != 'Principal':
                boton.bloquear('Sólo se pueden adquirir medios en la fase principal')
            elif g_paso != 'Recursos':
                boton.bloquear('Sólo se pueden adquirir medios en el paso de recursos')
            elif issubclass(medio, MedioAereo) and (not casilla or not casilla.es_base()):
                boton.bloquear('Los medios aéreos han de ser colocados en bases aéreas')
            elif issubclass(medio, MedioAntiaereo) and (not casilla or not casilla.hay_superioridad()):
                boton.bloquear('Los medios antiaéreos han de ser colocados en casillas con superioridad aérea')
            else:
                boton.desbloquear()

            # Actualizar botón y ayuda
            boton.indexar(sum(1 for producto in g_jugador.medios if type(producto) is medio))
            boton.actualizar()
            if boton.selec:
                g_ayuda.mostrar()

        # Actualizar botones de infraestructuras
        for infra in self.INFRAESTRUCTURAS:
            boton = self.botones[infra]

            # La capital sólo puede colocarse en la fase de preparación
            if g_fase != 'Preparación' and infra is Capital:
                boton.ocultar()
            else:
                boton.mostrar()

            # Condiciones para que el botón esté activo
            if g_fase != 'Preparación' and g_fase != 'Principal':
                boton.bloquear('Sólo se pueden construir infraestructuras en las fases de preparación y principal')
            elif g_fase == 'Principal' and g_paso != 'Recursos':
                boton.bloquear('Sólo se pueden construir infraestructuras en el paso de recursos')
            elif not casilla or not casilla.infraestructura and not casilla.hay_supremacia():
                boton.bloquear('Sólo se pueden construir infraestructuras en casillas con supremacía aérea')
            else:
                boton.desbloquear()

            # Actualizar botón y ayuda
            boton.indexar(sum(1 for producto in g_jugador.infraestructuras if type(producto) is infra))
            boton.actualizar()
            if boton.selec:
                g_ayuda.mostrar()

        # Si no hay ningún botón seleccionado, borramos el texto informativo
        selec = False
        for boton in self.botones.values():
            selec = selec or boton.selec
        if not selec:
            g_info.borrar()

    def dibujar(self):
        """Renderizar la tienda en pantalla"""
        self.panel.dibujar()
        for texto in self.textos.values():
            texto.dibujar()
        for boton in self.botones.values():
            boton.dibujar()

    def resetear(self):
        """Reiniciar el contenido de la tienda"""
        for producto, boton in self.botones.items():
            boton.resetear()
        self.actualizar_textos()

# < -------------------------------------------------------------------------- >
#                             CLASES DE LA INTERFAZ
# < -------------------------------------------------------------------------- >

class Panel:
    """Clase que representa un panel que contiene informacion"""
    def __init__(
            self,
            pos,                              # Posicion del panel en la superficie
            dim,                              # Dimensiones del panel
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

    def situar(self, x, y):
        """Cambiar la posición (absoluta) del panel"""
        self.pos = (x, y)
        self.rect = pygame.Rect(self.pos, self.dim)

    def mover(self, dx, dy):
        """Cambiar la posicion (relativa) del panel"""
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
            self, pos, origen=(0,0), texto=None, tamaño=BOTON_TAMANO_LETRA, imagen=None, textura='gotele',
            info=None, indice=None, accion=None, args=(), surface=g_pantalla, audio_sel='boton_sel', audio_pul='boton_pul',
            anchura=None, altura=None, bloqueado=False, block_razon=None, visible=True, negrita=False,
            color=BOTON_COLOR_NORMAL, color_selec=BOTON_COLOR_SOBRE, color_pulsado=BOTON_COLOR_PULSA
        ):
        if not texto and not imagen:
            return
        self.pos           = pos           # Posición del botón en pantalla
        self.texto         = None          # Texto del boton
        self.imagen        = None          # Imagen del boton
        self.info          = info          # Función a ejecutar si el botón es seleccionado
        self.accion        = accion        # Función a ejecutar si el botón es pulsado
        self.args          = args          # Argumentos que mandar a la función acción, si son necesarios
        self.surface       = surface       # Superficie sobre la que se renderiza en boton
        self.indice        = indice        # Pequeño número que aparezca en la esquina del botón
        self.audio_sel     = audio_sel     # Sonido que se reproduce al seleccionar el boton
        self.audio_pul     = audio_pul     # Sonido que se reproduce al pulsar el boton
        self.textura       = textura       # Textura a usar para el boton
        self.anchura       = anchura       # Anchura mínima del botón
        self.altura        = altura        # Altura mínima del botón
        self.block_orig    = bloqueado     # Un botón bloqueado no puede usarse. Copia del valor original, que puede cambiar.
        self.block_razon   = block_razon   # Razón por la cual el botón está bloqueado
        self.visible       = visible       # Un botón no visible no se actualiza ni dibuja
        self.selec         = False         # Verdadero si el ratón está encima del botón
        self.pulsado       = False         # Verdadero si el botón está siendo pulsado
        self.color         = color         # Color normal del botón
        self.color_selec   = color_selec   # Color del botón cuando el ratón está sobre él
        self.color_pulsado = color_pulsado # Color del botón cuando es pulsado

        # Calculamos el tamaño del boton
        if texto:
            if not tamaño in TEXTO_TAMANOS:
                tamaño = BOTON_TAMANO_LETRA
            self.texto = texto
            negrita_original = g_fuentes[tamaño].bold
            g_fuentes[tamaño].bold = negrita
            self.imagen = g_fuentes[tamaño].render(texto, True, (0, 0, 0))
            g_fuentes[tamaño].bold = negrita_original
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
        self.panel = Panel(self.pos, self.dim, self.color, surface=self.surface, origen=origen, textura=self.textura)

        self.resetear()

    def situar(self, x, y):
        """Cambiar la posicion (absoluta) del boton"""
        self.panel.situar(x, y)
        self.pos = (x, y)

    def mover(self, dx, dy):
        """Cambiar la posicion (relativa) del boton"""
        self.panel.mover(dx, dy)
        self.pos = (self.pos[0] + dx, self.pos[1] + dy)

    def bloquear(self, razon = None):
        """Bloquear el boton para impedir que pueda usarse"""
        self.block = True
        self.block_razon = razon

    def desbloquear(self):
        """Desbloquear el boton para que pueda volver a usarse"""
        self.block = False
        self.block_razon = None

    def mostrar(self):
        """Hacer el botón visible"""
        self.visible = True

    def ocultar(self):
        """Hacer el botón invisible (y, por ende, desactivado)"""
        self.visible = False

    def indexar(self, indice):
        """Cambiar el índice del botón"""
        if self.indice != indice:
            self.indice = indice
            self.renderizar()

    def actualizar(self):
        """Actualizar estado y propiedades del boton"""
        if not self.visible:
            return

        # Modificar estado (seleccionado / pulsado) y detectar cambios
        selec_antes    = self.selec
        pulsado_antes  = self.pulsado
        self.selec     = self.panel.raton()
        self.pulsado   = self.selec and g_click
        ha_selec       = not selec_antes and self.selec
        ha_pulsado     = not pulsado_antes and self.pulsado
        cambio_selec   = selec_antes != self.selec
        cambio_pulsado = pulsado_antes != self.pulsado
        cambio         = cambio_selec or cambio_pulsado

        # Reproducir sonidos
        if ha_selec and self.audio_sel:
            reproducir_sonido(self.audio_sel, 'interfaz')
        if ha_pulsado and self.audio_pul:
            reproducir_sonido(self.audio_pul, 'interfaz')
        if self.pulsado and self.block:
            emitir_error(self.block_razon)

        # Actualizar color y renderizar boton
        if cambio:
            if self.pulsado:
                self.panel.color = self.color_pulsado
            elif self.selec:
                self.panel.color = self.color_selec
            else:
                self.panel.color = self.color
            self.renderizar()

        # Mostrar información en el panel informativo
        if ha_selec and self.info:
            self.info()

        # Ejecutar acción si está pulsado
        if ha_pulsado and self.accion and not self.block:
            self.accion(*self.args)

        # Devolver si ha habido cambio de estado
        return cambio

    def renderizar(self):
        """Volver a renderizar el contenido del boton. Solo hace falta hacerlo cuando ha cambiado."""
        self.panel.renderizar()
        self.panel.lienzo.blit(self.imagen, ((self.anchura - self.tamaño[0]) / 2, (self.altura - self.tamaño[1]) / 2))
        if not self.indice:
            return
        fuente = g_fuentes[16]
        w1, h1 = self.dim
        w2, h2 = fuente.size(str(self.indice))
        Texto(str(self.indice), (w1 - 2, h1 - h2), 16, "#ff0000", alineado_h = 'd', surface = self.panel.lienzo).dibujar()

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

class Texto:
    """Representa un bloque de texto. Permite configurar el texto (tamaño, color, tipo, etc)
     y controlar los márgenes horizontales y verticales. Soporta múltiples líneas y páginas.
     OJO: Renderizar texto es lento, así que debe hacerse sólo cuando ha cambiado.
     Dibujarlo cada fotograma (blitearlo) es mucho más rápido, como cualquier superficie"""

    def __init__(self, cadena, posicion, tamaño = TEXTO_TAMANO, color = COLOR_TEXTO, alineado_h = 'i', alineado_v = 'a',
                 negrita = False, cursiva = False, subrayado = False, mono = False, surface = g_pantalla, max_ancho = None,
                 max_alto = None):

        # Inicializar miembros
        self.texto      = None # Cadena de texto
        self.pos        = None # Posición del texto en la superficie base (tupla de coordenadas)
        self.tamaño     = None # Tamaño de fuente del texto (entero)
        self.color      = None # Color del texto
        self.alineado_h = None # Alineacion horizontal [i(zquierda), c(entro), d(erecha)]
        self.alineado_v = None # Alineacion vertical [a(rriba), c(entro), b(ase)]
        self.negrita    = None # Usar tipo de fuente negrita (booleano)
        self.cursiva    = None # Usar tipo de fuente itálica (booleano)
        self.subrayado  = None # Usar tipo de fuente subrayado (booleano)
        self.mono       = None # Usar tipo de fuente monoespaciada (booleano)
        self.surface    = None # Superficie base donde se renderizará el texto
        self.max_ancho  = None # Margen horizontal del texto (en píxeles). Determinará las líneas.
        self.max_alto   = None # Margen vertical del texto (en líneas). Determinará las páginas.
        self.lineas     = None # Lista de líneas de texto (han de renderizarse por separado)
        self.imagenes   = None # Lista de líneas ya pre-renderizadas (superficies)
        self.paginas    = None # Número de páginas totales
        self.visible    = True # Renderizar o no el texto en pantalla

        # Configurar miembros
        self.editar(cadena, actualizar = False)
        self.escalar(tamaño, actualizar = False)
        self.tipar(negrita, cursiva, subrayado, mono, actualizar = False)
        self.mover(posicion, alineado_h, alineado_v)
        self.colorear(color, actualizar = False)
        self.marginar(max_ancho, actualizar = False)
        self.paginar(max_alto)
        self.surface = surface
        self.imagenes = []

        # Pre-renderizar texto
        self.renderizar()

    def editar(self, texto, actualizar = True):
        """Cambiar el contenido del texto"""
        if self.texto == texto:
            return
        self.texto = texto
        if actualizar:
            self.mover(self.pos, self.alineado_h, self.alineado_v)
            self.actualizar()

    def borrar(self):
        """Elimina el contenido del texto"""
        self.texto = ''

    def vacio(self):
        """Compueba si no hay caracteres en el texto"""
        return self.texto == ''

    def escalar(self, tamaño, actualizar = True):
        """Cambiar el tamaño del texto"""
        # Aseguramos que el tamaño de fuente deseado está disponible
        if self.tamaño == tamaño:
            return
        if not tamaño in TEXTO_TAMANOS:
            tamaño = TEXTO_TAMANO
        self.tamaño = tamaño
        if actualizar:
            self.actualizar()

    def tipar(self, negrita = None, cursiva = None, subrayado = None, mono = None, actualizar = True):
        """Cambiar el tipo de la fuente"""

        # Ver si se ha especificado realmente algún cambio de tipo
        cambio_negrita   = negrita   is not None and self.negrita   != negrita
        cambio_cursiva   = cursiva   is not None and self.cursiva   != cursiva
        cambio_subrayado = subrayado is not None and self.subrayado != subrayado
        cambio_mono      = mono      is not None and self.mono      != mono
        if not cambio_negrita and not cambio_cursiva and not cambio_subrayado and not cambio_mono:
            return

        # Guardar nuevos valores y actualizar
        if cambio_negrita:
            self.negrita = negrita
        if cambio_cursiva:
            self.cursiva = cursiva
        if cambio_subrayado:
            self.subrayado = subrayado
        if cambio_mono:
            self.mono = mono
        if actualizar:
            self.actualizar()

    def mover(self, posicion, alineado_h = 'i', alineado_v = 'a'):
        """Cambiar la posición del texto en la superficie base"""
        if type(posicion) is pygame.math.Vector2:
            posicion = posicion.xy
        self.pos = posicion
        self.alineado_h = alineado_h
        self.alineado_v = alineado_v

    def colorear(self, color, actualizar = True):
        """Cambiar el color del texto"""
        if self.color == color:
            return
        self.color = color
        if actualizar:
            self.actualizar()

    def marginar(self, max_ancho, actualizar = True):
        """Dividir el texto en líneas de la anchura deseada"""

        # Si no se especifica anchura máxima, forzamos una para que el algoritmo funcione
        self.max_ancho = max_ancho
        if not self.max_ancho:
            max_ancho = 1000000
        fuente = self.fuente()

        # Inicializar lista de palabras y líneas para preparar el algoritmo
        palabras = self.texto.split(' ')
        self.lineas = []
        linea_actual = ""

        # Iterar palabras y componer listado de líneas
        for palabra in palabras:
            if '\n' in palabra:
                sub_palabras = palabra.split('\n')
                for sub_palabra in sub_palabras[:-1]:
                    if fuente.size(linea_actual + sub_palabra)[0] <= max_ancho:
                        linea_actual += sub_palabra + " "
                    else:
                        self.lineas.append(linea_actual)
                        linea_actual = sub_palabra + " "
                    self.lineas.append(linea_actual)
                    linea_actual = ""
                linea_actual = sub_palabras[-1] + " "
            elif fuente.size(linea_actual + palabra)[0] <= max_ancho:
                linea_actual += palabra + " "
            else:
                self.lineas.append(linea_actual)
                linea_actual = palabra + " "
        self.lineas.append(linea_actual)

        # Opcionalmente, reparginar y renderizar el texto de nuevo, ya que las líneas han cambiado
        if actualizar:
            self.paginar()
            self.renderizar()

    def paginar(self, max_alto):
        """Cambiar el número de líneas por página, y en consecuencia, el número de páginas"""
        self.max_alto = max_alto
        if self.max_alto:
            self.paginas = max(math.ceil(len(self.lineas) / self.max_alto), 1)
        else:
            self.paginas = 1

    def fuente(self):
        """Obtener la fuente apropriada"""
        fuente = g_fuentes_mono[self.tamaño] if self.mono else g_fuentes[self.tamaño]
        fuente.underline = self.subrayado
        fuente.bold      = self.negrita
        fuente.italic    = self.cursiva
        return fuente

    def renderizar(self):
        """Renderizar la superficie del texto. Sólo hacer cuando haya un cambio."""
        fuente = self.fuente()
        self.imagenes = [fuente.render(linea, True, self.color) for linea in self.lineas]

    def actualizar(self):
        """Actualizar el texto. Debe llamarse cada vez que haya un cambio (de texto, de fuente, etc)"""
        self.marginar(self.max_ancho, actualizar = False)
        self.paginar(self.max_alto)
        self.renderizar()

    def mostrar(self):
        """Hacer el texto visible en pantalla"""
        self.visible = True

    def ocultar(self):
        """No dibujar el texto en pantalla"""
        self.visible = False

    def dibujar(self, pagina = 0):
        """Dibujar el texto en pantalla. Hacer todos los fotogramas."""
        if not self.visible:
            return
        fuente = self.fuente()
        salto = fuente.get_linesize()
        imagenes = self.imagenes[self.max_alto * pagina : self.max_alto * (pagina + 1)] if self.max_alto else self.imagenes
        for i, imagen in enumerate(imagenes):
            x, y = self.pos
            dx, dy = imagen.get_size()
            x -= (dx if self.alineado_h == 'd' else dx / 2 if self.alineado_h == 'c' else 0)
            y -= (dy if self.alineado_v == 'b' else dy / 2 if self.alineado_v == 'c' else 0)
            self.surface.blit(imagen, (x, y + i * salto))

class Ayuda:
    """Representa un pequeño recuadro de ayuda on texto que se muestra al
     pasar el ratón por encima de algunos objetos"""

    COLOR_FONDO = "#ffffc0"
    COLOR_BORDE = "#000000"
    COLOR_TEXTO = "#000000"
    TAMANO_TEXTO = 16

    def __init__(self, texto):
        self.texto = Texto(texto, (0, 0), self.TAMANO_TEXTO, self.COLOR_TEXTO)
        self.visible = False

    def cambiar(self, texto):
        """Modificar el texto de la ayuda"""
        if self.texto != texto:
            self.texto.editar(texto)

    def mostrar(self):
        """Hacer el recuadro de ayuda visible"""
        self.visible = True

    def ocultar(self):
        """Dejar de mostrar el recuadro de ayuda"""
        self.visible = False

    def dibujar(self):
        """Dibujar el recuadro de ayuda en pantalla"""
        if not self.visible:
            return
        x, y = g_raton[0] - 80, g_raton[1] + 20
        lineas = self.texto.imagenes
        anchura = max(linea.get_width() for linea in lineas)
        altura = sum(linea.get_height() for linea in lineas)
        pygame.draw.rect(g_pantalla, self.COLOR_FONDO, (x, y, anchura, altura))
        pygame.draw.rect(g_pantalla, self.COLOR_BORDE, (x, y, anchura, altura), 1)
        self.texto.mover((x + 2, y - 1))
        self.texto.dibujar()

# < -------------------------------------------------------------------------- >
#                         FUNCIONES AUXILIARES INTERFAZ
# < -------------------------------------------------------------------------- >

def tiempo():
    """Milisegundos (entero) desde inicio del programa"""
    return round(pygame.time.get_ticks())

def entre(n, a, b):
    """Mete el numero n en el intervalo [a, b]"""
    return min(max(a, n), b)

def cambiar_musica():
    """Mutear o no la música de fondo"""
    if g_config['musica']:
        pygame.mixer.music.set_volume(0)
        g_config['musica'] = False
    else:
        pygame.mixer.music.set_volume(MUSICA_VOLUMEN)
        g_config['musica'] = True

def emitir_error(texto = None):
    """Emitir un mensaje y sonido de error"""
    if texto:
        g_info.error(texto)
    reproducir_sonido('error', 'interfaz')

def emitir_fin():
    """Mensaje de error a emitir cuando la partida ya ha concluido"""
    emitir_error('La partida ya ha terminado, pulsa "Reiniciar" para comenzar otra')

# < -------------------------------------------------------------------------- >
#                       ACTUALIZACION DEL ESTADO DEL JUEGO
# < -------------------------------------------------------------------------- >

def actualizar_fondo():
    """Dibujar el fondo (primera capa del display)"""
    g_pantalla.fill(COLOR_FONDO)

def siguiente_fotograma():
    """Avanzar fotograma"""
    pygame.display.flip()   # Renderizar fotograma en pantalla y cambiar buffer
    g_reloj.tick(FPS)       # Avanzar reloj y limitar frecuencia de fotogramas

def siguiente_jugador():
    """Cambiar de turno"""
    global g_jugador, g_adversario
    if g_fase == 'Final':
        emitir_fin()
        return
    if not g_jugador:
        g_jugador = g_jugadores[0]
        g_adversario = g_jugadores[1]
    elif verificar_turno():
        g_jugador, g_adversario = g_adversario, g_jugador
    else:
        return
    g_info.info(f"Turno del jugador {g_jugador.indice + 1}")
    g_info.actualizar_texto()
    g_tienda.actualizar_textos()
    g_escenario.renderizar()
    if g_paso:
        resetear_paso()

def siguiente_fase():
    """Avanzar a la siguiente fase del juego"""
    global g_fase
    indice = g_fases.index(g_fase)
    if indice < len(g_fases) - 1:
        cambiar_fase(g_fases[indice + 1])
    else:
        resetear_fase()

def cambiar_fase(nombre):
    """Cambiar a otra fase del juego"""
    global g_fase
    if nombre in g_fases:
        g_fase = nombre
        if g_fase not in ['Pantallazo', 'Reglas']:
            g_info.info(f'Iniciada fase "{nombre}"')
            g_info.actualizar_texto()
        return True
    return False

def resetear_fase():
    """Volver a la primera fase del juego"""
    cambiar_fase('Preparación')

def siguiente_paso(manual = True):
    """Avanzar al siguiente paso del turno"""
    if g_fase == 'Final':
        emitir_fin()
        return
    if g_fase != 'Principal':
        emitir_error('Sólo la fase principal tiene pasos')
        return
    global g_paso
    indice = g_pasos.index(g_paso)
    if indice < len(g_pasos) - 1:
        cambiar_paso(g_pasos[indice + 1])
    elif manual:
        emitir_error('Ya no hay más pasos, juega para cambiar de turno')

def cambiar_paso(nombre):
    """Cambiar a otro paso del turno"""
    global g_paso, g_paso_listo
    if nombre in g_pasos:
        g_paso = nombre
        g_info.info(f'Iniciado paso "{nombre}"')
        g_info.actualizar_texto()
        g_paso_listo = False
        return True
    return False

def resetear_paso():
    """Volver al primer paso del turno"""
    cambiar_paso('Reporte')

def actualizar_variables():
    """Actualizacion de variables en cada fotograma"""
    global g_raton
    g_ayuda.ocultar()
    g_raton = pygame.mouse.get_pos()

def actualizar_interfaz():
    """Actualizar los paneles y el contenido del escenario, tienda e información"""
    # Actualizar estado sólo si el escenario es visible
    if not g_reglas.visible:
        if g_fase != 'Final':
            g_escenario.actualizar()
            g_tienda.actualizar()
        g_info.actualizar()

    # Dibujar contenido de los paneles
    g_escenario.dibujar()
    g_tienda.dibujar()
    g_info.dibujar()

    # Paneles adicionales opcionales
    if g_fase != 'Final':
        g_ayuda.dibujar()
    if g_reglas.visible:
        actualizar_fase_reglas()

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

def actualizar_fase_preparacion():
    """Actualizar estado en la fase preparatoria"""
    if not g_jugador:
        siguiente_jugador()

    # Saltar la fase preparatoria, para testear
    if SALTAR_PREPARACION:
        g_jugador.preparar()
        siguiente_jugador()
        return

    # Actualizar paneles y contenido del escenario, tienda e información
    actualizar_interfaz()

def actualizar_fase_principal():
    """Actualizar estado en la fase de turnos"""
    # Comenzamos el primer paso si acabamos de iniciar la fase
    if not g_paso:
        cambiar_paso('Reporte')
    if not g_jugador:
        siguiente_jugador()

    # Actualizar paneles y contenido del escenario, tienda e información
    actualizar_interfaz()

    # Actualizar paso específico del turno, si hace falta
    if g_paso_listo:
        return
    if g_paso == 'Reporte':
        actualizar_paso_reporte()
    elif g_paso == 'Inteligencia':
        actualizar_paso_inteligencia()
    elif g_paso == 'Ingresos':
        actualizar_paso_ingresos()
    elif g_paso == 'Recursos':
        actualizar_paso_recursos()
    elif g_paso == 'Despliegue':
        actualizar_paso_despliegue()

def actualizar_fase_final():
    """Actualizar estado en la fase final (partida terminada)"""
    actualizar_interfaz()

def actualizar_paso_reporte():
    """Desarrollar el paso de reporte. El jugador recibe un reporte
    informativo del movimiento del adversario."""
    global g_paso_listo
    for reporte in set(g_jugador.reporte):
        g_info.reporte(reporte)
    g_jugador.validar_reporte()
    g_paso_listo = True

def actualizar_paso_inteligencia():
    """Desarrollar el paso de inteligencia. El jugador recibe información adicional
    en función del nivel de inteligencia que haya adquirido."""
    global g_paso_listo
    if g_jugador.inteligencia >= 1:
        g_info.intel(f'I1: Tu adversario ha cosechado {g_adversario.cosechado}M€')
    if g_jugador.inteligencia >= 2:
        nivel_capital  = [str(infra.nivel) for infra in g_adversario.infraestructuras if type(infra) is Capital][0]
        nivel_ciudades = ', '.join([str(infra.nivel) for infra in g_adversario.infraestructuras if type(infra) is Ciudad])
        nivel_bases    = ', '.join([str(infra.nivel) for infra in g_adversario.infraestructuras if type(infra) is Base])
        g_info.intel(f'I2: Infraestructuras adversarias: Capital ({nivel_capital}), Ciudades ({nivel_ciudades}), Bases ({nivel_bases}).')
    if g_jugador.inteligencia >= 3:
        medios_aereos      = sum(1 for medio in g_adversario.medios if isinstance(medio, MedioAereo))
        medios_desplegados = sum(1 for medio in g_adversario.medios if isinstance(medio, MedioAereo) and medio.desplegado)
        medios_antiaereos  = sum(1 for medio in g_adversario.medios if isinstance(medio, MedioAntiaereo))
        g_info.intel(f'I3: Medios adversarios: Aéreos ({medios_aereos}, {medios_desplegados} desplegados), Anti-aéreos ({medios_antiaereos})')
    if g_jugador.inteligencia >= 4:
        if len(g_adversario.medios) == 0:
            g_info.intel('I4: Tu adversario no tiene medios')
        else:
            medio = random.sample(g_adversario.medios, 1)[0]
            estado = '' if isinstance(medio, MedioAntiaereo) else ' desplegado' if medio.desplegado else ' estacionado'
            g_info.intel(f'I4: Tu adversario tiene un {medio.NOMBRE}{estado} en la casilla {medio.casilla.id()}')
    if g_jugador.inteligencia >= 5:
        g_info.intel(f'I5: Tu adversario tiene inteligencia de nivel {g_adversario.inteligencia}')
    g_paso_listo = True

def actualizar_paso_ingresos():
    """Desarrollar el paso de ingresos. El jugador cosecha crédito adicional gracias
    a las casillas en las que tenga superioridad / supremacia aérea, así como sus ciudades."""
    global g_paso_listo
    g_jugador.cosechar()
    g_paso_listo = True

def actualizar_paso_recursos():
    """Desarrollar el paso de recursos. El jugador invierte crédito en adquirir medios
    aéreos, antiaéreos o estratégicos - como inteligencia o infraestructuras."""
    pass

def actualizar_paso_despliegue():
    """Desarrollar el paso de despliegue. El jugador moviliza aeronaves en alguna casilla."""
    pass

def verificar_turno():
    """Comprobar que el jugador ha realizado un turno válido y podemos pasar al siguiente"""
    if g_fase == "Preparación":
        # Verificar que se han construido las infraestructuras iniciales necesarias
        cantidades = { Capital: 0, Ciudad: 0, Base: 0 }
        for infra in g_jugador.infraestructuras:
            cantidades[type(infra)] += 1
        if cantidades[Capital] < Capital.CANTIDAD or cantidades[Ciudad] < Ciudad.CANTIDAD or cantidades[Base] < Base.CANTIDAD:
            emitir_error(f"Necesitas {Capital.CANTIDAD} capital, {Ciudad.CANTIDAD} ciudades y {Base.CANTIDAD} bases aéreas.")
            return False
        g_jugador.preparado = True
    elif g_fase == 'Principal':
        # Actualizar los medios aéreos del jugador (turnos, aterrizajes automáticos...)
        for medio in g_jugador.medios:
            if isinstance(medio, MedioAereo):
                medio.actualizar()
        # Llevar a cabo vigilancias de los medios del adversario
        for medio in g_adversario.medios:
            medio.vigilar()
    return True

def resetear():
    """
        Resetear la partida por completo.
        Tenemos que reinicializar todos los objetos del juego.
        El orden puede ser importante.
    """
    global g_jugador
    for jugador in g_jugadores:
        jugador.resetear()
    g_reglas.resetear()
    g_escenario.resetear()
    g_tienda.resetear()
    g_info.resetear()
    resetear_fase()
    g_jugador = None
    siguiente_jugador()

def terminar():
    """Terminar la partida, realizar el conteo de puntos y determinar el ganador"""
    if g_fase == 'Final':
        emitir_fin()
        return
    cambiar_fase('Final')
    g_info.info('Partida terminada')
    puntos = [jugador.puntuar() for jugador in g_jugadores]
    if puntos[0] == puntos[1]:
        g_info.info('¡Los jugadores han empatado!')
    else:
        g_info.info(f'¡Victoria para el jugador {puntos.index(max(puntos)) + 1}!')

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
    'informacion': Panel((sep, ALTURA * ALTURA_JUEGO + sep / 2), (ANCHURA - 2 * sep, ALTURA * ALTURA_INFORMACION - 1.5 * sep), textura='piedras')
}

# Inicializar variables globales para que estén disponibles
g_fase       = None  # Fase actual del juego
g_paso       = None  # Paso actual de la fase principal
g_paso_listo = False # Indica que el paso ha concluido
g_jugador    = None  # Jugador actual
g_adversario = None  # Jugador contrincante
g_reglas     = None  # Paginador de reglas
g_escenario  = None  # Casillas del mapa y su contenido
g_info       = None  # Panel informativo inferior
g_tienda     = None  # Tienda de productos

# Fases y pasos del juego. Los pasos son las distintas etapas en las que se divide un turno.
g_fases = ['Pantallazo', 'Reglas', 'Preparación', 'Principal', 'Final']
g_pasos = ['Reporte', 'Inteligencia', 'Ingresos', 'Recursos', 'Despliegue']
cambiar_fase('Pantallazo')

# Jugadores de la partida
g_jugadores  = [Jugador() for _ in range(2)]

# Principales partes de la interfaz (no cambiar estas líneas de orden!)
g_reglas    = Reglamento()
g_escenario = Escenario(paneles['escenario'])
g_info      = Informacion(paneles['informacion'])
g_tienda    = Tienda(paneles['tienda'])

# Configuracion
g_config = {
    'musica': MUSICA_REPRODUCIR
}

# Estado
g_ayuda = Ayuda('')
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
    if g_fase == 'Pantallazo':            # Pantallazo inicial
        actualizar_fase_pantallazo()
        if g_click:
            siguiente_fase()
    elif g_fase == 'Reglas':              # Pantallazo de reglas
        actualizar_fase_reglas()
        if not g_reglas.visible:
            siguiente_fase()
    elif g_fase == 'Preparación':         # Fase preparativa inicial
        actualizar_fase_preparacion()
        if sum(1 for jugador in g_jugadores if jugador.preparado) == 2:
            siguiente_fase()
    elif g_fase == 'Principal':           # Fase central del juego
        actualizar_fase_principal()
    else:
        actualizar_fase_final()           # Partida terminada

    siguiente_fotograma()