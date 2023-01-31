from turtle import Turtle, Screen
import random

my_screen = Screen()
my_screen.setup(height=400, width=500)
colors = ["red", "green", "blue", "yellow", "purple"]
user = my_screen.textinput(title="Guess", prompt=f"Guess the color of the turtle from {colors}")
game_on = True


y_cords = [-40, -10, 20, 50, 80]
all_turtle = []

for i in range(5):
	timmi = Turtle(shape="turtle")
	timmi.color(colors[i])
	timmi.penup()
	timmi.goto(x=-230, y=y_cords[i])
	all_turtle.append(timmi)

while game_on:

	for turtle in all_turtle:
		if turtle.xcor() > 230:
			print(turtle.color())
			game_on = False
			if user == turtle:
				print("Your Guess was correct")
			else:
				print("Your Guess was wrong")
		turtle.fd(random.randint(1, 10))

my_screen.exitonclick()
