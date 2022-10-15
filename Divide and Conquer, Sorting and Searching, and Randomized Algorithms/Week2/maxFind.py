def findMax(array,n):
    mid = n//2
    if n == 1: return array[0]
    elif array[mid] > array[mid-1]: return findMax(array[mid:],n-mid)
    else: return findMax(array[:mid],mid)

 
