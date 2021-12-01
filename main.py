# imported turtle module
import turtle

wind = turtle.Screen() #Iinitialize screen
wind.cv._rootwindow.resizable(False, False)
wind.title('Ping Pong By Sherif') # Set title of the window
wind.bgcolor('black') # Set the background of the window
wind.setup(width=800, height=600) # Set the width and height of the window
wind.tracer(0)


#madrab1
madrab1 = turtle.Turtle() # Iinitialize Turtle object(shape)
madrab1.speed(0) # set the speed of animation
madrab1.shape("square")# set the shape of the object
madrab1.color("blue") # set the color of the shape
madrab1.shapesize(stretch_wid=5, stretch_len=1) # stretches the shape to meet the size
madrab1.penup() # Stop The Object From Drawing Lines
madrab1.goto(-350, 0) # Set The Position of the object

#madrab2
madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=5, stretch_len=1)
madrab2.penup()
madrab2.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write(f"Player 1:{score1} Player2:{score2}", align="center", font=("Courier", 24, "normal"))


# functions
def madrab1_up():
    y = madrab1.ycor() # Set The y Cordanite of the madrab1
    y += 20 # Set The y to increase be 20
    madrab1.sety(y)
def madrab1_down():
    y = madrab1.ycor()
    y -= 20
    madrab1.sety(y)

def madrab2_up():
    y = madrab2.ycor()
    y += 20
    madrab2.sety(y)
def madrab2_down():
    y = madrab2.ycor()
    y -= 20
    madrab2.sety(y)

# KeyBoard Bindings
wind.listen() # Tell The Window to expect keyboard input
wind.onkeypress(madrab1_up, "w") # When Pressing W madrab1_up is invoked
wind.onkeypress(madrab1_down, "s")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")





# Main Game Loop
while True:
    wind.update() # Update The Screen EveryTime The Loop Run

    # Move Ball
    ball.setx(ball.xcor() + ball.dx) # Ball Starts at 0 and evrey time loop runs---> + 0.1 xaxis
    ball.sety(ball.ycor() + ball.dy) # Ball Starts at 0 and evrey time loop runs---> + 0.1 xaxis
    # Border Cheek, top border +300px, bottom border -300px, ball is 20px
    if ball.ycor() > 290: # if ball is at top border
        ball.sety(290) # Set y Cordanite +290
        ball.dy *= -1 # reverse dirction of the ball by -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write(f"Player 1:{score1} Player2:{score2}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write(f"Player 1:{score1} Player2:{score2}", align="center", font=("Courier", 24, "normal"))


    # Tasadom Madrab and ball
    if (ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < madrab2.ycor() + 40 and ball.ycor() > madrab2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1