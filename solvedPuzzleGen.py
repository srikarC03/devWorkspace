import random
def tripletGen(count = 0):
	a = [(1,2,3),(4,5,6),(7,8,9)]
	triplet = {}
	for r1 in a:
		for c1 in a:
			count+=1
			for r2 in r1:
				for c2 in c1:
					triplet[(r2,c2,count)] = None
	return triplet

def possibleGen(box,valDict):
	s = []
	g = [1,2,3,4,5,6,7,8,9]
	f = []
	count = 0
	for each in box:
		for coord in valDict:
			if box == coord:
				continue
			elif each == coord[count]:
				s.append(coord)
		count+=1
	for item in set(s):
		if valDict.get(item,0) != None:
			f.append(valDict.get(item,0))
	if len(set(f)) == 0:
		return g
	for item1 in set(f):
		g.remove(item1)
	return g 

def reEvaluate(goBack,valDict,currentVal,allPos,allPrev):
	tmpList = allPos[allPrev.index(currentVal)-goBack]
	tmpList.remove(valDict[allPrev[allPrev.index(currentVal)-goBack]])
	if len(tmpList) == 0: return reEvaluate(goBack+1,valDict,currentVal,allPos,allPrev)
	valDict[allPrev[allPrev.index(currentVal)-goBack]] = random.choice(tmpList)
	allPos[allPrev.index(currentVal)-goBack] = tmpList
	goBack-=1
	while not goBack < 0:
		valDict[allPrev[allPrev.index(currentVal)-goBack]] = None
		allPos.pop(allPrev.index(currentVal)-goBack)
		allPrev.pop(allPrev.index(currentVal)-goBack)
		goBack-=1
	currentVal = allPrev[len(allPrev)-1]
	return [valDict,allPos,allPrev,currentVal]


def sudokuGen(valDict,panList = [],eachList = []):
	for each in valDict:
		if valDict[each] is None:
			posList = possibleGen(each,valDict)
			panList.append(posList)
			eachList.append(each)
			if len(panList) > 2:
				if len(posList) == 0:
					s = reEvaluate(1,valDict,each,panList,eachList)
					(valDict,panList,eachList) = (s[0],s[1],s[2])
					return sudokuGen(valDict,panList,eachList)
			valDict[each] = random.choice(posList)
	return valDict

def peerP(valDict):
	check = 0
	valid =False
	for box in valDict:
		s = []
		count = 0
		for each in box:
			for coord in valDict:
				if box == coord:
					continue
				elif each == coord[count]:
					s.append(valDict[coord])
			count+=1
		if valDict[box] not in s: check+=1
	if check == 81: valid = True
	return print(f"\nValid Puzzle: {valid}")

def conv(a):
	anon = []
	for g in range(1,10):
		for h in range(1,10):
			for each in a:
				if g == each[0] and h == each[1]:
					anon.append(a[each])
	return anon

def display(list):
	for n in range(0,73,9):
		for b in range(n,n+9):
			print(list[b],end = "  ")
		print("\n")