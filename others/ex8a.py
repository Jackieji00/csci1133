def letterFrequency(str0):
    dic0 = {}
    str0 = str0.lower()
    list0 = list(str0)
    for x in list0:
        if x == ' ':
            del x
    for index in range(1,len(list0)):
        i = index-1
        value = list0[index]
        while i >=  0:
            if value < list0[i]:
                list0[i+1]=list0[i]
                list0[i]=value
                i -= 1
            else:
                break
    for x in list0:
        if x in dic0 and x != ' ':
            dic0[x]+=1
        elif x not in dic0 and x != ' ':
            dic0[x]=1
    for (k,v) in dic0.items():
        print(k,' ',v)
def main():
    str0= input("Enter a text string:")
    letterFrequency(str0)
if __name__ == '__main__':
    main()
