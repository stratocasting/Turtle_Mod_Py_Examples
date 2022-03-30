from turtle import Turtle
import random
FOOD_CAN_BE_AT = [0,10, 20,30, 40,50, 60,70, 80,90, 100,110, 120,130, 140,150, 160,170, 180,190, 200,210, 220,230, 240,
                  250, 260, 270, 280, -10, -20, -30, -40, -50, -60, -70, -80, -90, -100, -110, -120, -130, -140, -150,
                  -160, -170, -180, -190, -200, 210, -220, -230, -240, -250, -260, -270, -280]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.3, 0.3)
        self.color("red")
        self.speed("fastest")
        random_x = random.choice(FOOD_CAN_BE_AT)
        random_y = random.choice(FOOD_CAN_BE_AT)
        self.goto(x=random_x, y=random_y)
        self.refresh()

    def refresh(self):
        random_x = random.choice(FOOD_CAN_BE_AT)
        random_y = random.choice(FOOD_CAN_BE_AT)
        self.goto(x=random_x, y=random_y)















