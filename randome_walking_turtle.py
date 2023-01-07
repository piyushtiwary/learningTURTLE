import turtle
import random

colors = ["blue", "red", "green", "yellow", "pink", "Orange", "Brown", "DarkKhaki", "Magenta", "Olive"]
directions = [90, 270, 180]

timmi = turtle.Turtle()
timmi.speed(20)
i =3

for _ in range(200):
	timmi.width(i)
	timmi.pencolor(random.choice(colors))
	timmi.fd(10)
	timmi.lt(random.choice(directions))
	i += 0.005
	

my_screen = turtle.Screen()

my_screen.exitonclick()
