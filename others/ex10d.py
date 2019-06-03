class Smatrix:
    def __init__(self,dic={}):
        self.dic = dic
    def get(self,row,col):
        if (row,col) in self.dic:
            return self.dic[(row,col)]
        else:
            return 0
    def set(self,row,col,value):
        if value != 0 :
            self.dic[(row,col)] = value
        else:
            if (row,col) in self.dic:
                del self.dic[(row,col)]
    def __repr__(self):
        rep =[]
        mr = 0
        mc = 0
        for k,v in self.dic.items():
            if mr < k[0]:
                mr = k[0]
            if mc < k[1]:
                mc = k[1]
        rep.append([])
        while mc != 0:
            rep[0].append(0)
        rep = rep * mr
        for k,v in self.dic.items():
            rep[k[0]][k[1]]= v
        return rep
    def __add__(self,rhand):
        n = {}
        dit = self.dic
        for k,v in dit.items():
            n[k]=v
        for k,v in rhand.items():
            if k in n:
                n[k] += v
            else:
                n[k] = v
        return n
    def __sub__(self,rhand):
        n = {}
        dit = self.dic
        for k,v in dit.items():
            n[k]=v
        for k,v in rhand.items():
            if k in n:
                n[k] -= v
            else:
                n[k] = v
        return n
    def __mul__(self,rhand):
        n = {}
        dit = self.dic
        for k,v in dit.items():
            n[k]=v
        for k,v in rhand.items():
            if k in n:
                n[k] *= v
            else:
                n[k] = 0
        return n
