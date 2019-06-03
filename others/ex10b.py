class bug:
    def __init__(self,position=0):
        self.position = position+1
        self.direction = 'right'
    def turn(self):
        if self.direction == 'right':
            self.direction = 'left'
        else:
            self.dirction = 'right'
    def move(self):
        if self.direction == 'right':
            self.position +=1
        else:
            self.position -=1
    def display(self):
        x = self.position
        if self.direction == 'right':
            print('.'*x, '>')
        else:
            print('<','.'*abs(x))
def main():
    b=bug(10)
    b.turn()
    i = 0
    while i != 13:
        b.move()
        i += 1
    b.display()
if __name__ == '__main__':
    main()
