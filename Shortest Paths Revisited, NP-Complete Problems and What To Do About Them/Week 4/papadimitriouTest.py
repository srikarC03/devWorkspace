import papadimitriou as ppd

file = open("2sat6.txt")
data = file.readlines()
n = int(data[0])
data = data[1:]

clauses = []

for line in data:
    tmp = tuple(map(int,line.split(" ")))
    clauses.append(tmp)


print(ppd.papadimitriou(clauses))