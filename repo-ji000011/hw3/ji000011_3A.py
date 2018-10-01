#CSCI 1133 Homework 3
#Peiqi Ji
#Problem A
def intvert(lst):
    result = []
    i = len(lst)-1
    while i != -1:
        if type(lst[i]) is int:
            result.append(lst[i])
        i -= 1
    return result
def main():
    print(intvert([3,2,1]))
if __name__ == '__main__':
    main()
