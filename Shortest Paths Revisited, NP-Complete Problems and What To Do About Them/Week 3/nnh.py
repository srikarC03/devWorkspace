# Nearest Neighbor Hueristic for TSP
# Graph input is in the form of vertices as keys and their respective outgoing edges as values
import math

def dist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5


def nnHueristic(G,n):
    # Initialize all variables 
    tourCost = 0
    visitedCities = set([1])
    currentCity = 1
    nextCity = None
    to1 = []

    print("All variables initialized, starting tour...")
    print("1,",end="")

    # while there are unvisited cities loop through outgoing edges of current city and travel to nearest one
    while len(visitedCities) < n:
        
        min = math.inf

        for i in range(n):
            if i+1 in visitedCities: continue
            else:
                d = dist(G[currentCity-1][0],G[currentCity-1][1],G[i][0],G[i][1])
                if d == 0: print("error")
                if currentCity == 1: to1.append(d)
                if d < min:
                    min = d
                    nextCity = i+1
        
        currentCity = nextCity
        print(str(currentCity)+",",end="")
        visitedCities.add(currentCity)
        tourCost+=min
    
    tourCost+=to1[currentCity-2]
    print("1")
    print("Tour finished, heuristic solution: " + str(tourCost))
    return tourCost

