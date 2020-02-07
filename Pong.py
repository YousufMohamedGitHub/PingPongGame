

import turtle

wn = turtle.Screen()
wn.title("By Yousuf")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

#Paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350,0)




# Functions for A
def paddle_A_up():
    y = paddle_A.ycor()
    y += 40
    paddle_A.sety(y)

def paddle_A_down():
    y = paddle_A.ycor()
    y -= 40
    paddle_A.sety(y)




# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
#ball.shapesize(stretch_wid=5, stretch_len=1)
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = 2


#Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(350,0)


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#Functions for B
def paddle_B_up():
    y = paddle_B.ycor()
    y += 40
    paddle_B.sety(y)

def paddle_B_down():
    y = paddle_B.ycor()
    y -= 40
    paddle_B.sety(y)




#KeyWord
wn.listen()
wn.onkey(paddle_A_up,"w")
wn.onkey(paddle_A_down,"s")
wn.onkey(paddle_B_up,"Up")
wn.onkey(paddle_B_down,"Down")



while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -390:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0,0)
        ball.dx *= -1

    # Ball collide with paddle\

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_A.ycor() + 50 and ball.ycor() > paddle_A.ycor() - 50:
        ball.dx *= -1
        #os.system("afplay bounce.wav&")

    elif ball.xcor() > 340 and ball.ycor() < paddle_B.ycor() + 50 and ball.ycor() > paddle_B.ycor() - 50:
        ball.dx *= -1
        #os.system("afplay bounce.wav&")
