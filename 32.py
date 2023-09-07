from usefulStuff import intToList

pdProducts = [0]*10000
i = 2
j = 5000
iList = intToList(i)
jList = intToList(j)

while i<j:
	prod = i*j
	prodList = intToList(prod)
	digCount = len(iList)+len(jList)+len(prodList)
	if digCount > 9:
		jNotFound = True
		while(jNotFound):
			j -= 1
			jList = intToList(j)
			if 0 in jList:
				continue
			jNotFound = False
			for jD in jList:
				if jList.count(jD)>1:
					jNotFound = True
					continue		
		i = 2
		iList = [2]
		iNotFound = True
		if 2 not in jList:
			iNotFound = False
		while(iNotFound):
			i += 1	
			if i not in jList:
				iList = [i]
				iNotFound = False
	else:
		if digCount == 9 and (0 not in prodList):
			combList = iList+jList
			isPalProd = True
			for pD in prodList:
				if pD in combList or prodList.count(pD)>1:
					isPalProd = False
			if isPalProd:
				print "i={}, j={}, prod={}".format(i,j,prod)
				pdProducts[prod] = 1

		iNotFound = True
		while(iNotFound):
			i += 1
			iList = intToList(i)
			if 0 in iList:
				continue
			goodI = True
			for iD in iList:
				if iList.count(iD) > 1:
					goodI = False
					break
			if goodI:
				iNotFound = False
				for iD in iList:
					if iD in jList:
						iNotFound = True
						break

pdPro = []

for i in xrange(len(pdProducts)):
	if pdProducts[i] == 1:
		pdPro.append(i)

print sum(pdPro)
