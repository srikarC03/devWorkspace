def kMultiply(x,y):
    
    xN = numDigits(x)
    yN = numDigits(y)

    if xN==1 and yN==1: return int(x) * int(y)
    
    (a,b) = splitNum(x)
    (c,d) = splitNum(y)

    return ( ( 10**xN ) * kMultiply(a,c) ) + ( ( 10**( int(xN/2) ) ) * ( kMultiply(a,d) + kMultiply(b,c) ) )  + kMultiply(b,d)

def numDigits(x):
    return len(x)

def splitNum(x):
    n = int(len(x)/2)
    tmp1 = x[0:n]
    tmp2 = x[n:]
    return [tmp1,tmp2]


def even(x):
    if x%2 == 0: return True
    else: return False

def test(x,y):
    tmp = kMultiply(x,y)
    if tmp == int(x)*int(y):
        return [True,int(x)*int(y)]