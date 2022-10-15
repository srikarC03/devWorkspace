import unionFind

# Create maps for bits.
x = [1<<n for n in range(24)]

y = []
for i in range(23):
    tmp = 3<<i
    prev = 3<<i
    y.append(prev)
    for j in range(22-i):
        prev = prev ^ tmp<<j+1
        y.append(prev)

maps = [0]+x+y

# Read data and create the UnionFind Data Structure
file = open("clusteringData2.txt")
data = dict()
counter = 1

for bit in file.readlines()[1:]:

    tmp = int(int("".join(bit.split(" ")),base=2))
    if data.get(tmp) == None:
        data[tmp] = [counter]
    else: data[tmp].append(counter)
    counter+=1

clusters = unionFind.UnionFind([n+1 for n in range(200000)])

# Cluster the data
num_clusters = 200000
for mask in maps:
    for code in data:
        findBit = code^mask
        if data.get(findBit) is not None:
            if mask == 0:
                if len(data[findBit])>1: 
                    for bit in data[findBit][1:]:
                        clusters.union(data[findBit][0],bit)
                        num_clusters-=1
            
            else: 
                if clusters.find(data[code][0]) != clusters.find(data[findBit][0]):
                    clusters.union(data[code][0],data[findBit][0])
                    num_clusters-=1
                
print(num_clusters)

            




