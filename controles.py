def configurar_controles(ventana, jugador1, jugador2):
    def jugador1_arriba():
        y = jugador1.ycor()
        jugador1.sety(y + 25)

    def jugador1_abajo():
        y = jugador1.ycor()
        jugador1.sety(y - 25)

    def jugador2_arriba():
        y = jugador2.ycor()
        jugador2.sety(y + 25)

    def jugador2_abajo():
        y = jugador2.ycor()
        jugador2.sety(y - 25)

    ventana.listen()
    ventana.onkeypress(jugador1_arriba, "w")
    ventana.onkeypress(jugador1_abajo, "s")
    ventana.onkeypress(jugador2_arriba, "Up")
    ventana.onkeypress(jugador2_abajo, "Down")