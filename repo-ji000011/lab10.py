class rational:
    def __init__(self,num=0,den=1):
        self.numerator = num
        if den == 0:
            self.denominator = 1
        else:
            self.denominator = den
    def __str__(self):
        if self.numerator % self.denominator ==0:
            return str(int(self.numerator/self.denominator))
        return str(self.numerator) + '/' + str(self.denominator)
class measure:
    def __init__(self, feet=None,inch=None):
        self.ft = feet
        self.inch = inch
        if feet == None and inch == None:
            self.ft = 0
            self.inch = 0
        elif inch == None and feet != None:
            self.ft = feet//12
            self.inch = feet%12
        elif inch >= 12:
            self.ft += inch//12
            self.inch = inch%12
        elif inch <0:
            self.inch += 12
            self.ft -= 1
    def __str__(self):
        return str(self.ft) + "'" +str(self.inch) + '"'
    def __add__(self,rhand):
        return measure(self.ft+rhand.ft,self.inch+rhand.inch)
    def __sub__(self,rhand):
        return measure(self.ft-rhand.ft,self.inch-rhand.inch)
class vec3:
    def __init__(self,alit =[0,0,0]):
        self.vec = alit
    def __str__(self):
        return str(self.vec)
    def vlist(self):
        return self.vec
    def setValues(self,alist):
        self.vec = alist
    def __float__(self):
        return (self.vec[0]**2+self.vec[1]**2+self.vec[2]**2)**(1/2)
    def __add__(self,rhand):
        return [self.vec[0]+rhand.vec[0],self.vec[1]+rhand.vec[1],self.vec[2]+rhand.vec[2]]
    def __truediv__(self,scalar):
        return [self.vec[0]/scalar,self.vec[1]/scalar,self.vec[2]/scalar]
def main():
    alist = list(input('Please input forceA: '))
    blist = list(input('Plase input forceB: '))
    mass = float(input('Plase input mass: '))
    a = vec3(alist)
    b = vec3(blist)
    result = a +b
