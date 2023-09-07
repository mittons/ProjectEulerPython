from math import log
from math import log10
from math import atan, pi

def intToList(n):
    maxDigitSeat = int(log10(n))
    list = []
    for i in xrange(0,maxDigitSeat+1):
        list.append(int(n/pow(10,(maxDigitSeat-i)))%10)
    return list

def listToInt(list):
    l = len(list)
    num = 0
    for i in xrange(l):
        num += list[i]*pow(10,(l-1-i))
    return num

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

#TODO SKODA NAFN
def primesUpTo(n):
    primeList = [1]*(n+1)
    primes = []
    if (n == 2):
        primes.append(2)
    elif (n>2):
        for i in xrange(2,n+1):
            if primeList[i] == 1:
                primes.append(i)    
                j = 2
                while j*i < n+1:
                    primeList[j*i] = 0
                    j += 1
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
	
#returns a list of factors of a number, if a certain factor is of order b in the number then it appears b times in the list
def listFactors(n, primeList):
    div = n
    factors = []
    for prime in primeList:
        while (div%prime == 0):
            factors.append(prime)
            div /= prime
        if div == 1:
            return factors
    return factors

def mathematical((x0,y0),(x1,y1)):
    #dX = direction node1 is in relative to the line passing 
          #through node0 that is parallel to the x-axis 
    dX = 0
    if x0 == x1:
        if y0 < y1:
            dX = pi/2
        elif y0 > y1:
            dX = 3*pi/2 
        else:
            print "Error, comparing nodes at same coordinates"
    else:
        if x0 > x1:
            dX += pi
        dX += atan((y1-y0)/(x1-x0))
        dX %= (2*pi)
    return dX

	
def slopeBetweenPoints((x0,y0),(x1,y1)):
    return mathematical((x0,y0),(x1,y1))

#Permutations 

#Prints out every possible permutation of a number n,
#excluding the permutations that start with 0
#
#Params:
#lis
#   A list containing the digits n is composed of.
#   e.g. if n = 112, then lis = [1,1,2]

def createAllPermutations(lis):
    createAllPermutationsRecur(lis, 0, True)

def createAllPermutationsRecur(lis, num, isFirstRecursiveLayer):
    lisLen = len(lis)
    if lisLen == 0:
        print num

    lisSet = set(lis)

    if isFirstRecursiveLayer:
        lisSet.discard(0)
		
    for i in lisSet:
        newList = list(lis)
        newList.remove(i)

        createAllPermutationsRecur(newList, num + i * 10**(lisLen-1), False)
