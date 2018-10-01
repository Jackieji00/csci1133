import turtle
import random
class Shape:
    def __init__(self,x=0,y=0,fillcolor = '',isFill = False):
        self.x = x
        self.y = y
        self.fc = fillcolor
        self.iF = isFill
    def setFillcolor(self,str0):
        self.fc = str0
    def setFilled(self,bool0):
        self.iF = bool0
class Circle(Shape):
    def __init__(self,x=0,y=0,r=0):
        self.r = r
        Shape.__init__(self,x,y)
    def draw(self,t):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(self.x,self.y)
        t.pendown()
        if self.iF:
            t.fillcolor(self.fc)
            t.begin_fill()
            t.circle(self.r)
            t.end_fill()
        else:
            t.circle(self.r)
    def isIN(self,x,y):
        if x>= self.x and x >= self.x+self.w and y >=self.y and y <= self.y +self.h:
            return True
        else:
            return False
class Display:
    def __init__(self,elements = [],t= turtle.Turtle(),s=turtle.getscreen()):
        self.elements = elements
        self.t = t
        self.s = s
        self.t.speed(0)
        self.s.delay(0)
        self.t.hideturtle()
        self.s.onclick(self.mouseEvent)
        self.s.listen()
    def mouseEvent(self,x,y):
        self.t.hideturtle()
        self.color = ['red','blue','yellow','purple','pink','green','grey']
        random.shuffle(self.color)
        radius=random.randint(10,100)
        if self.elements[0] == 'circle':
            a = Circle(x,y,radius)
            self.remove('circle')
        elif self.elements[0] == 'rectangle':
            h=random.randint(10,100)
            w=random.randint(10,100)
            a = Rectangle(x,y,w,h)
            self.remove('rectangle')
        else:
            return False
        a.setFillcolor(self.color[0])
        a.setFilled(True)
        a.draw(self.t)
    def add(self,shape):
        self.elements.append(shape)
    def remove(self,shape):
        self.elements.remove(shape)
class Rectangle(Shape):
    def __init__(self,x=0,y=0,w=0,h=0):
        self.w = w
        self.h = h
        Shape.__init__(self,x,y)
    def draw(self,t):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(self.x,self.y)
        t.pendown()
        if self.iF:
            t.fillcolor(self.fc)
            t.begin_fill()
        t.fd(self.w)
        t.right(90)
        t.fd(self.h)
        t.right(90)
        t.fd(self.w)
        t.right(90)
        t.fd(self.h)
        if self.iF:
            t.end_fill()
    def isIN(self,x,y):
        if x>= self.x and x >= self.x+self.w and y >=self.y and y <= self.y +self.h:
            return True
        else:
            return False
Display()
