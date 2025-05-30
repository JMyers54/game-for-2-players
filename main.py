from ventana import crear_ventana
from pelota import crear_pelota
from jugadores import crear_jugador
from marcador import crear_marcador
from controles import configurar_controles

# Crear ventana
ventana = crear_ventana()

# Crear elementos del juego
pelota = crear_pelota()
jugador1 = crear_jugador(-545, "blue")
jugador2 = crear_jugador(540, "red")
marcador, marcador1, marcador2 = crear_marcador()

# Configurar controles
configurar_controles(ventana, jugador1, jugador2)

# Bucle principal del juego
while True:
    ventana.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Rebote arriba/abajo
    if pelota.ycor() > 305 or pelota.ycor() < -305:
        pelota.dy *= -1

    # Puntos
    if pelota.xcor() > 600:
        pelota.goto(0, 0)
        pelota.dx *= -1
        marcador1 += 1
        marcador.clear()
        marcador.write(f"{marcador1}    {marcador2}", align="center", font=("Courier", 40, "bold"))

    if pelota.xcor() < -600:
        pelota.goto(0, 0)
        pelota.dx *= -1
        marcador2 += 1
        marcador.clear()
        marcador.write(f"{marcador1}    {marcador2}", align="center", font=("Courier", 40, "bold"))

    # Limites para jugadores
    if jugador1.ycor() > 300:
        jugador1.sety(290)
    if jugador1.ycor() < -300:
        jugador1.sety(-290)
    if jugador2.ycor() > 300:
        jugador2.sety(290)
    if jugador2.ycor() < -300:
        jugador2.sety(-290)

    # Colisión con paletas
    if ((pelota.xcor() > 520 and pelota.xcor() < 550)
            and (jugador2.ycor() - 60 < pelota.ycor() < jugador2.ycor() + 60)):
        pelota.dx *= -1

    if ((pelota.xcor() < -520 and pelota.xcor() > -550)
            and (jugador1.ycor() - 60 < pelota.ycor() < jugador1.ycor() + 60)):
        pelota.dx *= -1
