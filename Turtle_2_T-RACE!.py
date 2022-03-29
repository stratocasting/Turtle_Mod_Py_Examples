from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="MAKE YOUR BET", prompt="WHICH TURTLE SILL WIN? ENTER A COLOR: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y_positions = [-70, -40, -10, 20, 50, 80]
for turtle_index in range (0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've Won {winning_color} is the best turtle")
            else:
                print (f"You've lost {user_bet} is worst goddamn turtle.")




        random_distance = random.randint(0, 8)
        turtle.forward(random_distance)













screen.exitonclick()