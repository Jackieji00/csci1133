# CSCI 1133 Homework5
# Peiqi Ji
# Problem 5A
import turtle
def triangle(t, length,depth):
    if depth == 0:
        return
    else:
        x = t.xcor()
        y = t.ycor()
        t.penup()#top line of the triangle
        t.goto(length/2+x,(3**(1/2))*length/4+y)
        t.pendown()
        t.goto(-length/2+x,(3**(1/2))*length/4+y)
        t.penup()
        t.goto(x,(3**(1/2))*3*length/8+y) #center point for top triangle
        triangle(t,length/2,depth-1)
        #left line of the triangle
        t.goto(-length/2+x,(3**(1/2))*length/4+y)
        t.pendown()
        t.goto(x,-(3**(1/2))*length/4+y)
        t.penup()
        t.goto(x-length/2,y-(3**(1/2))*length/8)#center point for the left
        triangle(t,length/2,depth-1)
        t.goto(length/2+x,(3**(1/2))*length/4+y)#right line
        t.pendown()
        t.goto(x,-(3**(1/2))*length/4+y)
        t.penup()
        t.goto(x+length/2,y-(3**(1/2))*length/8)#center point for the right
        triangle(t,length/2,depth-1)
        t.goto(x,y+(3**(1/2))*3*length/4)#outside part
        t.pendown()
        t.goto(length+x,-(3**(1/2))*length/4+y)
        t.goto(x-length, -(3**(1/2))*length/4+y)
        t.goto(x,y+(3**(1/2))*3*length/4)
        t.penup()
def main():
    t = turtle.Turtle()
    t.speed(0)
    triangle(t,200,4)
if __name__ == '__main__':
    main()
