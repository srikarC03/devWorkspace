import solvedPuzzleGen as base,random
import sys
sys.setrecursionlimit(10**6)

def reSolve(goBack,cList,pList,puzzle):
	t = len(cList)-goBack-1
	tmpList = pList[t]
	tmpList.remove(puzzle[cList[t]])
	if len(tmpList) == 0: return reSolve(goBack+1,cList,pList,puzzle)
	puzzle[cList[t]] = random.choice(tmpList)
	pList[t] = tmpList
	goBack -=1
	while not goBack<0:
		t = len(pList)-goBack-1
		puzzle[cList[t]] = None
		pList.pop(t)
		cList.pop(t)
		goBack-=1
	return [cList,pList,puzzle]

def reConv(l,ind):
	count = 0
	b = base.tripletGen()
	for n in range(1,10):
		for n2 in range(1,10):
			for each in b:
				if n == each[0] and n2 == each[1]: 
					if count == ind: c = each
					b[each] = l[count]
			count+=1
	return [c,b]




def solvePuzzle(puzzle,countL=[],posL=[]):
	
	for each in puzzle:
		if each is None:
			c1 = puzzle.index(each)
			t1 = reConv(puzzle,c1)
			tmp = base.possibleGen(t1[0],t1[1])
			countL.append(c1)
			posL.append(tmp)
			if len(tmp) == 0:
				k = reSolve(1,countL,posL,puzzle)
				[countL,posL,puzzle] = [k[0],k[1],k[2]]
				return solvePuzzle(puzzle,countL,posL)
			puzzle[c1] = random.choice(tmp)
	return puzzle
#Expert puzzle, not working:
#puz1 = [None,9,None,5,None,None,None,None,None,None,None,5,4,None,7,None,None,None,7,None,None,9,8,None,None,None,None,None,6,None,None,None,None,5,None,2,3,None,None,None,None,None,8,None,4,None,None,None,8,None,4,None,None,None,6,2,None,None,None,8,None,9,None,8,None,None,None,None,None,None,None,None,None,None,7,6,3,None,2,None,None]
#Medium puzzle, working:
puz1 = [5,3,None,None,8,None,None,None,7,4,None,None,None,3,5,1,6,None,None,1,9,7,None,None,None,None,2,2,None,5,None,None,None,9,None,None,None,7,None,None,None,6,2,5,None,None,None,None,None,None,None,None,8,6,None,4,1,None,None,None,None,None,None,7,None,None,None,None,2,None,1,None,None,None,None,None,None,3,6,4,None]
#hard puzzle, working:
#puz1 = [None,None,None,None,None,9,None,None,4,9,None,None,2,None,6,None,None,None,6,None,None,1,5,None,None,None,3,None,5,None,None,None,1,None,8,6,None,None,None,9,3,None,7,None,2,None,None,None,None,None,None,None,None,None,None,None,None,None,None,5,None,None,None,2,7,None,6,None,None,None,None,5,None,1,6,None,4,None,None,3,9]

solve = solvePuzzle(puz1)
base.display(solve)



