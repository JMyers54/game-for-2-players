import turtle

def crear_ventana():
    ventana = turtle.Screen()
    ventana.title("Pong")
    ventana.setup(width=1200, height=700)
    ventana.bgcolor("black")
    ventana.tracer(0)

    # Dibujar línea central punteada
    linea = turtle.Turtle()
    linea.color("white")
    linea.penup()
    linea.hideturtle()
    linea.goto(0, 350)
    linea.setheading(270)

    for _ in range(30):
        linea.pendown()
        linea.forward(15)
        linea.penup()
        linea.forward(15)

    # Línea superior
    borde_sup = turtle.Turtle()
    borde_sup.hideturtle()
    borde_sup.color("white")
    borde_sup.penup()
    borde_sup.goto(-600, 340)
    borde_sup.pendown()
    borde_sup.forward(1200)

    # Línea inferior
    borde_inf = turtle.Turtle()
    borde_inf.hideturtle()
    borde_inf.color("white")
    borde_inf.penup()
    borde_inf.goto(-600, -340)
    borde_inf.pendown()
    borde_inf.forward(1200)

    return ventana