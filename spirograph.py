import turtle
import random

turtle.colormode(255)

timmi = turtle.Turtle()
timmi.speed(20)
timmi.pensize(3)

def genCol():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	return (r, g, b)

for i in range(40):
	timmi.color(genCol())
	timmi.circle(100)
	timmi.lt(10)


my_screen = turtle.Screen()

my_screen.exitonclick()
