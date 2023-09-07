from usefulStuff import *
from math import sqrt
n = pow(10,6)
x = int(sqrt(n))
primesBool = sieve(x)
primes = sieveToPrimes(primesBool)
pLen = len(primes)

def bruteRecurse(c,i):
    recurSum = 0
    if i == pLen:
        return 0
    else:
        recurSum += bruteRecurse(c,i+1)
        p = primes[i]
        c *= p
        while (c <= n):
            recurSum += max((int(n/c)-c,0))
            recurSum += bruteRecurse(c,i+1)
            c *= p
        return recurSum

superSum = n*2

for i in xrange(len(primes)):
    superSum += bruteRecurse(1,i)

print superSum
