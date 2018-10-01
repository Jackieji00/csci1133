# CSCI 1133 Homework5
# Peiqi Ji
# Problem 5D
import turtle
def squares(t, length,depth):
    if depth == 0:
        return
    else:
        x = t.xcor()
        y = t.ycor()
        t.penup()#top line of the square
        t.goto(length/2+x,length/2+y)
        t.pendown()
        t.goto(-length/2+x,length/2+y)
        t.penup()
        t.goto(x,3*length/4+y) #center point for top square
        squares(t,length/2,depth-1)
        #left line of the square
        t.goto(-length/2+x,-length/2+y)
        t.pendown()
        t.goto(-length/2+x,length/2+y)
        t.penup()
        t.goto(x-3*length/4,y)#center point for the left
        squares(t,length/2,depth-1)
        t.goto(-length/2+x,-length/2+y)#bottom line
        t.pendown()
        t.goto(length/2+x,-length/2+y)
        t.penup()
        t.goto(x,y-3*length/4)#center point for the bottom
        squares(t,length/2,depth-1)
        t.goto(length/2+x,-length/2+y)#right line
        t.pendown()
        t.goto(length/2+x,length/2+y)
        t.penup()
        t.goto(x+3*length/4,y)#center point for the right
        squares(t,length/2,depth-1)
def main():
    t = turtle.Turtle()
    t.speed(0)
    squares(t,200,4)
if __name__ == '__main__':
    main()
