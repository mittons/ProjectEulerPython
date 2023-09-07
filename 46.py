from usefulStuff import *

primesBool = sieve(10000)
primes = sieveToPrimes(primesBool)
squares = [i**2 for i in xrange(1,100000)]
for i in xrange(len(primesBool)/2):
	num = i*2+1
	if primesBool[num] == 0:
		found = False
		for prime in primes:
			if prime >= num:
				break
			j = 0
			while num > prime + 2*squares[j]:
				j+=1
			if num == prime + 2*squares[j]:
				found = True
				break
		if not found:
			print num
			break
