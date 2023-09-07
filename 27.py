from usefulStuff import *
primesBool = sieve(10**6*3)
primes = sieveToPrimes(primesBool)

pIdx = 1
bestA = 0
bestB = 0
bestChain = 0
while primes[pIdx] < 1000:
    b = primes[pIdx]
    for a in xrange(-999,1000):
        n = 1
        counter = 1
        x = (n*(n+a)+b)
        while (x > 0) and primesBool[x]:
            counter += 1
            n += 1
            x = (n*(n+a)+b)
        if counter > bestChain:
            bestChain = counter
            bestA = a
            bestB = b
#            print bestA, bestB, bestChain
    pIdx += 1

#print bestA, bestB, bestChain, 
print bestA*bestB
