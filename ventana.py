import turtle
from config import VENTANA_ANCHO, VENTANA_ALTO, FONDO_IMG

def crear_ventana():
    ventana = turtle.Screen()
    ventana.title("Pong")
    ventana.setup(width=VENTANA_ANCHO, height=VENTANA_ALTO)
    ventana.tracer(0)
    ventana.bgpic(FONDO_IMG)
    return ventana

    VENTANA_ANCHO = 1200
    VENTANA_ALTO = 700
    COLOR_FONDO = "black"
    FONDO_IMG = "cancha.gif"