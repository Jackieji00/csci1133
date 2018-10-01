# CSCI 1133 Homework6
# Peiqi Ji
# Problem 6C
import turtle
class Caterpillar:
    def __init__(self,bodyColor = 'green',legsColor = 'purple',bodySize = 50):
        self.bc = bodyColor
        self.lc = legsColor
        self.bs = bodySize
        turtle.speed(0)
    def draw_body(self):
        turtle.hideturtle()
        turtle.penup()
        for i in range(1,6):
            turtle.goto(0,self.bs*i)
            turtle.dot(self.bs*2,self.bc)
        turtle.pendown()
    def draw_antennae(self):
        turtle.color(self.lc)
        turtle.penup()
        turtle.goto(self.bs*(1/2),self.bs*5+self.bs*(3**(1/2))/2)
        turtle.pendown()
        turtle.goto(self.bs,3**(1/2)*self.bs+self.bs*5)
        turtle.penup()
        turtle.goto(-self.bs*(1/2),self.bs*5+self.bs*(3**(1/2))/2)
        turtle.pendown()
        turtle.goto(-self.bs,3**(1/2)*self.bs+self.bs*5)
    def draw_legs(self):
        turtle.color(self.lc)
        for i in range(0,4):
            turtle.penup()
            turtle.goto(self.bs,i*self.bs + self.bs)
            turtle.pendown()
            turtle.goto(self.bs*2,i*self.bs +self.bs)
            turtle.goto(self.bs*3,i*self.bs +self.bs/2)
            turtle.penup()
            turtle.goto(-self.bs,i*self.bs +self.bs)
            turtle.pendown()
            turtle.goto(-self.bs*2,i*self.bs +self.bs)
            turtle.goto(-self.bs*3,i*self.bs +self.bs/2)
    def display(self):
        self.draw_legs()
        self.draw_body()
        self.draw_antennae()
class Butterfly(Caterpillar):
    def __init__(self,wingcolor = 'red',bodyColor = 'green',legsColor = 'purple',bodySize = 50):
        self.wc = wingcolor
        Caterpillar.__init__(self,bodyColor,legsColor,bodySize)
        turtle.speed(0)
    def draw_wings(self):
        turtle.color(self.wc)
        turtle.penup()
        turtle.goto(0,self.bs)
        turtle.pendown()
        turtle.fillcolor(self.wc)
        turtle.begin_fill()
        turtle.goto(-3*self.bs+10,-self.bs)
        turtle.goto(-3*self.bs+10,self.bs*6)
        turtle.goto(0,self.bs*4)
        turtle.goto(3*self.bs-10,self.bs*6)
        turtle.goto(3*self.bs-10,-self.bs)
        turtle.goto(0,self.bs)
        turtle.end_fill()
    def display(self):
        self.draw_body()
        self.draw_antennae()
        self.draw_legs()
        self.draw_wings()
