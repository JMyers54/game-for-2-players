import turtle 
from tkinter import *
import tkinter as tk

#Crear la ventana
class Juego():
    def __init__(self):

        ventana = turtle.Screen()
        ventana.title("Pong")
        ventana.setup(width=1200, height=700)
        ventana.tracer(0)
        ventana.bgpic("cancha.gif")

#marcador
        marcador1 = 0
        marcador2 = 0

        #Pelota
        pelota = turtle.Turtle()
        pelota.speed(0)
        pelota.shape("circle")
        pelota.color("white")
        pelota.penup()
        pelota.goto(0,0)
        pelota.dx = 1.5
        pelota.dy = 1.5

        #Lineas
        linea = turtle.Turtle()
        linea.color("white")
        linea.goto(0,400)
        linea.goto(0,-400)

        #Jugador de la izquierda
        jugador1 = turtle.Turtle()
        jugador1.speed(0)
        jugador1.shape("square")
        jugador1.color("blue")
        jugador1.penup()
        jugador1.goto(-545,0)
        jugador1.shapesize(stretch_wid=5, stretch_len=1)
        jugador1.pencolor("black")

        #Jugador de la derecha
        jugador2 = turtle.Turtle()
        jugador2.speed(0)
        jugador2.shape("square")
        jugador2.color("red")
        jugador2.penup()
        jugador2.goto(540,0)
        jugador2.shapesize(stretch_wid=5, stretch_len=1)
        jugador2.pencolor("black")

        #Marcador
        marcador = turtle.Turtle()
        marcador.speed(0)
        marcador.color("white")
        marcador.penup()
        marcador.hideturtle()
        marcador.goto(0,255)
        marcador.write("0    0", align="center", font=("Courier", 40, "bold"))

        #Movimientos
        def jugador1_arriba():
            y = jugador1.ycor()
            y += 25
            jugador1.sety(y)
            
        def jugador1_abajo():
            y = jugador1.ycor()
            y -= 25
            jugador1.sety(y)

        def jugador2_arriba():
            y = jugador2.ycor()
            y += 25
            jugador2.sety(y)
            
        def jugador2_abajo():
            y = jugador2.ycor()
            y -= 25
            jugador2.sety(y)

        #teclado
        ventana.listen()
        ventana.onkeypress(jugador1_arriba, "w")
        ventana.onkeypress(jugador1_abajo, "s")
        ventana.onkeypress(jugador2_arriba, "Up")
        ventana.onkeypress(jugador2_abajo, "Down")
        while True:
            ventana.update()
            
            pelota.setx(pelota.xcor() + pelota.dx)
            pelota.sety(pelota.ycor() + pelota.dy)
            
            #Bordes de arriba y abajo
            if pelota.ycor() > 305:
                pelota.dy *= -1
            if pelota.ycor() < -305:
                pelota.dy *= -1
                
            #Bordes del lado arriba y abajo
            if ((pelota.xcor() < -550 and pelota.xcor() > -600)
                and (pelota.ycor() < 260 + 70
                and pelota.ycor() > 260 - 70)):
                pelota.dx *= -1 
            
            if ((pelota.xcor() < -550 and pelota.xcor() > -600)
                and (pelota.ycor() < -255 + 70
                and pelota.ycor() > -255 - 70)):
                pelota.dx *= -1 
                
            if ((pelota.xcor() > 530 and pelota.xcor() < 600)
                and (pelota.ycor() < -255 + 70
                and pelota.ycor() > -255 - 70)):
                pelota.dx *= -1 

            if ((pelota.xcor() > 530 and pelota.xcor() < 600)
                and (pelota.ycor() < 260 + 65
                and pelota.ycor() > 260 - 65)):
                pelota.dx *= -1 
            
            #Marcador
            if pelota.xcor() > 600:
                pelota.goto(0,0)
                pelota.dx *= -1
                marcador1 += 1
                marcador.clear()
                marcador.write(f"{marcador1}    {marcador2}", align="center", font=("Courier", 40, "bold"))
                
            if pelota.xcor() < -600:
                pelota.goto(0,0)
                pelota.dx *= -1
                marcador2 += 1
                marcador.clear()
                marcador.write(f"{marcador1}    {marcador2}", align="center", font=("Courier", 40, "bold"))
                
            #Bordes para las barras de los jugadores
            if jugador1.ycor() > 300:
                jugador1.goto(-540, 290)
            
            if jugador1.ycor() < -300:
                jugador1.goto(-540, -290)
                
            if jugador2.ycor() > 300:
                jugador2.goto(540, 290)
            
            if jugador2.ycor() < -300:
                jugador2.goto(540, -290)
            
            #Colisiones con las barras
            if ((pelota.xcor() > 520 and pelota.xcor() < 550)
                and (pelota.ycor() < jugador2.ycor() + 60
                and pelota.ycor() > jugador2.ycor() - 60)):
                pelota.dx *= -1  
                
            if ((pelota.xcor() < -520 and pelota.xcor() > -550)
                and (pelota.ycor() < jugador1.ycor() + 60
                and pelota.ycor() > jugador1.ycor() - 60)):
                pelota.dx *= -1