import turtle

def crear_marcador():
    marcador = turtle.Turtle()
    marcador.speed(0)
    marcador.color("white")
    marcador.penup()
    marcador.hideturtle()
    marcador.goto(0, 255)
    marcador.write("0    0", align="center", font=("Courier", 40, "bold"))
    return marcador, 0, 0
