# CSCI 1133 Homework5
# Peiqi Ji
# Problem 5C
def factorial(num):
    if num == 1: #end case
        return 1
    else: #times a number smaller than itself by 1
        return num * factorial(num-1)
def taylor(term,radian):
    if term == 1: #the stop case
        return float(radian)
    else: #calculation
        if term % 2 == 1: # when the term is positive
            return float(radian**(term*2-1)/factorial(term*2-1)) + taylor(term-1,radian)
        return -float(radian**(term*2-1)/factorial(term*2-1)) + taylor(term-1,radian) #when the term is negative
def main():
    radian = float(input('Enter the angle to approximate (in radians): '))
    term = int(input('Enter the number of terms to compute: '))
    result = taylor(term,radian)
    print('sin (',radian,') ','is approximately ', result)
if __name__ == '__main__':
    main()
