import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.level = 1

    def create_car(self):
        """
        Creates cars on the right side of the window.
        The number of cars created depends on the level.
        """
        #           lower bound            upper bound
        #           1+3*(self.level-1)     self.level*5
        # level 1:          1                   5
        # level 1:          4                   10
        # level 1:          7                   15
        lower_bound = 1+3*(self.level-1)
        upper_bound = self.level*5
        for i in range(random.randint(lower_bound, upper_bound)):
            car = Turtle()
            car.shape("square")
            car.setheading(180)
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=3)
            car.color(COLORS[random.randint(0, len(COLORS) - 1)])
            car.goto(random.randint(300, 450), random.randint(-280, 280))
            self.cars.append(car)

    def drive(self):
        """
        Moves cars from the right side to the left side window.
        Speed of cars depends on level.
        """
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + (self.level - 1) * MOVE_INCREMENT)
            if car.xcor() < -350:
                self.cars.pop(self.cars.index(car))

    def get_amount_of_cars(self):
        return len(self.cars)

    def get_car(self, index):
        return self.cars[index]
