def phone(num):
    name = {'A':'2','B':'2','C':'2','D':'3','E':'3','F':'3','G':'4',\
    'H':'4','I':'4','J':'5','K':'5','L':'5','M':'6','N':'6','O':'6',\
    'P':'7','Q':'7','R':'7','S':'7','T':'8','U':'8','V':'8','W':'9',\
    'X':'9','Y':'9','Z':'9'}
    number = '1234567890'
    letters = ['A','B','C','D','E','F','G','H','I','J','K',\
    'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    num0 = num.upper()
    num1 = []
    for x in num0:
        if x  in number:
            num1.append(x)
        elif x in letters:
            num1.append(name[x])
    num1 = ''.join(num1)
    if len(num1)== 10:
        num1 = num1[:3] + '-' + num1[3:6] + '-' + num1[6:]
    elif len(num1)== 7:
        num1 = num1[:3] + '-' + num1[3:]
    else:
        num1 = 'Invalid Number'
    print(num1)
def main():
    num = input('phone number:')
    phone(num)
if __name__ == '__main__':
    main()
