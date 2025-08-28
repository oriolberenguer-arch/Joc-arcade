import turtle
import menu_pong

def jugar_pong(puntuacio_max):
    # Configuració de la pantalla
    wn = turtle.Screen()
    wn.title("Pong")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)  # línia provisional
    # codi real --> wn._root.attributes('-fullscreen', True)

    # Configuració pales i pilota
    pala1 = turtle.Turtle()
    pala1.speed(0)
    pala1.shape("square")
    pala1.color("white")
    pala1.shapesize(stretch_wid=5, stretch_len=0.5)
    pala1.penup()
    pala1.goto(-350, 0)

    pala2 = turtle.Turtle()
    pala2.speed(0)
    pala2.shape("square")
    pala2.color("white")
    pala2.shapesize(stretch_wid=5, stretch_len=0.5)
    pala2.penup()
    pala2.goto(350, 0)

    bola = turtle.Turtle()
    bola.speed(0)
    bola.shape("square")
    bola.color("white")
    bola.penup()
    bola.goto(0, 0)
    bola.dx = 3
    bola.dy = 3

    # Puntuació
    puntuacio1 = 0
    puntuacio2 = 0
    punt = turtle.Turtle()
    punt.speed(0)
    punt.color("white")
    punt.penup()
    punt.hideturtle()
    punt.goto(0, 260)
    punt.write(f"Jugador 1:{puntuacio1}          Jugador 2:{puntuacio2}", align="center", font=("Courier", 24, "normal"))

    # Funció per moure les pales
    def pala1_amunt():
        y = pala1.ycor()
        if y < 260:
            y += 20
            pala1.sety(y)

    def pala1_avall():
        y = pala1.ycor()
        if y > -240:
            y -= 20
            pala1.sety(y)

    def pala2_amunt():
        y = pala2.ycor()
        if y < 260:
            y += 20
            pala2.sety(y)

    def pala2_avall():
        y = pala2.ycor()
        if y > -240:
            y -= 20
            pala2.sety(y)

    wn.listen()
    wn.onkeypress(pala1_amunt, "w")
    wn.onkeypress(pala1_avall, "s")
    wn.onkeypress(pala2_amunt, "Up")
    wn.onkeypress(pala2_avall, "Down")

    # Bucle principal
    x = True
    while x:
        wn.update()
        bola.setx(bola.xcor() + bola.dx)
        bola.sety(bola.ycor() + bola.dy)

        # Rebot amb parets superior/inferior
        if bola.ycor() > 290:
            bola.sety(290)
            bola.dy *= -1
        if bola.ycor() < -280:
            bola.sety(-280)
            bola.dy *= -1

        # Punt per jugador 1
        if bola.xcor() > 380:
            bola.setx(380)
            bola.dx *= -1
            puntuacio1 += 1
            punt.clear()
            punt.write("Jugador 1:{}          Jugador 2:{}".format(puntuacio1, puntuacio2),
                       align="center", font=("Courier", 24, "normal"))
            bola.goto(0, 0)

        # Punt per jugador 2
        if bola.xcor() < -390:
            bola.setx(-390)
            bola.dx *= -1
            puntuacio2 += 1
            punt.clear()
            punt.write("Jugador 1:{}          Jugador 2:{}".format(puntuacio1, puntuacio2),
                       align="center", font=("Courier", 24, "normal"))
            bola.goto(0, 0)

        # Comprovació final del joc
        if puntuacio1 == puntuacio_max or puntuacio2 == puntuacio_max:
            bola.dx = 0
            bola.dy = 0
            punt.goto(0, 0)
            if puntuacio1 == puntuacio_max:
                punt.write("JUGADOR 1 GUANYADOR", align="center", font=("Courier", 48, "normal"))
            else:
                punt.write("JUGADOR 2 GUANYADOR", align="center", font=("Courier", 48, "normal"))
            x = False

        # Xocs entre pala i bola
        if bola.xcor() < -330 and pala1.ycor() - 50 < bola.ycor() < pala1.ycor() + 50:
            bola.dx *= -1
            bola.setx(-330)

        elif bola.xcor() > 330 and pala2.ycor() - 50 < bola.ycor() < pala2.ycor() + 50:
            bola.dx *= -1
            bola.setx(330)

    # Manté la finestra oberta després de finalitzar
    wn.mainloop()

