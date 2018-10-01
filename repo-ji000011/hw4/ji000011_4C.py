#CSCI 1133 Homework 4
#Peiqi Ji
#Problem C
def merge2(sentence1, sentence2):
    s1 = sentence1.split(' ')
    s2 = sentence2.split(' ')
    result = ''
    if len(s1) > len(s2): # find the range for the both
        mark = len(s2)
    else:
        mark = len(s1)
    if mark % 2 == 1: #because I am doing 2 each time , when plus one there is a risk of out of range, so I set to 2 cases.
        for i in range(0,mark-1,2):
            result = result + s1[i] +' ' + s1[i+1] + ' ' + s2[i] + ' ' + s2[i+1] + ' '
        if mark == len(s1): #put leftover on the result
            result += s1[mark-1] + ' '
            for word in s2[mark -1:]:
                result += word + ' '
        elif mark == len(s2):
            result += s1[mark-1] + ' ' + s1[mark] + ' ' + s2[mark-1] + ' '
            for word in s1[mark-1:]:
                result += word + ' '
    else:
        for i in range(0,mark,2):
            result = result + s1[i] +' ' + s1[i+1] + ' ' + s2[i] + ' ' + s2[i+1] + ' '
            print(result)
        if mark == len(s1): #put leftover on the result
            for word in s2[mark:]:
                result += word + ' '
        elif mark == len(s2):
            for word in s1[mark:]:
                result += word + ' '
    return result
