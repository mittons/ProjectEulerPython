from usefulStuff import sieve
from math import sqrt

primesBool = sieve(pow(10,7))
primes = []
primesBool[1] = 0
for i in xrange(1,pow(10,7)+1):
	if primesBool[i] == 1:
		primes.append(i)

def isPrime(n):
	if n<pow(10,7):
		return primesBool[n]
	else:
		i = 0
		m = sqrt(n)
		while (primes[i] < m):
			if n%primes[i] == 0:
				return False
			i += 1
		return True
