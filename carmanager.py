from turtle import Turtle, position
import random


COLOURS = [ 'red', 'blue', 'green', 'yellow','pink']
STARTING_MOVING_DISTANCE =5
MOVE_INCREMENT = 10


class Carmanager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVING_DISTANCE


    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()

            new_car.color(random.choice(COLOURS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_cor = random.randint(-250, 250)
            new_car.goto(300, y_cor)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT






