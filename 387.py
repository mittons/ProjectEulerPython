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
	

def harshadRecur(n, dSum, oldN, oldDSum, depth):
	if (n%dSum==0 and depth < 14):
		hSum = 0
		for i in xrange(0,10):
			hSum += harshadRecur(n*10+i,dSum+i,n,dSum,depth+1)
		return hSum
	else:
		if isPrime(n) and isPrime(oldN/oldDSum):
			return n
		return 0


sumH = 0

for i in xrange(1,10):
	for j in xrange(10):
		sumH += harshadRecur(i*10+j,i+j,i,i,2)
print sumH
