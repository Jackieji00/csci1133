# CSCI 1133 Homework5
# Peiqi Ji
# Problem 5B
def convertion(decnum,base):
    if decnum // base == 0: #the end case
        if decnum % base >=10: #when the reminder is bigger and equal to 10 convert to letters
            return chr(decnum%base+87)
        return str(decnum % base) #when the reminder is smaller than 10, left as number
    else: # the cases need to keep going
        if decnum % base >= 10: #when the reminder is bigger and equal to 10 convert to letters
            if decnum%base+87>122 # if the reminder exceeds 26
                num = (decnum%base-10)%26+96
            num = decnum%base+87
            return convertion(decnum//base,base) + str.upper(chr(num))
        else:#when the reminder is smaller than 10, left as number
            return convertion(decnum//base,base) + str(decnum%base)
def main():
    decnum = int(input('Enter your decimal number: '))
    base = int(input('Enter the base you want to convert to: '))
    outcome = convertion(decnum,base)
    print(decnum,' in base ',base,' is ', outcome)
if __name__ == '__main__':
    main()
