import unionFind as uf

def clustering(arr, n, k):  
    clusters = [m+1 for m in range(n)]
    clusters = uf.UnionFind(clusters)
    arr.sort()
    cluster_num = n
    prev = []
    for node in arr:
        if cluster_num == k:
            if clusters.find(node[1]) != clusters.find(node[2]):
                return [node[0],clusters]

        elif clusters.find(node[1]) != clusters.find(node[2]): 
            clusters.union(node[1],node[2])
            cluster_num-=1
        
        prev = node

file = open("clusteringData1.txt")
data = []
for line in file.readlines():
    if line == "500\n": t=5
    else:
        tmp = tuple(map(int,line.split()))
        data.append((tmp[2],tmp[0],tmp[1]))

[max,data] = clustering(data,500,4)

print(max)        
            

        


