import turtle
import random
def RandomWalk(x):
  x.speed(400)
  x.penup()
  i=0
  while x.xcor()<100 and x.ycor()<100:
    a=random.randint(1,4)
    if a==2:
      x.left(90)
    elif a==3:
      x.left(180)
    elif a==4:
      x.left(270)
    x.forward(20)
    i+=20
turtle.showturtle()
turtle.shape("turtle")
turtle.color("yellow")
RandomWalk(turtle)
b=turtle.Turtle()
b.showturtle()
b.shape("turtle")
b.color("red")
RandomWalk(b)
t=turtle.Turtle()
t.showturtle()
t.shape("turtle")
t.color("green")
RandomWalk(t)
