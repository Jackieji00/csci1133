#CSCI 1133 Homework 
#Peiqi Ji
#Problem 2A
def newFib(term1,term2,i):
    newseries = []
    result = ''
    newseries.append(term1)
    newseries.append(term2)
    while len(newseries) < i:
        term3 = term1 +term2
        term1 = term2
        term2 = term3
        newseries.append(term3)
    for x in newseries:
        result += str(x)
        result += ' '
    return result
def main():
    term1 = int(input('Enter the first term of the series: '))
    term2 = int(input('Enter the second term of the series: '))
    i = int(input('Enterthe number of terms you want to see: '))
    result = newFib(term1,term2,i)
    print('The first 4 terms of the new series are: ',result)
if __name__ == '__main__':
    main()
