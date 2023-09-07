from usefulStuff import *

primesBool = sieve(pow(10,5))
primes = sieveToPrimes(primesBool)
diagonal = 1

diagonalCount = 1
primeCount = 0.0

sideLength = 0

meanReductionSum = 0
last = 1

def isPr(x):
	for p in primes:
		if x%p==0:
			if x==p:
				continue
			return 0
	return 1

while True:
	sideLength += 2
	diagonalCount += 4
	for i in xrange(4):
		diagonal += sideLength
		primeCount += isPr(diagonal)
	if diagonal>pow(10,10):
		print "SKAMM"
		break
	if (primeCount/diagonalCount) < 0.1:
		break 

print sideLength+1
