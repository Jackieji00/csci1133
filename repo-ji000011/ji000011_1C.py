# CSCI 1133 Homework1
# Peiqi Ji
# Problem 1C
import turtle
def turtleshapes(w,h):
    turtle.showturtle()
    turtle.goto(0,h)
    turtle.goto(w,h)
    turtle.goto(w,0)
    turtle.goto(0,0)
    turtle.goto(3*w,0)
    turtle.goto(3*w,h)
    turtle.goto(2*w,0)
def main():
    w = int(input('Enter a width: '))
    h = int(input('Enter a height: '))
    turtleshapes(w,h)
if __name__ == '__main__':
    main()
