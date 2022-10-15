from collections import deque

# Initializing the test cases from the file
file = open("SCC.txt","r")
#file = open("testCases.txt","r")

data = list(file.readlines())

# initialize graphs, revG will become the list of finishing times
stack = deque()
gRev = []
revG = []
G = []
num = 875714

# create a list for each node for the edges
for n in range(num):
    G+=[[]]
    revG+=[[]]

# take each line and input it into the graph accordingly 
for line in data:
    if line == "\n": break
    edge = list(map(int,line.split(" ")[0:2]))
    if edge[0] == edge[1]: continue
    G[edge[0]-1].append(edge[1])
    revG[edge[1]-1].append(edge[0])

# This is the first pass of the algorithm on the reverse graph to compute finishing times
t = 1
for item in range(num-1,-1,-1):
    empty = False
    if isinstance(revG[item],list) and len(revG[item])>=0: 
        stack.append(item+1)
        for node in G[item]:
            revG[node-1].remove(item+1)
        currentNode = item+1
        while not empty:
            if len(revG[currentNode-1]) == 0: 
                revG[currentNode-1] = t
                t+=1
                stack.pop()
                if len(stack) == 0: 
                    empty = True
                else:
                    currentNode = stack[len(stack)-1]
            else:
                currentNode = revG[currentNode-1][0]
                stack.append(currentNode)
                for head in G[currentNode-1]:
                    revG[head-1].remove(currentNode)

    else: continue

G = []

# create a list for each node for the edges for the new graph 
for n in range(num):
    G+=[[]]
    gRev+=[[]]

# take each line and input it into the graph
for line in data:
    if line == "\n": break
    edge = list(map(int,line.split(" ")[0:2]))
    if edge[0] == edge[1]: continue
    tail = revG[edge[0]-1]
    head = revG[edge[1]-1]
    G[tail-1].append(head)
    gRev[head-1].append(tail)
del revG 

# any isolated nodes will automatically be given an scc size of 0
for arr in range(num):
    if len(G[arr]) == 0 and len(gRev[arr]) == 0: G[arr] = 0

# This is the second pass of the algorithm that will compute the leaders of the new graph
for dot in range(num-1,-1,-1):
    done = False
    if isinstance(G[dot],list) and len(G[dot])>=0: 
        leader = dot+1
        stack.append(dot+1)
        for head in gRev[dot]:
            G[head-1].remove(dot+1)
        currentNode = dot+1
        while not done:
            if len(G[currentNode-1]) == 0: 
                G[currentNode-1] = leader
                stack.pop()
                if len(stack) == 0: 
                    done = True
                else:
                    currentNode = stack[len(stack)-1]
            else:
                currentNode = G[currentNode-1][0]
                stack.append(currentNode)
                for end in gRev[currentNode-1]:
                    G[end-1].remove(currentNode)

    else: continue

del gRev
del stack
file.close()
del data

# Create a dictionary to keep track of the size of each scc
scc = {}
for lead in G:
    if lead == 0: continue
    if lead in scc: scc[lead] +=1
    else: scc[lead] = 1
del G

# Compute the 5 largest scc and add them to their corresponding index
topFive = [0,0,0,0,0]

for rank in range(5):
    if len(scc) == 0: break
    topFive[rank] = max(scc.values())
    ind = list(scc.values()).index(topFive[rank])
    key = list(scc.keys())[ind]
    scc.pop(key)

del scc

# display results
print(topFive)