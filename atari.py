import turtle
import time
from random import randint

score = 0
high_score = 0
delay = .1

# Set up background
win = turtle.Screen()
win.bgcolor('black')
win.title("Turtle Atari")
win.setup(width = 600, height = 600)
win.tracer(0)

# Going to be at the top of the area
blocks = []
i = 0
j = -200
while j < 340:
    i = 0
    while i < 275:
        block = turtle.Turtle()
        blocks.append(block)
        block.speed(0)
        block.penup()
        r = randint(0,255) 
        g = randint(0,255)  
        b = randint(0,255) 

        win.colormode(255)
        block.color(r,g,b)
        block.shape('square')
        block.shapesize(stretch_len = 10)
        block.goto(j, i)
        i += 25
    j += 75


# write the score
top = turtle.Turtle()
top.speed(0)
top.shape('circle')
top.color('white')
top.penup()
top.hideturtle()
top.goto(0,270)
top.write("Score: 0 High score: 0", align = "center", font=("Garamond", 24, "normal"))

# board
b = turtle.Turtle()
b.speed(0)
b.shape('square')
b.shapesize(stretch_wid = .5, stretch_len=4)
b.color('red')
b.penup()
b.goto(0,-280)
b.direction = "stop"


# ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,-270)
ball.speed(4)
ball.dx = -20
ball.dy = 20


# Directions for your paddle
def left():
    if b.xcor() > -290:
        b.setx(b.xcor() - 25)
def right():
    if b.xcor() < 290:
        b.setx(b.xcor() + 25)      

win.listen()
    
# # Set up keyboard interactions 
win.onkeypress(left, "Left")
win.onkeypress(right, "Right")

while True: 
    win.update()

    #
    # Check for collision
    time.sleep(delay)





