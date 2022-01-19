import turtle
import time
import random 

score = 0
high_score = 0
delay = .1

# Set up background
win = turtle.Screen()
win.bgcolor('black')
win.title("Why'd it have to be snakes")
win.setup(width = 600, height = 600)
win.tracer(0)

#snake 
snake = turtle.Turtle()
snake.speed(0)
snake.shape('circle')
snake.color('red')
snake.penup()
snake.goto(0,0)
snake.direction = "stop"

#food to eat
food = turtle.Turtle()
food.speed(0)
food.shape('square')
food.color('green')
food.penup()
food.goto(0,100)

parts = []

# write the score
top = turtle.Turtle()
top.speed(0)
top.shape('circle')
top.color('white')
top.penup()
top.hideturtle()
top.goto(0,270)
top.write("Score: 0 High score: 0", align = "center", font=("Garamond", 24, "normal"))

# Directions for your snake 
def up():
    if snake.direction != 'down':
        snake.direction = 'up'
def down():
    if snake.direction != 'up':
        snake.direction = 'down'
def left():
    if snake.direction != 'right':
        snake.direction = 'left'
def right():
    if snake.direction != 'left':
        snake.direction = 'right'

# Actually move the snake 
# 20 is an arbitrary number and ca be changed for faster movement 
def move():
    if snake.direction == "up": 
        snake.sety(snake.ycor() + 20)
    if snake.direction == "down": 
        snake.sety(snake.ycor() - 20)
    if snake.direction == "right": 
        snake.setx(snake.xcor() + 20)
    if snake.direction == "left": 
        snake.setx(snake.xcor() - 20)

win.listen()
    
# Set up keyboard interactions 
win.onkeypress(left, "Left")
win.onkeypress(right, "Right")
win.onkeypress(up, "Up")
win.onkeypress(down, "Down")

while True: 
    win.update()
    # Check boundaries 
    if snake.xcor() > 290 or snake.ycor() < -290 or snake.xcor() < -290 or snake.ycor() > 290:
        # reset 
        time.sleep(1)
        snake.goto(0,0)
        snake.direction = "stop"

        # Account for segmets and clear them
        for part in parts:
            part.goto(1000, 1000)
        parts.clear()

        #Update score
        score = 0
        delay = .1
        top.clear()
        top.write("Score: {} High score: {}".format(score, high_score),align="center", font=("Courier", 24, "normal"))
    
    if snake.distance(food) < 20:
        # Eat food 
        food.goto(random.randint(-290, 290), random.randint(-290, 290))
        # Add to snake 
        part_add = turtle.Turtle()
        part_add.speed(0)
        part_add.shape('circle')
        part_add.color('red')
        part_add.penup()
        parts.append(part_add)
        
        # Add to score and speed up
        delay -= .001
        score += 10
        if score > high_score: 
            high_score = score
        top.clear()
        top.write("Score: {} High score: {}".format(score, high_score),align="center", font=("Garamond", 24, "normal"))

    # Trail the body behind the snake
    for i in range(len(parts) - 1, 0, -1):
        x = parts[i - 1].xcor()
        y = parts[i - 1].ycor()
        parts[i].goto(x,y)
    if len(parts) > 0:
        x = snake.xcor()
        y = snake.ycor()
        parts[0].goto(x,y)
    move()
    for part in parts:
        if part.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction = "stop"
            for part in parts:
                part.goto(1000,1000)
            parts.clear()
            score = 0
            delay = .1
            top.clear()
            top.write("Score: {} High score: {}".format(score,high_score), align="center", font=("Courier", 24, "normal"))
    time.sleep(delay)
win.mainloop()





