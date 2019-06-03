# CSCI 1133 Homework1
# Peiqi Ji
# Bonus Problem 1
import turtle
def focalLength (od,imd):
    answer = od ** -1 + imd ** -1
    answer = answer ** -1
    print("the focal length:" + str(answer) + " mm")
    turtle.showturtle()
    turtle.goto(-od,0)
    turtle.color("red")
    turtle.shape("square")
    turtle.penup()
    turtle.goto(-od,10)
    turtle.pendown()
    turtle.stamp()
    turtle.color("black")
    turtle.penup()
    turtle.goto(-od,20)
    turtle.write('Object')
    turtle.goto(-od,0)
    turtle.pendown()
    turtle.goto(imd,0)
    turtle.color('blue')
    turtle.penup()
    turtle.goto(imd,10)
    turtle.pendown()
    turtle.stamp()
    turtle.penup()
    turtle.color('black')
    turtle.goto(imd,20)
    turtle.write('Image')
    turtle.goto(0,0)
    turtle.pendown()
    turtle.goto(0,100)
    turtle.goto(0,-100)
    turtle.goto(0,0)
    turtle.goto(answer,0)
    turtle.color('green')
    turtle.shape('circle')
    turtle.stamp()
    turtle.color('black')
    turtle.penup()
    turtle.goto(answer,-10)
    turtle.write('Focal Point')
    turtle.goto(-answer,0)
    turtle.color('green')
    turtle.pendown()
    turtle.stamp()
    turtle.penup()
    turtle.goto(-answer,-10)
    turtle.color('black')
    turtle.write('Focal Point')
    turtle.hideturtle()
def main():
    print("Welcome to the Focal Length Calculator!")
    od = float(input("enter an object distance(mm): "))
    imd = float(input("enter an image  distance(mm): "))
    focalLength(od,imd)
if __name__ == '__main__':
    main()
