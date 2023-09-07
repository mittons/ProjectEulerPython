from usefulStuff import *

def getReverse(i):
	r = intToList(i)
	r.reverse()
	return listToInt(r)


isLychrel = [-1]*10000
isLychrel[0] = 0

for i in xrange(1,10000):
	if isLychrel[i] == -1:
		num = i+getReverse(i)
		itr = 1
		chain = [i]
		while itr < 50:
			revN = getReverse(num)
			if num == revN:
				break
			else:
				chain.append(num)
				num += revN
				itr += 1
		isLycr = 0
		if itr == 50:
			isLycr = 1 
		
		for n in chain:
			if n<10000:
				isLychrel[n] = isLycr
			else:
				break

print sum(isLychrel)	
