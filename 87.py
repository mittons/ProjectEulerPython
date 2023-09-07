from usefulStuff import *

upperBound = 50*pow(10,6)

primesBool = sieve(int(pow(50*pow(10,6),1.0/2)))
primes = sieveToPrimes(primesBool)

l = len(primes)

numbersOfThisType = set([])

for i in primes:
	p1 = i**4
	if p1>=upperBound:
		break
	else:
		for j in primes:
			p2 = p1+(j**3)
			if p2>=upperBound:
				break
			else:
				for k in primes:
					p3 = p2+(k**2)
					if p3>=upperBound:
						break
					else:
						numbersOfThisType.add(p3)

print len(numbersOfThisType)
