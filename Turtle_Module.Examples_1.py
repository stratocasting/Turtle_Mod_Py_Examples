from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.speed("fastest")
# timmy.penup()
timmy.shapetransform()
# Use "W, A, S, D," for move, "C" for clear

def move_forwards():
    timmy.forward(10)

def move_backwards():
    timmy.backward(10)

def move_left():
    timmy.left(10)

def move_right():
    timmy.right(10)
def clear():
    timmy.penup()
    timmy.home()
    timmy.clear()
    timmy.pendown()

screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear)














screen.exitonclick()