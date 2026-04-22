import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")
carmanager=CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_scoreboard()

    carmanager.create_car()
    carmanager.move_cars()

    #Detect collision with car
    for car in carmanager.all_cars:
        if car.distance(player)<20:
            scoreboard.game_over()
            game_is_on=False


    #Detect a success full crossing
    if player.is_at_finish_line():
        player.gotostart()
        carmanager.level_up()
        scoreboard.increase_level()

screen.exitonclick()