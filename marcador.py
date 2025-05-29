import turtle

def crear_marcador():
    marcador = turtle.Turtle()
    marcador.speed(0)
    marcador.color("white")
    marcador.penup()
    marcador.hideturtle()
    marcador.goto(0, 255)
    marcador.write("0    0", align="center", font=("Courier", 40, "bold"))
    return marcador

def actualizar_marcador(marcador, m1, m2):
    marcador.clear()
    marcador.write(f"{m1}    {m2}", align="center", font=("Courier", 40, "bold"))
