# def mul(a,b):
#   i = 1
#   total = 0
#   while i <= b:
#     total +=a
#     i += 1
#   print(total)
def mul(a,b):
    product = 0
    while b != 0:
        b //= 2
        a *= 2
        if b % 2 != 0:
            product += a
            return(product)
def emul(a,b):
    product = 0
    print(a,b,product)
    if a >= 0 and b >= 0:
        product = mul(a,b)
        print(a,b,product)
    elif a < 0 and b < 0:
        product = mul(-a,-b)
        print(a,b,product)
    else:
        c = abs(a)
        d = abs(b)
        product = mul(c,d)
        product *= -1
        print(a,b,product)
if __name__ == '__main__':
    emul(5,-4)
