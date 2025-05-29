from ventana import crear_ventana
from jugadores import crear_jugador
from pelota import crear_pelota
from marcador import crear_marcador, actualizar_marcador
from controles import configurar_controles

class Juego(): 
    def __init__(self): 
        self.ventana = crear_ventana()
        self.jugador1 = crear_jugador(-545, "blue")
        self.jugador2 = crear_jugador(540, "red")
        self.pelota = crear_pelota()
        self.marcador = crear_marcador()
        self.configurar_controles(self.ventana, self.jugador1, self.jugador2)

        marcador1 = 0
        marcador2 = 0

        while True:
            self.ventana.update()

            self.pelota.setx(self.pelota.xcor() + self.pelota.dx)
            self.pelota.sety(self.pelota.ycor() + self.pelota.dy)

            # Rebote arriba/abajo
            if self.pelota.ycor() > 305 or self.pelota.ycor() < -305:
                self.pelota.dy *= -1

            # Gol
            if self.pelota.xcor() > 600:
                self.pelota.goto(0, 0)
                self.pelota.dx *= -1
                marcador1 += 1
                actualizar_marcador(self.marcador, marcador1, marcador2)

            if self.pelota.xcor() < -600:
                self.pelota.goto(0, 0)
                self.pelota.dx *= -1
                marcador2 += 1
                actualizar_marcador(self.marcador, marcador1, marcador2)

            # Rebote en paletas
            if ((self.pelota.xcor() > 520 and self.pelota.xcor() < 550) and 
                (self.pelota.ycor() < self.jugador2.ycor() + 60 and self.pelota.ycor() > self.jugador2.ycor() - 60)):
                self.pelota.dx *= -1

            if ((self.pelota.xcor() < -520 and self.pelota.xcor() > -550) and 
                (self.pelota.ycor() < self.jugador1.ycor() + 60 and self.pelota.ycor() > self.jugador1.ycor() - 60)):
                self.pelota.dx *= -1

            # Limitar movimiento de jugadores
            if self.jugador1.ycor() > 300:
                self.jugador1.sety(290)
            if self.jugador1.ycor() < -300:
                self.jugador1.sety(-290)
            if self.jugador2.ycor() > 300:
                self.jugador2.sety(290)
            if self.jugador2.ycor() < -300:
                self.jugador2.sety(-290)