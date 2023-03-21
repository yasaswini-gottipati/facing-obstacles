from turtle import Turtle,Screen
from player import Player
from missile import Missile
from enemy import Enemy
from score import Score
import time
import math

turtle = Turtle()
turtle.hideturtle()
turtle.penup()
turtle.color("white")
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("facing obstacles")
screen.tracer(0)

start_time = time.time()

score = Score()
player = Player()



enemies = []
missiles = []

for i in range(10):
    enemy = Enemy()
    enemies.append(enemy)

def fire_missile():
   missil = Missile()
   missil.goto(player.xcor(),player.ycor())
   missiles.append(missil)

def check_collision():
    for missil in missiles:
        for enemy in enemies:
            if missil.distance(enemy) < 30:
                missil.hideturtle()
                missil.clear()
                missiles.remove(missile)
                enemy.hideturtle()
                enemy.clear()
                enemies.remove(enemy)
                score.increase_score()

screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkey(fire_missile, "space")


def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15 :
        return True
    else:
        return False


is_game = True

while is_game:
    screen.update()
    time.sleep (0.09)
    elapsed_time = int (time.time () - start_time)
    turtle.goto(-210,260)
    turtle.clear()
    turtle.write(f"Time: {elapsed_time}", align = "center", font = ("Courier", 24, "normal"))

    for enemy in enemies:
        enemy.move()


        if is_collision(player, enemy):
            is_game = False
            score.game_over()



        for missile in missiles:
            if check_collision():
                missile.hideturtle()
                missile.goto(1000, 1000)
                score.increase_score()
            y = missile.ycor()
            y += 10
            missile.sety(y)


        if score.score == 10:
            score.clear()
            score.goto(0,0)
            score.write(f"Score: {score.score}/10", align = "center", font = ("Courier", 24, "normal"))

        if elapsed_time >= 60 :
            is_game = False
            score.game_over ()



screen.exitonclick ()