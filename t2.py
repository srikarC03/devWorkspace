def dp(n,k,numStack,platNeed,caseStore = {}):
	if platNeed == 0 or numStack == n: return 0
	if (numStack,platNeed) in caseStore: return caseStore[numStack,platNeed]
	maxStack = 0
	for choice in range(k+1):
		pLeft = platNeed - choice
		if pLeft < 0: break
		temp = dp(n,k,numStack+1,pLeft,caseStore) + compArray[numStack][choice]
		if temp > maxStack: maxStack = temp
	caseStore[numStack,platNeed] = maxStack
	return maxStack

nt = int(input())
for iter1 in range(1,nt+1):
	compArray = []
	(n,k,p) = map(int,input().split())
	for iter2 in range(n):
		tList = [0]
		for iter3 in list(map(int,input().split())):
			tList.append(tList[-1]+iter3)
		compArray.append(tList)
	print(compArray)
	print(f"Case #{iter1}: {dp(n,k,0,p,{})}")



