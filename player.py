# player.py

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.go_to_start()

    def up(self):
        self.setheading(90)
        self.forward(10)

    def player_is_at_finish(self):
        return self.ycor() > 280  # Just check, don't move

    def go_to_start(self):
        self.goto(0, -280)  # Corrected: start position is bottom of screen
