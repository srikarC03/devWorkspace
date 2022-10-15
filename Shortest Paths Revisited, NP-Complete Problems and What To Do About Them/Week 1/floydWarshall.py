import math

# input graph in the form of each pair of vertices being a key and the cost being the value

def floydWarshall(G,n):
    negCycle = False
    A = [[[] for i in range(n)] for j in range(2)]
    for i in range(n):
        for j in range(n):
            if G.get((i+1,j+1)) is None and i!=j: A[0][i].append(math.inf)
            elif i == j: A[0][i].append(0)
            else: A[0][i].append(G[(i+1,j+1)])
    for k in range(n):
        print(k)
        for i in range(n):
            for j in range(n):
                A[1][i].append(min(A[0][i][j],A[0][i][k]+A[0][k][j]))
                if k == n-1 and i == j: 
                    if A[1][i][j] < 0: negCycle = True

        A.pop(0)
        A.append([[] for a in range(n)])
    
    if negCycle: return "Negative Cycle"

    return A[0]

