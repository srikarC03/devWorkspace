import nnh

file = open("nn.txt")
data = file.readlines()
n = int(data[0])
G = [[] for m in range(n)]


cities = []


for line in data[1:]:
    cities.append(tuple(map(float,line.split(" ")[1:])))
    
print("Graph initialized, running heuristic...")
del data

nnh.nnHueristic(cities,n)
#print(nnh.dist(cities[1][0],cities))




