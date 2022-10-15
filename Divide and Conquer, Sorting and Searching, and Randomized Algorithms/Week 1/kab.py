def kMultiply(x,y):
    xN = numDigits(x)
    yN = numDigits(y)
    if xN==1 and yN: return x*y
    (a,b) = splitNum(x)
    (c,d) = splitNum(y)
    if even(xN) and even(yN):
        return ( ( 10**xN ) * kMultiply(a,c) ) + ( ( 10**( xN/2 ) ) * ( kMultiply(a,d) + kMultiply(b,c) ) )  + kMultiply(b,d)
    elif even(xN) and not even(yN):
        return (10**(((xN+yN)/2)-0.5) * kMultiply(a,c)) + ( ( 10**( xN/2 ) ) * kMultiply(a,d) ) + ( ( 10**( ( yN/2 ) - 0.5 ) ) * kMultiply(b,c) ) + kMultiply(b,d)
    elif not even(xN) and even(yN):
        return (10**(((xN+yN)/2)-0.5) * kMultiply(a,c)) + ( ( 10**( ( xN/2 ) - 0.5 ) ) * kMultiply(a,d) ) + ( ( 10**( yN/2 ) ) * kMultiply(b,c) ) + kMultiply(b,d)
    else:
        return ( (10**( xN-1 ) ) * kMultiply(a,c)) + ( ( 10**( ( xN/2 )-0.5 ) ) * ( kMultiply(a,d) + kMultiply(b,c) ) ) + kMultiply(b,d)

def numDigits(x):
    exp = 0
    n = 0
    while not x//10**exp == 0:
        x = x // 10**exp
        exp+=1
        n+=1
    return n

def splitNum(x):
    if numDigits(x)%2 == 0:
        tmp1 = x//(10**(numDigits(x)/2))
        tmp2 = x - tmp1*(10**(numDigits(x)/2))
    else:
        tmp1 = x//(10**((numDigits(x)/2)-0.5))
        tmp2 = x - tmp1*(10**((numDigits(x)/2)-0.5))
    return [tmp1,tmp2]

def even(x):
    if x%2 == 0: return True
    else: return False

