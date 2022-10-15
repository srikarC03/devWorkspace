
d = {}

def ackermann(k,r):
    if k == 0: 
        d[(k,r)] = r+1
        return r+1

    if d.get((k,r)) is not None:
        return d[(k,r)]

    tmp = ackermann(k-1,r)
    for n in range(r-1):
        tmp = ackermann(k-1,tmp)
    
    d[k,r] = tmp
    return tmp


