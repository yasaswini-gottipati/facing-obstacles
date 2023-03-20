from turtle import Turtle



class Missile (Turtle) :

    def __init__(self) :
        super ().__init__ ()
        self.shape ("triangle")
        self.color ("yellow")
        self.penup ()
        self.speed(0)
        self.setheading (90)
        self.shapesize (0.5, 0.5)
        self.speed_value = 20
        self.state = "ready"






