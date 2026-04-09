#SNAKE GAME
#TODO: 1. create a snake body
#TODO: 2. move the snake
#TODO: 3. create snake food
#TODO: 4. detect collision with food
#TODO: 5. create a scorecard
#TODO: 6. detect collision with wall
#TODO: 7. detect collision with tail

from turtle import Turtle,Screen
import time
from snake import Snake

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)


snake = Snake()
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
screen.exitonclick()
