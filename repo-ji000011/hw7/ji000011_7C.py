# CSCI 1133 Homework7
# Peiqi Ji
# Problem 7C
def mine_file(fname):
    infile = open(fname,'r')
    frequency = {}
    content = infile.readline()
    uniqueWordCount = [] #storage every different word
    frequency['Apostrophe Word Count'] = 0
    total = 0       #store total Word Count
    while content:
        content = content.replace('--',' ') #change hash or dash into space
        content = content.replace('-',' ')
        listContent = content.split(' ') #split by space
        letters = "abcdefghijklmnopqrstuvwxyz'"
        if '\n' in listContent:
            listContent.remove('\n') # get rid of '\n' which could cause error
        for word in listContent:
            if "'" in word:
                frequency['Apostrophe Word Count'] += 1
            newWord = '' # only keep the letters and '
            for letter in word:
                if letter.lower() in letters:
                    newWord += letter.lower()
            if newWord not in uniqueWordCount:
                uniqueWordCount.append(newWord)
            if newWord not in frequency:
                frequency[newWord] = 1
            else:
                frequency[newWord] += 1
            total += 1
        content = infile.readline()
    infile.close()
    klist = []      #store keys
    vlist = []      #store value
    for key,value in frequency.items():
        if value >= 5 and key != 'Apostrophe Word Count':   #only store the key and values that bigger or equal to 5
            klist.append(key)
            vlist.append(value)
    print('Word Count: ',total)
    print('Unique Word Count: ', len(uniqueWordCount))
    print('Apostrophe Word Count: ',frequency['Apostrophe Word Count'])
    while len(vlist) != 0:      #sort the order by value
        maxnum = max(vlist)
        print(klist[vlist.index(maxnum)],': ', maxnum)
        del klist[vlist.index(maxnum)]
        vlist.remove(maxnum)
