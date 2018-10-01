#CSCI 1133 Homework 
#Peiqi Ji
#Problem 2B
def ZodiacSigns(month, day):
    if month == 1:
        if day >= 20:
            return 'Aquarius'
        else:
            return 'Capricorn'
    elif month == 2:
        if day >= 19:
            return 'Pisces'
        else:
            return 'Aquarius'
    elif month == 3:
        if day <= 20:
            return 'Pisces'
        else:
            return 'Aries'
    elif month == 4:
        if day <=19:
            return 'Aries'
        else:
            return 'Taurus'
    elif month == 5:
        if day <= 20:
            return 'Taurus'
        else:
            return 'Gemini'
    elif month == 6:
        if day <= 20:
            return 'Gemini'
        else:
            return 'Cancer'
    elif month == 7:
        if day <= 22:
            return 'Cancer'
        else:
            return 'Leo'
    elif month == 8:
        if day <= 22:
            return 'Leo'
        else:
            return 'Virgo'
    elif month == 9:
        if day <= 22:
            return 'Virgo'
        else:
            return 'Libra'
    elif month == 10:
        if day <= 22:
            return 'Libra'
        else:
            return 'Scorpio'
    elif month == 11:
        if day <= 21:
            return 'Scorpio'
        else:
            return 'Sagittarius'
    elif month == 12:
        if day <= 21:
            return 'Sagittarius'
        else:
            return 'Capricorn'
def checkthedate(month,day):
    month30 = [4,6,9,11]
    if month < 0 or month >12:
        return 0
    elif day >31 or day < 0:
        return 0
    elif month in month30 and day > 30:
        return 0
    elif month == 2 and day > 28:
        return 0
    else:
        return 1
def main():
    month = int(input('Month of birth: '))
    day = int(input('Day of birth: '))
    i = checkthedate(month,day)
    while i == 0:
        print('Invalid date')
        month = int(input('Month of birth: '))
        day = int(input('Day of birth: '))
        i = checkthedate(month,day)
    print(ZodiacSigns(month,day))
if __name__ == '__main__':
    main()
