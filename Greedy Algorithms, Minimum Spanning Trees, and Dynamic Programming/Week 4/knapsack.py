file = open("knapsack1.txt")
data = file.readlines()
(capacity,n) = tuple(map(int,data[0].split(" ")))
items = {m+1:[] for m in range(n)}
c = 1
for item in data[1:]:
    items[c] = list(map(int,item.split(" ")))
    c+=1

A = [[] for j in range(n+1)]
A[0] = [0 for k in range(capacity+1)]

 
for i in range(n):
    for x in range(capacity+1):
        if items[i+1][1] > x: subSolution = A[i][x]
        else: subSolution = max(A[i][x],A[i][x-items[i+1][1]]+items[i+1][0])
        A[i+1].append(subSolution)

print(A[n][capacity])




