import random as r

class graphNode:
    xPosList = [n for n in range(14,1286)]
    yPosList = [n for n in range(14,786)]
    graph = []

    def __init__(self,number,edges):
      self.color = (r.randint(50,255),r.randint(50,255),r.randint(50,255))
      x = r.choice(self.xPosList)
      y = r.choice(self.yPosList)
      self.position = [x,y]
      self.number = number
      self.edges = edges
      self.graph.append(self)

      

    


    


