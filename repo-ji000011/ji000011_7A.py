class Complex:
    def init(self,real = 0.0,imag = 0.0):
        self.real = real
        self.imag = imag
    def __add__(self,righthand):
        resultReal = self.real + righthand.real
        resultImag = self.imag + righthand.imag
        return Complex(resultReal,resultReal)
    def __sub__(self,righthand):
        resultReal = self.real - righthand.real
        resultImag = self.imag - righthand.imag
        return Complex(resultReal,resultReal)
    def __mul__(self,righthand):
        resultReal = self.real * righthand.real + self.imag * righthand.imag *-1
        resultImag = self.real * righthand.imag + self.imag * righthand.real
        return Complex(resultReal,resultReal)
    def __truediv__(self,righthand):
        if righthand.imag == 0 
