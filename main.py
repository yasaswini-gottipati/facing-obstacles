from turtle import Screen
from player import Player
from missile import Missile
from enemy import Enemy
from score import Score
import time
import math
import random

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("facing obstacles")
screen.tracer(0)

score = Score()
player = Player()
missile = Missile()
enemy = Enemy()


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

    for enemy in enemies:
        enemy.move()

        # if enemy.xcor() > 280 or enemy.xcor() < -280:
        #     enemy.speed_value *= -1
        #     for e in enemies :
        #         y = e.ycor ()
        #         y -= 10
        #         e.sety(y)

        if is_collision(player, enemy):
            is_game = False
            score.game_over()


        if is_collision(missile, enemy):
            missile.hideturtle()
            missile.state = "ready"
            enemy.hideturtle()
            score.increase_score ()
            enemies.remove(enemy)

        for missile in missiles:
            if check_collision():
                missile.hideturtle()
                missile.goto(1000, 1000)
                missiles.remove(missile)
                enemy.goto (random.randint (-200, 200), random.randint (100, 250))
                #enemies.remove(enemy)
                score.increase_score()
    # for i in missiles:
    #     if i.state == "fired" :
    #          y = i.ycor ()
    #          y += i.speed_value
    #          i.sety (y)

            y = missile.ycor()
            y += 10
            missile.sety(y)

        # if len(enemies) == 0:
        #     is_game = False
        #     score.write(f"Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
        if score.score == 10:
            score.clear()
            score.goto(0,0)
            score.write(f"Score: {score.score}/10", align = "center", font = ("Courier", 24, "normal"))



screen.exitonclick ()