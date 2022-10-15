import maxFind as mf
import random

def genUnimodal(lengthI,lengthD,upper):
    x = []
    tmp = 0
    for a in range(lengthI):
        tmp = random.randint(tmp,upper)
        x.append(tmp)
    for b in range(lengthD):
        tmp = random.randint(0,tmp)
        x.append(tmp)
    return x

i = genUnimodal(9,35,10000)
print(i)
print("Max: " + str(mf.findMax(i,len(i))))





