def secondGreatest(array,n):
    if n == 2:
        if array[0] > array[1]:
            return (array,[array[1]])
        else:
            return ([array[1],array[0]],[array[0]])
    
    mid = len(array) // 2

    (bestA,worstA) = secondGreatest(array[:mid],mid)
    (bestB,worstB) = secondGreatest(array[mid:],mid)

    while True:
        if bestA[0] > bestB[0]:
            worstA.append(bestB[0])
            return ([bestA[0],bestB[0]],worstA)
        else: 
            worstB.append(bestA[0])
            return ([bestB[0],bestA[0]],worstB)
    
def getSecondGreatest(array):
    max = 0
    (best,pos) = secondGreatest(array,len(array))
    for n in range(1,len(pos)):
        if pos[max] < pos[n]:
            max = n
    
    return pos[max]

        
            


