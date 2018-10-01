#CSCI 1133 Homework 4
#Peiqi Ji
#Problem B
def wordsCount(sentence):
    letters = 'qwertyuiopasdfghjklzxcvbnm ' #by definetion given in instruction, elements could appear in sentence
    errorMessage = 'Error.'
    for letter in sentence: #check if the input is valid
        if letter.lower() not in letters:
            return errorMessage
    sentence = sentence.split(' ')  # change a string into a list that every element in list is a word
    result = {}
    index = 0 # record the index since list.index() only return the 1st one.
    for word in sentence: #count the word
        if word.lower() not in result:
            result[word.lower()] = [index]
        else:
            result[word.lower()] += [index]
        index += 1
    return result
def main():
    while True:
        sentence = input('Enter a sentence: ') #ask input
        output =  wordsCount(sentence) #call the function
        for (k,v) in output.items():  # print the result
            str0 = str(k)
            for x in v:
                str0 = str0 + '  ' + str(x)
            print(str0)
        cont = input('Do you want to enter another sentence (Y/N)? ') #check if the program need to continue
        while cont.lower() != 'y' and cont.lower() != 'n': # if not y or n, keep asking
            cont = input('Invalid. Do you want to enter another sentence (Y/N)? ')
        if cont.lower() == 'y':
            continue
        elif cont.lower() == 'n':
            break
if __name__ == '__main__':
    main()
