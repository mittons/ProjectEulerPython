import copy
#All the different combos of digits in squares under 100, counting 6 and 9 as the same
sqc = [(0,1),(0,4),(0,6),(1,6),(2,5),(3,6),(6,4),(8,1)]

D = {i:i for i in xrange(10)}
D[9] = 6
print D

def isInV2(n,lis):
	for l in lis:
		if n == D[l]:
			return True
	return False

def recurse(cubeA):
	count = 0
#	if len(cubeA) == 5:
#		if 6 in cubeA:
#			c = copy.copy(cubeA)
#			c.append(9)
#			count += recurse(c)

	if len(cubeA) < 6:
		for i in xrange(cubeA[-1]+1,10):
			if i not in cubeA:
				c = copy.copy(cubeA)
				c.append(i)
				count += recurse(c)
	else:
		sqcCover = [[],[]]
		for i in xrange(len(sqc)):	
			if isInV2(sqc[i][0],cubeA):
				if isInV2(sqc[i][1],cubeA):
					sqcCover[1].append(sqc[i])
				elif sqc[i][1] not in sqcCover[0]:
					sqcCover[0].append(sqc[i][1])
			elif isInV2(sqc[i][1],cubeA):
				if sqc[i][0] not in sqcCover[0]:
					sqcCover[0].append(sqc[i][0])
			else:
				return 0
		print cubeA,sqcCover
		return createCubeBFromA(cubeA,[],sqcCover)
	return count
		
def createCubeBFromA(cubeA,cubeB,sqcCover):
	count = 0
	print cubeA, cubeB, sqcCover
	if len(cubeB) < 5:
		sqcco = copy.deepcopy(sqcCover)
		toRemove = []
		if D[cubeA[0]] in sqcco[0]:
			toRemove.append(D[cubeA[0]])
		for tr in toRemove:
			sqcco[0].remove(tr)
		toRemove = []
		for sqcc in sqcco[1]:
			if D[cubeA[0]] in sqcc:
				toRemove.append(sqcc)
		for tr in toRemove:
			sqcco[1].remove(tr)
		c = copy.copy(cubeB)
		count += createCubeBFromA(cubeA[1:],c+[cubeA[0]],sqcco)
		for i in xrange(cubeA[0]+1,10):
			print i
			sqcco = copy.deepcopy(sqcCover)	
			toRemove = []
			if D[i] in sqcco[0]:
				toRemove.append(D[i])

			for tr in toRemove:
				sqcco[0].remove(tr)

			toRemove = []
			for sqcc in sqcco[1]:
				if D[i] in sqcc:
					toRemove.append(sqcc)

			for tr in toRemove:
				sqcco[1].remove(tr)
			c = copy.copy(cubeB)
			count += createRestOfCubeB(c+[i],sqcco,cubeA)
	elif len(cubeB) == 5:
		for i in xrange(cubeA[0],10):
			sqcco = copy.deepcopy(sqcCover)	
			toRemove = []
			if D[i] in sqcco[0]:
				toRemove.append(D[i])
			for tr in toRemove:
				sqcco[0].remove(tr)
			
			toRemove = []
			for sqcc in sqcco[1]:
				if D[i] in sqcc:
					toRemove.append(sqcc)
			for tr in toRemove:
				sqcco[1].remove(tr)
	
			if len(sqcco[0]) == 0 and len(sqcco[1]) == 0:
				count += 1
				print cubeA
				print cubeB
				print sqcco
#				if i == 6:
#					count += 1
#				if 6 in cubeB:
#					count += 1

#		if len(cubeB) == 5:
#			if 6 in cubeB:
#				if sqcCover[0] == 0 and sqcCover[1] == 0:
#					count += 1
	return count

def createRestOfCubeB(cubeB,sqcCover,cubeA):
	count = 0
	for i in xrange(cubeB[-1]+1,10):
		sqcco = copy.deepcopy(sqcCover)	
		toRemove = []
		if D[i] in sqcco[0]:
			toRemove.append(D[i])
		for tr in toRemove:
			sqcco[0].remove(tr)
		
		toRemove = []
		for sqcc in sqcco[1]:
			if D[i] in sqcc:
				toRemove.append(sqcc)
		for tr in toRemove:
			sqcco[1].remove(tr)
		if len(cubeB) < 5:
			c = copy.copy(cubeB)
			count += createRestOfCubeB(c+[i],sqcco,cubeA)
		elif len(sqcco[0]) == 0 and len(sqcco[1]) == 0:
			count += 1
			print cubeA, cubeB, i, sqcco
#			if i == 6:
#				count += 1
#			if 6 in cubeB:
#				count += 1
#	if len(cubeB) == 5:
#		if 6 in cubeB:
#			if sqcCover[0] == 0 and sqcCover[1] == 0:
#				count += 1
	return count

print recurse([0])
