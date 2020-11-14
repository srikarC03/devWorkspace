numT = int(input())
for case in range(numT):
    count = 0 
    (n,b) = map(int,input().split())
    hList = list(map(int,input().split()))
    hList.sort()
    for house in hList:
        if house<=b:
            b-=house
            count+=1
            
    print("Case #"+str(case+1)+": "+str(count))
    