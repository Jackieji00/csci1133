# CSCI 1133 Homework6
# Peiqi Ji
# Problem 6A
UNICODE_DICTIONARY = {
'pizza': 127829,'chicken':127831,'apple':127822,'peach':127825,
'cherry':127826,'yam':127840,'pineapple':127821,'cookie':127850,
'bread':127838,'lemon':127819,'banana':127820,'strawberry':127827
}         #global variable that will not changed.
def lookup(d,item):    #lookup method
    if item.lower() in d.keys():
        result = chr(UNICODE_DICTIONARY[item.lower()])
        print(item.lower(),' ',d[item.lower()]*result)
    return
def addItem(d,item):   #add item in to the dictionary
    if item.lower() in d.keys():
        d[item.lower()] += 1
    else:
        d[item.lower()] = 1
    return d
def subItem(d,item): #sub item into the dictionary
    if item not in d:
        return d
    elif d[item.lower()] == 1:
        del d[item.lower()]
    elif d[item.lower()] > 1:
        d[item.lower()] -= 1
    return d
def show(d): #show everything in the dictionary
    for k,v in d.items():
        print(k.lower(),chr(UNICODE_DICTIONARY[k.lower()])*v)
def main():
    d = {}
    while True:
        item = input('=> ')
        list0 = item.split(' ')
        if list0[0].lower() == 'add':
            d = addItem(d,list0[1])
        elif list0[0].lower() == 'sub':
            d = subItem(d,list0[1])
        elif list0[0].lower() == 'show':
            show(d)
        elif list0[0].lower() == 'lookup':
            lookup(d,list0[1])
        elif list0[0].lower() == 'quit':
            break
if __name__ == '__main__':
    main()
