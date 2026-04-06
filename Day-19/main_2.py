from turtle import Turtle,Screen
import random

y_value=-100
def move_to_position(self,position_value,colour):
    self.shape('turtle')
    self.penup()
    self.color(colour)
    all_turtles.append(self)
    self.goto(x=-230, y=y_value+position_value)

race_on=False
all_turtles=[]

screen = Screen()
screen.setup(width=500,height=400)

choice=screen.textinput("Input","Bet on you're jockey")
timmy=Turtle()
move_to_position(timmy,0,'red')

timmy2=Turtle()#CREATING A DIFFERENT INSTANCES
move_to_position(timmy2,40,'blue')

timmy3=Turtle()
move_to_position(timmy3,80,'green')

timmy4=Turtle()
move_to_position(timmy4,120,'pink')

timmy5=Turtle()
move_to_position(timmy5,160,'violet')

if choice:
    race_on=True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            race_on = False
            winning_color=turtle.pencolor()
            if winning_color==choice:
                print("congratulations, you win")
            else:
                print(f'{winning_color} won the race, you lose.')


        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()