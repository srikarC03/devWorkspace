class UnionFind:

    def __init__(self, data):
        self.data = {}
        for node in data:
            self.data[node] = (node,0)
    
    def __str__(self):
        return(str(self.data))
    
    def parent(self, element):
        return self.data[element][0]


    def rank(self, element):
        return self.data[element][1]
    

    def updateRank(self, element):
        self.data[element] = (self.parent(element),self.rank(element)+1)
    

    def updateParent(self,element, parent):
        self.data[element] = (parent,self.rank(element))
    

    def find(self, element):
        pointer = None
        current = element
        while True:
            pointer = self.parent(current)
            if self.parent(pointer) == pointer:
                self.data[element] = (pointer,self.rank(element))
                return pointer
            else:
                current = pointer
    

    def union(self, element1, element2):
        x = self.find(element1)
        y = self.find(element2)
        if self.rank(x) >= self.rank(y):
            self.updateParent(y,x)
            if self.rank(x) == self.rank(y): 
                self.updateRank(x)
        else:
            self.updateParent(x,y)




