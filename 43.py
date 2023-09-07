from usefulStuff import *
pList = [2,3,5,7,11,13,17]

def recurse(numList, depth):
	if depth == 0:
		if listToInt(numList[:3])%2 == 0:
			return [numList]
	if listToInt(numList[:3])%pList[depth] == 0:
		retL = []
		for i in xrange(10):
			if i not in numList:
				retL += recurse([i]+numList, depth-1)
		return retL
	return []

li = []
for i in xrange(10):
	for j in xrange(10):
		for k in xrange(10):
			if i != j and j!=k and k != i:
				li += recurse([i,j,k], 6)

su = 0
for l in li:
	for i in xrange(10):
		if i not in l:
			su += listToInt([i]+l)
print su
