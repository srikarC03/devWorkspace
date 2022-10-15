#input path graph data into array and initialize store for subproblems
file = open("mwis.txt")

count = False
weights = []

for line in file.readlines():
    if count is False: 
        numberOfNodes = int(line)
        count = True
    else:
        weights.append(int(line))

A = {0:0,1:weights[0]}

#loop through nodes and find the max weights of independent sets of G

for i in range(2,numberOfNodes+1):
    A[i] = max(A[i-1],A[i-2]+ weights[i-1])

#loop through graph backwards to reconstruct max-weight independent set of G

S = []
i = numberOfNodes
while i >= 1:
    if i == 1: 
        S.append(i)
        break
    if A[i-1] >= A[i-2] + weights[i-1]: i-=1
    else:
        S.append(i)
        i-=2
print("done")
#search algorithm

def binSearch(arr,x):
    start = 0
    end = len(arr)-1
    mid = (start + end) // 2
    found = False
    while not found:
        if x == arr[mid]: 
            found = True
        elif x > arr[mid]:
            start = mid+1
            mid = (start + end) // 2
        elif x < arr[mid]:
            end = mid-1
            mid = (start + end) // 2
        elif start == end:
            break
    return found 

# search max weight independent set for the desired nodes

find = [1,2,3,4,17,117,517,997]
S = S[::-1]

print(S)
    

