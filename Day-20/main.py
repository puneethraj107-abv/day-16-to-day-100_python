#SNAKE GAME
#TODO: 1. create a snake body
#TODO: 2. move the snake
#TODO: 3. create snake food
#TODO: 4. detect collision with food
#TODO: 5. create a scorecard
#TODO: 6. detect collision with wall
#TODO: 7. detect collision with tail

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)


snake = Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')


screen.update()

game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #TODO 4. detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase()
    #TODO: 6. detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on=False
        scoreboard.game_over()
    # TODO: 7. detect collision with tail
    for segment in snake.segments[1:]:

        if snake.head.distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()


