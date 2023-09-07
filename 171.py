isSquare = []

def populateIsSquareArray():
    for i in xrange(1700):
        isSquare.append(0)

    i = 1;
    while i**2 < 1700:
        isSquare[i**2] = True;
        i += 1

factorial = []
def populateFactorialsArray():
    factorial.append(0)
    factorial.append(1)
    for i in xrange(2,21):
        factorial.append(factorial[i-1]*i)

populateIsSquareArray()

populateFactorialsArray()    

def calculateSquareSum(lis):
    sqSum = 0
    for x in lis:
        sqSum += x**2
    return sqSum

"""
def permutations(lis):
    n = len(lis)
    nFac = factorial[n]

    x = lis[0]
    c = 1
    for i in xrange(1,n):
        if lis[i] == x:
            c += 1
        else:
            nFac /= factorial[c]
            c = 1
            x = lis[i]
    
    nFac /= factorial[c]
    
    if x == 0:
        nFac /= n
        nFac *= (n-c)

    return nFac

def squareSumForAllPerm(lis, singleSqSum):
    return (singleSqSum * permutations(lis)) % 10**10


#Returns the sum modulo 10 of every possible permutation of a number n,
#excluding the permutations that start with 0
#
#Params:
#lis
#   A list containing the digits n is composed of.
#   e.g. if n = 112, then lis = [1,1,2]

def sumOfAllPermutations(lis):
    return sumOfAllPermutationsRecur(lis, 0, True)

def sumOfAllPermutationsRecur(lis, num, isFirstRecursiveLayer):
    lisLen = len(lis)
    if lisLen == 0:
        return num

    retSum = 0

    lisSet = set(lis)

    if isFirstRecursiveLayer:
        lisSet.discard(0)
		
    for i in lisSet:
        newList = list(lis)
        newList.remove(i)
        if lisLen <= 9:
            retSum += sumOfAllPermutationsRecur(newList, num + i * 10**(lisLen-1), False)
        else:
            retSum += sumOfAllPermutationsRecur(newList, 0, False)

    return retSum
"""

def createDigitCounts(digitList):
    digitCounts = [0]*10

    x = digitList[0]
    c = 1
    for i in xrange(1,len(digitList)):
        if digitList[i] == x:
            c += 1
        else:
            digitCounts[x] = c
            c = 1
            x = digitList[i]
    
    digitCounts[x] = c
    
    return digitCounts
    
def createDigitSet(digitCounts):
    retLis = []
    for i in xrange(10):
        if digitCounts[i] > 0:
            retLis.append(i)
    
    return retLis

def permutationsDigitCounts(digitCounts):
    n = sum(digitCounts)
    nFac = factorial[n]

    for i in xrange(10):
        if digitCounts[i] > 0:
            nFac /= factorial[digitCounts[i]]
    
    if digitCounts[0] > 0:
        nFac /= n
        nFac *= (n-digitCounts[0])
    
    return nFac 

    
def sumOfAllPermutationsRecur(digitCounts, i):
    if i > 8:
        return 0
    
    retSum = 0
    
    digitSet = createDigitSet(digitCounts)
    for x in digitSet:
        if sum(digitCounts) == 1:
            retSum += x * 10**i
        else:
            newDigitCounts = list(digitCounts)
            newDigitCounts[x] -= 1
            retSum += (x * 10**i) * permutationsDigitCounts(newDigitCounts)
            if i <= 7:
                retSum += sumOfAllPermutationsRecur(newDigitCounts, i+1)
        
    return retSum
    
def recur(lis):
    retSum = 0
    lisLen = len(lis)
    if lisLen < 20:
        for i in range(lis[len(lis)-1]+1)[::-1]:
            if lisLen == 2:
                print "\t {}".format(i)
            newLis = list(lis)
            newLis.append(i)
            retSum += recur(newLis)
             
    lisSqSum = calculateSquareSum(lis)
    if (isSquare[lisSqSum]):
#        retSum += sumOfAllPermutationsRecur(createDigitCounts(lis), 0)
        retSum += 1
    return retSum % 10**10




ans = 0

for i in range(1,10)[::-1]:
    print i
    ans += recur([i])

ans = ans % 10**10

print ans



#print permutationsDigitCounts([0,1,2,3,4,5,6,7,8,9])

#print permutationsDigitCounts([1,3,0,0,0,0,0,0,0,0])

#print sumOfAllPermutationsRecur([0,1,2,1,1,1,1,1,1,4], 0)
