import tsp
import itertools as it
import time

file = open("tsp.txt")
data = file.readlines()
n = int(data[0])

def dist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

cities = []
for line in data[1:]:
    cities.append(tuple(map(float,line.split(" "))))

cityEdges = {}

for i in range(len(cities)):
    for j in range(len(cities)):
        cityEdges[(i+1,j+1)] = dist(cities[i][0],cities[i][1],cities[j][0],cities[j][1])

del cities
del data

print("Input Data Processed")

start = time.time()
tsp.TSP(cityEdges,n)
end = time.time()
print(start-end)
