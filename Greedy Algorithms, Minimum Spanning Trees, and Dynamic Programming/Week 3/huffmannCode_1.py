from collections import deque
# initialize all data strucutures and write data into dictionary.
file = open("huffman.txt")
weightFreq = {}
nodes = []
jointNodes = deque()
codeLen = deque()
for each in file.readlines()[1:]:
    tmp = int(each)
    nodes.append(tmp)
    if weightFreq.get(tmp) is None:
        weightFreq[tmp] = deque([0])
    else:
        weightFreq[tmp].append(0)
nodes.sort()
nodes = deque(nodes)


while len(nodes) != 0 or len(jointNodes) != 1:
    i=0
    j=0
    join = []

    #use pointers and go through both queues and find the two smallest weights
    while len(join) < 2:
        if i > len(nodes) - 1:
            join.append(jointNodes[j])
            jointNodes.popleft()
            
        elif j > len(jointNodes)-1:
            join.append(nodes[i])
            nodes.popleft()
            
        elif nodes[i] <= jointNodes[j]:
            join.append(nodes[i])
            nodes.popleft()
        else:
            join.append(jointNodes[j])
            jointNodes.popleft()
    
    #find the max code length for each weight
    tmp = sum(join)
    jointNodes.append(tmp)
    for n in range(2):
        join[n] = weightFreq[join[n]].popleft()
    
    #merge the two weighs and calculate the new max code length
    maximum = min(join)+1
    codeLen.append(maximum)
    if weightFreq.get(tmp) is None:
        weightFreq[tmp] = deque([maximum])
    else:
        weightFreq[tmp].append(maximum)


print(codeLen.pop())


 
