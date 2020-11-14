import mathIAfile as ia
from PIL import Image
import numpy as np
import matplotlib.pyplot as py

imgData =  np.array(Image.open("iaImg3.jpg"))
pngConvert = Image.fromarray(imgData)
pngConvert.save("testImg.png")
k = int(input("Enter number of Clusters: "))
iteration = int(input("Enter number of iterations: "))


costList = []
min = 1000000000
for n in range(2):
    cL = []
    cVal = ia.initCentroid(k)
    for a in range(iteration):
        cData = ia.closeCentroid(cVal,imgData)
        cL.append(ia.costfunc(cVal,cData))
        cVal = ia.moveCentroid(cData,cVal)
    costList.append(cL)
    if ia.costfunc(cVal,cData)<min: 
        min = ia.costfunc(cVal,cData)
        track = n
costList = costList[n]


for b in range(len(algList[n][2])):
   for iter in algList[n][2][b]:
        imgData[iter[0][0]][iter[0][1]] = algList[n][1][b]

imgNew = Image.fromarray(imgData)
imgNew.save("iaImgNew.png")
imgNew.show()

X = [n*(3.472 * (10**-6)) for n in range(iteration)]
Y = costList
py.plot(X,costList,marker = "o", ms = 1)
min2 = 10000000000

for i in range(iteration):
    d = (ia.distFunc(np.array([0,0]), np.array([X[i], Y[i]])))**0.5
    if d<min2: 
        min2 = d
        stor = i
py.plot([0, X[stor]],[0, Y[stor]], marker = "+")
py.show()




