import randContraction as rc
import math as m


#d = {1:[2,3],2:[1,3],3:[1,2]}
f = open("kargerMinCut.txt","r")


adjList = {}
for each in f.readlines():
    tmp = each.split("\t")
    tmp.remove("\n")
    tmp = list(map(int,tmp))
    adjList[tmp[0]] = tmp[1:]

rep = int(((len(adjList))**2) * m.log(len(adjList)))
rep=10
graphArr = []
minArr = []
for n in range(rep):
    (arr,minCut) = rc.randContraction(adjList,200)
    graphArr.append(arr)
    minArr.append(minCut)

m = min(minArr)
g = graphArr[minArr.index(m)]

print(m,g)




