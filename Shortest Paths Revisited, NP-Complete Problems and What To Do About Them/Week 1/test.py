import floydWarshall as fW

file = open("g3.txt")

data = file.readlines()

n = int(data[0].split(" ")[0])

G = {}

for line in data[1:]:
    edge = list(map(int,line.split(" ")))
    G[tuple(edge[:2])] = edge[2]

path = fW.floydWarshall(G,n)

superPath = []
for i in path:
    for j in i:
        superPath.append(j)

superPath.sort()

print(superPath[0])



