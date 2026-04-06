#FUNCTION AS INPUT

import turtle

t = turtle.Turtle()

screen = turtle.Screen()

# Movement functions
def move_forward():
    t.forward(20)

def move_backward():
    t.backward(20)

def turn_left():
    t.left(15)

def turn_right():
    t.right(15)

def clearscreen():
    t.clear()
    t.reset()

# Keyboard bindings
screen.listen()
screen.onkeyrelease(move_forward, "w")
screen.onkeyrelease(move_backward, "s")
screen.onkeyrelease(turn_left, "a")
screen.onkeyrelease(turn_right, "d")
screen.onkeyrelease(clearscreen, "c")
screen.exitonclick()

screen.mainloop()