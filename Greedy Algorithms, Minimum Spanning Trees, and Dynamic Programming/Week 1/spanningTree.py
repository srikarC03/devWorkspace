import heapq as hq


def heapify(graph):
    heap = list(tuple(graph.items()))
    hq.heapify(heap)
    heap = dict(heap)
    return heap

def pop(graph):
    heap = list(tuple(graph.items()))
    tmp = hq.heappop(heap)
    if len(tmp[1]) > 1: 
        heap.append((tmp[0],tmp[1][1:]))
        tmp = (tmp[0],tmp[1][0])
        heap = dict(heap)
        return [tmp,heap]
    else:
        heap = dict(heap)
        tmp = (tmp[0],tmp[1][0])
        return [tmp,heap]


def minSpanningTree(graph):
    n = len(graph)
    X = {x+1:False for x in range(n)}
    current = 1
    notX = {}
    cost = 0
    count = 1

    while count < n:
        X[current] = True

        for edge in graph[current-1]:
            if not X[edge[0]]:
                if notX.get(edge[1]) is None:
                    notX[edge[1]] = [edge[0]]
                else:
                    notX[edge[1]].append(edge[0])
        while True:
            #print(notX)
            notX = heapify(notX)
            (minCross,notX) = pop(notX)
            #print(notX)
            if X[minCross[1]] == False:
                break
        cost+=minCross[0]
        current = minCross[1]
        count+=1

    return cost



                


        

