import turtle
import random
class Shape:
    def __init__(self, x=0, y=0, fillColor='', B=False):
        self.x=x
        self.y=y
        self.fillColor=fillColor
        self.B=B
    def setFillcolor(self,str):
        self.fillColor= str
    def setFilled(self,bool):
        self.B = bool
    def isFilled(self):
        return str(x)+','+str(y)+str(self.fillcolor)
class Circle(Shape):
    def __init__(self,x=0,y=0,radius=100,fillColor='', B=False):
        self.r=radius
        super().__init__(x,y,fillColor,B)
    def draw(self,t):
        t.goto(self.x,self.y)
        if self.B:
            t.fillcolor(self.fillColor)
            t.begin_fill()
            t.circle(self.r)
            t.end_fill()
        else:
            t.circle(self.r)
class Display:
    def __init__(self, elements=[],t=turtle.Turtle(),Screen=turtle.getscreen()):
        self.t = t
        self.t.penup()
        self.Screen = Screen
        self.t.hideturtle()
        self.t.speed(0)
        self.Screen.delay(0)
        self.elements=elements
        self.Screen.onclick(self.mouseEvent)
        self.Screen.listen()
    def mouseEvent(self,x,y):
        radius=random.randint(10,100)
        color=['red','blue','black','yellow']
        a = Circle(x,y,radius)
        a.setFillcolor(random.choice(color))
        a.setFilled(True)
        a.draw(self.t)
    # def add(shape):
    #     self.elements.append(shape)
    #     shape.draw(t)

def main():
    a = Display()
if __name__ == '__main__':
    main()
