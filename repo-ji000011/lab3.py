# def roundit(number):
#     if number >= 0:
#         number += 0.5
#         number = int(number)
#     else:
#         number -= 0.5
#         number = int(number)
#     return number

# import turtle
# turtle.showturtle()
# def Drawsquare( ):
#     i=0
#     a = turtle.numinput("","")
#     while i<360/a:
#      turtle.forward(100)
#      turtle.left(90)
#      turtle.forward(100)
#      turtle.left(90)
#      turtle.forward(100)
#      turtle.left(90)
#      turtle.forward(100)
#      turtle.left(90)
#      turtle.left(a)
#      i+=1
# if __name__ == '__main__':
#      Drawsquare()
# import random
# import turtle
# def RandomWalk():
#     turtle.penup()
#     i=0
#     while turtle.xcor()<200 and turtle.ycor()<200:
#         a=random.randint(1,4)
#         if a==2:
#             turtle.left(90)
#         elif a==3:
#             turtle.left(180)
#         elif a==4:
#             turtle.left(270)
#         turtle.pendown()
#         turtle.forward(20)
#         i+=20
#     print("step",i)
# if __name__ == '__main__':
#      RandomWalk()

# import random
# import turtle
# def MonteCarlo():
#     turtle.speed(0)
#     turtle.penup()
#     turtle.goto(100,100)
#     turtle.pendown()
#     turtle.goto(-100,100)
#     turtle.goto(-100,-100)
#     turtle.goto(100,-100)
#     turtle.goto(100,100)
#     turtle.penup()
#     turtle.goto(0,-100)
#     turtle.pendown()
#     turtle.circle(100)
#     turtle.penup()
#     i=1
#     a=0
#     while i<=1000:
#         x=random.uniform(-100,100)
#         y=random.uniform(-100,100)
#         turtle.goto(x,y)
#         turtle.pendown()
#         turtle.dot(5,"black")
#         if turtle.distance(0,0)<=100.1:
#             turtle.dot(5,"red")
#             turtle.penup()
#             a+=1
#         if turtle.distance(0,0)>100.1:
#             turtle.dot(5,"green")
#             turtle.penup()
#         i+=1
#     print(a/i*4)
# if __name__ == '__main__':
#     MonteCarlo()
