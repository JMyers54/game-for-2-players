import turtle

def crear_pelota():
    pelota = turtle.Turtle()
    pelota.speed(0)
    pelota.shape("circle")
    pelota.color("white")
    pelota.penup()
    pelota.goto(0, 0)
    pelota.dx = 1.5
    pelota.dy = 1.5
    return pelota