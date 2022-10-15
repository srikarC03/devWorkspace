import heapq


# input graph in the form of nodes as keys and costs and outgoing edges as values
def dijkstra(G,n,s):
    notX = [(0,s)]
    X = []
    pathLen = [None for i in range(n)]

    while len(X) < n: 
        heapq.heapify(notX)
        minNode = heapq.heappop(notX)
        X.append(minNode[1])
        pathLen[minNode[1]-1] = minNode[0]

        for edge in G[minNode[1]]:
            if pathLen[edge[1]-1] is None:
                dist = pathLen[minNode[1]-1] + edge[0]
                notX.append((dist,edge[1]))
    
    return pathLen 



    