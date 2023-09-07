from usefulStuff import *

primes = sieve(1000000)

circularPrimeCount = 0
for i in xrange(2,len(primes)):
	if primes[i] == 1:
		pr = intToList(i)
		allPrime = True
		#STOLEN FROM PROJEULER
		if (len(pr)> 1 and reduce(lambda x,y: x or y, map(lambda x: x==5 or x%2==0, pr))):
			continue
		#END OF STOLEN
		for j in xrange(len(pr)-1):
			pr = [pr[-1]]+pr[:-1]
			pri = listToInt(pr)
			if primes[pri] == 0:
				allPrime = False
			primes[pri] = 2
		
		if allPrime == True:
			uniformPrime = reduce(lambda x,y: x if x==y else False, pr)
			if uniformPrime:
				circularPrimeCount += 1
			else:
				circularPrimeCount += len(pr)

print circularPrimeCount
			


