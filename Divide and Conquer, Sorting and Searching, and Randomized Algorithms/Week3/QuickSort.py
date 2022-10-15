import random as r

def quickSort(A,n):
    #print(n)
    if n < 2: return (A,n,0)
    (A,p) = choosePivot(A,n)
    A = partition(A,0,n-1)
    ind = A.index(p)
    (B,n1,c1) = quickSort(A[:ind],ind)
    (C,n2,c2) = quickSort(A[ind+1:],n-ind-1)
    return (B+[p]+C), (n1+n2+1), (c1+c2+n-1)

def partition(A,l,r):
    p = A[l]
    i = l+1
    for j in range(l+1,r+1):
        if A[j] < p: 
            A = swap(A,i,j)
            i+=1
    return swap(A,l,i-1)

def choosePivot(A,n):
    #x = r.randint(0,n-1)
    p=0
    if n >=3: 
        tmp = [A[0],A[(n-1)//2],A[n-1]]
        for a in range(3):
            c = 0
            for b in range(3):
                if tmp[a] > tmp[b] and a!=b: c+=1 
            if c == 1: 
                p = tmp[a]
                break
    else:
        x = r.randint(0,1)
        p = A[x]
        
    A = swap(A,0,A.index(p))
    return (A,p)

def swap(A,i,j):
    tmp = A[j]
    A[j] = A[i]
    A[i] = tmp
    return A

    
