# main.py

from turtle import Screen
from player import Player
from carmanager import Carmanager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
carmanager = Carmanager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.create_car()
    carmanager.move_cars()

    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.player_is_at_finish():
        player.go_to_start()
        carmanager.level_up()       # Make cars go faster
        scoreboard.increase_level() # Increase score/level












screen.exitonclick()