import random as r
import copy 
def randContraction(graph,n):
    x = copy.deepcopy(graph)
    newVertex = n
    while n > 2:
        newVertex+=1
        c = randomEdge(x)
        updateGraph(x, c, newVertex)
        n-=1
    edges = minCut(x)
    return (x,edges)
    

def updateGraph(g, contraction, new):
    tmp = []
    for vertex in g:
        if vertex in contraction:
            for obj in g[vertex]:
                if obj not in contraction:
                    tmp.append(obj)

        else:
            for pair in range(len(g[vertex])):
                if g[vertex][pair] in contraction:
                    g[vertex][pair] = new

    for element in contraction:
        g.pop(element)
    g[new] = tmp

def randomEdge(g):
    tmp = list(g.keys())
    x = r.choice(tmp)
    y = r.choice(g[x])
    return (x,y)

def minCut(g):
    count = 0
    k = list(g.keys())
    for each in g[k[0]]:
        count+=1
    return count
