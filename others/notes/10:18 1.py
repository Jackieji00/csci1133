def main():
    userwishes = True
    while userwishes:
        ister = input("enter a binary value:")
        value = binaryToint(ister)
        cont = input("Continue?(y/n)")
        if cont == 'y' or cont == 'Y':
            userwishes = False
        print(value)
def binaryToint(bstr):
    i = len(bstr)-1
    pow2 = 0
    value = 0
    while i >= 0:
        value += int(bstr[i])*2**pow2
        i -= 1
        pow2 += 1
    return value
if __name__ == '__main__':
    main()

recursive:
    1.have a if statement that will consider any posible input.
    2.base case or a stopping case always return a revie value
    3.recrusion statement, redesion stops.
