import spanningTree as st


file = open("edges.txt")
data = list(file.readlines())[1:]
graph = [[] for n in range(500)]
for edge in data:
    tmp = list(map(int,edge.split(" ")))
    graph[tmp[0]-1].append((tmp[1],tmp[2]))
    graph[tmp[1]-1].append((tmp[0],tmp[2]))

(cost) = st.minSpanningTree(graph)
print(cost)

