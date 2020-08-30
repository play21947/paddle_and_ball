import turtle
import time

wn = turtle.Screen()
wn.title("Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)

#score
score_a = 0
score_b = 0


# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball1
ball = turtle.Turtle()
ball.speed()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 4

#ball2
#ball2 = turtle.Turtle()
#ball2.speed()
#ball2.shape("square")
#ball2.color("white")
#ball2.penup()
#ball2.goto(0, 0)
#ball2.dx = -4
#ball2.dy = 2

#scoreshow
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(-50, 260)
score.write("Player 1 : 0 Player 2 : 0")
score.penup()

#function
def paddle_a_up():
    y = paddle_a.ycor() #ให้ y เท่ากับ ค่า y ของ paddle_a
    y = y + 20 #ให้ ค่า y + 20
    paddle_a.sety(y) #ให้ paddle_a มาอยู่ที่ sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y = y - 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #ให้ y เท่ากับ ค่า y ของ paddle_a
    y = y + 20 #ให้ ค่า y + 20
    paddle_b.sety(y) #ให้ paddle_a มาอยู่ที่ sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y = y - 20
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'i')
wn.onkeypress(paddle_b_down, 'k')


while True:
    wn.update()

    #ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #ball2.setx(ball.xcor() + ball2.dx)
    #ball2.sety(ball.ycor() + ball2.dy)



    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1

    if ball.xcor() > 355 :
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        score_a = score_a + 1
        score.clear()
        score.write("Player 1 : {} | Player 2 : {}".format(score_a, score_b))

    if ball.xcor() < -355:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        score_b = score_b + 1
        score.clear()
        score.write("Player 1 : {} | Player 2 : {}".format(score_a, score_b))

    ##paddle coord
    if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50):
        ball.dx = ball.dx * -1
    if ball.xcor() < -340 and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50):
        ball.dx = ball.dx * -1


    #AI
    if paddle_b.ycor() < ball.ycor():
        paddle_b_up()

    elif paddle_b.ycor() > ball.ycor():
        paddle_b_down()

    #win
    if score_a == 3:
        score.goto(0, 50)
        score.write("Player 1 win")
        time.sleep(3)
        break
    elif score_b == 3:
        score.goto(0, 50)
        score.write("Player 2 win")
        time.sleep(3)
        break
