#TURTLE GRAPHICS, TUPLES
#   TKINTER
import random
import turtle as t

def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    random_color=(r,g,b)
    return random_color

t.colormode(255)
timmy=t.Turtle()
timmy.shape('turtle')
myscreen=t.Screen()
timmy.pensize(1)
t.speed('fastest')

direction=[90,180,270,360]

for angle in range(0, 360, 10):  # rotate by 10° each time
    t.color(random_color())
    t.setheading(angle)          # tilt direction
    t.circle(100)                # same radius, same center

t.done()

myscreen.exitonclick()