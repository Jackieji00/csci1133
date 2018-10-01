#CSCI 1133 Homework 4
#Peiqi Ji
#Problem A
def two_sums(aList,target):
    for i in range(0,len(aList)):
        for index in range(i+1,len(aList)):
            if aList[i] + aList[index] == target:
                return (aList[i],aList[index])      
