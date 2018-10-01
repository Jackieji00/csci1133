import turtle
def checkshape(shape):
    if shape.lower() == 'triangle' or shape.lower() =='square' or shape.lower() == 'octagon':
        return 1
    else:
        return 0
def checkcolor(color):
    if color.lower() == 'pink' or color.lower() == 'black' or color.lower() == 'yellow' or color.lower() == 'rainbow' or color.lower() == 'purple':
        return False
    else:
        return True
def drawTri(size):
    turtle.fd(size)
    turtle.left(120)
    turtle.fd(size)
    turtle.left(120)
    turtle.fd(size)
    turtle.left(120)
def drawSqr(size):
    turtle.fd(size)
    turtle.left(90)
    turtle.fd(size)
    turtle.left(90)
    turtle.fd(size)
    turtle.left(90)
    turtle.fd(size)
    turtle.left(90)
def drawOct(size):
    turtle.fd(size)
    turtle.left(45)
    turtle.fd(size)
    turtle.left(45)
    turtle.fd(size)
    turtle.left(45)
    turtle.fd(size)
    turtle.left(45)
    turtle.fd(size)
    turtle.left(45)
    turtle.fd(size)
    turtle.left(45)
    turtle.fd(size)
    turtle.left(45)
    turtle.fd(size)
    turtle.left(45)
def main():
    shape = input('What kind of shape do you want to draw?  ')
    i = checkshape(shape)
    while i == 0 :
        print('ERROR: ',shape,'is not a valid choice. Please enter triangle,square, or octagon. ')
        shape = input('What kind of shape do you want to draw?  ')
        i = checkshape(shape)
    number = int(input ('How many would you like to draw?  '))
    size = int(input('How big should the shapes be?  '))
    color = input('What color do you want? Please enter black, yellow, rainbow, purple, or pink. ')
    while checkcolor(color):
        color = input('Error! Please enter black, yellow, rainbow, purple, or pink. ')
    count = 0
    increment = int(input('What increment does you want? Please enter a number. '))
    turtle.speed(0)
    rainbowcolor = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    while count < number:
        if color.lower() != 'rainbow':
            turtle.fillcolor(color)
        else:
            if count > 7:
                colornumber = count % 7
            else:
                colornumber = count
            turtle.fillcolor(rainbowcolor[colornumber-1])
        turtle.begin_fill()
        if shape.lower() == 'trangle':
            drawTri(size)
        elif shape.lower() =='square':
            drawSqr(size)
        elif shape.lower() == 'octagon':
            drawOct(size)
        size += increment
        turtle.end_fill()
        turtle.left(360/number)
        count += 1
    turtle.hideturtle()
if __name__ == '__main__':
    main()
