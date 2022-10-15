
file = open("knapsack_big.txt")
data = file.readlines()
(capacity,n) = tuple(map(int,data[0].split(" ")))
items = []
for item in data[1:]:
    tmp = list(map(int,item.split(" ")))
    items.append(tmp[::-1])
    
items.sort()

cache = {}

def knapsack(A,n,capacity):
    if capacity - A[len(A)-1][0] < 0: 
        if n == 1:
            return 0
        return cacheFunc(A[:len(A)-1],n-1,capacity)
    elif n == 1:
        return A[0][1]
    else:
        option1 = cacheFunc(A[:len(A)-1],n-1,capacity)
        cache[(n-1,capacity)] = option1
        option2 = cacheFunc(A[:len(A)-1],n-1,capacity-A[len(A)-1][0])
        cache[(n-1,capacity-A[len(A)-1][0])] = option2
        solution = max(option1, option2 + A[len(A)-1][1])
        cache[n,capacity] = solution
        return solution


def cacheFunc(A,n,capacity):
    if cache.get((n,capacity)) is None: return knapsack(A,n,capacity)
    else: return cache[(n,capacity)]


print(knapsack(items,n,capacity))