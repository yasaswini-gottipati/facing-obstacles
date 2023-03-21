from turtle import Turtle
import random

shapes = ["square", "circle"]


class Enemy (Turtle):

    def __init__(self):
        super().__init__()
        self.shape(random.choice(shapes))
        self.color("red")
        self.penup()
        self.speed(0)
        self.goto(random.randint(-250, 250), random.randint(150, 250))
        self.dx = random.randint(1,5)
        self.speed_value = 5

    def move(self):
        x = self.xcor() + self.dx
        self.setx(x)
        if self.xcor() > 280 or self.xcor() < -280:
            self.dx *= -1
            self.sety(self.ycor() - 80)


