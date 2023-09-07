from usefulStuff import *

notFound = True
i = 1
upperBound = 10
while(notFound):
	if i * 6 >= upperBound:
		i = upperBound
		upperBound *= 10
		print "new upperbound {}".format(upperBound)
		continue
	else:
		iList = intToList(i)
		iList.sort()
		for j in xrange(1,7):
			iMultList = intToList(i*j)
			iMultList.sort()
			notFound = False
			if iMultList != iList:
				i += 1
				notFound = True
				break
print i
