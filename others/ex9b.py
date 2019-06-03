def rerange(exname):
    exfile = open(exname,'r')
    contents = list(exfile.readlines())
    for i in range(0,len(contents[0])):
        for x in range(0,len(contents)):
        print(contensts[x][i])
