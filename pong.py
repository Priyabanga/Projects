import turtle

wn=turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#Score
score_a=0
score_b=0

#PaddleA
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("White")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#PaddleB
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("White")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball
Ball=turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("White")
Ball.penup()
Ball.goto(0,0)
Ball.dx=2
Ball.dy=-2

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align="center",font=("Courier",24,"normal"))

#Function
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")


while True:
    wn.update()

    #Move the Ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    #Border Checking
    if Ball.ycor()>290:
        Ball.sety(290)
        Ball.dy*=-1

    if Ball.ycor()<-290:
        Ball.sety(-290)
        Ball.dy*=-1

    if Ball.xcor()>390:
        Ball.goto(0,0)
        Ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))

    if Ball.xcor()<-390:
        Ball.goto(0,0)
        Ball.dx *=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))


    #Paddle and ball collision
    if (Ball.xcor()>340 and Ball.xcor()<350) and (Ball.ycor()<paddle_b.ycor()+40 and Ball.ycor()>paddle_b.ycor()-50):
        Ball.setx(340)
        Ball.dx *=-1

    if (Ball.xcor()<-340 and Ball.xcor()>-350) and (Ball.ycor()<paddle_a.ycor()+40 and Ball.ycor()>paddle_a.ycor()-50):
        Ball.setx(-340)
        Ball.dx *=-1
