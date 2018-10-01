# CSCI 1133 Homework7
# Peiqi Ji
# Problem 7A
class Complex:
    def __init__(self,real = 0.0,imag = 0.0):
        self.real = real
        self.imag = imag
    def __add__(self,rhand):
        return Complex(self.real + rhand.real,self.imag + rhand.imag)
    def __sub__(self,rhand):
        return Complex(self.real-rhand.real,self.imag-rhand.imag)
    def __mul__(self,rhand):
        return Complex(self.real*rhand.real-self.imag*rhand.imag,self.real*rhand.imag+rhand.real*self.imag)
    def __truediv__(self,rhand):
        if rhand.imag+rhand.real == 0:
            return None
        else:
            return Complex((self.real*rhand.real+self.imag*rhand.imag)/(rhand.imag**2+rhand.real**2),(self.imag*rhand.real-self.real*rhand.imag)/(rhand.imag**2+rhand.real**2))
    def __str__(self):
        if self.real != 0:
            if self.imag > 0:
                return str(self.real) + '+' + str(self.imag) + 'i'
            elif self.imag < 0:
                return str(self.real) + str(self.imag) + 'i'
            elif self.imag == 0:
                return str(self.real)
        elif self.real == 0:
            if self.imag != 0:
                return str(self.imag) + 'i'
            else:
                return str(0)
def main():
    real1 = float(input('Enter the real value of the first complex number: '))
    imag1 = float(input('Enter the imaginary value of the first complex number: '))
    real2 = float(input('Enter the real value of the first complex number: '))
    imag2 = float(input('Enter the imaginary value of the first complex number: '))
    c1 = Complex(real1,imag1)
    c2 = Complex(real2,imag2)
    print('C1 = ',c1)
    print('C2 = ',c2)
    print('C1+C2 = ',c1+c2)
    print('C1-C2 = ',c1-c2)
    print('C1*C2 = ',c1*c2)
    if c1/c2 == None:
        print('C1/C2 = ',c1/c2,'; Divide by Zero Error!')
    else:
        print('C1/C2 = ',c1/c2)
if __name__ == '__main__':
    main()
