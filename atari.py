import turtle
import time
import random 

score = 0
high_score = 0
delay = .1

# Set up background
win = turtle.Screen()
win.bgcolor('black')
win.title("Turtle Atari")
win.setup(width = 600, height = 600)
win.tracer(0)

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
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,-270)

# Going to be at the top of the area
blocks = []

# # write the score
# top = turtle.Turtle()
# top.speed(0)
# top.shape('circle')
# top.color('white')
# top.penup()
# top.hideturtle()
# top.goto(0,270)
# top.write("Score: 0 High score: 0", align = "center", font=("Garamond", 24, "normal"))

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
    time.sleep(delay)
win.mainloop()





