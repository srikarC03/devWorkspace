import copy as c
import math
import itertools as it

# graph is a dictionary in the form of vertices as keys and incoming edges as values

def nCr(n,r):
    return math.factorial(n) / (math.factorial(n-r) * math.factorial(r))

def subSets(n):
    S = []
    s = [l+1 for l  in range(n)]
    for m in range(n):
        tmp = list(it.combinations(s,m+1))
        tmp = tmp[:int(nCr(len(s)-1,m))]
        for subproblem in tmp:
            S.append(subproblem)
    return S



def TSP(G,n):

    #Preprocessing all subsets of data and initializing them
    A = {}
    S = subSets(n)
    size = 2
    for sets in S:
        if A.get(len(sets)) is None:
            if sets == (1,): A[len(sets)] = {(sets,1):0}
            else: A[len(sets)] = {(sets,1):math.inf}
        else:
            A[len(sets)][(sets,1)] = math.inf
    print("All data structures initialized")
    print("Subsets of size 2: ", end = "")
    
    #Looping through all subproblem from smallest to largest, solving the min solution for each case
    for series in S[1:]:
        if len(series) > size:
            print("finished")
            del A[size-1]
            size+=1
            print("Subsets of size " + str(size) + ": ",end = "")

        for j in range(len(series)-1,0,-1):
            min = math.inf
            for k in range(len(series)):
                if k != j:
                    tmp = list(series)
                    tmp.pop(j)
                    tmp2 = (A[size-1][(tuple(tmp),series[k])] + G[(series[k],series[j])])
                    if  tmp2 < min:
                        min = tmp2
                        del tmp
            A[size][(series,series[j])] = min
        del series
    del S
    print("Shortest paths for all subproblems computed")

    # find optimal solution for full set of cities for all paths
    s = tuple([a+1 for a in range(n)])
    min = math.inf 
    for J in range(2,n+1):
        tmp2 = A[size][(s,J)] + G[(J,1)]
        if tmp2 < min:
            min = tmp2
    
    print("Solution found: ",min)




    
    