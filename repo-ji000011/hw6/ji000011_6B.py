# CSCI 1133 Homework6
# Peiqi Ji
# Problem 6B
def parse_string(string):
    WORD_NO_NEEDED = ['to', 'the', 'and', 'I', 'of','he', 'she', 'a', 'I’ll', 'I’ve',
 'but', 'by', 'we', 'whose', 'how', 'go', 'such', 'this', 'me', 'can', 'she’s',
 'he’s', 'have', 'has', 'had', 'an', 'did', 'so', 'to', 'we’ll','on','him','well',
 'or', 'be', 'as', 'those', 'there', 'are', 'do', 'too','if', 'it', 'at', 'what',
 'that', 'you', 'will', 'in', 'with' ,'not' ,'for', 'is' ,'my' ,'o' ,'her' ,'his', 'am']
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    stringNoP = ''
    for x in string: #get rid of the punctuation or special character.
        if x.upper() in letters:
            stringNoP += x
    listBefore = stringNoP.split(' ')
    result = {}
    for word in listBefore: # count the words
        if word.lower() not in WORD_NO_NEEDED and word not in WORD_NO_NEEDED: #Discount the boring word
            if word not in result: #set the first one in dictionary
                result[word] = 1
            else:
                result[word] += 1
    for k,v in result.items(): #printout the result
        if v >=5:
            print(k,' ','X'*(v//5),'*'*(v%5))
        else:
            print(k,' ','*'*v)
def main():
    parse_string('I had a good dog not a cat. A dog eats pizzas. A dog is happy. There is a happy dog there in the dog park.')
if __name__ == '__main__':
    main()
