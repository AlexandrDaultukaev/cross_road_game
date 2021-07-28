import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

tim = Player()
car = CarManager()


# Event handlers
screen.onkey(tim.up, "Up")
screen.onkey(tim.down, "Down")
car.create_car()

game_is_on = True
count = 0.0
while game_is_on:
    time.sleep(0.1)
    count += 0.1
    print(count)
    # 3/car.level - frequency cars spawn
    if count > 3/car.level:
        count = 0.0
        car.create_car()
    car.drive()
    screen.update()
    for index in range(car.get_amount_of_cars()):
        if car.get_car(index).distance(tim) < 20:
            exit()

screen.exitonclick()
