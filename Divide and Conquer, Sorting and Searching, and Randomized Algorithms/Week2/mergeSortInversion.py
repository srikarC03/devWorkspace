def countInversions(array,n):
    # initialize sum and sorted array
    arrD = []
    z = 0

    # base case of recursive call if the size of the array is 1
    if n == 1: 
        return [array,0]

    # recursive calls to split up array for sorting and counting left and right inversions
    (arrB,x) = countInversions(array[:(n//2)],n//2) 
    (arrC,y) = countInversions(array[(n//2):],n-(n//2))
    
    # initialize pointers
    i = 0
    j = 0

    # loop through the two sorted arrays and merge back into a bigger array
    for a in range(n):
        if i > len(arrB)-1:
            arrD.append(arrC[j])
            j+=1
        elif j > len(arrC)-1:
            arrD.append(arrB[i])
            i+=1
        elif abs(arrB[i]) <= abs(arrC[j]):
            arrD.append(arrB[i])
            i+=1
        else:
            # if item from left array added then count inversions
            arrD.append(arrC[j])
            j+=1
            z+=(len(arrB)-i)
    
    return [arrD,(x+y+z)]

