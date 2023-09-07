from usefulStuff import *

def fitty():
	primes = sieve(10000)
	primesDigit4 = []
	for i in xrange(1000,10000):
		if primes[i] == 1:
			primesDigit4.append(i)
	permutPrimeGroups = [[] for i in xrange(10000)]
	for i in xrange(len(primesDigit4)):
		intList = intToList(primesDigit4[i])
		intList.sort()
		permutPrimeGroups[listToInt(intList)].append(primesDigit4[i])
		print permutPrimeGroups[listToInt(intList)]
	for i in xrange(10000):
		if len(permutPrimeGroups[i]) > 2:
			for j in range(len(permutPrimeGroups[i])-2):
				for k in range(j+1, len(permutPrimeGroups[i])-1):
					if (permutPrimeGroups[i][k]*2-permutPrimeGroups[i][j]) in permutPrimeGroups[i]:
						print permutPrimeGroups[i][j]*pow(10,8)+permutPrimeGroups[i][k]*pow(10,4)+(permutPrimeGroups[i][k]*2-permutPrimeGroups[i][j])

fitty()

