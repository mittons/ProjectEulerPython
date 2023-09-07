from usefulStuff import *
from math import sqrt


MAXPRIME = int(pow(10,7)*6.5)
primesBool = sieve(MAXPRIME)
primes = sieveToPrimes(primesBool)
#primeI = range(2,len(primes))
pow2 = [int(pow(2,i)) for i in xrange(16)]
	
squireFree = [65535]*(25000000)
theta = [[0,6,12],[2,8,14],[4,10]]
beta = 0

for i in xrange(len(squireFree)):
	for thet in theta[beta]:
		squireFree[i] = (squireFree[i] & (~pow2[thet]))
	beta = (beta+1)%3

print "Yess"

fiboSqDiv = [0]*len(primes)
fiboSqDiv[0] = 6
fiboSqDiv[1] = 12
#fiboInd = [0,1]
leastI = 2
upperBound = pow(10,8)*4
greatestI = len(primes) #UPPER BOUND exclusive, not greatest value(inclusive)
nextDivisorPrime = 1
def findDivisors(n,d):
	global fiboSqDiv
	global fiboInd
	global squireFree
	global leastI
	global greatestI
	if leastI == -1:
		return 0
	i = leastI
#	idx = primeI[i]
	pr = primes[i]
#	oldIdxs = []
	divi = d*pr
	if divi > upperBound:
		leastI = -1
		print "STOP OF DIVISORS FUNCTION"
		return
	while n >= pr:
		if (fiboSqDiv[i] == 0) and (n%pr == 0):
	#		if fiboSqDiv[i] == 0:
			if i == leastI:
				leastI = i+1
				for j in xrange(i+1, greatestI):
					if fiboSqDiv[j] == 0:
						leastI = j
						print "Lowerbound upped to {}".format(j)
						break
			
			fiboSqDiv[i] = divi
	#		fiboInd.append(i)
			print "Going for {}".format(primes[i])
	#		divi = primes[i]*d
			divis = divi
			while divis<(pow(10,8)*4):
				squireFree[int(divis/16)] &= (~pow2[divis%16])
				divis += divi
			print "Done for {}".format(primes[i])
	#		else:
	#			if ((n/primes[i])%primes[i] != 0):
#					print "duplicate p: {} d: {}, old: {}".format([primes[i]],d, fiboSqDiv[i])
	#				assert ((d*primes[i])%fiboSqDiv[i] == 0)
		i += 1
		if i == greatestI:
			break
#		idx = primeI[i]
		pr = primes[i]
		divi = pr*d
		if divi > upperBound:
			print "Upperbound lowered to {}".format(i)
			greatestI = i
			break
	
#	for idxe in oldIdxs:
#		primeI.remove(idxe)
	
def isSquareFree(d):
	return (squireFree[int(d/16)] & pow2[d%16] != 0)

#	for i in fiboInd:
#		if d%fiboSqDiv[i] == 0:
#			return False
#	return True

f1 = 1
f2 = 2
c = pow(10,14)
d = 4
sqfr = 3
f1 = 3

while(True):
#	print "squareFree: {}, f: {}".format(findDivisors(f1),f1)
	squareFree = isSquareFree(d)
	if squareFree:
		sqfr += 1
#		print "nr: {}, squareFree: {}, f: {}, ff:{:e}, fff:{}".format(d,squareFree,f1,f1,f1%pow(10,16))
#	else:
#		print "nr: {}, squareFree: {}, f: {}, ff: {:e}, fff:{}".format(d,squareFree,f1,f1,f1%pow(10,16))
	if sqfr == pow(10,8):
		print "fibo nr: {}".format(d)
		break
#		print "nr: {}, squareFree: {}, f: {}, ff: {}".format(d,squareFree,fA,f1%pow(10,16))
		break
#	if sqfr == 200:
#		print "{:e}".format(f1)
#		break
	if sqfr%pow(10,5) == 0:
		print "{} hundred(s) of thousands!".format(sqfr/pow(10,5))
	
	if leastI != -1:
		findDivisors(f1,d)
		temp = f2
		f2 = f1
		f1 = (temp + f2)
		
	d += 1
