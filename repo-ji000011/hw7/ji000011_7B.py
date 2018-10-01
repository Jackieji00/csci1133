# CSCI 1133 Homework7
# Peiqi Ji
# Problem 7B
class Member:
    def __init__(self,instrument,player):
        self.instrument = instrument
        self.player = player

    def getInstrument(self):
        return self.instrument

    def getPlayer(self):
        return self.player

    def setInstrument(self,instrument):
        self.instrument = instrument

    def setPlayer(self,player):
        self.player = player

    def __str__(self):
        return str(self.player) + ' plays ' + str(self.instrument)

    def __eq__(self,rhand):     #case non sensetive
        if self.instrument.lower() == rhand.instrument.lower() and self.player.lower() == rhand.player.lower():
            return True
        else:
            return False


class Band:
    def __init__(self,name,listMembers):
        self.name = name
        self.listMembers = listMembers

    def getBandName(self):
        return self.name

    def getPlayers(self):
        list0 = [] #empty list for player name
        for x in self.listMembers:
            list0.append(x.getPlayer())
        return list0

    def getInstruments(self):
        dic = {}
        for x in self.listMembers:
            if x.getInstrument().lower() in dic:
                dic[x.getInstrument().lower()] += 1
            else:
                dic[x.getInstrument().lower()] = 1
        return dic

    def addMember(self,member):
        self.listMembers.append(member)

    def removeMember(self,member):
        dellist = []   # it it the delete list
        for x in self.listMembers:
            if x == member:
                dellist.append(x)
        for deletion in dellist:
            self.listMembers.remove(deletion)

    def __str__(self):
        str0= ''
        for x in self.listMembers:   # unpacking the list and convert them to string
            if x == self.listMembers[len(self.listMembers)-1]: # the last won't have the new line
                str0 += str(x)
            else:
                str0 += str(x) +'\n'
        return 'Members of ' + self.name +':\n' + str0

    def findPlayer(self,player):
        list0 = []
        for x in self.listMembers:           #find the same player and none case sensetive
            if x.getPlayer().lower() == player.lower():
                list0.append(x)
        if len(list0) == 0:            #return if nothing find
            return self.name + ' does not have any player named ' + player
        else:                          #return if find something
            str0 = ''
            for y in list0:
                str0 += str(y) + '\n'
            return str0

    def findInstrument(self,instrument):
        list0 = []
        for x in self.listMembers:
            if x.getInstrument().lower() == instrument.lower():    #find the same instrument and none case sensetive
                list0.append(x)
        if len(list0) == 0:        #if find nothing
            return self.name + ' does not have any ' + instrument + ' players'
        else:
            str0 = ''
            for y in list0:       #if find something
                str0 += str(y) + '\n'
            return str0
