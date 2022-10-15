import math

# input graph in the form of all vertices as keys and  incoming edges and their respective costs as values

def bellmanFord(G,n,s):
    A = [[math.inf for m in range(n)],[]]
    A[0][s-1] = 0
    count = 0

    for i in range(n-1):
        for v in range(n):
            if len(G[v+1]) == 0: A[1].append(A[0][v])
            else:
                tmp = []
                for edge in G[v+1]:
                    tmp.append(A[0][edge[0]-1]+edge[1])
                tmp = min(tmp)
                A[1].append(min(tmp,A[0][v]))
            if A[0][v] == A[1][v]: count+=1
        if count == n: break
        A.pop(0)
        A.append([])
    
    count = 0
    for vrtx in range(n):
        if len(G[vrtx+1]) == 0: A[1].append(A[0][vrtx])
        else:
            tmp = []
            for edge in G[vrtx+1]:
                tmp.append(A[0][edge[0]-1]+edge[1])
            tmp = min(tmp)
            A[1].append(min(tmp,A[0][vrtx]))
        if A[0][vrtx] == A[1][vrtx]: count+=1
    if count != n: return "Negative Cycle"
    return A[0]
    


                    


    
