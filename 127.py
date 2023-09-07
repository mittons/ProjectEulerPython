from usefulStuff import *
primesBool = sieve(60000)
primes = sieveToPrimes(primesBool)
Q = {}
#print len(primes)
#for pr in primes:
#	for i in xrange(120000):
#		if i%pr != 0:
#			Q.setdefault(pr, []).append(i)
#	print pr

#print "Yesh"

D = {}

q = 2
consec = 0
while q < 120000:
	if q not in D:
		D[q] = ([q],q,[])
		D.setdefault(q+q,[]).append(q)
		consec = 0
	else:
		rad = 1
		for p in D[q]:
			D.setdefault(p+q, []).append(p)
			rad *= p	
		D[q] = (D[q], rad,[])
	q += 1


cSum = 0
for i in xrange(2,120000-2):
	print i
	Checker = D[i][2]
#	twoCheck = False
#	threeCheck = False
#	if i%2 == 0:
#		twoCheck = True
#	if i%3 == 0:
#		threeCheck = True
	for j in xrange(i+1,120000):
#		if twoCheck:
#			if j%2==0:
#				continue
#		if threeCheck:
#			if j%3==0:
#				continue
#		c = i+j
#		if D[i][1]*D[j][1]*D[c][1] >= c:
#			continue
		gcd1 = True
		for fac in D[j][0]:
			if fac in D[i][0]:	
				gcd1 = False
				break
		if gcd1:
			Checker.append(j)			
#		if gcd1:
#			for fac in D[j][0]:
#				if fac in D[c][0]:
#					gcd1 = False
#					break
#		if gcd1:
#			for fac in D[i][0]:
#				if fac in D[c][0]:
#					gcd1 = False
#					break
#		if gcd1:
#			cSum += c

print cSum
			
