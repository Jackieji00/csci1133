def Countingkeword():
    pyname = input('Enter the filename:')
    keywords = ['False','class','finally','is','return',\
    'None','continue','for','lambda','try','True','def',\
    'from','nonlocal','while','and','del','global','not',\
    'with','as','elif','if','or','yield','assert','else',\
    'import','pass','break','except','in','raise']
    pyfile = open(pyname,'r')
    scrits = list(pyfile.readlines())
    result = {}
    letters = ['A','B','C','D','E','F','G','H','I','J','K',\
    'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for x in range(0,len(scrits)-1):
        scrits[x] = scrits[x].split(' ')
    for n in range(0,len(scrits)-1):
        for i in range(0,len(scrits[n])-1):
            if scrits[n][i] in keywords:
                if scrits[n][i] in result:
                    result[scrits[n][i]] += 1
                else:
                    result[scrits[n][i]] = 1
    pyfile.close()
    list0 = []
    for (k,v) in result.items():
        list0.append(k)
    list0.sort()
    print(result)
    print('Keyword frequency in alphabetic order:')
    for h in list0:
        print(h,' ',result[h])
