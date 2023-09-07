from usefulStuff import *
baseFractions = [(i,j) for i in xrange(1,10) for j in xrange(i+1,10)]


rm = []
for i in xrange(len(baseFractions)):
	b = baseFractions[i]
	for j in xrange(2,5):
		if b[1]*j > 9:
			continue
		t = (b[0]*j,b[1]*j)
		if t in baseFractions and t not in rm:
			rm.append((b[0]*j,b[1]*j))
for r in rm:
	baseFractions.remove(r)

for i in xrange(len(baseFractions)):
	b = baseFractions[i]
	baseFractions[i] = []
	for j in xrange(1,5):
		if b[1]*j > 9:
			continue
		baseFractions[i].append((b[0]*j,b[1]*j))

	for j in xrange(10/b[0], (99/b[1])+1):
		if b[0]*j < 10:
			continue
		num = j*b[0]
		den = j*b[1]
		if num%11==0 and den%11==0:
			continue
		numD = intToList(num)
		denD = intToList(den)
		if (numD[0],denD[1]) in baseFractions[i]:
			if numD[1] == denD[0]:
				print "  ",num, den, numD[0], denD[1]
#		elif (numD[1],denD[0]) in baseFractions[i]:
#			print "   ", num, den, numD[1], denD[0]
#		if (numD[0],denD[0]) in baseFractions[i]:
#				print num, den, numD[0], denD[0]
