def makeDictionary(names,scores):
    scoreDict = dict(zip(names, scores))
    return scoreDict
def getScore(name,dic):
    if name in dic:
        return dic[name]
    else:
        return -1
def MorseCode():
    astr = input("Enter a phrase:")
    astr= astr.upper()
    morse = {
        'A' : ". _",
        'B' : "_ . . .",
        'C' : "_ . _ .",
        'D' : "_ . .",
        'E' : ".",
        'F' : ". . _ .",
        'G' : "_ _ .",
        'H' : ". . . .",
        'I' : ". .",
        'J' : ". _ _ _",
        'K' : "_ . _",
        'L' : ". _ . .",
        'M' : "_ _",
        'N' : "_ .",
        'O' : "_ _ _",
        'P' : ". _ _ .",
        'Q' : "_ _ . _",
        'R' : ". _ .",
        'S' : ". . .",
        'T' : "_",
        'U' : ". . _",
        'V' : ". . . _",
        'W' : ". _ _",
        'X' : "_ . . _",
        'Y' : "_ . _ _",
        'Z' : "_ _ . ."
    }
    for x in astr:
        print(morse[x])
def rankandSuitCount(alist):
    ranks= ['2','3', '4','5','6', '7', '8', '9', 'T', \
            'J', 'Q', 'K', 'A' ]
    suits= [ 'C', 'S', 'D', 'H' ]
    rank = {}
    suit = {}
    for x in alist:
        if x[0] in rank:
            rank[x[0]]+=1
        elif x[0] in suit:
            suit[x[0]] += 1
        elif x[0] in ranks:
            rank[x[0]] = 1
        else:
            suit[x[0]] = 1
        if x[1] in rank:
            rank[x[1]]+=1
        elif x[1] in suit:
            suit[x[1]] += 1
        elif x[1] in ranks:
            rank[x[1]] = 1
        else:
            suit[x[1]] = 1
    return rank,suit
def pokerHand(cards):
    rank,suit = rankandSuitCount(cards)
    if len(rank) == 5:
        str0 = ''
        if len(suit) == 1:
            str0 += 'flush'
        kr = rank.keys()
        kr = kr.sort()
        count = 0
        for x in kr:
            i = kr.index(x)
            if x.isnumeric():
                if x == '9':
                    if 'A' in kr or 'a' in kr:
                        break
                    if 'K' in kr or 'k' in kr:
                        if i >= 1:
                            break
                    if 'Q' in kr or 'q' in kr:
                        if i >=2:
                            break
                    if 'J' in kr or 'j' in kr:
                        if i >= 3:
                            break
                    if 'T' in kr or 't' in kr:
                        if i >= 4:
                            break
                    if i == 4:
                        count += 1
                elif int(kr[i+1])-int(kr[i]) == 1:
                    count+= 1
        if count == 4:
            str0 += 'straight'
        if str0 == '':
            print('high-card')
        else:
            print(str0)
    elif len(rank) == 4:
        print('one pair')
    elif len(rank) == 3:
        kindo3 = 0
        for k,v in rank.items():
            if v == 3:
                kindo3 = 1
        if kindo3 == 1:
            print('three-of-a-kind')
        else:
            print('two pair')
    elif len(rank) == 2:
        kindo4 = 0
        for k,v in rank.items():
            if v == 4:
                kindo4 = 1
        if kindo4 == 1:
            print("four-of-a-king")
        else:
            print('full-house')
def main():
    #warm up
    names = ['joe', 'tom', 'barb', 'sue', 'sally']
    scores = [10,23,13,18,12]
    scoreDict = makeDictionary(names,scores)
    scoreDict['john'] = 19
    print(scoreDict)
    #stretch
    MorseCode()
    #workout 1
    rank, suit = rankandSuitCount(['AS','AD','2C','TH','TS'])
    print(rank)
    print(suit)
if __name__ == "__main__":
    main()
