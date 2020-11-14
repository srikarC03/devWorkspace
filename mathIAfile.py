import numpy as np
import random
import time

def initCentroid(k):
    x = []
    for iter in range(k):
        c = []
        for count in range(3):
            v = random.randrange(0,255)
            c.append(v)
        x.append(c)
    x = np.array(x)
    return x


def distFunc(Xval,centroid):
    x = 0
    x = np.sum((((Xval) + (centroid * -1))**2))
    return x

def costfunc(centroidVal,centroidData):
    x = 0
    c = centroidVal.shape[0]*centroidVal.shape[1]
    for n in range(centroidVal.shape[0]):
        for item in range(len(centroidData[n])):
            x = (distFunc(centroidData[n][item][1],centroidVal[n])/c) + x
    return x

def closeCentroid(centroidVal,imageData):
    lst1 = []
    row = 0
    x = centroidVal.shape[0]
    for n in range(x):
        lst1.append([])
    for item in imageData:
        col = 0
        for pixel in item:
            min = 1000000
            for c in range(x):
                k = distFunc(pixel,centroidVal[c])
                if k < min: 
                    min = k
                    pos = c
            lst1[pos].append( [[row,col],pixel.tolist()] )
            col+=1
        row+=1
    return lst1

def moveCentroid(centroidData,centroidVal):
    data = []
    iter = 0
    for c in centroidData:
        if len(c) == 0: continue
        elif len(c) == 1:
            data.append(centroidVal[iter])
        else:
            arr = [0,0,0]
            for pixel in c:
                for i in range(3):
                    arr[i] = arr[i] + pixel[1][i]
            for each in range(3):
                arr[each] = arr[each] / len(c)
            data.append(arr)
        iter+=1
    c = np.array(data)
    return c

