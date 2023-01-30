import colorgram
import turtle

turtle.colormode(255)
timmi = turtle.Turtle()
timmi.shapesize(1)
timmi.penup()
timmi.speed(20)

y = 10

colors = colorgram.extract('test.webp', 30)
list_colors = []

for i in range(30):
	list_colors.append(colors[i].rgb)

print(list_colors)

j = 0
for i in range(5):
	timmi.setx(-80)
	for k in range(5):
		timmi.dot(15, list_colors[j])
		timmi.color(255,255,255)
		timmi.fd(50)
		j += 1
	
	y += 30
	timmi.sety(y)
	



my_screen = turtle.Screen()
my_screen.exitonclick()