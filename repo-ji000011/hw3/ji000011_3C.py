#CSCI 1133 Homework 3
#Peiqi Ji
#Problem C
def summation(lowerb,upperb,stro):
    number = lowerb
    result = 0
    while number != upperb+1 :
        if stro.lower() == 'square':
            result += number **2
        elif stro.lower() == 'cube':
            result += number ** 3
        else:
            result += number ** -1
        number += 1
    return result
def check(lowerb,upperb,stro):
    num = '1234567890'
    for x in lowerb:
        if x not in num:
            return True
    for y in upperb:
        if y not in num:
            return True
    lowerb = int(lowerb)
    upperb = int(upperb)
    if lowerb == 0 or upperb < lowerb or upperb == 0:
        return True
    if stro.lower() == 'square' or  stro.lower() == 'cube' or stro.lower() == 'inverse':
        return False
    else:
        return True
def main():
    num = '1234567890'
    lowerb = input('Lower bound for the bound:  ')
    upperb = input('Upper bound for the bound:  ')
    stro = input('Function to be summed. Please choose from square, cube, and inverse.  ')
    while check(lowerb,upperb,stro):
        print('Your input is inappopriate. Please re-enter. ')
        lowerb = input('Enter a lower bound for the bound:  ')
        upperb = input('Enter a upper bound for the bound:  ')
        stro = input('Enter a function name to be summed. Please choose from square, cube, and inverse.  ')
    result = summation(int(lowerb),int(upperb),stro)
    print('The result of the summation is ',result )
if __name__ == '__main__':
    main()
