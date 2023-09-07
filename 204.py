from usefulStuff import *

primesBool = sieve(100)
primes = sieveToPrimes(primesBool)
def bruteMult(i,num):
    if i == len(primes):
        return 0
    else:
        counter = bruteMult(i+1,num)
        num *= primes[i]
        while num <= pow(10,9):
            counter += (1 + bruteMult(i+1,num))
            num *= primes[i]
        return counter

print 1+bruteMult(0,1)
