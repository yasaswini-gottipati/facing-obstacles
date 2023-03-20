from turtle import Turtle

class Player(Turtle) :

    def __init__(self) :
        super().__init__()
        self.shape("triangle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.goto(0, -250)
        self.setheading(90)
        self.speed_value = 15


    def move_left(self) :
        x = self.xcor() - self.speed_value
        if x < -280 :
            x = -280
        self.setx(x)


    def move_right(self):
        x = self.xcor() + self.speed_value
        if x > 280:
            x = 280
        self.setx(x)





