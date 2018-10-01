#CSCI 1133 Homework 4
#Peiqi Ji
#Problem C
import ji000011_4A
def check(aList,atarget): #check if inputs are valid
    letters = '-1234567890 ' #elements that will appear in both atarget and aList
    for x in aList: # check list
        if x not in letters:
            return True
    for y in atarget: # check target
        if y not in letters or y == ' ': #space is no needed because there is only one # for target
            return True
    return False
while True: #for further continue
    atarget = input('Input target: ')
    aList = input('Input list of numbers separated by a space: ')
    while check(aList,atarget):                 #check if inputs are valid. If it is not valid, keep running
        print('Your inputs are invalid. Both target and list should only contain integer.')
        atarget = input('Input target: ')
        aList = input('Input list of numbers separated by a space: ')
    atarget = int(atarget)
    aList = aList.split(' ')
    for i in range(0,len(aList)):   # change all elements in list from string to intege
        aList[i] = int(aList[i])
    (num1,num2) = ji000011_4A.two_sums(aList,atarget)
    print('The two numbers that sum up to', atarget, ' are ',num1,' and ',num2)
    cont = input('Would you like to enter another list and target? (y/n): ')
    while cont.lower() != 'y' and cont.lower() != 'n': # if not y or n, keep asking
        cont = input('Invalid. Do you want to enter another sentence (Y/N)? ')
    if cont.lower() == 'y':
        continue
    elif cont.lower() == 'n':
        break
