import turtle
import os

# Configuració de la pantalla
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600) # línia provisional
# codi real--> wn._root.attributes('-fullscreen', True)

# Configuració pales
pala1 = turtle.Turtle()
pala1.speed(0)
pala1.shape("square")
pala1.color("white")
pala1.shapesize(stretch_wid=5, stretch_len=1)
pala1.penup()
pala1.goto(-350, 0)

pala2 = turtle.Turtle()
pala2.speed(0)
pala2.shape("square")
pala2.color("white")
pala2.shapesize(stretch_wid=5, stretch_len=1)
pala2.penup()
pala2.goto(350, 0)



while True:
  wn.update()
  
