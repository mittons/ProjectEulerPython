from usefulStuff import *

primesBool = sieve((10**8)/2)
primes = primesFromSieve(primesBool)

maxI = len(primes)
p = 10**10
for i in xrange(maxI):
	if primes[i]<

