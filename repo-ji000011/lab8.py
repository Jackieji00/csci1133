import turtle
import random
def foo(n):
    if n<1:
        print('')
    else:
        print('*',end='')
        foo( n-1 )
def reverseNum(n):
    n = str(n)
    if len(n) < 1:
        print('')
    else:
        print(n[len(n)-1],end='')
        reverseNum(n[:-1])
def maxValue(vals):
    if len(vals) <2:
        print(vals[0])
    else:
        if vals[0] > vals[len(vals)-1]:
            maxValue(vals[:-1])
        else:
            maxValue(vals[1:])
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def tree(t,trunkLength):
    t.speed(0)
    if trunkLength < 5:
        return
    else:
        rand_angle = random.randint(15,45)
        rand_length = random.randint(12,18)
        t.forward(trunkLength)
        t.right(rand_angle)
        tree(t, trunkLength-rand_length)
        t.left(2*rand_angle)
        tree(t, trunkLength-rand_length)
        t.right(rand_angle)
        t.backward(trunkLength)

def choose(n,k):
    result = 0
    if k == 0 or n == k:
        result = 1
        return result
    else:
        return choose(n-1,k-1)+choose(n-1,k)
def GCD(a,b):
    if b ==0:
        return a
    else:
        return GCD(b,a%b)
def main():
    foo(12)
    reverseNum(5786)
    vals = [1,8,9,10,2,4,5,6,5]
    maxValue(vals)
    n=20
    i = 0
    t = turtle.Turtle()
    tree(t,100)
    while n > i:
        print(fibonacci(i),end=',')
        i += 1
    print(fibonacci(i))
    print(choose(52,5))
    print(GCD(1260,198))
if __name__ == '__main__':
    main()
