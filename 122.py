from collections import deque
import copy
import time 


#####General helper functions#####
def sieve(n):
    primeList = [1]*(n+1)
    if (n>2):
        for i in xrange(2,n+1):
			if primeList[i] == 1:
				j = 2
				while j*i < n+1:
					primeList[j*i] = 0
					j += 1
	return primeList

def sieveToPrimes(sieveList):
	primes = []
	for i in xrange(2,len(sieveList)):
		if sieveList[i] == 1:
			primes.append(i)
	return primes

#returns a list containing how many of each prime from primeList that the number n has as a factor (the list only contains counts for primes up to the largest factor)
def factorsByList(n, primeList):
	div = n
	factors = []
	for prime in primeList:
		count = 0
		while (div%prime == 0):
			count += 1
			div /= prime
		factors.append(count)
		if div == 1:
			return factors
	return factors

#####General helper functions end#####


#This function createsa an upper bound on m(k) for k in [1..n]
#We always have k > upperbound(m(k)) => m(k)
#This function returns max(upperbound(m(k))) for k in [1..n]
#In any comment I will use a as some arbitraty number whose powers we are working with
def prob122UpperBound(n):

	primesBool = sieve(n)
	primes = sieveToPrimes(primesBool)
	uOfmForPrimes = []
	uOfm = [0,0]	

	
	for i in xrange(2,n+1):
		x = 0
		#If the k whose upperbound for m(k) we are checking in this iteration is a prime
			#We use upperbound(m(k-1))+1
			#We see that upperbound(m(k)) => upperbound(m(k-1)) + 1 since a^(k-1)*a^1 = a^k == one operation
		if primesBool[i] == 1:
			x = uOfm[-1]+1
			uOfmForPrimes.append(x)
		else:
			x = prob122Helper(factorsByList(i,primes), uOfmForPrimes)
		
		uOfm.append(x)		

	return max(uOfm)

#We see that if we have can create a^x from a^1 in n steps using some 
#intermediate values a^o_0, a^o_1.. a^o_i for o_0,o_1,...,o_i in [2..k-1]
#then we can create a^(x*j) from a^j in the steps a^o_0*j,a^o_1*j,..a^o_i*j using the same o_0,o_1,..,o_i
#If we have some a^k whose upperbound we want to know for m(k), and we know upperbound(m(p)) for every prime p < k
#then we can see that for k there is some upperbound(m(k)) = mult(factors(k)) given that factors() gives every prime factor as many times
#as its power in k (that is if k = 12 then factors(12) gives 2,2,3)

#TL;DR
#This function computes an upperbound for any k given its list of factors and a list upperbounds of m(k) for every prime less than k
def prob122Helper(factorList, uOfmForPrimes):
	retValue = 0
	for i in xrange(len(factorList)):
		if factorList[i] > 0:
			retValue += uOfmForPrimes[i] * factorList[i]
	return retValue

def prob4(n):
	maxD = prob122UpperBound(n)	
	pow2 = [pow(2,i) for i in xrange(maxD)]
	m = [0]*(n+1)
	#Number of m(k) values found
	found = 1
	#The smallest k that m(k) has not been found for
	minUnfoundK = 2	

	bfsQ = deque([(1,0,deque([1]))])
	currD = 0
	currK = 1
	currPowers = [1]
	
	
	while (found < n):
		nextD = currD+1
		xD = maxD-nextD
		for power in currPowers:
			nextPower = currK+power
			#We see that if we have found u = max(upperbound(m(k))) for k in [1..n] and the power x we
			#currently have was created in d multiplications then the largest power we can
			#create using x in u-d multiplications is pow(2,u-d)*x. 
			#If pow(2,u-d)*x is less than the smallest k we have not computed m(k) for we can skip going
			#further with this x
			#(This check reduced the max number if items bfsQ contained at any point from ~10mil to ~1mil, and
			# and took the runtime from ~70 sec to ~13 sek for n=200)
			if nextPower <= n and nextPower*pow2[xD] >= minUnfoundK: 
				if m[nextPower] == 0:
					m[nextPower] = nextD
					found += 1
					print "Found m(k) for {} k's".format(found)
					if nextPower == minUnfoundK:
						while found < n and m[minUnfoundK] != 0:
							minUnfoundK += 1
						print "The smallest k that m(k) that hasn't been found for is now {}".format(minUnfoundK)
				used = copy.copy(currPowers)
				used.append(nextPower)
				a = (nextPower,nextD,used) 
				bfsQ.append(a)
		guy = bfsQ.popleft()	
		currK = guy[0]
		currD = guy[1]
		currPowers = guy[2]

	return sum(m)

start = time.clock()
print prob4(200)
end = time.clock()
print (end-start)
