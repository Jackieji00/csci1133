class measure:
    def __init__(self,feet=0,inches=0):
        if inches >= 12:
            self.feet = feet + inches//12
            self.inches = inches%12
        else:
            self.feet = feet
            self.inches = inches
    def str(self):
        ffeet = str(self.feet)+ "'"
        finches = str(self.inches)+ '"'
        if self.feet == 0:
            ffeet = ''
        if self.inches == 0:
            finches =''
        return ffeet + finches
    def __add__(self,rhand):
        inches0 = self.inches + rhand.inches
        feet0 = self.feet + rhand.feet
        m = measure(feet0,inches0)
        return m
    def __sub__(self,rhand):
        inches0 = self.inches - rhand.inches
        feet0 = self.feet - rhand.feet
        m = measure(feet0,inches0)
        return m
    def __repr__(self):
        ffeet = str(self.feet)+ "'"
        finches = str(self.inches)+ '"'
        if self.feet == 0:
            ffeet = ''
        if self.inches == 0:
            finches =''
        return ffeet + finches
