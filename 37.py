from usefulStuff import *

primesBool = sieve(1000000)
primes = sieveToPrimes(primesBool)

primesBool[0],primesBool[1] = 0,0

s = 0

for pr in primes[4:]:
	p = intToList(pr)
	l = len(p)
	truncateable = True
	for i in xrange(1,l):
		if not (primesBool[listToInt(p[:l-i])] == 1 == primesBool[listToInt(p[i:])]):
			truncateable = False
	if truncateable:
		s += pr
		print pr

print s	
