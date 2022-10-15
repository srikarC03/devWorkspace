import QuickSort as qs
import random as r


def genSeq(l):
    x = []
    for n in range(l):
        x.append(r.randint(0,1000))
    return set(x)

f = open("IntegerArray.txt","r")
x = []
for n in f:
    x.append(int(n))

(A,n,c) = qs.quickSort(list(x),len(x))

print(c)


