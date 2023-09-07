
ab = [1]*28111

for i in xrange(2,20000):
	mult = 2
	imult = 2*i
	while imult<28111:
		ab[imult] += i
		mult += 1
		imult = i*mult

abundant = []
for i in xrange(2,len(ab)):
	if i < ab[i]:
		abundant.append(i)

isAbunSum = [0]*29000
maxNum = len(isAbunSum)
maxJ = len(abundant)

for i in xrange(len(abundant)):
	for j in xrange(i,maxJ):
		s = abundant[i]+abundant[j]
		if s < maxNum:
			isAbunSum[s] = 1
		else:
			maxJ = j+1
			print "At i={} max j became: {}".format(i, maxJ)
			break

#print isAbunSum
#for i in xrange(1,len(isAbunSum)):
#	if isAbunSum[i] == 0:
#		su += i
#print su

print reduce(lambda x,y: x+y if isAbunSum[y] == 0 else x, range(len(isAbunSum)))

