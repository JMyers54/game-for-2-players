


class Configuraciones():
    def __init__(self):
    
    def configurar_controles(ventana, jugador1, jugador2):
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

        ventana.listen()
        ventana.onkeypress(jugador1_arriba, "w")
        ventana.onkeypress(jugador1_abajo, "s")
        ventana.onkeypress(jugador2_arriba, "Up")
        ventana.onkeypress(jugador2_abajo, "Down")