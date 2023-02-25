import turtle
import winsound
# import os



import time
wn = turtle.Screen()
wn.setup(width=800,height=600)
wn.bgcolor("black")
wn.tracer(0) #manages animation speed

# score
scorea=0
scoreb=0
# paddle_a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.penup()
paddle_a.color("red")
paddle_a.goto(-350,0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)

# 
jumo=turtle.Turtle()
jumo.penup()
jumo.goto(0,260)
jumo.speed(0)
jumo.pencolor("white")
jumo.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24))
jumo.color("white")
jumo.hideturtle()

jumo.shape("square")
# paddle_b
paddle_b = turtle.Turtle()
paddle_b.penup()
paddle_b.speed(0)
paddle_b.color("red")
paddle_b.goto(350,0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
# ball
ball=turtle.Turtle()
ball.color("white")
ball.speed(0)
ball.penup()
ball.goto(0,0)
ball.shape("square")
ball.dx=2.2
ball.dy=2.2
#scorebord
# fns
def paddle_b_up():
    yb=paddle_b.ycor()
    yb+=20
    paddle_b.sety(yb)
def paddle_a_up():
    ya=paddle_a.ycor()
    ya+=20
    paddle_a.sety(ya)

def paddle_a_down():
    y=paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)





#keywndw
wn.listen()
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_a_down,"S")
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_up,"W")
wn.onkeypress(paddle_b_down,"Down")
wn.onkeypress(paddle_b_up,"Up")
# man lopp

while True:
    start_time =time.time()
   
    #moveball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #chexkbord
    if ball.ycor()>290:
        # winsound.PlaySound('Users\Rahul\Documents\RAHUL PYTHON\bounce.wav', winsound.SND_ASYNC)
        ball.sety:(290)
        ball.dy*=-1

    if ball.ycor()<-290:
        # winsound.PlaySound('Users\Rahul\Documents\RAHUL PYTHON\bounce.wav', winsound.SND_ASYNC)
        ball.sety:(-290)
        ball.dy*=-1
    
    if ball.xcor()>390:
        #aler
        winsound.PlaySound('Users\Rahul\Documents\RAHUL PYTHON\bounce.wav', winsound.SND_ASYNC)
        # os.startfile('bounce.wav')
        scorea+=1
        jumo.clear()
        jumo.write("Player A: {} Player B: {}".format(scorea,scoreb), align="center", font=("Courier", 24))
        ball.goto(0,0)
        ball.dx*=-1
    if ball.xcor()<-390:
        #aler
        winsound.PlaySound('Users\Rahul\Documents\RAHUL PYTHON\bounce.wav', winsound.SND_ASYNC)
        # os.startfile('bounce.wav')
        scoreb+=1
        jumo.clear()
        jumo.write("Player A: {} Player B: {}".format(scorea,scoreb), align="center", font=("Courier", 24))
        ball.goto(0,0)
        ball.dx*=-1
        # 

    if ball.xcor() > 340 and ball.xcor()<350 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor()>paddle_b.ycor()-50:
        ball.setx(340)
        winsound.PlaySound('Users\Rahul\Documents\RAHUL PYTHON\bounce.wav', winsound.SND_ASYNC)
        # os.startfile('bounce.wav')
        ball.dx*=-1
    if ball.xcor() < -340 and ball.xcor()>-350 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor()>paddle_a.ycor()-50:
        ball.setx(-340)
        # os.system("start bounce.wav")
        winsound.PlaySound('Users\Rahul\Documents\RAHUL PYTHON\bounce.wav', winsound.SND_ASYNC)
        ball.dx*=-1
        
    wn.update()
    end_time = time.time()
    delay = max(0, (1/60) - (end_time - start_time))
    
    # wait for delay
    time.sleep(delay)
    