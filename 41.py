from usefulStuff import *
import copy
a = sieve(31623)

b = []
for i in xrange(2, 31624):
	if a[i] == 1:
		b.append(i)


def recursion(numlist, depth):
	if (depth == 7):
		n = listToInt(numlist)
		p = True
		for prime in b:
			if n == prime:
				print n
			if n % prime == 0:
				p = False
				break
		if p == True:
			print n

	for i in xrange(1,8):
		j = 8-i
		if j not in numlist:
			nList = copy.copy(numlist)
			nList.append(j)
			recursion(nList, depth+1)

recursion([], 0)	
