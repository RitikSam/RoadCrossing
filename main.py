import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
tim = Player()
car_manager = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(tim.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(tim) < 20:
            game_is_on = False

    if tim.at_finish_line():
        tim.restart()
        car_manager.levels_up()
        score.increase()

