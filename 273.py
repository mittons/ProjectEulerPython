from usefulStuff import *
primesBool = sieve(150)
primes = sieveToPrimes(primesBool)
primes4kplus1 = [n for n in primes if (n-1)%4 == 0]
print int(((reduce(lambda x,y: x*y,primes4kplus1)+1)/2)**(1/2.0))
#http://mathoverflow.net/questions/29644/enumerating-ways-to-decompose-an-integer-into-the-sum-of-two-squares