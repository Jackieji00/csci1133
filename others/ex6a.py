def wordlist(prose):
    prose = prose.rstrip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    list0 = prose.split(' ')
    list1 = [ ]
    i = 0
    for x in range(0,len(list0)):
        if list0[x] not in list1:
            list1.append(list0[x])
    if '' in list1:
        list1.remove('')
    print(list1)
def main():
    prose = input("enter a string:")
    wordlist(prose)
if __name__ == '__main__':
    main()
