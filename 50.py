from usefulStuff import *

upperBound = pow(10,6)

primesBool = sieve(upperBound)
primes = sieveToPrimes(primesBool)

l = len(primes)

maxPrimeChain = 0
bestPrime = 0

for i in xrange(l-1):
	pChain = primes[i]	
	for j in xrange(i+1,l):
		pChain += primes[j]
		if pChain >= upperBound:
			break
		if primesBool[pChain] and j+1-i > maxPrimeChain:
			maxPrimeChain = j+1-i
			bestPrime = pChain
			print "New best: {} made from the sum of {} primes! This was made from the sum of primes {} to {}".format(bestPrime, maxPrimeChain, primes[i], primes[j])

print "The best chained prime under {} is... {}! It was made from the sum of {} consecutive primes!".format(upperBound, bestPrime, maxPrimeChain)
