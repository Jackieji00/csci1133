# CSCI 1133 Homework7
# Peiqi Ji
# Problem 7C
def crime_report(fnameCSV):
    infile = open(fnameCSV,'r')
    outfile = open('stealingOffenses.txt','w')
    title = infile.readline()
    content = infile.readline()
    theft = {}
    burglary = {}
    robbery = {}
    while content:
        content = content.split(',')
        theft = findCrimeLocation('THEFT',content,theft)
        burglary = findCrimeLocation('BURGLARY',content,burglary)
        robbery = findCrimeLocation('ROBBERY',content,robbery)
        content = infile.readline()
    outfile.write(dicToReport('Theft',theft))
    outfile.write(dicToReport('Burglary',burglary))
    outfile.write(dicToReport('Robbery',robbery))
    infile.close()
    outfile.close()
def findCrimeLocation(typeCrime,content,record): #find crime and its location, then record them into dictionary
    if typeCrime in content[5]:
        if content[2] not in record:
            record[content[2]] = 0
        record[content[2]] += 1
    return record
def dicToReport(typeCrime,record): #change dictionary to report
    str0 = typeCrime + ' by District:\n'
    listKey = [] # to sort the District from small to big
    for key in record.keys():
        listKey.append(key)
    listKey.sort()
    for k in listKey:
        str0 += k + ': ' + str(record[k]) + '\n'
    return str0
