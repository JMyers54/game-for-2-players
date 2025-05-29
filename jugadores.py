import turtle

def crear_jugador(x, color):
    jugador = turtle.Turtle()
    jugador.speed(0)
    jugador.shape("square")
    jugador.color(color)
    jugador.penup()
    jugador.goto(x, 0)
    jugador.shapesize(stretch_wid=5, stretch_len=1)
    jugador.pencolor("black")
    return jugador