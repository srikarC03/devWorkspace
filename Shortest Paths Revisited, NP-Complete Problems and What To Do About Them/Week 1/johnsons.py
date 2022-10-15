import bellmanFord as bf
import dijkstras as ds

def johnson(G,n):
    for node in G:
        G[node].append((n+1,0))
    G[n+1] = []
    newG = {}
    print("done")

    weights = bf.bellmanFord(G,n+1,n+1)
    print("done")

    if weights == "Negative Cycle": return weights

    for v in G:
        for edge in G[v]:
            if edge[0] == n+1: continue
            else:
                w = weights[edge[0]-1]-weights[v-1]
                if newG.get(edge[0]) is None:
                    newG[edge[0]] = [(edge[1]+w,v)]
                else:
                    newG[edge[0]].append((edge[1]+w,v))

    print("done")
    
    A = [[] for i in range(n)]

    for s in range(n):
        print(s)
        A[s] = ds.dijkstra(newG,n,s+1)
    
    print("done")
    
    for a in range(n):
        for b in range(n):
            A[a][b] = A[a][b] - weights[a] + weights[b]
    
    print("done")
    
    return A




    

