from usefulStuff import *

triN = lambda n:(n*(n+1))/2
sqN = lambda n: n**2
pentN = lambda n:(n*((3*n)-1))/2
hexN = lambda n: n*((2*n)-1)
heptN = lambda n: (n*((5*n)-3))/2
octN = lambda n: n*((3*n)-2)

polyFunctions = [triN, sqN, pentN, hexN, heptN, octN]

polyNumbers = []
for polyFunc in polyFunctions:
	i = 1
	while polyFunc(i) < 1000:
		i += 1
	polys = []
	while polyFunc(i) < 10000:
		polys.append(polyFunc(i))
		i += 1
	polyNumbers.append(polys)

def recurse(currentStart, currentPoly, polyFinished, currentList):
	if len(polyFinished) == 6:
		end = int(currentList[0]/100)
		currStart = currentStart*100
		currUBound = currStart + 100
		for pN in polyNumbers[currentPoly]:
			if pN < currStart:
				continue
			if pN >= currUBound:
				break
			if pN%100 == end:
				currentList += [pN]
				print "List of cycle: {}, sum of cycle: {}".format(currentList, sum(currentList))
	else:
		currStart = currentStart*100
		currUBound = currStart + 100
		for pN in polyNumbers[currentPoly]:
			if pN < currStart:
				continue
			if pN >= currUBound:
				break
			for polyType in xrange(5):
				if polyType not in polyFinished:
					recurse(pN%100, polyType, polyFinished + [polyType], currentList + [pN])

for pN in polyNumbers[5]:
	for i in xrange(5):
		recurse(pN%100, i, [5,i], [pN])
