import turtle
import random
import pong_ai_final

def jugar_pong(puntuacio_max, dificultat):
    # Configuració de la pantalla
    wn = turtle.Screen()
    wn.title("Pong")
    wn.bgcolor("black")
    wn._root.attributes('-fullscreen', True)

    # Configuració pales i pilota
    pala1 = turtle.Turtle()
    pala1.speed(0)
    pala1.shape("square")
    pala1.color("white")
    pala1.shapesize(stretch_wid=7.5, stretch_len=0.75)
    pala1.penup()
    pala1.goto(-600, 0)

    pala2 = turtle.Turtle()
    pala2.speed(0)
    pala2.shape("square")
    pala2.color("white")
    pala2.shapesize(stretch_wid=7.5, stretch_len=0.75)
    pala2.penup()
    pala2.goto(600, 0)

    bola = turtle.Turtle()
    bola.speed(0)
    bola.shape("square")
    bola.color("white")
    bola.penup()
    bola.goto(0, 0)
    bola.dx = 3.5
    bola.dy = 3.5
    bola.shapesize(stretch_wid=1.35, stretch_len=1.35)

    # Puntuació
    puntuacio1 = 0
    puntuacio2 = 0
    punt = turtle.Turtle()
    punt.speed(0)
    punt.color("white")
    punt.penup()
    punt.hideturtle()
    punt.goto(0, 300)
    punt.write(f"Jugador 1:{puntuacio1}          Jugador 2:{puntuacio2}", align="center", font=("Courier", 36, "normal"))

    # Funció per moure les pales
    def pala1_amunt():
        y = pala1.ycor()
        if y < 310:
            y += 20
            pala1.sety(y)

    def pala1_avall():
        y = pala1.ycor()
        if y > -300:
            y -= 20
            pala1.sety(y)

    def pala2_amunt():
        y = pala2.ycor()
        if y < 310:
            y += 20
            pala2.sety(y)

    def pala2_avall():
        y = pala2.ycor()
        if y > -300:
            y -= 20
            pala2.sety(y)

    wn.listen()
    wn.onkeypress(pala1_amunt, "w")
    wn.onkeypress(pala1_avall, "s")


    # Bucle principal
    x = True
    while x:
        wn.update()
        bola.setx(bola.xcor() + bola.dx)
        bola.sety(bola.ycor() + bola.dy)


        # Moviment de la IA
        if bola.xcor() > 100:  # Només quan la pilota està a la seva meitat
            error = random.randint(-dificultat, dificultat) # Com més gran, més fàcil
            if bola.ycor() > pala2.ycor() + 10 + error:
                pala2.sety(pala2.ycor() + 12)
            elif bola.ycor() < pala2.ycor() - 10 + error:
                pala2.sety(pala2.ycor() - 12)

        # Rebot amb parets superior/inferior
        if bola.ycor() > 370:
            bola.sety(370)
            bola.dy *= -1
        if bola.ycor() < -360:
            bola.sety(-360)
            bola.dy *= -1

        # Punt per jugador 1
        if bola.xcor() > 660:
            puntuacio1 += 1
            bola.setx(660)
            bola.dx *= -1
            # Fem que cada ronda la pilota vagi més ràpida
            if bola.dx > 0:
                bola.dx = 3.5 + (puntuacio1 + puntuacio2)/4
                bola.dy = 3.5 + (puntuacio1 + puntuacio2)/4
            else:
                bola.dx = -3.5 - (puntuacio1 + puntuacio2)/4
                bola.dy = -3.5 - (puntuacio1 + puntuacio2)/4
            punt.clear()
            punt.write("Jugador 1:{}          Jugador 2:{}".format(puntuacio1, puntuacio2),
                       align="center", font=("Courier", 36, "normal"))
            bola.goto(0, 0)

        # Punt per jugador 2
        if bola.xcor() < -670:
            puntuacio2 += 1
            bola.setx(-670)
            bola.dx *= -1
            # Fem que cada ronda la pilota vagi més ràpida
            if bola.dx > 0:
                bola.dx = 3.5 + (puntuacio1 + puntuacio2)/4
                bola.dy = 3.5 + (puntuacio1 + puntuacio2)/4
            else:
                bola.dx = -3.5 - (puntuacio1 + puntuacio2)/4
                bola.dy = -3.5 - (puntuacio1 + puntuacio2)/4
            punt.clear()
            punt.write("Jugador 1:{}          Jugador 2:{}".format(puntuacio1, puntuacio2),
                       align="center", font=("Courier", 36, "normal"))
            bola.goto(0, 0)

        # Comprovació final del joc
        if puntuacio1 == puntuacio_max or puntuacio2 == puntuacio_max:
            bola.dx = 0
            bola.dy = 0
            punt.goto(0, 0)
            wn.clear()
            if puntuacio1 == puntuacio_max:
                pong_ai_final.pantalla_final("1", puntuacio_max)
            else:
                pong_ai_final.pantalla_final("2", puntuacio_max)
            x = False

        # Xocs entre pala i bola
        if bola.xcor() < -580 and pala1.ycor() - 50 < bola.ycor() < pala1.ycor() + 50:
            bola.dx *= -1.15
            bola.dy *= 1.15
            bola.setx(-580)

        elif bola.xcor() > 580 and pala2.ycor() - 50 < bola.ycor() < pala2.ycor() + 50:
            bola.dx *= -1.15
            bola.dy *= 1.15            
            bola.setx(580)

