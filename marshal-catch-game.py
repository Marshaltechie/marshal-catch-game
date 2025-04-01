import turtle
import random

# SCREEN SETUP
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Marshal-Catch game")
screen.tracer(0)

# PAC-MAN SETUP
pacman = turtle.Turtle()
pacman.shape("circle")
pacman.color("white")
pacman.penup()
pacman.goto(0, -250)

# FOOD SETUP
food = turtle.Turtle()
food.shape("circle")
food.color("yellow")
food.penup()
food.shapesize(0.5, 0.5)
food.speed(0)
food.goto(random.randint(-280, 280), random.randint(-280, 280))

# SCORE SETUP
score = 0
score_turtle = turtle.Turtle()
score_turtle.color("white")
score_turtle.penup()
score_turtle.hideturtle()
score_turtle.goto(0, 260)
score_turtle.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

# MOVE DIRECTIONS
speed = 20

def go_up():
    if pacman.heading() != 270:
        pacman.setheading(90)

def go_down():
    if pacman.heading() != 90:
        pacman.setheading(270)

def go_left():
    if pacman.heading() != 0:
        pacman.setheading(180)

def go_right():
    if pacman.heading() != 180:
        pacman.setheading(0)

# KEYBOARD BINDINGS
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# GAME LOOP
def game_loop():
    global score

    # MOVE PAC-MAN
    pacman.forward(speed)

    # CHECK FOR COLLISION WITH WALLS
    if pacman.xcor() > 290 or pacman.xcor() < -290 or pacman.ycor() > 290 or pacman.ycor() < -290:
        pacman.goto(0, -250)
        pacman.setheading(90)
        score = 0
        score_turtle.clear()
        score_turtle.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

    # CHECK FOR COLLISION WITH FOOD
    if pacman.distance(food) < 15:
        # REPOSITION THE FOOD
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        # UPDATE SCORE
        score += 10
        score_turtle.clear()
        score_turtle.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

    # KEEP THE GAME LOOP RUNNING
    screen.ontimer(game_loop, 100)  # Calls game_loop every 100ms (10 frames per second)
    screen.update()  # Updates the screen every loop

# START THE GAME LOOP
game_loop()

# MAINLOOP
screen.mainloop()
