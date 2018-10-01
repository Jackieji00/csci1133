import turtle
def check(shape):
    if shape.lower() == 'triangle' or shape.lower() =='square' or shape.lower() == 'octagon':
        return 1
    else:
        return 0
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
    i = check(shape)
    while i == 0 :
        print('ERROR: ',shape,'is not a valid choice. Please enter triangle,square, or octagon. ')
        shape = input('What kind of shape do you want to draw?  ')
        i = check(shape)
    number = int(input ('How many would you like to draw?  '))
    size = int(input('How big should the shapes be?  '))
    count = 0
    turtle.speed(0)
    while count < number:
        if shape.lower() == 'trangle':
            drawTri(size)
        elif shape.lower() =='square':
            drawSqr(size)
        elif shape.lower() == 'octagon':
            drawOct(size)
        turtle.left(360/number)
        count += 1
    turtle.hideturtle()
if __name__ == '__main__':
    main()
