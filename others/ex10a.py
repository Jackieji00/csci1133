import math
class Circle():
    def __init__(self,radius=0):
        self.radius = radius
    def setRadius(self,r):
        self.radius = r
    def getCircumference(self):
        circumference = math.pi * 2 * self.radius
        return circumference
    def getArea(self):
        Area = math.pi * (self.radius **2)
        return Area
