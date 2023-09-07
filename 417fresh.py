from usefulStuff import *
#primesBool = sieve(pow(10,8))
#print "ooo"
#primes = sieveToPrimes(primesBool)
#print"Yay"

#PSEUDO:
#DO THE SIEVE:
    #Each time a prime is found, calculate the period length using repeated squares to find the order of 10 mod p (which is the period length)
    #Instead of flagging numbers bool style, flag them with the factors of the period length (or just the period length), if the number has already been flagged, set the flag to the lcm of the old flag and the order of the current period length.
    #Each time a number is reached, prime or not, after fetching its period length, add it to the sum and set the list entry for it to null.
    #If this requires too much memory use dictionaries to do the lazy sieve.


def orderOf10modp(p, pminus1factors):
    #uses the least squares method to find the order of 10 mod p    
    #return the order, and the factorization of the order in the form [(p1, k2),(p2, k2)...] where p1 is a prime divisor of the order and k1 is the order of p1...

    order = p-1
    maxHighOrderBit = int(log(order,2))
    #array containing tuples (a,b) where a = 10^{2^n} mod p and b = 2^n for n = 0 to maxHighOrderBit 
    orderOf2Powers = [0] * (maxHighOrderBit + 1)
    orderOf2Powers[0] = (10 % p, 1)
    for i in xrange(1, maxHighOrderBit+1):
        orderOf2Powers[i] = ((orderOf2Powers[i-1][0])**2 % p, orderOf2Powers[i-1][1]*2)
    #Array that lists 10**f mod p where f is a prime factor mod 10
    
    orderFactors = {}
    

    for factor in pminus1factors:
        count = 0
        for power in xrange(pminus1factors[factor]):
            newOrder = order/factor
            currentOrder = newOrder
            tenToTheNewOrder = 1
            while currentOrder != 0:
                nextBit = int(log(currentOrder,2))
                tenToTheNewOrder *= orderOf2Powers[nextBit][0]
                currentOrder -= orderOf2Powers[nextBit][1]
            if tenToTheNewOrder % p == 1:
                order = newOrder
            else:
                count += 1
        if count > 0:
            orderFactors[factor] = count
    #print orderFactors
    return order, orderFactors
#print orderOf10modp(71, [(2,1),(5,1),(7,1)])

def powersOfPrimeFactors(n, primeDivisorsOfN):
    #using the knowledge of which primes divide n, returns a list of tuples (p, k) where p is a prime factor and 
    #k is the power of p in the composition of n
    div = n
    factorization = {}
    for prime in primeDivisorsOfN:
        #prime[0] is the actual prime
        p = prime[0]
        power = 1
        div /= p
        while div % p == 0:
            div /= p
            power += 1
        factorization[p] = power
    return factorization

#a =  powersOfPrimeFactors(503200,[(2,[1]),(5,[2]),(17,[4]),(37,[5])])
#b =  powersOfPrimeFactors(2161720,[(2,[1]),(5,[2]),(11,[4]),(17,[5])])

def getLCMofPeriodLengthsOfPrimeFactors(n, primeFactors):
    lcmFactors = {}
    l = len(primeFactors)
    if l == 2:
        if primeFactors[0][0] == 5:
            if primeFactors[1][0] == 2:
                return 0
    if l == 1:
        if primeFactors[0][0] == 5 or primeFactors[0][0] == 2:
            return 0
    pwrs = powersOfPrimeFactors(n, primeFactors)
    for prime in primeFactors:
        p = prime[0]
        if p in [2,5]:
            continue
        if p in [3,487,56598313]:
            pwrs[p] -= 1
        if pwrs[p] > 1:
            lcmFactors.setdefault(p, 1)
            lcmFactors[p] = max(lcmFactors[p], pwrs[p]-1)
            
        #prime is a tuple containing the prime and its period length factorized as list of tuples, each is a prime and its power in the composition
        for f in prime[1]:
            lcmFactors.setdefault(f, 1)
            lcmFactors[f] = max(lcmFactors[f], prime[1][f])
    lcm = 1
    #print lcmFactors
    for f in lcmFactors:
        lcm *= f**lcmFactors[f]
    return lcm
#print getLCMofPeriodLengthsOfPrimeFactors([(2,a),(3,b)])

def prob417(n):
    pLenSum = 0
    #Since we skip 3 which has pLen 1
    pLenSum += 1
    D = {6:[(3,{}),(2,{})],10:[(5,{})]}
    q = 6
    lastItemNotPrime = False
    while q < n+1:
        if q not in D:
            #q is prime
            #start by finding the period length of q
            qminus1factors = powersOfPrimeFactors(q-1,D[q-1])
            #print q, qminus1factors
    #        print qminus1factors
            pLen, pLenFactors = orderOf10modp(q, qminus1factors)
     #       print pLenFactors
 #           print q, pLen
            #mark 2*q as non prime, divisible by q, period length divisible by q's period length
            D.setdefault(q + q, []).append((q, pLenFactors))
            pLenSum += pLen

            if lastItemNotPrime:
                del D[q-1]
            lastItemNotPrime = False

        else:
            #q is not prime 
            #calculate pLen from the elements in D[q] and add it to the sum 
   #         print "q: {}, lcm: {}".format(q, getLCMofPeriodLengthsOfPrimeFactors(q, D[q]))
            pLenSum += getLCMofPeriodLengthsOfPrimeFactors(q, D[q])
            #for each prime divisor p of q mark the next number divisible by p, p+q, with the tuple (p, pLen) 
            #where pLen is the factorization of the period length of p
            for p in D[q]:
                D.setdefault(p[0]+q, []).append(p)

            if lastItemNotPrime:
                del D[q-1]
            lastItemNotPrime = True
        if q % pow(10,6) == 0:
            print q      
        q += 1
    return pLenSum
print prob417(100000000)
#print orderOf10modp(11, {2: 1, 5: 1})
