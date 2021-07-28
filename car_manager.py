COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

import random
import time
from turtle import Turtle


class CarManager():
    def __init__(self):
        self.cars = []
        self.level = 3

    def create_car(self):
        for i in range(random.randint(1+3*(self.level-1), self.level*5)):
            car = Turtle()
            car.shape("square")
            car.setheading(180)
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=3)
            car.color(COLORS[random.randint(0, len(COLORS) - 1)])
            car.goto(random.randint(300, 450), random.randint(-280, 280))
            self.cars.append(car)

    def drive(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + (self.level - 1) * MOVE_INCREMENT)
            if car.xcor() < -350:
                self.cars.pop(self.cars.index(car))
