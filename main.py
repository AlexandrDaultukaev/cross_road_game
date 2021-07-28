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

# Event handlers
screen.onkey(tim.up, "Up")
screen.onkey(tim.down, "Down")

car = CarManager()
car.create_car()

score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    # 3/car.level - frequency cars spawn
    car.drive()
    screen.update()
    car.create_car()
    for index in range(car.get_amount_of_cars()):
        if car.get_car(index).distance(tim) < 20:
            game_is_on = False
    if tim.ycor() > 280:
        car.level_up()
        tim.level_up()
        score.clear()
        score.level_up()


screen.exitonclick()
