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
        if random.randint(1, 6) < 2 + self.level - 1:
            car = Turtle()
            car.shape("square")
            car.setheading(180)
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
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

    def level_up(self):
        for car in self.cars:
            car.hideturtle()
            car.clear()
        self.level += 1
        self.cars = []
