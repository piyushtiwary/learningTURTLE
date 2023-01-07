import turtle
import random

turtle.colormode(255)

def genCol():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	return (r, g, b)

timmi = turtle.Turtle()
timmi.pensize(3)

for i in range(1,7):
	timmi.pencolor(genCol())
	for j in range(i+2):
		timmi.fd(80)
		timmi.rt(360/(i+2))
	
my_screen = turtle.Screen()
