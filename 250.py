from math import *
import copy
orders = [0]*250
defaultValues = [0]*250

for i in xrange(250):
    j = 2
    last = 500
    vals = [i]
    v = i**j % 250
    while v != i:
        vals.append(v)
        j += 1
        if v == last:
            defaultValues[i] = last
            j = -j+2
            break
        else:
            last = v
        v = i**j % 250

    j-= 1
    orders[i] = j
    if j > 0:
        defaultValues[i] = vals
#    print i, orders[i]

n = 250251

modValues = [0]*n

valueCount = [0]*250

for i in xrange(1,n):
    x = i % 250
    if orders[x] <= 0:
        modValues[i] = defaultValues[x]
        valueCount[modValues[i]] += 1
    else:
        k = i % orders[x]
        j = (i-1 % (orders[x]))+1 #-1 shift and +1 shift back so if i = orders[x] the j will become i instead of 0 (we dont want i**0, we want i**i)
        modValues[i] = defaultValues[x][k-1]
        valueCount[modValues[i]] += 1
#    print i**i % 250, modValues[i]
#    assert modValues[i] == i**i % 250






F = {}
def nCk(n,k):
    if n in F:
        if k in F[n]:
            return F[n][k]
    else:
        F[n] = {}
    
    F[n][k] = (factorial(n) / factorial(k) / factorial(n-k)) % 10**16
    return F[n][k]

for i in xrange(250):
    print i, valueCount[i]

D = {}
D[0] = {}
#the number of subsets containing "0" elements whos subsetssum is 0 % 250. We dont count the empty set.
D[0][0] = (2**(valueCount[0]) - 1) % 10**16

for i in xrange(1,250):
    if valueCount[i] != 0:
        if i == 125:
            D[i] = {}
            D[i][125] = (2**25024) % 10**16
            D[i][0] = ((2**25024) - 1) % 10**16
            continue
        #find the order x of i in Z_250 under addition
        j = 1
        while (j*250) % i != 0:
            j += 1
        #x is the order if i % 250, i can generate x numbers.
        x = j*250/i
        
        D[i] = {}
        
        n = valueCount[i]

        for j in xrange(1,x+1):
            k = j*i % 250
            m = int((n-j)/x)
            D[i][k] = 0
            
            for setSize in xrange(m+1):
#                print "Calculating number of {}-subsets from the set of the {} elements with value only {}, each of whose subset sum is {} mod 250.".format(j + setSize*250, n, i, k)
                #every set of size j + setSize*x has sum k%250. adding x numbers to a set of size j does not change the sum mod 250. 
                #setSize is only a multipler for x
                D[i][k] = (D[i][k] + nCk(n, j + setSize*x)) % 10**16
        
        #dont#count the empty subset
        #D[i][0] = (D[i][0] + 1) % 10**16

    print i

print "wee"

subsets = [0]*250

subsets[0] = D[0][0]
subsetCounts = [((2**i) % 10**16) for i in valueCount]
for i in xrange(1,250): 
    if i not in D:
        continue
    newSubsets = copy.copy(subsets)
    for v in D[i]:
        newSubsets[v] += D[i][v]
        for j in xrange(250):
            vj = (v+j) % 250
            #print newSubsets[vj], D[i][v], subsets[j], (newSubsets[vj] + (D[i][v] * subsets[j])) % 10**16
            newSubsets[vj] = (newSubsets[vj] + (D[i][v] * subsets[j])) % 10**16
    subsets = newSubsets
    print i, (sum(subsets) % 10**16) == (reduce(lambda x,y: ((x*y) % 10**16), subsetCounts[:i+1]) - 1) % 10**16
    

print subsets[0]
print sum(subsets)
